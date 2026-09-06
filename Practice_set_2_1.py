# 1. wap to i/p a no. and determine whether it is +ve,-ve or 0

print("Solution 1\n")
a=int(input("Enter a number: "))
if a>0:
    print("Given no. is positive.")
elif a<0:
    print("Given no. is negative.")
else:
    print("Given no. is zero.")

# 2. wap to check whether a given no. is even or odd

print("\n\nSolution 2\n")
a = 20
if a%2==0:
    print("No. is even.")
else:
    print("No. is odd.")

# 3. wap to i/p 3 no. and print largest among them using if-elif-else

print("\n\nSolution 3\n")
a=int(input("Enter 1st no.: "))
b=int(input("Enter 2nd no.: "))
c=int(input("Enter 3rd no.: "))
if a>=b and a>=c:
    print("Largest no. among 3 is",a)
elif b>=a and b>=c:
    print("Largest no. among 3 is",b)
else:
    print("Largest no. among 3 is",c)

# 4. wap to i/p marks marks (0-100) and display the grades:
# A(90-100), B(75-89), C(60-74), D(40-59), Fail(<40)

print("\n\nSolution 4\n")
mark = int(input("Enter the marks: "))
if mark<=100 and mark>=90:
    print("Your grade is A")
elif mark<=89 and mark>=75:
    print("Your grade is B")
elif mark<=74 and mark>=60:
    print("Your grade is C")
elif mark<=59 and mark>=40:
    print("Your grade is D")
else:
    print("Fail")

# 5. wap to check whether the given year is leap year or not

print("\n\nSolution 5\n")
year = int(input("Enter year to check leap year or not: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else:
    print("Not leap year")

# 6. wap to determine that allows withdrawal from ATM only if: PIN is correct, Account balance is 
# sufficient.otherwise, display the appropriate message 

print("\n\nSolution 6\n")
user = input("Enter user: ").lower()
if user=="chirag aggarwal":
    pin = int(input("Enter pin: "))
    if pin == 9970:
        bal = int(input("Enter current balance: "))
        wit = int(input("Enter withdrawal amount: "))
        if wit<=bal:
            print("Withdrawal possible")
            bal = bal-wit
            print("Remaining balance is: ",bal)
        else:
            print("Insufficient balance")
    else:
        print("Incorrect pin.")
else:
    print("Invalid user")

# 7. a student is eligible for a scholarship only if: marks>=85, attendance>=75%. wap to check eligiblity

print("\n\nSolution 7\n")
marks = int(input("Enter marks: "))
if marks >= 85:
    att = int(input("Enter attendance in % : "))
    if att>=75:
        print("Eligible for scholarship")
    else:
        print("Insufficient attendance! Not eligible")
else:
    print("Insufficient marks! Not eligible")

# 8. calculate electricity bill using following slabs: up to 100 units: ₹5/unit,
# 101-300 units: ₹7/unit, above 300 units: ₹10/unit

print("\n\nSolution 8\n")
unit = int(input("Enter electricity used(in kW/h)(+ve integer only): "))
bill=-1
if unit>=0 and unit<=100:
    bill = unit*5
elif unit>=101 and unit<=300:
    bill = 500+((unit-100)*7)
elif unit>300:
    bill = 500+1400+((unit-300)*10)
else:
    print("Invalid units!")
if bill>-1:
    print(f"Electricity bill is: ₹{bill}")

# 9. wap that performs addition, subtraction, multiplication, or division based on the user's choice using if_elif_else

print("\n\nSolution 9\n")
num1 = int(input("Enter first operand/number: "))
ch = int(input("Choose and enter the number of operation from below:\n1.Addition,\n2.Subtraction,\n3.Multiplication,\n4.Division\nChoice: "))
num2 = int(input("Enter second operand/number: "))
if ch ==1:
    print("Required answer: ",num1+num2)
elif ch ==2:
    print("Required answer: ",num1-num2)
elif ch ==3:
    print("Required answer: ",num1*num2)
elif ch ==4:
    print("Required answer: ",num1/num2)
else:
    print("Invalid choice!")

# 10. wap to validate a user's surname and password. if both are correct, display "Login Successful"; otherwise, display "Invalid Username or Password"

print("\n\nSolution 10\n")
user = input("Enter username: ").lower()
pas = input("Enter password: ")
if user=="chirag aggarwal" and pas=="9970@0799":
    print("Login succesful")
else:
    print("Invalid Username or Password")
