# Write a function
# rhymes_with(suffix, words)
# that takes a string suffix
# and a list words and returns a
# list of words in words that end
# with the given suffix. For example
# rhymes_with('ate', ['date', 'rate', 'foo'])
# should return ['date', 'fate'].

name = "adeel"


letters = []
for letter in name:
    if letter in "aeiou":
        letters.append(letter)


letters = [letter for letter in name if letter in "aeiou"]

