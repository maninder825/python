# 1. Think of an Object
#     Customer is object
#    name, phone, email, gender, address are Attributes

# 2. Create its Class
class Customer:

    #__init__ : constructor, which gets executed when we create objcet
    #           init can have inputs as many as you want

    # self is a reference variable variable, which holds the hashcode of current object
    # name of self can by any name of your choice
    # But self is always the first input to __init__
    def __init__(self, name, phone, email, gender, address):
        print("init executed")
        print(">> self is:", self)
        # LHS | self.name | is creating attribute in current Object
        # RHS | name      | is input containing data which we assign to attribute
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address

    # OVERLOADING : NOT SUPPORTED
    # Creating same__init__finction will create new init and delete old init
    """
    def __init__(self, name, phone, email, gender, address, customerType):
        print("init executed")
        print(">> self is:", self)
        # LHS | self.name | is creating attribute in current Object
        # RHS | name      | is input containing data which we assign to attribute
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address
    """

    def upgradeCustomerToPrime(self, customerType, wallet):
        self.customerType = customerType
        self.wallet = wallet

    def updateCustomerDetails(self, name, phone, email, gender, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.address = address

    # if we create any function in class, its first input is self
    def showCustomerDetails(self):
        print(">> {} can be called at {} and lives in {}. for email {}".format(self.name, self.phone, self.address, self.email))

        print(">> Gender:", self.gender)

    def showPrimeCustomerDetails(self):
        print(">> {} can be called at {} and lives in {}. for email {}".format(self.name, self.phone, self.address, self.email))

        print(">> Gender:", self.gender)
        print(">> Wallent Balance: \u20b9",self.wallet)


# 3. From class Create Real Object
cRef1 = Customer("john", "+91 99999 88888", "john@example.com", "male", "Redwood Shores") # object consrtruction statement
print(">> cRef1 is:", cRef1)

cRef2 = Customer("Fionna", "+91 909090 80808 ", "fionna@example.com", "female", "Country Homes") #Objcet consrtruction statement
print(">> cRef2 is:", cRef2)

cRef1.upgradeCustomerToPrime("Prime", 100)

# cRef1.showCustomerDeatils()
cRef1.showPrimeCustomerDetails()
cRef1.showCustomerDetails()

cRef2.updateCustomerDetails("Fionna Flynn", "+91 909909 80808", "fionna.flymm@example.com", "Female", "Country Homes")

#cRef2.name = "Fionna Flynn"
#cRef2.customerType = "Prime"
#del cRef2.gender

print(">> cRef1 :", cRef1.__dict__)
print(">> cRef2 :", cRef2.__dict__)