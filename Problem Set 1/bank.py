def main():
    hi = input("What is your greeting?").lower().strip()
    output(hi)


def output(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()