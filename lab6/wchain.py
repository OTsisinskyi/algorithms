def read_file(file_path):
    file_open = open(file_path, "r")
    data = file_open.readlines()
    list_of_word = []
    for word in data:
        list_of_word.append(word.strip("\n"))
    return list_of_word


def max_chain(words):
    words = sorted(words, key=len)
    chain_words = {}
    result_list = []
    len_chain = 1
    if len(words) == 0:
        return len(words)
    else:
        for word in words:
            for letter in range(0, len(word)):
                possible_word = word[:letter] + word[letter + 1:]
                if possible_word in chain_words and len_chain < chain_words[possible_word]:
                    len_chain = chain_words[possible_word]
                    result_list.append(word)
            chain_words[word] = len_chain + 1
        return len_chain


if __name__ == '__main__':
    data = read_file('wchain.in')
    result = max_chain(data)
    print(f"Max chain -> {result}")
