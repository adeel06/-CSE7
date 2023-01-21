# n = input("Enter Countries Names: ")
# m = int(input("Enter Countries Medal Count: "))
# medal_tally(countries,count)
# https://realpython.com/python-string-formatting/ - String Interpolation
# For fun


MEDALS = 3
COUNTRIES = 8

def medal_tally(countries, count):
  # countries = ["Canada", "Italy","Germany", "Japan", "Kazakhstan", "Russia", "South Korea", "United States"]
  # count = [ [ 0, 3, 0 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 1, 0, 0 ], [ 0, 0, 1 ], [ 3, 1, 1 ], [ 0, 1, 0 ], [ 1, 0, 1 ] ]

  for ele in range(len(countries)):
    print(f"{countries[ele]: >56}{count[ele][0]: >8d}{count[ele][1]: >8d}{count[ele][2]: >8d}{sum(count[ele]): >8d}")

# Country with the longest name - https://www.worldatlas.com/articles/what-is-the-longest-country-name-in-the-world.html
# This is so any country can be added but the table will still look the same.
# as The United Kingdom of Great Britain and Northern Ireland has 56 characters

countries = ["Canada", "Italy","Germany", "Japan", "Kazakhstan", "Russia", "South Korea", "United States"]
count = [ [ 0, 3, 0 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 1, 0, 0 ], [ 0, 0, 1 ], [ 3, 1, 1 ], [ 0, 1, 0 ], [ 1, 0, 1 ] ]

medal_tally(countries, count)