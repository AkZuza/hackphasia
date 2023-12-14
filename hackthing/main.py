import re
from subject import *
from synonym import *
import json


with open("dataset.json","r",encoding='utf-8') as f:
    dataset = json.load(f)


def derive_vocab(user_input):
    vocab_list = []
    subjects = extract_subjects(user_input)
    for i in subjects:
        syno = get_synonyms(i)
        syno = list(syno)
        
        
        syno_without_drone = [word for word in syno if not re.search(r'\bdrone\b', word, flags=re.IGNORECASE)]
        
        vocab_list.extend(syno_without_drone)
        
       
        if re.search(r'\bdrone\b', i, flags=re.IGNORECASE):
            vocab_list.append("UAV")
    return vocab_list

def dataset_iterator(x):
    s=''
    for i in range(len(dataset)):
        for j in dataset[i]["Content"].split():
            if j in x:
                TITLE = dataset[i]["Title"]
                CONTENT = (dataset[i]["Content"])
                s += CONTENT + ' '
    return s



def abstracts(inp):
    vocab = derive_vocab(inp)
    return dataset_iterator(vocab)