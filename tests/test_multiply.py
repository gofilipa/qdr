import unittest
from lib import multiply
import nltk

# to run tests:
# python -m unittest -v

class TestMultiply(unittest.TestCase):

    def test_find_similar_words(self):
        word = "woman"
        file = open('tests/o_test_file.txt')
        data = file.read()
        file.close()
        tokens = nltk.word_tokenize(data)
        result = multiply.find_similar_words(tokens, word)
        expected = "reached till friend word moment saw always could cried sailor wit scarcely petticoat go servant conclusion"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()