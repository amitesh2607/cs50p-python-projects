def main():
    word = input("Enter a word: ")
    print(remove_vowel(word))


def remove_vowel(word):
    new_word = []
    for letter in word:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_word.append(letter)

    return "".join(new_word)

main()