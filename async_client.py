from text_generation import Client

from typing import List
# endpoint socket address
serving_system_socket: str = "http://127.0.0.1:3000"
prompt: str = "This is a prompt"

import asyncio
from text_generation import AsyncClient

client = AsyncClient(serving_system_socket)
prompt_1 = "Translate the following sentence into English: Estoy hambriento. English:"
prompt_2 = "This is another prompt"

prompts = [prompt_1, prompt_2]

async def batch():
    return await asyncio.gather(client.generate(prompt_1, repetition_penalty=1.5, max_new_tokens=10), client.generate(prompt_2))
    
results = asyncio.run(batch())

text = ""
for prompt, response in zip(prompts,results):
    print(prompt + response.generated_text)
print(text)