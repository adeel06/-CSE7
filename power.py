def power (x, n):       # raise x to the n'th powe
    if n == 0:
        return 1.0    # base case
    elif n > 0:
    	if n%2==0:
     		return power(x,n/2)**2
    	return x * power(x, n-1)
    else:
        return 1.0 / power (x, -n)
    print(power)
#TESTING AROUND
x = 3.14159052
n = 5                                                                                      
print(power(x, n))

#

#Total number of calls log2(1024) = 10
#Answer is 10

# 1^2 = 1 2^2 = 4 3^2= 9 4^2 = 16 5^2 = 25 6^2 = 36 7^2 = 49 64 81 100 121 144