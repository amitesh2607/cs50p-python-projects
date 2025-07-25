def main():
    dict1 = {}
    for i in range(3):
        name = input("What is your name? ")
        phone_number = input("What is your phone number? ")
        dict1[name] = phone_number
    check = input("What name would you like to search for? ")
    if check in dict1:
        print(dict1[check])
    else:
        print("Not found")


if __name__ == '__main__':
    main()




