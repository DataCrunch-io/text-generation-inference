import asyncio
from text_generation import AsyncClient

client = AsyncClient("http://127.0.0.1:8080")

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