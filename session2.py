# single value container

# container creation statement
age = 20
# type -> class
# id -> hashcode
print("age:", age, type(age), id(age))
print(age, type(age), hex(id(age)))
print(age, type(age), bin(id(age)))
print(age, type(age), oct(id(age)))

# container creation statement
johnsage = 20
print("johnsage:", johnsage, type(johnsage), id(johnsage))


# container update statement
age = 30
print("age:", age, type(age), id(age))

# containers in memory stored  as data structure : hashtable with algorithm called as hashing
fionnasage = age # reference copy operation
print("fionnasage:", fionnasage, type(fionnasage), id(fionnasage))

# delete operation
del age
# print("age:", age, type(age), id(type))
print("fionnasage:", fionnasage, type(fionnasage), id(fionnasage))

del fionnasage

# ps: age, johnsage and fionnasage are known as reference variable
# refernce variable will hold hashcode