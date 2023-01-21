def power (x, n):       # raise x to the n'th power
    if n == 0:
        return 1.0    # base case
    elif n > 0:
    	if n%2==0:
     		return power(x,n/2)**2
    	return x * power(x, n-1)
    else:
        return 1.0 / power (x, -n)

# 12