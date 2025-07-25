
def main():

    percent = get_percent()
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent:.0f}%")




def get_percent():
    while True:
        try:
            x, y  = input("Fraction: ").strip().split('/')


            x = int(x)
            y = int(y)

            if x < 0 or y < 0 or x > y:
                raise ValueError()

            return x / y * 100
        except ValueError:
            pass
        except ZeroDivisionError:
            pass








main()