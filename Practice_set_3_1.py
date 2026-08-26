# 1. create a list of your 5 favourite movies and display it

movie = ["Avatar","Avatar: The way of water","Spider Man 3","The amazing spider-man 2","Transformers"]
print("The list of 5 movies:\n",movie)
print("\n\n")

# 2. create a list containing 10 numbers and display: First, Last, Middle element

number= [84,468,84,684,115,64,46,6,558,846]
x,*y,z = number
print(f"The list: {number}\nFirst elemment: {x}\nMiddle elements: {y}\nLast element: {z}")
print("\n\n")

# 3. create a list of 5 cities and print the list in reverse order using slicing

cities = ["Delhi","Jaipur","Srinagar","Merrut","Ghaziabad"]
rev = cities[::-1]
print(f"Original list = {cities}\nReversed list = {rev}")
print("\n\n")

# 4. create 2 list of 5 no. and combine

a = [5,6,7,8,9]
b=[0,1,2,3,4]
c=b+a
print(f"Combined list = {c}")
print("\n\n")

# 5. create a list and show it 3 times

a = ['a','b','d','f']
print("Printing list 3 times:\n",a*3)
print("\n\n")

# 6. create a list of 5 fruits and add one more fruit. now, insert your favorite colour at second position of a list 

fruit = ["Apple","Mango","Pineapple","Kiwi","Berry"]
print(fruit)
fruit.insert(1,"Sky Blue")
print(fruit)
print("\n\n")

# 7. Create 2 lists & combine them using 'extend()'. now, remove last element

a = [5,4,6,1,2]
b=[7,8,9,3]
print(a)
print(b)
a.extend(b)
print(a)
print("\n\n")

# 8. remove the third element using 'del'. now, remove all elements

a = [58,89,9,59,846,85]
print(f"Original list: {a}")
del(a[2])
print(f"removed 3rd element: {a}")
a.clear()
print(f"removed all elements: {a}")
print("\n\n")

# 9. create a list of numbers and sort it in ascending and descending order

num = [42,53,43,57,23,453,35,22,765,8]
print(f"Unsorted list: {num}")
num.sort()
print(f"Ascending order: {num}")
num.sort(reverse=True)
print(f"Descending order: {num}")
print("\n\n")

# 10. reverse a list using the 'reverse()' method

stud = [2502311530025,"Chirag Aggarwal","2-D","CSE-AIML"]
print(f"Original list: {stud}")
stud.reverse()
print("Reversed list: ",stud)
print("\n\n")

# 11. create a copy of list using 'copy()' and print both lists

org = [0,1,2,3,4]
cop = org.copy()
print(f"Original: {org}\nCopy: {cop}")
print("\n\n")

# 12. create a list containing duplicate values and count the occurrence of a particular value using 'count()'

a = [54,43,46,54,33,5,'$']
num = a.count(54)
print(f"Number of occurences of 54 in list {a} is: {num}")
print("\n\n")

# 13. find the index of a given element using the 'index()'

a=[65,1,"see","heart","Liver",346]
ind = a.index("heart")
print(f"Index of \'heart\' in list {a} is: {ind}")
print("\n\n")

# 14. create a nested list representing 3x3 matrix and print it.

matrix = [[5,4,6],[8,1,5],[4,2,5]]
a,b,c = matrix
print(a,b,c,sep="\n")
print("\n\n")

# 15. perform the following slicing operations on a list of numbers from 1 to 10: first 5 elements, last five elements,
# every second element, reverse the list

num =[1,2,3,4,5,6,7,8,9,10]
print(f"Original list:\n{num}\nFirst five elements:\n{num[:5]}\nLast five elements:\n{num[-1:-6:-1]}\nReversed list:\n{num[::-1]}")