# 1. create variable to store your name, age, city and salary then print them.

name = input("Enter your full name: ")
age = int(input("Enter your age in years only: "))
city = input("Enter your city: ")
salary = int(input("Enter your monthly salary in ₹: "))
print(f"\nYour name is {name}.\nYou are {age} years old.\nYou live in {city}.\nYour monthly salary is ₹{salary}.")
print("\n\n")

# 2. swap the values of two variables using both the traditional method and python's tuple unpacking.
# traditional method
a = 20
b = 30
print(f"original value:{a} and {b}")
c = a
a = b
b = c
print(f"swapped values: {a} and {b}")
a=20
b=90
print(f"original value:{a} and {b}")
a,b=b,a
print(f"swapped values: {a} and {b}")
print("\n\n")

# 3. accept 2 numbers from the user and print their sum

num1 = int(input("Enter first number to get the number: "))
num2 = int(input("Enter second number: "))
print("The sum of given 2 numbers is: ",num1+num2)
print("\n\n")


# 4. create variables of type int,float,str,bool and display their data types using type()

a = 9
print(type(a))
a = 45.5
print(type(a))
a = "Chirag Aggarwal"
print(type(a))
a = True
print(type(a))
print("\n\n")

# 5. create 3 variables with 1 statement and print them

a,b,c = 10,20,30
print(a,b,c,sep="\n")
print("\n\n")

# 6. assign the same value to 3 variables and verify the result

a=b=c=10
print(a)
print(b)
print(c)
print("\n\n")

# 7. delete a variable using del and observe the error when trying to access it

a = 10
del a
print(a)
print("\n\n")

# 8. write a program to input your age and print:
#           You are<age>years old

age = int(input("Enter your age in years only: "))
print(f"You are {age} years old")
print("\n\n")

# 9. write a program to input the first name and last name separatelly and display full name in a single line.

first = input("Enter your first name: ")
last = input("Enter your last name: ")
print(first,last)
print("\n\n")

# 10. write a program to input an emplloyee's name and monthly salary, then display the annual salary.

employee_name = input("Enter enployee's name: ")
sal = int(input("Enter employee's monthly salary in ₹: "))
annual = sal*12
print(f"{employee_name}, your annual salary is ₹{annual}.")