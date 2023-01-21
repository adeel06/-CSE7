6height = int(input("How tall do you want your right triangle to be?:"))

for i in range(1,height+1):
   for j in range(1,height+1):
       if(j<i):
           print(end=" ")
       else:
           print("*",end="")
   print()
# prior code typed in CS50 by myself to try to figure out how to do this without needing
# a nested for loop. Couldn't figure it out.
# for i in range(0, h):
#     hashtag = i + 1
#     space = w - hashtag
# #print spaces in triangle
#     print(" " * space, end="")
#     #print hashes in triangle
#     print("#" * hashtag)