# Write A Program::

# 1. to calculate average of first n natural number. where n is entered by the user

print("Solution 1\n")
n=int(input("Enter the natural number till which average is required: "))
sum=0
for i in range(1,n+1):
    sum+=i
avg = sum/n
print("Average is:",avg)

# 2. to print the multiplication table of n. where n is to be entered by the user

print("\n\nSolution 2\n")
n = int(input("Enter a number to get it's table: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# 3. to calculate factorial of n

print("\n\nSolution 3\n")
n = int(input("Enter the number to get factorial: "))

if n < 0:
    print("Invalid input!")
else:
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("factorial =", f)

# 4. to calculate power(x,n)

print("\n\nSolution 4\n")
x = int(input("Enter the number to get it's exponential: "))
n = int(input("Enter power: "))
r=1
for i in range(1,n+1):
    r=r*x
print("Answer =",r)

# 5. to sum the series ---- 1+1/2+1/3+.......+1/n

print("\n\nSolution 5\n")
n = int(input("Enter nth digit of the series: "))
if n<=0:
    print("Invalid input!")
else:
    s=0
    for i in range(1,n+1):
        s=s+(1/i)
    print("Sum =",s)

# 6. to generate the calender of a month given the start day and no of days in the month

print("\n\nSolution 6\n")
start_day = int(input("Enter start day of month (0=Mon 1=Tue 2=Wed 3=Thr 4=Fri 5=Sat 6=Sun): "))
num_days = int(input("Enter number of days in the month: "))
print("\nMon Tue Wed Thu Fri Sat Sun")
for i in range(0,start_day):
    print("    ", end="")
day_of_week = start_day
for day in range(1, num_days + 1):
    if day<10:
        print(f"{day}   ", end="")
    else:
        print(f"{day}  ", end="")
    day_of_week += 1
    if day_of_week % 7 == 0:
        print()

# 7. to print the following patterns
print("\n\nSolution 7\n")
# *
# **
# ***
# ****
# *****

for i in range(1,6):
    print("*"*i)

# 1
# 12
# 123
# 1234
# 12345

for i in range(1,7):
    for j in range(1,i):
        print(j,end="")
    print("")

# 1
# 22
# 333
# 4444
# 55555

for i in range(0,6):
    for j in range(0,i):
        print(i,end="")
    print("")

# 0
# 12
# 345
# 6789

a=0
for i in range(1,6):
    for j in range(1,i):
        print(a,end="")
        a+=1
    print("")

#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

for i in range(0,7):
    for j in range(0,7-i):
        print(" ",end="")
    for k in range(1,i):
        print(k,"",end="")
    print("")

#     1
#    121
#   12321
#  1234321
# 123454321

k=0
for i in range(0,7):
    for j in range(0,7-i):
        print(" ",end="")
    for k in range(1,i):
        print(k,end="")
    if i>0:
        for t in range(k-1,0,-1):
            print(t,end="")
    print("")

#     1
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5
print("")
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(0,i):
        print(i,"",end="")
    print("")