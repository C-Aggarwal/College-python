# organizing a program using multiple functions

# 16. student marks program: create a program using separate functions: input_marks(), calculate_total(), calculate_average(),
# display_result(). program should be accept marks of 5 subjects & display total, average and result

print("Solution 16\n")
def input_marks():
    print("Enter the marks of 5 subjects consecutively:\n")
    mark=[]
    for i in range(1,6):
        b=int(input(f"Input marks of subject {i}: "))
        mark.append(b)
    calculate_total(mark)
def calculate_total(marks):
    s=sum(marks)
    calculate_average(marks,s)
def calculate_average(marks,sumation):
    average=sumation/len(marks)
    display_result(marks,sumation,average)
def display_result(mark,s,avg):
    print("\n\tMarksheet")
    for i in range(0,5):
        print(f"Subject {i+1}   : {mark[i]}")
    print(f"\nTotal marks  : {s}")
    print(f"Average marks: {avg}%")
    if avg>45:
        print("\nStatus       : Pass")
    else:
        print("\nStatus       : Fail")
input_marks()

# 17. Simple Calculator: Organise a calculator program using separate functions: add(), subtract(), multiply(), divide()
# The main program should ask the user for two numbers and an operation.

print("\n\nSolution 17\n")
def add(a,b):
    print(f"{a} + {b} = {a+b}")
def sub(a,b):
    print(f"{a} - {b} = {a-b}")
def pro(a,b):
    print(f"{a} * {b} = {a*b}")
def div(a,b):
    print(f"{a} / {b} = {a/b}")
a=int(input("Enter 1st operand: "))
b=int(input("Choose operation from below(1-4):\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter: "))
c=int(input("Enter 2nd  operand: "))
if b==1:
    add(a,c)
elif b==2:
    sub(a,c)
elif b==3:
    pro(a,c)
elif b==4:
    if c!=0:
        div(a,c)
    else:
        print("Divisor cannot be 0.")
else:
    print("Invalid operation!")

# 18. Electricity Bill: Create a program using functions: get_units(), calculate_bill(), display_bill()
# Calculate electricity bill based on units consumed.

print("\n\nSolution 18\n")
def get_units():
    unit = int(input("Enter electricity used(in kW/h)(+ve integer only): "))
    calculate_bill(unit)
def calculate_bill(unit):
    bill=-1
    if unit>=0 and unit<=100:
        bill = unit*5
        display_bill(unit,bill)
    elif unit>=101 and unit<=300:
        bill = 500+((unit-100)*7)
        display_bill(unit,bill)
    elif unit>300:
        bill = 500+1400+((unit-300)*10)
        display_bill(unit,bill)
    else:
        print("Invalid units!")
def display_bill(unit,bill):
    if bill>-1:
        print(f"Electricity bill for {unit}kwh: ₹{bill}")
get_units()

# 19. Shopping Bill: Create separate functions: input_items(), calculate_total(), calculate_discount(), generate_bill()
# The program should accept item prices and quantities and finally display the bill.

print("\n\nSolution 19\n")
def input_items():
    a=[]
    name=""
    print("Enter item name as \"done\" when finished.")
    while name.lower()!="done":
        name=input("Enter the item name: ")
        if name.lower()!="done":
            price=int(input(f"Enter the price of 1 unit of {name}: ₹"))
            quantity=int(input(f"Enter the quantity of {name}: "))
            print("")
            total=price*quantity
            if price>=0 and quantity>=0:
                a.append({"Name":name,"Price":price,"Quantity":quantity,"Total":total})
            else:
                print("Invalid input!")
        else:
            calculate_total(a)
def calculate_total(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]["Total"]
    calculate_discount(a,s)
def calculate_discount(a,s):
    dis = input("Enter which discount you have:\n1. 5% of total\n2. 8% of total\n3. 10% of total\n4. 15% of total\n5. 0% of total\nChoice: ")
    if dis=='1':
        disc=0.05
        generate_bill(a,s,disc*s)
    elif dis=='2':
        disc=0.08
        generate_bill(a,s,disc*s)
    elif dis=='3':
        disc=0.1
        generate_bill(a,s,disc*s)
    elif dis=='4':
        disc==0.15
        generate_bill(a,s,disc*s)
    elif dis=='5':
        disc=0
        generate_bill(a,s,disc*s)
    else:
        print("Invalid choice! Hence 0% discount as a default will be entered")
        disc=0
        generate_bill(a,s,disc*s)
def generate_bill(a,s,dis):
    print(f"\n\n{"SHOPPING BILL":^60}\n")
    b=len(a)
    print(f"{"Item Name":<15}{"Price(in ₹)":>15}{"Quantity":>15}{"Total":>15}")
    for i in range(0,b):
        print(f"{a[i]["Name"]:<15}{a[i]["Price"]:>15}{a[i]["Quantity"]:>15}{a[i]["Total"]:>15}")
    print(f"\n\tDiscount   : ₹{dis}\n\tGrand total: ₹{s-dis}")
input_items()

# 20. Number Analysis Program: Create a program using separate functions:
# input_number(), check_even_odd(), check_prime(), find_factorial(), display_result()
# The program should accept a number and display all the required results.

print("\n\nSolution 20\n")
def input_number():
    a=int(input("Enter a positive integer: "))
    check_even_odd(a)
def check_even_odd(a):
    if a%2==0:
        b="EVEN"
    else:
        b="ODD"
    check_prime(a,b)
def check_prime(a,b):
    c=0
    if a<=1:
        p="NEITHER PRIME NOR COMPOSITE"
    else:
        for i in range(1,a):
            if a%i==0:
                c+=i
        if c>1:
            p="NOT PRIME"
        else:
            p="PRIME"
    find_factorial(a,b,p)
def find_factorial(a,b,c):
    f=1
    if a==1 or a==0:
        f=1
    else:
        for i in range(1,a+1):
            f=f*i
    display_result(a,b,c,f)
def display_result(a,b,c,f):
    print(f"\nNumber={a}\n{a} is {b}\n{a} is {c}\nFactorial of {a}={f}")
input_number()

# Think and organize

# 21. Convert this program into functions
# Given: name = input("Enter name: ")
# marks = []
# for i in range(5):
#      marks.append(int(input("Enter marks: ")))
# total = sum(marks)
# average = total / 5
# if average >= 40:
#     result = "Pass"
# else:
#     result = "Fail"
# print("Name:", name)
# print("Total:", total)
# print("Average:", average)
# print("Result:", result)
# Task: Divide this program into at least 4 meaningful functions.

print("\n\nSolution 21\n")
marks=[]
def data():
    name=input('Enter your name: ')
    for i in range(5):
        marks.append(int(input("Enter marks: ")))
    avg(name)
def avg(n):
    s=sum(marks)
    res(n,s,s/5)
def res(n,s,m):
    if m>=40 and m<=100:
        dis(n,s,m,"PASS")
    else:
        dis(n,s,m,"FAIL")
def dis(n,s,m,a):
    print("Name:", n)
    print("Total:", s)
    print("Average(in %):", m)
    print("Result:", a)
data()

# 22. Find the problem. Consider:

print("\n\n")
def calculate(a, b):
    print(a + b)
result = calculate(10, 20)
print(result)

# What will be the output? Why doesn't result contain 30?
print("Solution 22")
print("Output: 30\nNone\nAs there is no return function in user-defined function calculate(a,b), therefore, result gets no value assigned to it and is displayed as none")

# 23. Function Calling Function. Create the following functions:
# get_number(), square(), cube(), display()
# get_number() should provide a number to square() and cube(), and display() should display the results.

print("\n\nSolution 23\n")
def get_number():
    num = float(input("Enter a number: "))
    sq_result = square(num)
    cb_result = cube(num)
    display(num, sq_result, cb_result)
def square(n):
    return pow(n,2)
def cube(n):
    return pow(n,3)
def display(original, sq, cb):
    print(f"\n--- Results ---")
    print(f"Original Number: {original}")
    print(f"Square:          {sq}")
    print(f"Cube:            {cb}")
get_number()

# 24. Menu-Driven Program. Create a menu-driven program using functions:
# 1. Check Even/Odd
# 2. Check Prime
# 3. Find Factorial
# 4. Find Square
# 5. Exit
# Each operation must be implemented using a separate function.

print("\n\nSolution 24\n")
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."
def check_prime(number):
    if number <= 1:
        return f"{number} is not a Prime number."
    c=0
    for i in range(1, number):
        if number % i == 0:
            c+=i
    if c==1:
        return f"{number} is a Prime number."
    else:    
        return f"{number} is not a Prime number."
def find_factorial(number):
    if number < 0:
        return "Factorial cannot be calculated for negative numbers."
    f = 1
    for i in range(1, number + 1):
        f *= i
    return f"The factorial of {number} is {f}."
def find_square(number):
    return f"The square of {number} is {number ** 2}."
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Check Even/Odd")
        print("2. Check Prime")
        print("3. Find Factorial")
        print("4. Find Square")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Exiting the program")
            break
        elif choice in [1,2,3,4]:
            num = int(input("Enter an integer: "))
            if choice == 1:
                a=check_even_odd(num)
                print(a)
            elif choice == 2:
                a=check_prime(num)
                print(a)
            elif choice == 3:
                a=find_factorial(num)
                print(a)
            elif choice == 4:
                a=find_square(num)
                print(a)
        else:
            print("Invalid choice! Please choose a valid option from the menu.")
main()

# 25. Mini Project – Student Management. Organise a program using functions to:
# Accept student name and marks
# Calculate total
# Calculate average
# Determine grade
# Display result
# Condition: main() should control the complete program, while each individual task should be performed by a separate function.

print("\n\nSolution 25\n")
def accept_details():
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    for i in range(num_subjects):
        m = int(input(f"Enter marks for subject {i + 1}: "))
        marks.append(m)
    return name, marks
def calculate_total(marks):
    total = sum(marks)
    return total
def calculate_average(total, num_subjects):
    average = total / num_subjects
    return average
def determine_grade(average):
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return grade
def display_result(name, marks, total, average, grade):
    print("\n---- Student Report ----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print(f"Average: {average:.2f}")
    print("Grade:", grade)
def main():
    name, marks = accept_details()
    num_subjects = len(marks)
    total = calculate_total(marks)
    average = calculate_average(total, num_subjects)
    grade = determine_grade(average)
    display_result(name, marks, total, average, grade)
main()