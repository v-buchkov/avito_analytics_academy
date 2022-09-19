"""
Buchkov Viacheslav, DS Track, Python - HW1

Please, note:
As specified in HW output example - if "get_feature_names" does not take any input and
class itself does not take any input, it is assumed that the idea is to define the text corpus only in "fit_transform"
=> it is assumed that it will be always run first
"""


class CountVectorizer:
    """
    The class operates with sentences, classifying the unique words

    Please note that function "fit_transform" should be always run before function "get_feature_names"
    """
    @staticmethod
    def split_sentence(text):
        return [[word.lower() for word in sentence.split(' ')] for sentence in text]

    @staticmethod
    def create_new_words_counter(unique_words):
        return {unique_word: 0 for unique_word in unique_words}

    def fit_transform(self, corpus: list) -> list:
        """
        Function "fit_transform" returns the term-document matrix
        """
        # Get the list of lists of words, assuming that the words are split by one space
        self._all_sentences = self.split_sentence(corpus)
        # Use function to get the list of unique words
        unique_words = self.get_feature_names()
        target_matrix = []
        for sentence in self._all_sentences:
            # Create a dict of all unique words as keys with frequency as value (zero before processing a sentence)
            words_counter = self.create_new_words_counter(unique_words)
            for unique_word in words_counter.keys():
                for word in sentence:
                    if unique_word == word:
                        words_counter[unique_word] += 1
            # Append the list of values => frequencies
            target_matrix.append(list(words_counter.values()))
        return target_matrix

    def get_feature_names(self) -> list:
        """
        Function "get_feature_names" returns the list of unique words
        """
        # Via dict get unique words -> transform into list -> sum up all the lists into one
        return sum([list(dict.fromkeys(sentence)) for sentence in self._all_sentences], [])
