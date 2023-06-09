import argparse
from lib import load
from lib import actions
import matplotlib.pyplot as plt
import pprint


# creating parser object with properties (arguments and options) for
# specifying text, keyword, iteration, and visualization.
parser = argparse.ArgumentParser()
parser.add_argument("text", help="Source text for running text analysis")
parser.add_argument("keyword", help="Keyword for caculating similarity in source text.")
parser.add_argument("-c", "--context", action='store_true', help="Show context for keyword from the text.")
# parser.add_argument("-g", "--graph", action='store_true', help="Create a network graph")
args = parser.parse_args()

# grabbing args from the command line
word = args.keyword 
filename = args.text

# actions: loading, tokenize, cleaning
loaded = load.launch(filename)
tokenized = load.preprocess(loaded)
cleaned = load.clean(tokenized)

# showing the context
if args.context == True:
    print(actions.context(tokenized, word))
else:
    pprint.pprint(actions.similar(cleaned, word))
    
# # visualize the results
# if args.graph == True:
#     graph = multiply.visualize_sim_1(cleaned, word)
#     plt.show(graph)
