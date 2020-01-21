# https:// www.python.org/dev/peps/pep-0008/
# passing Refernce | As value
def square(num): # num is a reference variable which holds hashCode of 10
    print(">> [SQUARE] num is:", num, hex(id(num)))
    num = num * num
    print(">> [SQUARE] num is:", num, hex(id(num)))



num = 10   # num is a refernce variable which holds Hashcode of 10
print(">> [MAIN] num is:", num, hex(id(num)))
square(num)
print(">> [MAIN] num is:", num, hex(id(num)))
