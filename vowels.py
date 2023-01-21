def vowel_count(data:str):
    data=data.lower()
    vowels='aeiou'
    output=[]
    for vowel in vowels:
        output.append(data.count(vowel))
    return output

def main():
    temp = "I think, therefore I am"
    print(vowel_count(temp))
    temp = "I found a chair in my room"
    print(vowel_count(temp))

main()