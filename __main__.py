import sys
from lib import load
from lib import multiply

# to run this app on the terminal:
# % python qdr orlando.txt woman

filename = sys.argv[1]
loaded = load.load_text(filename)
cleaned = load.clean_the_text(loaded)
print(multiply.find_similar_words(cleaned))