# %%
import torch
import torch.nn as nn
import torch.nn.functional as F

from typing import List

from transformers import GPT2Tokenizer, GPT2LMHeadModel
# %%

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model__name= "gpt2-xl" if torch.cuda.is_available() else "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model__name)
load_config = {
    "device_map": "auto",
    "torch_dtype": torch.float16,
} if torch.cuda.is_available() else {}

model = GPT2LMHeadModel.from_pretrained(model__name, **load_config).to(device)
# %%
def perplexities(text: str, stride: int = 128):

    def tokenize(text: str) -> torch.LongTensor:
        return tokenizer(tokenizer.bos_token + text, return_tensors="pt").input_ids[0].to(device)
    def token_list(tokens: torch.LongTensor) -> List[int]:
        return tokenizer.batch_decode(tokens.unsqueeze(1))
    
    context_window = model.config.n_ctx
    input_ids = tokenize(text).to(device).unsqueeze(0)
    sequence_length = input_ids.size(1)
    # decoding parameters
    top_k = 10

    tokens = []
    for begin_loc in range (0, max(1, sequence_length - context_window + stride), stride):
        end_loc = min(begin_loc + context_window, sequence_length -1)
        span_input_ids = input_ids[:, begin_loc:end_loc]
        target_ids = input_ids[:, begin_loc+1:end_loc+1]

        with torch.no_grad():
            outputs = model(span_input_ids, labels=target_ids)
            logits = outputs.logits
            log_probs = F.softmax(logits, dim=-1)
            probs = F.softmax(logits, dim=-1)
            target_log_probs = log_probs.gather(2, target_ids.unsqueeze(2)).squeeze(2)
            target_probs = probs.gather(2, target_ids.unsqueeze(2)).squeeze(2)
            greedy_log_probs, greedy_tokens = log_probs.topk(top_k, dim=2)
            greedy_probs = torch.exp(greedy_log_probs)
            for tok, predicted_toks, log_prob, prob in list(zip(
                token_list(target_ids[0]),
                [
                    zip(topk_log_probs, topk_probs, token_list(topk_tokens))
                    for topk_log_probs, topk_probs, topk_tokens
                    in zip(
                        greedy_log_probs[0].tolist(),
                        greedy_probs[0].tolist(),
                        greedy_tokens[0],
                    )
                ],
                target_log_probs[0].tolist(),
                target_probs[0].tolist(),
            ))[context_window - stride if begin_loc > 0 else 0:]:
                tokens.append({
                    'token': tok,
                    'predicted_tokens': [{
                        'token': tok,
                        'log_prob': log_prob,
                        'prob': prob,
                    } for log_prob, prob, tok in predicted_toks],
                    'log_prob': log_prob,
                    'prob': prob,
                })
    return tokens
# %%
tokens = perplexities("Hello, my dog is cute", stride=128)
# %%
print(tokens.__class__)
print(tokens[0].__class__)
# %%
for token in tokens:
    print(token)

# %%
