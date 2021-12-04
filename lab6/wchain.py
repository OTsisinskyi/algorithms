def read_file(file_path):
    file_open = open(file_path, "r")
    data = file_open.readlines()
    list_of_word = []
    for word in data:
        list_of_word.append(word.strip("\n"))
    return list_of_word


def maximum_chain(words: list):
    words = sorted(words, key=len, reverse=True)
    chain_result = []
    literally_words = []

    for word in words:
        literally_words.append(get_literally(str(word)))

    chain_result.append(literally_words[0])
    literally_words = literally_words[1:]
    temp = []

    while literally_words:
        current = chain_result[-1]
        for i in current:
            for j in literally_words[0]:
                if i == j:
                    temp.append(i)

        if temp in literally_words and len(temp) == len(current) - 1:
            chain_result.append(temp)

        literally_words = literally_words[1:]
        temp = []
    output = []
    for item in chain_result:
        output.append(get_word(item))

    return output


def get_literally(word):
    item = []
    for i in word:
        item.append(i)
    return item


def get_word(literally):
    return "".join(literally)


if __name__ == '__main__':
    file = "wchain.in"
    word_list = read_file(file)
    result = maximum_chain(word_list)
    print(f"List chain: {result} \n"
          "Length: ", len(result))

