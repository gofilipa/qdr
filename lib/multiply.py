import nltk
import networkx as nx
import matplotlib.pyplot as plt


# script that computes associated words which are 
# distinct across the binary. 

# We can choose the number of times we run similarity

### similar words, first level

def find_similar_words(clean_text, word):
    idx = nltk.text.ContextIndex(clean_text)
    # put words similar to woman in a list
    sim_1 = idx.similar_words(word)
    sim_1_str = " ".join(sim_1)
    return sim_1_str

### similar words, second level
def find_similar_words_2(clean_text, sim_1_str):
    idx = nltk.text.ContextIndex(clean_text)
    sim_2_nested = []
    sim_1_list = sim_1_str.split(" ")
    for word in sim_1_list:
        sim_2 = idx.similar_words(word)
        sim_2_nested.append(sim_2)
    # un-nest the words
    sim_2 = [inner
        for outer in sim_2_nested
            for inner in outer]
    # filter out 'woman'
    sim_2_clean = []
    for word in sim_2:
        if word != 'woman':
            sim_2_clean.append(word)
    # turn into a string
    sim_2_str = " ".join(sim_2_clean)
    return sim_2_str

# create a graph of first level similar words
def visualize_sim_1(clean_text, word):
    idx = nltk.text.ContextIndex(clean_text)
    sim_1 = idx.similar_words(word)
    G = nx.Graph()
    G.add_node(word)
    G.add_nodes_from(sim_1)
    G.add_edges_from(interweave(word, sim_1))
    return nx.draw(G, with_labels=True, font_weight='bold', node_size=500, node_color="#A0CBE2")

# create a list of tuples to pass into graph as edge/node pairs
def interweave(term, similar):
    woven = []
    for word in similar:
        edge = term, word
        woven.append(edge)
    return woven