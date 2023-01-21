def digit_sum (n):
     if  n < 10:
          return n # base case
     else:
          #return int(str(n)[0])+digit_sum(int(str(n)[1:]))
          #the above has a slower time complexity, the bottom has only 2 operators
          return n%10 + digit_sum(n//10)



print(digit_sum(3456))
