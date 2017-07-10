arr = [6,3,9,7]
len(arr) #> 4
min(arr) #> 3
max(arr) #> 9

Add an element to the end of a list:
arr = ["a", "b", "c", "d"]
arr.append("e") # this is a mutating operation
arr #> ["a", "b", "c", "d", "e"]

Concatenate two lists:
arr = ["a", "b", "c", "d"]
arr2 = ["x", "y", "z"]
arr3 = arr + arr2
arr3 #> ["a", "b", "c", "d", "x", "y", "z"]

Sort a list:
arr = [6,3,8]
arr.sort() # this is mutating
arr #> [3, 6, 8]
arr.reverse() # this is mutating
arr #> [8, 6, 3]

Remove duplicate values in a list by converting it to another datatype called a "Set" and then converting it back to a "List":

arr = [1,2,2,2,3]
arr2 = list(set(arr))
arr2 #> [1, 2, 3]
list(set(["hello", "hello", "hello"])) #> ['hello']


A list can be iterated, or "looped" using a for ... in ... statement:

for letter in ["a", "b", "c", "d"]:
    print(letter)

#> a
#> b
#> c
#> d


A common pattern is to loop through one list to populate the contents of another:
arr = [1, 2, 3, 4]
arr2 = []

for i in arr:
  arr2.append(i * 100)

arr #> [1, 2, 3, 4]
arr2 #> [100, 200, 300, 400]

Lists can be looped "in-place" using Python's built-in map() function. The map() function takes two parameters. The first parameter is the name of a pre-defined function to perform on each item in the list. The function should accept a single parameter representing a single list item. The second parameter is the actual list to be operated on.

arr = [1, 2, 3, 4]

def enlarge(num):
    return num * 100

arr2 = map(enlarge, arr)

# Python 2.x:
arr2 #> [100, 200, 300, 400]

# Python 3.x:
arr2 #> <map object at 0x10c62e710>
list(arr2) #> [100, 200, 300, 400]


Use the filter() function to select a subset of items from a list - only those items matching a given condition. The filter function accepts the same parameters as the map() fuction:
arr = [1,2,4,8,16]

def all_of_them(i):
    return True # same as ... return i == i

def equals_two(i):
    return i == 2

def greater_than_two(i):
    return i > 2

def really_big(i):
    return i > 102

# Python 2.x:
filter(all_of_them, arr) #> [1, 2, 4, 8, 16]
filter(equals_two, arr) #> [2]
filter(greater_than_two, arr) #> [4, 8, 16]
filter(really_big, arr) #> []

# Python 3.x:
filter(all_of_them, arr) #> <filter at 0x103fa71d0>
list(filter(all_of_them, arr)) #> [1, 2, 4, 8, 16]
list(filter(equals_two, arr)) #> [2]
list(filter(greater_than_two, arr)) #> [4, 8, 16]
list(filter(really_big, arr)) #> []

If your list is full of dictionaries, you can filter() based on their attribute values:
teams = [
    {"city": "New York", "name": "Yankees"},
    {"city": "New York", "name": "Mets"},
    {"city": "Boston", "name": "Red Sox"},
    {"city": "New Haven", "name": "Ravens"}
]

def yanks(obj):
    return obj["name"] == "Yankees"

def from_new_york(obj):
    return obj["city"] == "New York"

def from_new_haven(obj):
    return obj["city"] == "New Haven"

def from_new_something(obj):
    return "New" in obj["city"]

# Python 2.x:
print(filter(yanks, teams)) #> [{...}]
filter(from_new_york, teams) #> [{...}, {...}]
filter(from_new_haven, teams) #> [{...}]
filter(from_new_something, teams) #> [{...}, {...}, {...}]

# Python 3.x:
list(filter(yanks, teams)) #> [{...}]
list(filter(from_new_york, teams)) #> [{...}, {...}]
list(filter(from_new_haven, teams)) #> [{...}]
list(filter(from_new_something, teams)) #> [{...}, {...}, {...}]
