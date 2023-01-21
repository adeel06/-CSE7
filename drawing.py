# Write a function named top() that draws this figure (there are precisely 7
# underscore characters in the top line):
#   ________
#  /        \
# /          \
# Now write a function named bottom() that draws this figure:
# \          /
#  \________/
# Finally, define a main function that uses the top() and bottom() functions
# (along with any additional functions you wish) to output the following sequence:

#   _______
#  /       \
# /         \
# \         /
#  \_______/
# -"-'-"-'-"-
#   _______
#  /       \
# /         \
# \         /
#  \_______/
#
# -"-'-"-'-"-
# \         /
#  \_______/
#   _______
#  /       \
# /         \
# -"-'-"-'-"-
# \         /
#  \_______/


def top():
    print("   _______  ")
    print("  /       \ ")
    print(" /         \ ")


def bottom():
    print(" \         /" )
    print("  \       / " )
    print("   _______  ")

def middle():
    print(''' -"-'-"-'-"-''' )

def main():
    top()
    bottom()
    middle()
    top()
    bottom()
    print("\n")
    middle()
    bottom()
    top()
    middle()
    bottom()

main()
