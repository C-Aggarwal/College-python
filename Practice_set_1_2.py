# 1. wap to input 2 integers and display:their +,-,*,/,//,%,,**

num1 = int(input("Enter first number: "))
num2 = int(input("Enterr second number: "))
add = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2
fdiv = num1//num2
mod = num1%num2
exp = num1**num2

print(f"\n{num1} + {num2} = {add}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} // {num2} = {fdiv}")
print(f"{num1} % {num2} = {mod}")
print(f"{num1} ** {num2} = {exp}")
print("\n\n")

# 2. wap that: takes an integer as input. apply the following operations one by one: +=10, -=5, *=2, /=3. display the value 
# after each operation.

num1 = int(input("Enter an integer: "))
num1 += 10
print(num1)
num1 -= 5
print(num1)
num1 *= 2
print(num1)
num1 /= 3
print(num1)
print("\n\n")

# 3. wap to i/p 2 no. and check: are they equal?are they not equal? is the 1st no. > 2nd?is the 1st no. < 2nd no.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
res = num1 is num2
res1 = num1 is not num2
res2 = num1 > num2
res3 = num1< num2
print(f"{num1} equal to {num2}: {res}")
print(f"{num1} not equal to {num2}: {res1}")
print(f"{num1} greater than {num2}: {res2}")
print(f"{num1} less than {num2}: {res3}")
print("\n\n")

# 4. i/p the marks of a student in 2 subjects:
#   print "Pass" if both marks are 35 or above
#   print "Eligible for sholarship" if either mark is 90 or above
#   print whether the student has not failed using the not operator

phy = int(input("Enter the marks obtained in physics: "))
math = int(input("Enter the marks obtained in maths: "))

((phy > 100) or (math > 100)) and print("Invalid marks!")
((phy >= 35) and (math >= 35)) and print("Pass")
((phy >= 90) or (math >= 90)) and print("Eligible for Scholarship")
(not phy<35 and not math<35) and print("Not failed")
print("\n\n")

# 5. input a sentance and a word and check whether the word is present in the sentance using in operator

sent = input("Enter the sentence: ")
word = input("Enter the word: ")

(word in sent) and print(f"{word} is present in given sentence")
print("\n\n")

# 6. i/p a sentence and a word: check whether the word is not present in the sentence

sent = input("Enter the sentence: ")
word = input("Enter the word: ")

(word not in sent) and print(f"{word} is not present in given sentence")
print("\n\n")

# 7. create 2 variables: check whether a is b. then create c and check whether a is c

a = 50
b = 60

print("Is \"a\" equal to \"b\"? =", (a==b))
c=50
print("Is \"a\" equal to \"c\"? =", (a==c))
print("\n\n")

# 8. using hte variables from ques 7, check a is not b and a is not c. explain the o/p

print("\"a\" is not equal to \"b\"? =", (a is not b))
print("\"a\" is not equal to \"c\"? =", (a is not c))
print("\n\n")

# 9. i/p 2 integers. display: bitwise AND(&) bitwise OR(|) 

a = int(input("Enter 1st integer: "))
b= int(input("Enter 2nd integer: "))

print(f"Bitwise AND: {a&b}\nBitwise OR: {a|b}")
print("\n\n")

# 10. i/p an integer .display: Bitwise XOR with another no. entered by the user. Bitwise NOT(~)

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))

print(f"Bitwise XOR between {a} and {b} = {a^b}.")
print(f"Bitwise NOT of {a} = {~a}")
print("\n\n")

# 11. i/p a no.. display: result after left shifting by 2 bits(<<2) and result after rigght shifting by 2 bits(>>2)

a = int(input("Enter an integer: "))
print(f"{a} << 2 = {a<<2}") 
print(f"{a} >> 2 = {a>>2}")
print("\n\n")

# 12. i/p 3 no.. check whether: the 1st no. is greater than the second and the third number is greater than the first. display 
# the result

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
c = int(input("Enter an integer: "))

print(f"{a} > {b} = {a>b}")
print(f"{c} > {a} = {c>a}")