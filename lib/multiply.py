import sys
import nltk

#######################################################################

### ideally, write a script that computes associated words which are 
# distinct across the binary. 
# We can choose the number of times we run similarity

#######################################################################

### similar words, first level

word = sys.argv[2]

def find_similar_words(clean_text):
    idx = nltk.text.ContextIndex(clean_text)
    # put words similar to woman in a list
    sim_1 = idx.similar_words(word)
    sim_1_str = " ".join(sim_1)
    return sim_1_str