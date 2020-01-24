s1 = {1, 2, 3, 4, 5, 2}
s2 = {3, 4, 5, }

print(s1, type(s1))
print(s2, type(s2))

s3 = s1 | s2 #Union
s4 = s1 & s2 #Intersection
s5 = s1 - s2 #Difference

print("union:", s3)
print("Intersection:", s4)
print("Difference:", s5)

