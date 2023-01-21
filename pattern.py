# NROWS = 32
# j = 0
# for i in range (NROWS//2,-1,-4):
#         print("/" * i, end="")
#         print("*" * j, end="")
#         print(r"\" * i, end="\n")
#         j+=8
# Couldn't find documentation on how to switch between r"\"" and not r\ in the same line



NROWS = 32
j = 0
for i in range (NROWS//2,-1,-4):
        print("/ " * i, end="")
        print("* " * j, end="")
        print("\ " * i, end="\n")
        j+=8

