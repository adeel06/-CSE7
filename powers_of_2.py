# used https://www.w3schools.com/python/ref_func_pow.asp to find pow - power function without using ** or importing the math library

def print_powers_of_2(n):
    for x in range (n+1):
        print(pow(2,x),end=" ")

def main():
    print_powers_of_2(5)
    print()
    print_powers_of_2(10)
    print()
    print_powers_of_2(20)
    print()
    print_powers_of_2(30)
    print()

main()