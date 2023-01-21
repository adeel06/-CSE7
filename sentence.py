def sentence_type(a_string):
    if a_string[-1] == ".":
        return "declarative"
    elif a_string[-1] == "!":
        return "exclamatory"
    elif a_string[-1] == "?":
        return "interrogative"
    else:
        return "bad ending"

def main():
    temp = "answer?"
    print(sentence_type(temp))
    temp = "answer."
    print(sentence_type(temp))
    temp = "answer!"
    print(sentence_type(temp))
    temp = "answer"
    print(sentence_type(temp))
    n = input("Enter a sentence? ")
    print(sentence_type(n))
    
main()