def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

def main():
    emoji = input("What is your emoticon? ")
    emoji = convert(emoji)
    print(emoji)

main()


