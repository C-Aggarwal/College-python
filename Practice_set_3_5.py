# 1. wap to add following elements to an existing set: 25,35,45.Print new set 

print("Solution 1\n")
a={5,10,15,20}
a.update([25,35,45])
print(a)

# 2. wap to remove elements from a set using:
# 'remove()','discard()','pop()' display the set after each operation

print("\n\nSolution 2\n")
a={5,10,15,20,25,30,35,40,45}
a.remove(10)
print("After remove(10):",a)
a.discard(45)
print("After discard(45):",a)
a.pop()
print("After pop:",a)

# 3.wap to create 2 sets and perform the following operation :
# union, intersection, difference, symmetric difference.Display the result of each operation

print("\n\nSolution 3\n")
a={5,10,15,20,25,30,35,40,45,50}
b={10,20,30,40,50,60,70,80,90,100}
print(a,b,sep="\n")
print(f"union:\n{a|b}")
print(f"intersection:\n{a&b}")
print(f"difference:\n{a-b}")
print(f"symmetric difference:\n{a^b}")

# 4. wap to determine whether 2 sets are disjoint

print("\n\nSolution 4\n")
a={5,10,15,20,25,30,35,40,45,50}
b={10,20,30,40,50,60,70,80,90,100}
print(a,b,sep="\n")
print(f"Both sets are disjoint: {a.isdisjoint(b)}")

# 5. wap to remove duplicate values from the list using set

print("\n\nSolution 5\n")
a = [10,20,30,40,30,20,10]
a=set(a)
a=list(a)
print(a)

# 6. wap to find common subjects chosen by two students.
#  example: student1 = {"Python","Java","SQL","Excel"}
#  student2 = {"Python","C","Excel","Power BI"}   Display common subjects

print("\n\nSolution 6\n")
student1 = {"Python","Java","SQL","Excel"}
student2 = {"Python","C","Excel","Power BI"}
print(student1,student2,sep="\n")
print(f"Common subjects:  {student1&student2}")

# 15. A college has 2 clubs:
# science club = {'Aman','Riya','Rahul','Priya','Ankit'}
# coding club = {"Rahul","Ankit","Simran","Rohit","Riya"}
# wap to:
# 1. display all student enrolled in either club
# 2. display students enrolled in both clubs
# 3. display students only in science club
# 4. display students only in coding club
# 5. check whether the 2 clubs have any common members
# 6. add a new student to the coding club
# 7. remove 1 student from science club
# 8. print the updated sets

print("\n\nSolution 15\n")
sci = {'Aman','Riya','Rahul','Priya','Ankit'}
cod= {"Rahul","Ankit","Simran","Rohit","Riya"}
print("Both sets of club members:",sci,cod,sep="\n")
print(f"\nstudents in either club:\n{sci|cod}")
print(f"\nstudents in both club:\n{sci&cod}")
print(f"\nstudents in science club only:\n{sci-cod}")
print(f"\nstudents in coding club only:\n{cod-sci}")
print(f"\nBoth clubs do not have common members: {sci.isdisjoint(cod)}")
cod.update(["Abhinav"])
sci.pop()
print(f"\nUpdated sets science club and coding club respectively:\n{sci}\n{cod}")