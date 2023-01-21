#imported random module and read https://www.w3schools.com/python/module_random.asp for information on using it


import random
alpha = "abdefghijklmnopqrstuvwxyz".upper()

for i in range(20):
    plate = ""
    plate += str(random.randint(1,9))
    plate += str(random.randint(0,9))
    plate += str(random.randint(0,9))
    plate += " "
    for j in range(3):
        plate += random.choice(alpha)
    print(plate)

