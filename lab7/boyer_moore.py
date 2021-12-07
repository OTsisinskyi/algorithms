def get_unicode_list(string, size):
    unicode_list = [-1] * 256
    for i in range(size):
        unicode_list[ord(string[i])] = i
    return unicode_list


def boyer_moore(text, pattern):
    pattern_len = len(pattern)
    text_len = len(text)
    unicode_list = get_unicode_list(pattern, pattern_len)
    search_index = 0
    list_of_found_indexes = []
    if pattern_len == 0:
        return [None]
    while search_index <= text_len - pattern_len:
        j = pattern_len - 1
        while j >= 0 and pattern[j] == text[search_index + j]:
            j -= 1
        if j < 0:
            print(f'Text:    {text} \nPattern: %s%s' % ("." * search_index, pattern))
            print("Search_index: " + str(search_index) + "\n")
            list_of_found_indexes.append(search_index)
            search_index += (pattern_len - unicode_list[ord(text[search_index + pattern_len])]
                             if search_index + pattern_len < text_len else 1)

        else:
            search_index += max(1, j - unicode_list[ord(text[search_index + j])])
    if search_index == text_len and pattern not in text:
        print(f'"{pattern}" is not in "{text}"')
        return [None]
    print("List of found indexes: ", list_of_found_indexes)
    return list_of_found_indexes


if __name__ == '__main__':
    txt = "Hello, the session is nears"
    pat = "sion"
    boyer_moore(txt, pat)
