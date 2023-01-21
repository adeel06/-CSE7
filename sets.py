def abbreviate(a_string):
    output=""
    for word in a_string.split(" "):
        output+=word[0]
        for char in word[1:]:
            if char.lower() not in "aeiou":
                output+=char
        output+=' '
    return output[:-1]

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

print('Part A')
print(set1.issubset(set2))

print('Part B')
print(set1.intersection(set3)==set())

print('Part C')
print(set1.union(set2))

print("Part D")
print(set2.intersection(set3))

print('Part E')
print('Method 1')

print(set1-set2)
print("Method 2")

print(set1.difference(set2))

print("Part F")
set1.discard(5)
print(set1)