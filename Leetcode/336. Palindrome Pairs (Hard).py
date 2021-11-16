class Solution:
    def palindromePairs(self, words):
        words_dict = dict()
        index_list = set()

        for index, word in enumerate(words):
            words_dict[word] = words_dict.get(word, index)

        for word in words_dict:

            for index in range(len(word)+1):

                if word[0:index] == word[0:index][::-1]:
                    search_word = word[index:len(word)][::-1]

                    if search_word in words_dict and search_word != word:
                        index_list.add(
                            (words_dict[search_word], words_dict[word]))

                if word[index:] == word[index:][::-1]:
                    search_word = word[0:index][::-1]

                    if search_word in words_dict and search_word != word:
                        index_list.add(
                            (words_dict[word], words_dict[search_word]))

        return list(index_list)
