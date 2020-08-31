# Lists in python
print("List is a sequence of values (similar to an array in other programming languages but more versatile)")
print("A list can be a list of integer, boolean, string, float, complex numbers and a combination of all of this")

L = [1, 2, 3]
M = ['red','orange','green']
N = [1, 'deenamma_jeevitham', 1.23, (3+4j), True]
print(L, '  ', M, '  ', N)

print("A list can be empty and still exist")
P = []
print (P)

print("you can convert other data types to lists using Python's list() constructor.")

# Convert a string to a list
B = list('abc')
print(B)
# this will print ['a', 'b', 'c']

# Convert a tuple to a list
L = list((1, 2, 3))
print(L)
# this will print [1, 2, 3]

print("Nested Lists")
print("A list can contain sublists, which in tun can contain sublists themselves, and so on. This is known as nested list")
print("You can use them to arrange data into hierarchical structures.")
print("A nested list is created by placing a comma-seperated sequence of sublists.")

L = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

print("Nested list items can be accessed by indexes or by value")
print(L[2])
####  print(L[2][1])
print(L[1][1][1])
# -----------------------------------------------------------        )
print(L[1][1][0])

print("Negative List Indexing in a Nested List is permitted")
print("Negative index count backward from the end of the list. So L[-1] refers to the last item, L[-2] is second last item and so on")
print(L[-3])
print(L[-3][-1])
print(L[-3][-3][-2])

print("Change Nested List Item Value")
L[1][1] = 0
print(L)

print("To add new values to the end of the nested list use append() method")
L[1].append('xx')
print(L)

print("When you want to insert an item at a specific position in a nested list, use insert() method.")
L[1].insert(0,'mmm')
print(L)

print("You can merge one list into another by using extend() method.")
L[1].extend([1,2,3])
print(L)

print("Remove items from nested list")
x = L[1].pop(2)
print (x)
print (L)

print("If you do not need the removed item use 'del' statement")
del L[1][1]
print(L)

print("If you are not sure where the item is in the list, use remove() method o delete it by value")
L.remove('g')
print(L)

print("You can use the built-in len() function to find how many items a list and a nested sublist has.")
print(len(L))
print(len(L[1]))

print("Iterate through a Nested List")
print("To iterate over the items of a nested list, use simple for loop.")
Li = [[1,2,3], [4,5,6], [7,8,9]]
for list in Li:
    for number in list:
        print(number, end=' ')


print ("There is a lot to cover in list comprehension and lambda today")




