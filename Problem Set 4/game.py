import random

def main():
    level  = get_level()
    number = generate_number(level)
    guess = get_guess(number)
  
    print(guess)

def get_level():
    while True:
        try:
        
            number = int(input("Level: "))
            if number < 1:
                raise ValueError
            return number


        except ValueError:
            pass


def generate_number(level):
    return random.randint(1,level)

def get_guess(number):
    while True:

        try:

            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
            if guess < number:
                print("Too small!")
            elif guess > number:
                 print("Too large!")
            elif guess == number:
                return "Just right!"
            
        except ValueError:
            pass



main()
