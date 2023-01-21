#Regular Problem (Not for extra credit)


def vowel_index(word:str):
    temp = "aeiou"
    count = 0
    for char in word:
        if char.lower() not in temp:
            count+=1
        else:
            break
    if 'y' in word:
        if len(word)<4:
            if word[-1]=='y':
                if count>=len(word)-1:
                    count=len(word)-1
        elif 'y' in word[1:-1]:
            if count>=word.index('y'):
                count=word.index('y')
    return count


def piggie(data:str):
    vowel = vowel_index(data)
    if vowel == 0:
        return data+"-way"
    else:
        return data[vowel:]+"-"+data[:vowel].lower()+"ay"

def main():
    data=input("Write an english sentence: ")
    output=[]
    for word in data.split(' '):
        output.append(piggie(word))
    print(' '.join(output))

main()

