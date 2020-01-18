# container creation
num1 = 10
print("num1:", num1, id(num1))

# container creation and reference copy operation
num2 = num1
print("num2:", num2, id(num2))

# update operation
num1 = 100
print("num1 after updated:", num1, id(num1))

# container creation
# Tuple : IMMUTABLE | we cannot change it later
# numbers1 : (10, 20, 30, 40, 50)

# list : MUTABLE | we can change it later
numbers1 = [10, 20, 30, 40, 50]

# refernce copy opeartion
numbers2 = numbers1

print("numbers1:", numbers1, type(numbers1), id(numbers1))
print("numbers2:", numbers2, type(numbers2), id(numbers2))

print("numbers1[2] is :", numbers1[2])
print("numbers2[2] is :", numbers2[2])

# update operation | for tuple(err) | for list[work]
numbers1[2] = 33

print("numbers1[2] now is :", numbers1[2])
print("numbers2[2] now is :", numbers2[2])




