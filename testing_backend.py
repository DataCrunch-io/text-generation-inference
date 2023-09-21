from typing import List
import time

from text_generation_server.pb import generate_pb2
from text_generation_server.models.seq2seq_lm import Seq2SeqLM, Seq2SeqLMBatch
from text_generation_server.models.types import GeneratedText
from pynvml import (
    nvmlInit,
    nvmlShutdown,
    nvmlDeviceGetHandleByIndex,
    nvmlDeviceGetUtilizationRates,
    nvmlDeviceGetMemoryInfo
)
from transformers import AutoTokenizer
import torch
from torch import IntTensor

nvmlInit()
handle = nvmlDeviceGetHandleByIndex(0)

tokenizer_name: str =  "google/flan-t5-xl"
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
tokenizer.bos_token_id = 0
st = time.perf_counter_ns()
default_seq2seq_lm = Seq2SeqLM("google/flan-t5-xl")
et = time.perf_counter_ns() - st
model_malloc = nvmlDeviceGetMemoryInfo(handle)
print(f"Model allocation GPU memory: {(model_malloc.used / 2**30):.4f} GB")
print(f"Model loading time: {et*1e-9:.4f} s")
# Generation configuration
sequence_length: int = 25
max_new_tokens: int = 25

default_pb_parameters = generate_pb2.NextTokenChooserParameters(
    temperature=1.0,
    repetition_penalty=1.0,
    top_k=0,
    top_p=1.0,
    typical_p=1.0,
    do_sample=False
)
default_pb_stop_parameters = generate_pb2.StoppingCriteriaParameters(
    max_new_tokens=max_new_tokens,
    stop_sequences=[],
    ignore_eos_token=True
)
dummy_input: IntTensor = IntTensor([[21820]])
multiple_dummy_repeat = dummy_input.repeat(1, sequence_length - 1)
prompt: str = tokenizer.decode(multiple_dummy_repeat[0], skip_special_tokens=True)
default_pb_request = generate_pb2.Request(
    id=0,
    inputs=prompt,
    prefill_logprobs=True,
    truncate=25,
    parameters=default_pb_parameters,
    stopping_parameters=default_pb_stop_parameters,
)

from copy import copy

requests: List[generate_pb2.Request] = []
# batch size equals len(requests)
batch_size: int = 256
for i in range(batch_size):
    req_tmp = copy(default_pb_request)
    req_tmp.id = i
    requests.append(req_tmp)

print(len(requests))
print(requests[-1].id)
print(requests[-1])

batch = generate_pb2.Batch(id=0, requests=requests, size=batch_size)
dtype = torch.float16
device = torch.device("cuda")

default_seq2seq_lm_batch = Seq2SeqLMBatch.from_pb(
                                batch,
                                tokenizer=tokenizer,
                                dtype=dtype,
                                device=device,
)

sequence_length: int = len(default_seq2seq_lm_batch.input_ids[0])
print(sequence_length)
torch.cuda.cudart().cudaProfilerStart()
for idx in range(max_new_tokens):
    """
    NVIDIA Nsight Systems (CUDA new profiler)

    usage
    $nsys profile -o timeline python testing_client.py
    
    generate stats
    nsys stats timeline.nsys-rep 
    """
    torch.cuda.nvtx.range_push("generate_token")
    generations, next_batch = default_seq2seq_lm.generate_token(default_seq2seq_lm_batch)
    torch.cuda.nvtx.range_pop()
    print(f"First generation of the batch: {generations[0]}")
    print(f"Last generation of the batch: {generations[-1]}")
    print(f"Generated token: {generations[0].token_text}")
    print(f"Prefill tokens: {generations[0].prefill_tokens}")
    if isinstance(generations[0].generated_text, GeneratedText):
        print(f"Generated text: {generations[0].generated_text}")
        assert generations[0].generated_text.generated_tokens == max_new_tokens
    # next batch provides a lot of information about decoding
    # print(next_batch)
    # assert generations[0].generated_tokens == max_new_tokens
    mem = nvmlDeviceGetMemoryInfo(handle)
    print(f"GPU memory: {(mem.used / 2**30):.4f} GB")
    util = nvmlDeviceGetUtilizationRates(handle)
    print(f"GPU utilization: {util.gpu} %")
torch.cuda.cudart().cudaProfilerStop()
nvmlShutdown()
