import os
import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# launching and tokenizing the text

def launch(filename):
    with open(os.path.join(sys.path[0], f'texts/{filename}'), "r") as file:
        raw = file.read()
        file.close()
        return raw

def preprocess(raw):
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    return text

# cleaning the text

def clean(text):
    lower_no_punct = [word.lower() for word in text if word.isalpha()]
    stops = stopwords.words('english')
    no_stops = [word for word in lower_no_punct if word not in stops]
    wordnet_lemmatizer = WordNetLemmatizer()
    clean_text = [wordnet_lemmatizer.lemmatize(word) for word in no_stops]
    return clean_text

