values = [[18, 14, 29], [12, 7], [2, 22, 5]]
def cap(data,big):
    for row in data:
        for i in range(len(row)):
            if row[i] > big:
                row[i] == big
    values = [[18, 14, 29], [12, 7], [2, 22, 5]]

print(cap(values, 20))