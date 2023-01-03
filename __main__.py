import argparse
from lib import load
from lib import multiply
import matplotlib.pyplot as plt


# 
parser = argparse.ArgumentParser()
parser.add_argument("text", help="Source text for running text analysis")
parser.add_argument("keyword", help="Keyword for caculating similarity in source text.")
parser.add_argument("-i", "--iteration", help="Number of iterations for calculating similarity on keyword. Default is 1.")
parser.add_argument("-v", "--visualize", action='store_true',help="Create a network graph")
args = parser.parse_args()

# grabbing args from the command line
word = args.keyword 
filename = args.text
visual = args.visualize

# we always load up the text, tokenize, and clean it
loaded = load.launch(filename)
tokenized = load.preprocess(loaded)
cleaned = load.clean(tokenized)

# we assume 1 level of multiplication
first_level = multiply.find_similar_words(cleaned, word)

# in the case that we want to iterate twice
if args.iteration: 
    if int(args.iteration) == 2:
        second_level = multiply.find_similar_words_2(cleaned, first_level)
        print(second_level)
else:
    print(first_level)

# visualize the results
if args.visualize == True:
    graph = multiply.visualize_sim_1(cleaned, word)
    plt.show(graph)
