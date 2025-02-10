cost = 50

while 1:
    money = int(input("Insert Coin: "))
    if money == 5 or money == 10 or money == 25:
        cost = cost - money
        if cost > 0:
            print("Amount Due:", cost)
        else:
            print("Change Owed:", abs(cost))
            break
    else:
        print("Amount Due:", cost)

