# 1. write a python program to input a string from the user and display:
# original string, length of the string, data type of the variable

print("Solution 1.")
name="Chirag Aggarwal"
print(f"\nOriginal string: {name}\nLength of the string: {len(name)}\nData type of the variable: {type(name)}")

# 2. write a python program to print the following slices of a string
# 1st 5 characters, last 5 characters, characters from index 3 to 10, every second character, reverse of the string

print("\n\nSolution 2.")
name="Chirag Aggarwal"
print(f"\nFirst 5 characters: {name[:5]}\nLast 5 characters: {name[-1:-6:-1]}\nCharacters from index 3 to 10: {name[3:11]}\nEvery second character: {name[1::2]}\nReverse of the string: {name[::-1]}")

# 3. WAP that counts the no. of: uppercase letters, lowercase letters, digits, spaces,
# special characters in a given string

print("\n\nSolution 3.\n")
a = "Cold wind blew through the open 10th-door the lobby."
up=0
low=0
dig=0
spa=0
rest=0
print(a)
for i in a:
    if i.isupper()==True:
        up+=1
    elif i.islower()==True:
        low+=1
    elif i.isdigit()==True:
        dig+=1
    elif i.isspace()==True:
        spa+=1
    else:
        rest+=1
print(f"Number of:\nUppercase letter: {up}\nLowercase letter: {low}\nDigits: {dig}\nSpaces: {spa}\nSpecial character: {rest}")

# 4. wap to check if the given string is pallindrome or not

print("\n\nSolution 4.\n")
org = "BOB"
pal = org[::-1]
if pal==org:
    print("Given string is a pallindrome.")
else:
    print("Given string is NOT a pallindrome.")

# 5. write a python program to replace every space with a hyphen('-')

print("\n\nSolution 5.\n")
a = "Cold wind blew through the open 10th-door the lobby."
print(f"Original:\n{a}")
b = a.replace(" ","-")
print(f"After replacing:\n{b}")

# 6. wap to check if two strings are anagrams or not

print("\n\nSolution 6.\n")
a = input("Enter 1st string to check if anagrams or not:\n")
b = input("Enter 2nd string to check if anagram or not")
temp1 = a.lower()
temp2 = b.lower()
c={}
d={}
for char in temp1:
    if char in c:
        c[char]+=1
    else:
        c[char]=1
for char in temp2:
    if char in d:
        d[char]+=1
    else:
        d[char]=1
c[" "]=1
d[" "]=1
if c==d:
    print("Given 2 strings are anagrams")
else:
    print("Given 2 strings are not anagram")

# 7. wap to find frequency of each character in a string

print("\n\nSolution 7.\n")
a = "Hello! My name is Chirag Aggarwal"
frequency = {}
for char in a:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print(f"Frequency of each character is :\n{frequency}")

# 8. wap in python to i/p a sentance and display every word on a new line

print("\n\nSolution 8.\n")
sent = input("Enter a sentance: ")
for i in sent:
    print(i)

# 9. wap in python to reverse the order the of words in a sentance

print("\n\nSolution 9.\n")
a = "My name is Chirag Aggarwal"
b = a.split()
c = " ".join(b[::-1])
print(f"Original string: {a}")
print(f"String after reversing the order of words:\n{c}")

# 10. wap in python to remove duplicate characters from string

print("\n\nSolution 10.\n")
a = "My name is Chirag Aggarwal"
b = ""
for char in a:
    if char not in b:
        b = b+char
print(f"Original string: {a}")
print(f"Without duplicate characters: {b}")

# 11. wap in python to find the longest word in python

print("\n\nSolution 11.\n")
a = "Hello! My name is Chirag Aggarwal."
b = a.split()
d = b[0]
for c in b:
    if len(c)>len(d):
        d=c
print(f"Longest word is: {d}")

# 12. wap in python that performs the followingoperations on a given string:
# Convert to uppercase, Convert to lowercase, Swap Case, Remove leading/trailing spaces,
# Replace one word with another, Split into words, Join the words using a hypen('-')

print("\n\nSolution 12.\n")
a = "Hello! My name is Chirag Aggarwal."
b=a.upper()
c=a.lower()
d=a.swapcase()
e=a.strip()
f=a.replace("My","my")
g=a.split()
h="-".join(g)
print(f"Original string: {a}")
print(f"Uppercase string: {b}")
print(f"Lowercase string: {c}")
print(f"Swapcase string: {d}")
print(f"Without leading/trailing spaces: {e}")
print(f"Replace \"My\" with \"my\": {f}")
print(f"Split into words: {g}")
print(f"String joined using \"-\": {h}")