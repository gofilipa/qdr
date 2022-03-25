import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# loading up and tokenizing the text

def load_text(filename):
    file = open(filename, encoding = "ISO-8859-1")
    raw = file.read()
    file.close()
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    return text

# cleaning the text

def clean_the_text(text):
    lower_no_punct = [word.lower() for word in text if word.isalpha()]
    stops = stopwords.words('english')
    no_stops = [word for word in lower_no_punct if word not in stops]
    wordnet_lemmatizer = WordNetLemmatizer()
    clean_text = [wordnet_lemmatizer.lemmatize(word) for word in no_stops]
    return clean_text

