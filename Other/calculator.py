#x = float(input("What is x?"))
#y = float(input("What is y?"))

#z = x / y
#print (f"{z:.2f}")

def main():
    x = int(input("What is x?"))
    y = int(input("What is y?"))
    z = add(x,y)
    return z

def add(x, y):
    return x + y



z = main()
print(z)

  