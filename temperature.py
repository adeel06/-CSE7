#%.1f Trucates the float to 1 decimal like the example in the problem set
celsius = float(input("Input a Celcius temperature to be converted: "))
fahrenheit = (celsius * 9/5) + 32
print('%.1f degrees Celcius equals: %.1f degrees Fahrenheit' %(celsius, fahrenheit))