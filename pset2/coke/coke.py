def main():
    total_amount = 0

    while total_amount < 50:
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            total_amount += coin
            amount_due = 50 - total_amount
            if amount_due > 0:
                print("Amount Due:", amount_due)
        else:
            print("Amount Due:", 50 - total_amount)

    change = total_amount - 50
    print("Change Owed:", change)


main()
