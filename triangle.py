#Write a program that produces the output in problem 16

#set initial variable equal to x
x=0

#iterate over 9 times, including the first instance in which i = 100
for i in range(1,10):
    y=i*100
    for j in range(i):
        #print y, add spacing
        print(y,end="    ")
        #y=x+y for every j depending on range (i)
        y=x+y
    #add 2 to itself x for every i in range 1,10
    x+=2
    print()

