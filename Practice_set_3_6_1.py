# Single Function Program

# Write A Function: (ques 1 to 15)

# 1. greet() that prints "Welcome to Python Programming"

print("\n\nSolution 1\n")
def greet():
    print("Welcome to Python Programming")
greet()

# 2. square(n) that accepts a number and returns its square

print("\n\nSolution 2\n")
def square(n):
    return n**2
a = int(input("Enter a number to get it's square: "))
print("Square =",square(a))

# 3.  is_even(n) that returns True if number is even, otherwise False

print("\n\nSolution 3\n")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(21,"is even:",is_even(21))

# 4. maximum(a,b) that returns the larger of the 2 number 

print("\n\nSolution 4\n")
def maximum(a,b):
    if a>b:
        print(f"{a} is greater than {b}")
    elif a<b:
        print(f"{a} is lesser than {b}")
    else:
        print(f"{a} is equal than {b}")
a = int(input("Enter no.: "))
b= int(input("Enter 2nd no.: "))
maximum(a,b)

# 5. calculate_area(radius) that claculates and returns the area of a circle

print("\n\nSolution 5\n")
def calculate_area(r):
    pi = 3.14
    return (pi*(r*r))
radius = int(input("Enter the radius of the circle(in cm): "))
print(f"Area = {calculate_area(radius)} square cm")

# 6. calculate(a,b) that returns the sum, difference, product, and division of two numbers

print("\n\nSolution 6\n")
def calculate(a,b):
    return a+b,a-b,a*b,a/b
a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))
s,d,p,r= calculate(a,b)
print(f"Sum: {s}\nDifference: {d}\nProduct: {p}\nDivision: {r}")

# 7. student_result(marks) that accepts a list of marks and returns:
# total marks, average marks, highest marks, lowest marks

print("\n\nSolution 7\n")
def student_result(marks,n):
    total=sum(marks)
    average = total/n
    high=max(marks)
    low=min(marks)
    return (total,average,high,low)
n = int(input("Enter the number of subjects: "))
a=[]
for i in range(0,n):
    b=int(input("Enter marks: "))
    a.append(b)
total,average,high,low=student_result(a,n)
print(f"Total marks: {total}\nAverage marks: {average}%\nHighest marks: {high}\nLowest marks: {low}")

# 8. count_vowels(text) that accepts a string and returns the number of vowels in it

print("\n\nSolution 8\n")
def count_vowels(text):
    v=0
    for i in text:
        if i.lower() in ("a","e","i","o","u"):
            v+=1
    return v
a = "The curious cat chased a red ball across the wooden floor."
b = count_vowels(a)
print(f"Sentance:\n{a}\nNo. of vowels: {b}")

# 9. reverse_number(n) that returns the reverse of a number

print("\n\nSolution 9\n")
def reverse_number(n):
    return int(n[::-1])
a = 76543567654
b=reverse_number(str(a))
print(f"Original number: {a}\nReverse number: {b}")

# 10. factorial(n) that returns teh factorial of a number

print("\n\nSolution 10\n")
def factorial(n):
    f=1
    if n==1 or n==0:
        return f
    elif n>1:
        for i in range(1,n+1):
            f=f*i
        return f
a = int(input("Enter a number to get its' factorial: "))
if a<0:
    print("Invalid input!")
else:
    print("Factorial =",factorial(a))

# 11. check_primr(n) that returns whether a number is prime or not

print("\n\nSolution 11\n")
def check_prime(n):
    if n==1 or n==0:
        print("Neither prime nor composite")
    elif n<0:
        print("Negative integers are not accepted")
    else:
        c=0
        for i in range(1,n):
            if n%i==0:
                c=c+1
        if c==1:
            print("Given number is prime")
        else:
            print("Given number is not prime")
a = int(input("Enter a number to check if it is prime or not: "))
check_prime(a)

# 12. print_table(n) that prints the multiplication table of n.

print("\n\nSolution 12\n")
def print_table(n):
    print("Multiplication table is given below:")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
a = int(input("Enter the number to get its' table: "))
print_table(a)

# 13. sum_of_digits(n) that returns the sum of digits of a number

print("\n\nSolution 13\n")
def sum_of_digits(n):
    s=0
    b=str(n)
    for i in b:
        s=s+int(i)
    return s
a = int(input("Enter a number to get the sum of its' digits: "))
c=sum_of_digits(a)
print("Sum =",c) 

# 14. count_numbers(numbers) that accepts a list and returns the number of:
# +ve numbers, -ve numbers, 0

print("\n\nSolution 14\n")
def count_numbers(numbers):
    p=n=z=0
    for i in numbers:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    return n,p,z
num=[]
a=int(input("Enter the size of list: "))
for j in range(0,a):
    b=int(input("Enter number: "))
    num.append(b)
n,p,z=count_numbers(num)
print(f"No. of positive integers: {p}\nNo. of negative integers: {n}\nNo. of zeros: {z}")

# 15. get_grade(marks) that returns the grages according to:
# 90-100->A,  80-89->B, 70-79->C, 60-69->D, Below 60->F

print("\n\nSolution 15\n")
def get_grade(marks):
    if marks<=100 and marks>=90:
        return "A"
    elif marks<=89 and marks>=80:
        return "B"
    elif marks<=79 and marks>=70:
        return "C"
    elif marks<=69 and marks>=60:
        return "D"
    else:
        return "F"
a=int(input("Enter marks to get grades: "))    
if a>=0 and a<=100:
    b=get_grade(a)
    print("Your grade is:",b)
else:
    print("Invalid input!")