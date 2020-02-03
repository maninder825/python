def add(num1, num2):
    sum = num1 + num2
    print(">> sum is {}".format(sum))


print(">> add is:", add)

add(11, 33)


# Re-Definig Function is not OVERLOADING in Python
#It will Create a new Function in memory and old function will ne deleted
def add(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    print(">> sum is {}".format(sum))


print(">> add now is:", add)


# add(10, 20) # error
add(10, 20, 30, 40, 50)
