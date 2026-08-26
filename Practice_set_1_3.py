# 1. declare one variable of each numerical of each numerical data type and print their values annd data types

integer = 58
decimal = 98.5
comp = complex(8,10)

print(f"{integer} is {type(integer)}")
print(f"{decimal} is {type(decimal)}")
print(f"{comp} is {type(comp)}")
print("\n\n")

# 2. i/p 2 integers and perform all arithmetic operations

a = 15
b = 14
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
print(f"{a} % {b} = {a%b}")
print("\n\n")

# 3. convert an integer into  a float and a complex number

a = 78
b = float(a)
c = complex(a)

print(f"{a} is {type(a)}")
print(f"{b} is {type(b)}")
print(f"{c} is {type(c)}")
print("\n\n")

# 4. create a complex no. using both 'a+bj' notation and the 'complex()' function. also pprint the real and imaginary parts of a 
# complex number.

a=21+15j
b=complex(21,15)

print(f"Real part = {a.real}")
print(f"Imaginary part = {a.imag}")
print("\n\n")

# 5. wap to calculate the average of 3 floating point no.

a = 60.1
b = 54.2
c = 15.7

print(f"Average of three floating point integers {a,b,c} = {(a+b+c)/3}")
print("\n\n")

# 6. demonstrate automatic type promotion using 'int','float' and 'complex'

a = 78
b = float(a)
c = complex(a)

print(f"{a} is {type(a)}")
print(f"{b} is {type(b)}")
print(f"{c} is {type(c)}")
print("\n\n")

# 7. wap to i/p an integer, a float and a complex no., then display their value and type

a = int(input("Enter an integer: "))
b = float(input("Enter a floating point integer: "))
c = int(input("Enter real part: "))
d = int(input("Enter imaginary part: "))
e = complex(c,d)

print(a,type(a),sep="\t")
print(b,type(b),sep="\t")
print(e,type(e),sep="\t")
print("\n\n")

# 8. Write a Python program that stores the following details using variables: Basic Salary = ₹58,750, HRA = 22% of Basic Salary,
# DA = 15% of Basic Salary, Professional Tax = ₹2,500. Perform the following tasks: Calculate Gross Salary, Calculate Net Salary
# after deducting Professional Tax, Print all values using formatted print statements, Print the data type of Net Salary, Round
# Net Salary to two decimal places.

b_sal = 58750
hra = 0.22*b_sal
da = 0.15*b_sal
p_tax = 2500

g_sal = b_sal + hra + da
n_sal = g_sal - p_tax

print("Basic salary = {}".format(b_sal))
print("HRA = {}".format(hra))
print("DA = {}".format(da))
print("Professional tax = {}".format(p_tax))
print("Gross salary = {}".format(g_sal))
print("Net salary = {}".format(round(n_sal,2)),type(n_sal))
print("\n\n")

# 9. Create variables: A = 245 B = 37 C = - 128.75 Write a program to: Calculate A² using pow(), Find the absolute value of C,
# Print the maximum and minimum among A, B, and abs(C), Calculate the average of all three numbers., Display every result with appropriate labels.

A = 245
B = 37
C = -128.75

squr_A = pow(A,2)
print(f"Square of {A} = {squr_A}")
absolute_C = abs(C)
print(f"Absolute Value of {C} = {absolute_C}")
print(f"Maximum = {max(A,B,absolute_C)}\nMinimum = {min(A,B,absolute_C)}")

avg = (A+B+C)/3
print(f"Average = {avg}")
print("\n\n")

# 10. Create two complex variables: c * 1 = 6 + 9j c * 2 = 4 - 7j Write a program to: Add the two complex numbers, Multiply them,
# Find the magnitude (absolute value) of each complex number, Print the data type of each result, Print the memory address of 
# both variables.

c1 = 6+9j
print(f"Memory address of {c1} = {id(c1)}\nData type of {c1}={type(c1)}")
c2 = 4-7j
print(f"Memory address of {c2} = {id(c2)}\nData type of {c2}={type(c2)}")
sumation = c1+c2
print(f"Sumation of both complexes = {sumation}\nData type of {sumation}={type(sumation)}")
mult = c1*c2
print(f"Multiplication = {mult}\nData type of {mult}={type(mult)}")
absolute1 = abs(c1)
print(f"Absolute of {c1} = {absolute1}\nData type of {absolute1}={type(absolute1)}")
absolute2 = abs(c2)
print(f"Absolute of {c2} = {absolute2}\nData type of {absolute2}={type(absolute2)}")
print("\n\n")

# 11. Write a program to print following output
# ---------------
# STUDENT PROFILE
# ---------------
# Name      :Rahul Sharma
# Age       :20
# Course    :B.Tech
# University:ABC University
# City      :Delhi
# ---------------

print("---------------")
print("STUDENT PROFILE")
print("---------------")
print("Name      :Rahul Sharma")
print("Age       :20")
print("Course    :B.Tech")
print("University:ABC University")
print("City      :Delhi")
print("---------------")