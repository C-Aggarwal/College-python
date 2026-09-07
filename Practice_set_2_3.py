# WRITE A PROGRAM

# 1. to print all even & odd no. separately from 1 to 50 using a loop and conditional statements

print("Solution 1\n")
odd=[]
even=[]
for i in range(1,51):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even:\n{even}")
print(f"Odd:\n{odd}")

# 2. to find the sum of all no. b/w 1 and 100 that are divisible by both 3 and 5

print("\n\nSolution 2\n")
s=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        s+=i
print("Answer =",s)

# 3. to accept 10 no. from the user and count how many are +ve, -ve, and 0 using a loop and conditional statements

print("\n\nSolution 3\n")
pos=0
neg=0
zer=0
for i in range(10):
    a=int(input("Enter a integer: "))
    if a<0:
        neg+=1
    elif a>0:
        pos+=1
    else:
        zer+=1
print("Number of +ve no.:",pos)
print("Number of -ve no.:",neg)
print("Number of 0's:",zer)

# 4. to check whether a given no. is an armstrong or not

print("\n\nSolution 4\n")
n = int(input("enter a number to check if armstrong no.: "))
a = str(n)
c = len(a)
arm=0
for i in a:
    b=int(i)
    arm=arm+(b**c)
if arm==n:
    print("Given number is armstrong.")
else:
    print("Given no. is not armstrong")

# 5. to generate the multiplication table from 1 to 5. for each table, display only those multiplies that are even

print("\n\nSolution 5\n")
for i in range(1,6):
    print("Table of",i,"even multipliers only:")
    for j in range(1,11):
        if (i*j)%2==0:
            print(f"{i} * {j} = {i*j}")

# 6. using nested loops to print the following pattern:

"""Incomplete question"""

# 7. using nested loops to print all pairs (i,j) where i and j range from 1 to 5, but display only those pairs whose sum is even.

print("\n\nSolution 7\n")
pair=[]
for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            pair.append((i,j))
print(pair)

# 8. using nested loop to print the multiplication tables from 2 to 5, with each table containing multiples from 1 to 10.
# Use a conditional statement to display only the multiples that are divisible by 3.

print("\n\nSolution 8\n")
for i in range(2,6):
    print("Table of",i,"even multipliers only:")
    for j in range(1,11):
        if (i*j)%3==0:
            print(f"{i} * {j} = {i*j}")

# 9. to print numbers form 1 to 20, but use continue to skip all no. that are divisible by 3

print("\n\nSolution 9\n")
for i in range(1,21):
    if i%3==0:
        continue
    else:
        print(i)

# 10. that repeatedly accepts no. from the user and calculates their sum . terminate the loop using break when the user enters 0

print("\n\nSolution 10\n")
a = int(input("Enter any number to get the sum of all entered numbers and enter 0 to print sum:\n"))
s=0
i=1
while i>0:
    s+=a
    a = int(input("Next number: "))
    if a==0:
        break
print("\nSum =",s)

# 11. to print numbers from 1 to 10. use pass when no. is 5 and observe that the loop continues normally. also display all the no.

print("\n\nSolution 11\n")
for i in range(1,11):
    if i==5:
        pass
    else:
        print(i)