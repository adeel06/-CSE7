# NROWS = 18
# j = 0
# for i in range(NROWS,-1,-4):
#     print("Na ") * i, end="")
#     print("na ") * i, end="")
#     print(" ... ") * i, end="")
#     print("BATMAN!") * i, end="")


NROWS = 9
print("Na", end=" ")
for i in range(NROWS,-1,-4):
    print("na " * i, end="")

print("... BATMAN!")