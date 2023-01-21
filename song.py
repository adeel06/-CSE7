#Write a Python program that produces as output the lyrics of the song, “There
# Was an Old Lady.”  Use functions for reach verse and the refrain.  Here are the
# song’s the complete lyrics:

###### This was so long. -___________________-

def printOldLady(name):
    print("There was an old lady who swallowed a %s"%(name))

def printWhy(name):
    print("I don’t know why she swallowed that %s\nPerhaps she'll die."%(name))

def printThat():
    print("That wriggled and jiggled and wiggled inside her.")

def printToCatchThe(x,y):
    print("She swallowed the %s to catch the %s"%(x,y))

def main():
    printOldLady("fly.")
    printWhy("fly,")
    print()

    printOldLady("spider,")
    printThat()
    printToCatchThe("spider", "fly.")
    printWhy("fly,")
    print()

    printOldLady("bird;")
    print("How absurd, to swallow a bird!")
    printToCatchThe("bird", "spider")
    printThat()
    printToCatchThe("spider", "fly.")
    printWhy("fly,")
    print()

    printOldLady("cat.")
    print("Imagine that, she swallowed a cat.")
    printToCatchThe("cat", "bird,")
    printToCatchThe("bird", "spider")
    printThat()
    printToCatchThe("spider", "fly.")
    printWhy("fly,")
    print()

    printOldLady("dog.")
    print("What a hog! To swallow a dog!")
    printToCatchThe("dog", "cat,")
    printToCatchThe("cat", "bird,")
    printToCatchThe("bird", "spider,")
    printThat()
    printToCatchThe("spider", "fly.")
    printWhy("fly,")
    print()

    printOldLady("goat.")
    print("Just opened her throat and swallowed a goat!")
    printToCatchThe("goat", "dog,")
    printToCatchThe("dog", "cat,")
    printToCatchThe("cat", "bird,")
    printToCatchThe("bird", "spider,")
    printThat()
    printToCatchThe("spider", "fly.")
    printWhy("fly,")
    print()

    printOldLady("cow.")
    print("I don't know how she swallowed a cow!")
    printToCatchThe("cow", "goat,")
    printToCatchThe("goat", "dog,")
    printToCatchThe("dog", "cat,")
    printToCatchThe("cat", "bird,")
    printToCatchThe("bird", "spider,")
    printThat()
    printToCatchThe("spider", "fly.")
    printWhy("fly,")
    print()

    printOldLady("horse,")
    print("She died, of course.")

main()