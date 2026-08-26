# 1. create a tuple of 5 integers and print all elements. access the first, last, and the middle elements of a tuple.

num = (7,1,2,3,4)
x,*y,z = num
print(f"The tuple: {num}\nFirst elemment: {x}\nMiddle elements: {y}\nLast element: {z}")
print("\n\n")

# 2. count occurrence of a specific value. also, find the index of a given index

value = (4,5,4,7,9,6,551)
no = value.count(4)
print(f"Tuple:\n{value}\nNo. of occurence of 4: {no}\nIndex of 551: {value.index(551)}")
print("\n\n")

# 3. concatenate 2 tuples and display the result. also, repeat a tuple 3 times

a = ("Chirag","Lavish")
b=("Abhishek","Aditya")
print(f"original two:\n{a}\n{b}\nconcanated: {a+b}\nrepeated first:\n{a*3}")
print("\n\n")

# 4. reverse a tuple using slicing, find max,min,sum and average

num = (10,20,40,50,31)
rev = num[::-1]
max1 = max(num)
min1 = min(num)
sum1 = sum(num)
avg = sum1/len(num)
print(f"Original: {num}\nReversed: {rev}\nMaximum: {max1}\nMinimum: {min1}\nSum: {sum1}\nAverage:{avg}")
print("\n\n")

# 5. convert a list into a tupleand a tuple into a list

a = (25,50,75,100,125)
print(f"Original tuple: {a}\n{type(a)}")
b= list(a)
print(f"Converted list: {b}\n{type(b)}")
c=tuple(b)
print(f"Converted tuple: {c}\n{type(c)}")
print("\n\n")

# 6. perform tuple packing and unpacking for student details. demonstrate extended unpacking

a = 10,20,58
x,y,z = a
print(f"tuple packing: {a}\ntuple unpacking:\n{x}\n{y}\n{z}")
*b,c=a
print(f"extended unpacking:\n{b}\n{c}")
print("\n\n")

# 7. create a nested tuple and access inner elements

tup = (10,20,(225,50,75,100),40,50)
inn = tup[2][:]
print(f"Tuple: {tup}\nInner elements: {inn}")
print("\n\n")

# 8. store student records as tuples inside a list and display names with marks

stud = [("Ravi",80),("Ramesh",85),("Raju",75)]
a,b,c = stud
print(a,b,c,sep="\n")
print("\n\n")

# 9. swap 2 variables using tuple unpacking

a=20
b=90
a,b=b,a
print(f"original value:{a} and {b}\nswapped values: {a} and {b}")
print("\n\n")

# 10. genertae squares of no. from 1 to 10 and store them in a tuple using tuple(x*x for x in range(1,11))

square = tuple(x*x for x in range(1,11))
print(square)