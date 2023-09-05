# %%
from transformers import AutoTokenizer
import numpy as np
# %%
tokenizer_name: str = "tiiuae/falcon-40b"
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
tokenizer.name_or_path
# %%
prompt: str = "hello world"

# %%
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
input_ids
# %%
np.shape(input_ids)
# %%
tokens_size = np.shape(input_ids)[-1] -1
# %%
tokens_size
# %%
input_ids

# %%
from torch import IntTensor, Tensor
import torch
# %%
dummy_input: Tensor = IntTensor([[21820]])
# %%
dummy_input
# %%
output = tokenizer.decode(dummy_input[0], skip_special_tokens=True)
# %%
print(output)
# %%
multiple_dummy: IntTensor = IntTensor([[21820, 21820]])
# %%
multiple_dummy_repeat = dummy_input.repeat(1, 2)
print(multiple_dummy_repeat)
np.shape(multiple_dummy_repeat)
# %%
multiple_dummy_cat = torch.cat((dummy_input, dummy_input), dim=0)
print(multiple_dummy_cat)
np.shape(multiple_dummy_cat)
# %%
"""
Example batch decode of multiple tensors

Target sequence: "Hello world"
"""
hello_world_tensor: IntTensor = IntTensor([[21820, 296]])
print(hello_world_tensor)
print(np.shape(hello_world_tensor))
outputs = tokenizer.batch_decode(hello_world_tensor, skip_special_tokens=True)
outputs
# %%
# Batch decoding: Same token
outputs = tokenizer.batch_decode(multiple_dummy_repeat, skip_special_tokens=True)
outputs

# %%
