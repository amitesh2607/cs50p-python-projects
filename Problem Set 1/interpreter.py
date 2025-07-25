def main():
    exp = input("Enter expression: ")
    x, y, z = exp.split()
    x = float(x)
    z = float(z)
    inter(x, y, z)

def inter(x, y, z):
    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)


main()