#For Normal Credit

def occurences(data:int):
    output = []
    data = str(data)
    for i in range(10):
        output.append(str(data.count(str(i))))
    return output


def main():
    temp = abs(int(input("Please enter an integer: ")))
    print("Digit:      0 1 2 3 4 5 6 7 8 9")
    print("Occurences:",' '.join(occurences(temp)))

main()