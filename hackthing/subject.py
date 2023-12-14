import nltk
from nltk import word_tokenize, pos_tag

def extract_subjects(user_input):
    words = word_tokenize(user_input)
    pos_tags = pos_tag(words)
    subjects = [word for word, pos in pos_tags if pos.startswith('N')]
    return subjects