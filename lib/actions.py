from nltk import Text
import networkx as nx
import matplotlib.pyplot as plt
import gensim
from gensim.models import Word2Vec


# script that computes associated words which are 
# distinct across the binary. 

def similar(cleaned, word):
    """ 
    Creates a word embedding model and returns the most similar words
    to the keyword.
    """
    model = Word2Vec([cleaned], vector_size=100, window=10,
                     min_count=1, workers=4)
    if word == "woman":
        words = model.wv.most_similar(positive=word, negative="man")
    elif word == "man":
        words = model.wv.most_similar(positive=word, negative="woman")
    else:
        words = model.wv.most_similar(word)
    return words

    ## to print out just the words, not vectors
    # words = []
    # for i in similar_w:
    #     words.append(i[0])
    # return words
    # return similar_w

def context(tokenized, word):
    """
    Gets the context for the keyword from the source text.
    """
    text = Text(tokenized)
    context = text.concordance(word, width=100)
    for i in context:
        if i in context == word:
            i.upper()
    return context

def subtract(cleaned, word, operand):
    """
    Subtracts a vector from another vector.
    """
    model = Word2Vec([cleaned], vector_size=100, window=10,
                     min_count=1, workers=4)
    result = model.wv(positive=word, negative=operand)
    return result
    
         
# ### similar words, second level
# def second_level(cleaned, first_level):
#     print(f"running second level with {first_level} words, with type {type(first_level)}")
#     model = Word2Vec([cleaned], vector_size=100, window=10,
#                      min_count=1, workers=4)
#     words = []
#     for word in first_level:
#         similar_w = model.wv.most_similar(word[0])
#         words.append(similar_w)
#         for word in similar_w:
#             words.append(word[0])
#     ## to print out / sort just words, not vetors
#     ## only works if first level is similarly returning just words. 
#     # words = set(words)
#     # words = words.sort()
#     return words


# # create a graph of first level similar words
# def visualize_sim_1(clean_text, word):
#     idx = nltk.text.ContextIndex(clean_text)
#     sim_1 = idx.similar_words(word)
#     G = nx.Graph()
#     G.add_node(word)
#     G.add_nodes_from(sim_1)
#     G.add_edges_from(interweave(word, sim_1))
#     return nx.draw(G, with_labels=True, font_weight='bold', node_size=500, node_color="#A0CBE2")

# # create a list of tuples to pass into graph as edge/node pairs
# def interweave(term, similar):
#     woven = []
#     for word in similar:
#         edge = term, word
#         woven.append(edge)
#     return woven

# perhaps need to make a class for this, to keep the same text no
# matter how many computations we run on it. 
# def make_model(cleaned):
#     model = Word2Vec([cleaned], vector_size=100, window=10,
#                      min_count=1, workers=4)
#     return model
