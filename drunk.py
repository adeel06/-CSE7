import random

def drunk_walk():
    steps = 0
    street = 6

    while (street != 1) and (street != 11):
        x = random.randint(0,1)
        if (x == 1):
            steps += 1
            street += 1
        else:
            steps += 1
            street -= 1
    return steps


N = int(input("Number of steps: "))

total_steps = 0
for i in range(N):
    total_steps += drunk_walk()

average = total_steps/N

print("Here we go again... time for a walk!")
print("Took", total_steps, "steps, and")

street = 0

if street == 1:
    print("Landed at HOME")
else:
    print("Landed in JAIL")


# print("Landed at" )
print("Average # of steps equals", average)