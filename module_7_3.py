import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation.replace("'", '')))
                words_list = text.split()
                all_words[file_name] = words_list
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))