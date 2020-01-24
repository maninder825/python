name = "John Watson"
print(name, type(name), hex(id(name)))

# name is a reference variable which will hold hashcode of john watson
# john watson will be created in Constant pool
print(">> Length of name:", len(name))  # 11 [0 to 10]
print(">> max of name is:", max(name))  # t
print(">> min of name is :", min(name)) # space

print(name[1])
print(name[len(name)-1])

print(name[1:4])
# -ve Indexing means reverse order
print(name[1], name[-2])

print(name[::-1])

email = input("Enter Your Email: ")
print(">> You Entered:", email)

phone = input("Enter Your Phone: ")
print(">> You Entered:", phone)

if "@" in email and "." in email:
    print(">> Valid Email")
else:
    print(">> Invalid Email")

if len(phone) > 10 and len(phone) <= 15:
    print(">> Vaild Phone")
else:
    print(">> Invalid phone")
