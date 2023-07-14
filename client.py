import asyncio
import logging
from text_generation import AsyncClient

from time import perf_counter

from typing import List, Dict
import torch
from torch import IntTensor
from transformers import AutoTokenizer
import numpy as np

from hydra import (
    compose,
    initialize
)
from omegaconf import DictConfig, OmegaConf


log = logging.getLogger(__name__)
# intialize Hydra subsystem
initialize(version_base=None, config_path="conf")
cfg: DictConfig = compose("config.yaml")

# endpoint socket address
serving_system_socket: str = f"{cfg.endpoint.addr}:{ cfg.endpoint.port}"
client = AsyncClient(serving_system_socket)
max_concurrent_requests: int = cfg.endpoint.max_concurrent_requests

# uncomment for use natural language prompts
# prompt: str = "Hello" * 100
# output_lenght (decoding length)
max_new_tokens: int = cfg.GenerationConfig.max_new_tokens
# generation_strategy
repetition_penalty: float = cfg.GenerationConfig.repetition_penalty
do_sample: bool = cfg.GenerationConfig.do_sample
# generation finish reason
stop_sequences: List[str] = [stop for stop in cfg.GenerationConfig.stop_sequences]

# local experimentation tokenizer: "google/flan-t5-xl"
tokenizer_name: str =  "google/flan-t5-xl"
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
# "id": 21820 = "Hello"
dummy_input: IntTensor = IntTensor([[21820]])
# inverse tokenization (sanity check)
# token: str = tokenizer.decode(dummy_input[0], skip_special_tokens=True)
sequence_length: int = 100
multiple_dummy_repeat = dummy_input.repeat(1, sequence_length - 1)
prompt: str = tokenizer.decode(multiple_dummy_repeat[0], skip_special_tokens=True)

generate_kwargs: Dict = {"do_sample": do_sample,
                         "max_new_tokens": max_new_tokens,
                        "repetition_penalty": repetition_penalty,
                        "stop_sequences": stop_sequences}

prompts: List = [prompt] * max_concurrent_requests
# create many coroutines
coros = [client.generate(prompt, **generate_kwargs) for prompt in prompts]

async def batch():
    return await asyncio.gather(*coros)
    
start: float = perf_counter()
results = asyncio.run(batch())
stop: float = perf_counter()
elapsed_time: float = stop - start
print(f"Serving elapsed time: {elapsed_time:0.4f} seconds")
# check the last response
print(results[-1].details)

input_tokens = tokenizer(prompt, return_tensors="pt").input_ids
assert np.shape(input_tokens)[-1] == sequence_length

total_input_sequence_tokens: int = max_concurrent_requests * sequence_length
total_decoded_tokens: int = 0

for prompt, response in zip(prompts,results):
    # uncomment for see generations
    # print(prompt + response.generated_text)
    # assert np.shape(tokenizer(response.generated_text, return_tensors="pt").input_ids)[-1] -1 == max_new_tokens
    # assert response.details.generated_tokens == max_new_tokens
    total_decoded_tokens += response.details.generated_tokens

# stats
print(f"Serving elapsed time: {elapsed_time:0.4f} seconds")
print(f"Total requests: {max_concurrent_requests}")
print(f"Total input_ids: {total_input_sequence_tokens}")
print(f"Sequence length: {np.shape(input_tokens)[-1]}")
print(f"Total decoded tokens: {total_decoded_tokens}")
print(f"Throughput: {total_decoded_tokens/elapsed_time} tokens/sec")
print(f"Total processed tokens: {total_decoded_tokens + total_input_sequence_tokens}")