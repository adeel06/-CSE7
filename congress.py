def eligibleForSenate(age,lengthOfCitizenship):
    if age >= 30 and lengthOfCitizenship >= 9:
        return True
    return False

def eligibleForHouse(age,lengthOfCitizenship):
    if age >= 25 and lengthOfCitizenship >= 7:
        return True
    return False

def main():
    print("CONGRESS ELIGIBILITY")
    age=int(input("Enter age of candidate: "))
    lengthOfCitizenship=int(input("Enter years of U.S. Citizenship: "))
    rule_one = eligibleForSenate(age,lengthOfCitizenship)
    rule_two = eligibleForHouse(age,lengthOfCitizenship)
    if rule_one and rule_two:
        print("The candidate is eligible for election to the House of Representatives and for election to the Senate")
    elif (rule_two and not rule_one):
        print("The candidate is eligible for election to the House of Representatives but NOT eligible to the Senate")
    else:
        print("The candidate is NOT eligible for election to either the House of Representatives or the Senate")

main()