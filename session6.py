# for i in range(1, 11):
# for i in range(1, 11, 2):
for i in range(10, 0, -1):
    print(">> i is:", i)

print("=========")

"""
    show(num) => print num
"""

# creating or defining a function
# recursion -> Excecuting the same function again and again
#              from the same function
def show(num):

    if num == 0:
        return

    print(">> num is:", num)

    num -= 1  # num = num - 1


    show(num)


# Executing a function
show(10)
# show(9)
# show(7)
# show(6)
# show(5)



# Running time of loop and Recursive Function
# is same or different
# if same or more then whats the fun ? why we need it or use it?