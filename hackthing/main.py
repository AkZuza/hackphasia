import re
from hackphasia.hackthing.subject import *
from hackphasia.hackthing.synonym import *
import json


with open("hackphasia/hackthing/dataset.json","r",encoding='utf-8') as f:
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
    l=[]
    for i in range(len(dataset)):
        counter=0
        for j in x:
            
            if j in dataset[i]["Content"].split():
                counter +=1
                TITLE = dataset[i]["Title"]
                CONTENT = (dataset[i]["Content"])
                s += CONTENT + ' '
        l+=[counter]
        
    resp = dataset[l.index(max(l))]["Content"]
    title = dataset[l.index(max(l))]["Title"]
    url = dataset[l.index(max(l))]["Url"]
    to_ret = None
    if max(l) != 0:
        to_ret = (resp, title, url)
    else:
        to_ret = ("Beyond my vast immense knowledge", None, None)
    return to_ret



def abstracts(inp):
    vocab = derive_vocab(inp)
    out = dataset_iterator(vocab)
    return out
