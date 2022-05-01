def main():
    mystery(-2, -6)
    mystery(2, 3)
    mystery(4, 8)
    mystery(10, 31)

def mystery (x, y):
    s = 0
    while x > 0 and 2*y >= x:
        print(s, end=" ")
        y = y - x
        x -= 1
        s = s + 2 * x
    print(s)

main()