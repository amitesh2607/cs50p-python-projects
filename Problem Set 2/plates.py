def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    print(letters(s))
    print(numbers(s))
    print(symbols(s))

    return letters(s) and numbers(s) and symbols(s)

def letters(s):
    return 6 >= len(s) >= 2 and s[:2].isalpha()



def numbers(s):
    nums = []

    for letter in s:
        if letter.isdigit():
            nums.append(letter)
        if letter.isalpha() and nums:
            return False
    if nums and nums[0] == '0':
        return False
    return True



def symbols(s):
    return s.isalnum()

main()