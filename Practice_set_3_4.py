# 1. create a dictionary details of an employee. Print Employee Name, Department,
# Salary, Designation by accessing the values using their keys

print("\nSolution 1\n")
employee = {"Name":"Chirag Aggarwal","Department":"IT","Salary":"10000","Designation":"Software engineer intern"}
print(employee["Name"],employee["Department"],employee["Salary"],employee["Designation"],sep="\n")

# 2. WAP to add the following new key-value pairs to an existing Dictionary:
#  *Email *Phone Number. Print the updated dictionary

print("\n\nSolution 2\n")
employee = {"Name":"Chirag Aggarwal","Department":"IT","Salary":"10000","Designation":"Software engineer intern"}
employee["Email"]="abc@gmail.com"
employee["Phone"]="xxxxxx2334"
print(employee)

# 3. WAP to update the salary of an employee stored in a dictionary.

print("\n\nSolution 3\n")
emp = {'Name':'Amit','Salary':45000}
print(f"Original dictionary:\n{emp}")
emp['Salary']=52000
print(f"Updated dictionary:\n{emp}")

# 4. WAP to remove: specific key, last inserted item
# Display the dictionary after each operation

print("\n\nSolution 4\n")
emp = {'Name':'Amit','Salary':45000,'Department':'HR'}
print(f"Original: {emp}")
emp.pop("Salary")
print(f"Removed Salary: {emp}")
emp.popitem()
print(f"Removed last item: {emp}")

# 5. given the dictionary: student={"Roll":101,"Name":"Rahul","Branch":"Cse","Sem":5}
# wap to: print all keys, all values and all key value pairs.

print("\n\nSolution 5\n")
student={"Roll":101,"Name":"Rahul","Branch":"Cse","Sem":5}
print(f"All keys: {student.keys()}\nAll values: {student.values()}\nAll key-values pair:\n{student}")

# 6. wap to check whether a given key exists in a dictionary.
#example: i/p: name, o/p: key found, otherwise display: key not found

print("\n\nSolution 6\n")
student={"Roll":101,"Name":"Rahul","Branch":"Cse","Sem":5}
key = student.keys()
a = input("Enter a key to find it: ")
if a in key:
    print("Key found.")
else:
    print("Key not found")

# 7. wap to count the total no of key-value pairs present in a dictionary

print("\n\nSolution 7\n")
student={"Roll":101,"Name":"Rahul","Branch":"Cse","Sem":5}
num = student.keys()
print(f"No. of key value pairs is {len(num)}")

# 8. wap to create a dictionary from the following 2 lists.
# keys=["ID","Name","Age","City"]
# values = [101,"Ankit",20,"Delhi"]
# expected o/p:  {'ID':101,'Name':'Ankit','Age':20,'City':'Delhi'}

print("\n\nSolution 7\n")
key=["ID","Name","Age","City"]
value = [101,"Ankit",20,"Delhi"]
dic = dict(zip(key,value))
print(dic)

# 9. create a nested dictionary to store details of 3 students. each should have:
# Name,Branch,Semester,CGPA.  Print the complete dictionary

print("\n\nSolution 9\n")
stud = {1:{'name':'aditya','branch':'aiml','semester':'3rd','cgpa':7.3},2:{'name':'abhishek','branch':'aiml','semester':'3rd','cgpa':7.2},3:{'name':'chirag','branch':'aiml','semester':'3rd','cgpa':7.7}}
print(stud)

# 10. using the nested list created in qustion 9, print only:
# name of student 2, branch of student 3, cgpa of student 1

print("\n\nSolution 10\n")
print(f"Name of student 2: {stud[2]['name']}\nBranch of student 3: {stud[3]['branch']}\nCgpa of student 1: {stud[1]['cgpa']}")

# 11. create a nested dictionary for each department of rdec. department should contain hod name, numbe of faculty, number of students
# then write statements to: 1. print the hod of ece department; 2. print the no. of departments in the cse department
# ;3. update the faculty count of the me department; 4. add a new department named civil; 5. print all department names; 6. print the complete nested dictionary

print("\n\nSolution 11\n")
rdec={"CSE & Allied Branches":{"HOD":"Luv Dixit","No. of Faculty":10,"No. of students":150},"ECE":{"HOD":"Abhinav Kaushik","No. of Faculty":8,"No. of students":50},"ME":{"HOD":"Rudra","No. of Faculty":3,"No. of students":30},"Chemical":{"HOD":"YUg Sharma","No. of Faculty":5,"No. of students":31}}
print("HOD of ECE department:",rdec["ECE"]["HOD"])
print("No. of student in CSE department:",rdec["CSE & Allied Branches"]["No. of students"])
rdec["ME"]["No. of faculty"]=7
print("All the departments: ",rdec.keys())
print(rdec)