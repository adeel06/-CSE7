#recursiveTriangle.py
def stars(n, descending=True):
    if (descending):
        print '*'*n

    if n==1:
        if not descending:
            print '*'
        return

    stars(n-1, descending)
    if not descending:
        print '*'*n

stars(5)
print()
stars(5, descending=False)

# def print_triangle (sideLength, descendening = True):
#         if (descendening):
#             print("[]"*sideLength)
#         if sideLength < 1:
#             return
#         print_triangle (sideLength-1)
#         print ( "[]"* sideLength)
#         if sideLength == 1:
#             if not descendening:
#                 print("[]")
#             return
#         print_triangle(sideLength-1, descendening)
#         print ( "[]"* sideLength)


# print(print_triangle(4, descendening=True))


# def recursive_triangle(num, char):
#     if num > 0:
#         recurse_triangle(num-1, char)
#         print(char*num)

# recursive_triangle(5, "[]")