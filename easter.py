# y= int(input = ("Enter a year: ")
y = int(input("Enter a year: "))
a=y%19
b=int(y/100)
c=y%100
d=int(b/4)
e=b%4
g=int((8*b+13)/25)
h=((19*a+b-d-g+15)%30)
j=int(c/4)
k=c%4
m=int(((a+11)*h)/319)
r=((2*e+2*j-k-h+m+32)%7)
n=int((h-m+r+90)/25)
p=(h-m+r+n+19)%32

# print("Then Easter falls on the day", p, "of month", n)
print("Then Easter falls on",n,"/",p)


# # y= int(input = ("Enter a year: ")
# y = int(input("Enter a year y:  "))
# a=y%19
# b=int(y/100)
# c=y%100
# d=int(b/4)
# e=b%4
# g=int((8*b+13)/25)
# h=((19*a+b-d-g+15)%30)
# j=int(c/4)
# k=c%4
# m=int(((a+11)*h)/319)
# r=((2*e+2*j-k-h+m+32)%7)
# n=int((h-m+r+90)/25)
# p=(h-m+r+n+19)%32

# # print("Then Easter falls on the day", p, "of month", n)
# print("Then Easter falls on",n,p)

# if n == 1:
#     print("January")
#     x=n
# if n == 2:
#     print("February")
#     x=n
# # if n == 3:
# #     print("March")
# #     n=x
# if n == 4:
#     print("April")
#     x=n
# # if n == 5:
# #     print("May")
# #     n=x
# # if n == 6:
# #     print("June")
# #     n=x
# # if n == 7:
# #     print("July")
# #     n=x
# # if n == 8:
# #     print("August")
# #     n=x
# # if n == 9:
# #     print("September")
# #     n=x
# # if n == 10:
# #     print("October")
# #     n=x
# # if n == 11:
# #     print("November")
# #     n=x
# # if n == 12:
# #     print("December")
# #     n=x

# print("Then Easter falls on",x,p)
