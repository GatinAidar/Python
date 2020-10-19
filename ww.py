#asdf asd
def text_split(string):
    result = ''
    for word in string.split():
        result = result + reverse_word(word) + ' '
    return result.strip()


def reverse_word(string):
    word = list(string)
    # words = string.split()
    # for word in words:
    temp = list()
    count = -1
    #    text = string.split()
    #    for elems in text:
    for i in range(len(word) - 1, -1, -1):
        if word[i].isalpha():
            temp.append(word[i])

    for i in range(0, len(word)):
        if word[i].isalpha():
            count += 1
            print("wag: ", word[i])
            word[i] = temp[count]

    #        else:

    #            print("YA tyt:", word[i])
    print("Gotoviy:", word)
    print("Temp is:", temp)
    return ''.join(word)


if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe")
    ]

    for text, reversed_text in cases:
       # print(text_split(text) +"=="+ reversed_text)
        assert text_split(text) == reversed_text


#string = "ab1cd"
# print(type(cases[0]))

#print("Original is", string)

# text_split(string)

#print(string[3])
#reverse(string)
# print(temp)
# print("xz is",string)
