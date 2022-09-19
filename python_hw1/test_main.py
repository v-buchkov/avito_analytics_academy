"""
Buchkov Viacheslav, DS Track, Python - HW1
"""

# Import function for testing
from main import CountVectorizer


# Class for testing
class OutputTest:
    # Initialize with input (corpus) and expected outputs
    def __init__(self, corpus: list, expected_feature_names: list, expected_term_document_matrix: list):
        self.corpus = corpus
        self.expected_feature_names = expected_feature_names
        self.expected_term_document_matrix = expected_term_document_matrix

    def test(self):
        vectorizer = CountVectorizer()
        term_document_matrix = vectorizer.fit_transform(self.corpus)
        feature_names = vectorizer.get_feature_names()
        # If both outputs equal to expected outputs => test is passed
        if term_document_matrix == self.expected_term_document_matrix and feature_names == self.expected_feature_names:
            return True
        else:
            return False


if __name__ == '__main__':
    # Initialize test from HW example
    test_process = OutputTest(corpus=['Crock Pot Pasta Never boil pasta again',
                                      'Pasta Pomodoro Fresh ingredients Parmesan to taste'],
                              expected_feature_names=['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pasta',
                                                      'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste'],
                              expected_term_document_matrix=[[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                                             [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])

    # Print the result (True-False)
    print(test_process.test())
