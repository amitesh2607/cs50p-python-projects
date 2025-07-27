import random


def main():
    level = get_level()
    count = 0
    for i in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        for j in range(3):

            answer = input(f"{x} + {y} = ")
            try:
                if int(answer) == x + y:
                    count += 1
                    break
                else:
                    if j != 2:
                        print("EEE")
                    else:
                        print(f"{x} + {y} = {x + y}")
            except ValueError:
                if j != 2:
                    print("EEE")
                else:
                    print(f"{x} + {y} = {x + y}")

    print(f"Score: {count}")


def get_level():

    while True:
        try:
            level = int(input("Level:"))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(11, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
