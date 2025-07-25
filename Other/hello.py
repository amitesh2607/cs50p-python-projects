# Ask user for their name
#name = input("What is your name? ").strip().title()

#SPlit users name into first name and last name
#first, last = name.split(" ")

# Say hello to user
#print(f"Hello, {first}")

def hello(to = "world"):
    print(f"Hello {to}")

hello()
name = input("What is your name? ")
hello(name)
