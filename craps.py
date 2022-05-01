import random

# x = random.randint(1, 6)
# y = random.randint(1, 6)

# print(x+y)
# # if (x+y) == (4,5,6,8,9,10):
# #     print("point: ")

def do_roll():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    print("Computer rolls a %d and a %d for a total of %d."%(x, y, x+y))
    return x+y

# Your program will “roll” two dice until the total value is 4, 5, 6, 8, 9, or 10.
# This number becomes the player’s “point.”
point = 0

# while point != [4,5,6,8,9,10]:
while point not in [4,5,6,8,9,10]:
    point = do_roll()
print("%d is now the established POINT."%point)

craps = 0

# while craps != [point,7]:
while craps not in [point, 7]:
    craps=do_roll()
if craps == 7:
    print("YOU LOSE")
else:
    print("YOU WIN")

