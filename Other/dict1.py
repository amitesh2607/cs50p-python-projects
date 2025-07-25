def main():

    sentence = input('Enter a sentence: ').split()
    dictionary = counter(sentence)
    for key, value in dictionary.items():
        print(f"{key}: {value}")


def counter(sentence):
    dict1 = {}
    for word in sentence:
        if word not in dict1:
            dict1[word] = 1
        else:
            dict1[word] += 1
    return dict1


if __name__ == '__main__':
    main()