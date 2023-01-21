#primes
def prime(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return num > 1


def main():
    num = int(input('Enter an integer:  '))
    for i in range(num):
        if prime(i):
            print(i)
main()