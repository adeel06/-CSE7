amount = int(float(input("Enter the amount of a countribution: $")))
if amount >= 10000.00:
    print("Benefactors")
elif (amount >= 1000.00 and amount < 10000.00):
    print("Patrons")
elif (amount >= 200.00 and amount < 1000.00):
    print("Supporters")
elif (amount >= 15.00 and amount < 200.00):
    print("Friends")
elif (amount >= 0.00 and amount < 15.00):
    print("Cheapskates")
else:
    print("You have entered a negative number as a contribution. Good bye")