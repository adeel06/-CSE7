checksum = []
checksum = input("Enter your 8 digit credit card number: ").replace(" ","")
total_1 = 0
total_2 = 0

for i in checksum[-1::-2]:
    total_1 += int(i)

for i in checksum[-2::-2]:
    total_2 += sum(int(x) for x in str(int(i)*2))

num = (total_1 + total_2) % 10

if num == 0:
    print ("Your credit card number is valid")

else:
    invalid = int(checksum[-1])

    if invalid - num < 0:
        correct = invalid + (10 - num)

    else:
        correct = invalid - num

    print("Your credit card number is invalid - the value of the check digit is {}".format(correct))


# amount = int(float(input("Enter the amount of a countribution: $")))
