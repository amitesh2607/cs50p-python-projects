def main():
    cost = 50
    while cost > 0:
        coin = int(input("Insert a coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            cost -= coin
            if cost > 0:
                print(f"Amount Due: {cost}")
            else:
                continue
        else:
            print(f"Amount Due: {cost}")

    print(f"Change Owed: {abs(cost)}")






main()