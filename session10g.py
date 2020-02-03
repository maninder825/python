"""

    OOPS : Object Oriented Programming Structure
           How we design Software
           Its a Methodology
    1. Object
    2. Class
    Real World
        Object : Anything which exists in Reality
        Class  : Represents how an object will look like
                 Drawing of an Object
        Principle of OOPS
        1. Think of an Object
        2. Create its Class
        3. From Class Create Real Object
    Computer Science
        Object : Multi Value Container
                 Homo/Hetro
                 Data in Object is stored as Dictionary
                 where keys are known as attributes which will hold values as data
        Class : Represent how an object will look like
                What it should contain as data
                Provide certain functionalities to process the data as well in Object
        Principle of OOPS
        1. Think of an Object
            We need to analyse detailed requirements from client regarding his/her software needs
            Identify all those terms which will have lot of data associated with it
            that term -> Object and data associated -> attributes
            Requirement by John:
            We wish to create a food delivery app.
            Customer should register.
            We will display him all the restaurants.
            For Every Restaurant we will display menu.
            Customer will select Dishes and add them to Cart.
            Customer will process Order by paying online/offline
            Think of an Object [Customer and Restaurant]
            Customer    : name, phone, email, gender, address
            Restaurant  : name, phone, email, address, rating, pricePerPerson, openingHours, category
        2. Create its Class
        3. From Class Create Real Object
"""


# 2. Create its class
class Customer:
    pass

# From Class Create Real Object
# Object Construction Statement
cRef = Customer()

print(">> cReef is:", cRef)
print(">> cRef HashCode is:", hex(id(cRef)))
print(">> Type of cRef:", cRef.__dict__)

# Add Data In OBject
cRef.name = "john Watson"
cRef.Phone = "+91 99999 88888"
cRef.email = "Redwood Shores"
cRef.gender = "Male"

# Update Data In Object
cRef.phone = "+91 98765 67890"

# Delete Data In Object
#del cRef.address

# Object Deletion
# del cRef

print(">> cRef Dicitionary now is:", cRef.__dict__)