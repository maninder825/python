"""

     1. Check all opeartions on set |
     2. check Concatenation Immutable property on set | NO
     3. Try concatenating List and tuple into Set | NO
     4. repetition + Indexing + Slicing | No
     4. See if for Loop with range works set
     5. See if for - each loop works with set

"""

students = {"john", "jennie", "jim", "jack", "joe"}
print(students)
print(type(students))

# PS : In set data will be unordered due to hashing
#  Data will be unique



# 3. Membership Testing
print("john" in students)
print("Dave" not in students)

# Enchanced Version of For Loop -> For - Each Loop
for student in students:
    print(student)

