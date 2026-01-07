class bs:
    def __init__(self, stock):
        self.stock = stock

    def db(self):
        print("Total bikes available:", self.stock)

    def rent(self, q):
        if q <= 0:
            print("Enter a positive value")
        elif q > self.stock:
            print("Enter value less than or equal to stock")
        else:
            print("Total price:", q * 100)
            self.stock -= q
            print("Remaining bikes:", self.stock)


ob = bs(100)

while True:
    uc = int(input('''
1. Display stock
2. Rent a bike
3. Exit
Enter choice: '''))

    if uc == 1:
        ob.db()

    elif uc == 2:
        n = int(input("Enter quantity: "))
        ob.rent(n)

    elif uc == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
