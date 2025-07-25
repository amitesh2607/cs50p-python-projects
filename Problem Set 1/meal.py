def main():
    time = input("What is the time? ").strip()
    time = convert(time)
    if time < 7:
        print("")
    elif time <= 8:
        print("breakfast time")
    elif time <= 13:
        print("lunch time")
    elif time <= 19:
        print( "dinner time")
    else:
        print("")



def convert(time):
    hours, minutes = time.split(sep = ":")
    minutes = float(minutes) / 6 / 10
    hours = float(hours)
    time = hours + minutes
    return time




if __name__ == "__main__":
    main()


