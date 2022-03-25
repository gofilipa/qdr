import sys
import load
import multiply

filename = sys.argv[1]
loaded = load.load_text(filename)
cleaned = load.clean_the_text(loaded)
print(multiply.find_similar_words(cleaned))