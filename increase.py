# largest_increase = 0
# initial_num = 0 #int(input("Enter stock price: "))
# days = 10
# for i in range (days):
#     price = int(input("Enter stock price: "))

#     if (i>0):
#         largest_increase = price-initial_num
#         highest_price = initial_num
#         lowest_price = price
#         initial_num = price
#         day_1 = (i)
#         day_2 = (i+1)
#         print("Largest change of "+str(largest_increase)+" from "+str(highest_price)+ " to "+str(lowest_price))
#         print("occured between day #"+str(day_1)+" and day #"+str(day_2))
#     else (price-initial_num) == largest_increase:
#         print("The price never changes")

days = 10
price_increase = 0
last_price = 0

for i in range(days):
	current_price = int(input("Enter stock price: "))

	if i > 0:
		difference = current_price - last_price

		if difference > price_increase:
			price_increase = difference
			low_price = last_price
			high_price = current_price
			day_1 = i
			day_2 = i+1

	last_price = current_price


if price_increase > 0:
	print("Largest increase of {} from {} to {}".format(price_increase, low_price, high_price))
	print("occurred between day #{} and day #{}".format(day_1, day_2))
else:
	print("Price never increases!")
