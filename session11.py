# 1. Think of Object
#    Customer is Object
#    name, phone, email, gender, address are Attributes

# 2. Create its Class
class Customer:
    pass

# 3. From Class Create Real Object
cRef1 = Customer() # Object Construction Statement
cRef2 = Customer() # Object Construction Statement
cRef3 = cRef1      # Referenceb Copy Operation

print(">> cRef1 is:", cRef1)
print(">> cRef2 is:", cRef2)
print(">> cRef3 is:", cRef3)

# Operation on Object
# 1. Add Data in Object
cRef1.name = "john"
cRef3.phone = "+91 9999 88888"
cRef1.email = "john@example.com"
cRef1.gender = "Male"
cRef3.address = "Redwood Shores"

cRef2.name = "Fionna"
cRef2.phone = "+91 99999 1111"
cRef2.email = "john@example.com"
cRef2.gender = "Female"
cRef2.address = "Country Homes"
cRef2.vehicle = "KA10AB3456"
cRef2.company = "ABC International"
cRef2.priceperperson = 300
cRef2.openingHours ="10:00 - 20:00"

# Read Data from Object

# For us i.e Development to check the contents of object as Dictionary
print(">> cRef1 Details:")
print(cRef1.__dict__)
print()

print(">> cRef2 Details:")
print(cRef2.__dict__)
print()

print("cRef3 Details:")
print(cRef3.__dict__)
print()


# For End User : How we must show data
print(">> {} can be called at {} and lives in {}. For Email {}".format(cRef3.name, cRef1.phone, cRef1.address, cRef3.email))
print(">> {} can be called at {} and lives in {}. For Email {}".format(cRef2.name, cRef2.phone, cRef2.address, cRef2.email))


# 3. Update Data in Object
cRef1.name = "john Watson"
cRef3.email = "John.watson@example.com"

cRef2.name = "Fionna Flynn"
cRef2.phone = "91 90909 80808"

print("===Details Uodated===")

print(">> {} can be called at {} and lives in {}. For Email {}".format(cRef3.name, cRef1.phone, cRef1.address, cRef3.email))
print(">> {} can be called at {} and lives in {}. For Email {}".format(cRef2.name, cRef2.phone, cRef2.address, cRef2.email))

# Delete Data from Object
del cRef1.email
del cRef2.vehicle

print(">> cRef1:", cRef1.__dict__)
print(">> cRef2:", cRef2.__dict__)

# Delete Entire Object
del cRef1
del cRef2

# print(cRef1.__dict__)
# print(cRef2.__dict__)

print(cRef3.__dict__)


