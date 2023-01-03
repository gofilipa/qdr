import unittest
from lib import load
import nltk

# to run tests:
# python -m unittest -v

class TestLoad(unittest.TestCase):

    def test_preprocess(self):
        file = open('tests/test_file.txt')
        data = file.read()
        file.close()
        result = load.preprocess(data)
        self.assertIsInstance(result, nltk.text.Text)
    
    def test_clean(self):
        # check the capitalizations, punctuations, and lemmatizations
        test_string = ["children", "TeST", "hello!", "0", "#%()"]
        result = load.clean(test_string)
        self.assertEqual(result, ["child", "test"])

if __name__ == '__main__':
    unittest.main()