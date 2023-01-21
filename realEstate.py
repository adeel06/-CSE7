def abbreviate(a_string:str):
    a_string=a_string.title()
    vowels = "aeiou"
    for vowel in vowels:
        a_string=a_string.replace(vowel,"")
    return a_string.capitalize()


def main():
    temp = "Desirable unfurnished flat in quiet residential area"
    print(abbreviate(temp))
    n = input("Enter a sentence? ")
    print(abbreviate(n))

main()