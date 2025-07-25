import inflect

p = inflect.engine()

name_list = []
start = "Adieu, adieu, to "

while True:

    try:

        name = input("Name: ").title().strip()

        name_list.append(name)





    except EOFError:
        break


names = p.join(name_list)
print(start + names)