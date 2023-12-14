import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
from main import *


tokenizer=AutoTokenizer.from_pretrained('T5-base')
model=AutoModelWithLMHead.from_pretrained('T5-base', return_dict=True)

sequence = (abstracts())
output = model.generate(inputs, min_length=80, max_length=100)
summary=tokenizer.decode(output[0])
print(summary)