# Tuple : IMMUTABLE
num1 = (10, 20, 30, 40, 50, 30)
print("num1:", num1, type(num1))

# LIST : MUTABLE
num2 = [10, 20, 30, 40, 50, 30]
print("num2:", num2, type(num2))

# SET  : UNIQUE AND MUTABLE  with add and delete not for update
# To achieve uniqueness set hashes the data and we don't have indexes here
# due to hashing here is set ouput is unordered
num3 = {10, 20, 30, 40, 50, 30}
print("num3:", num3, type(num3))

# STRING : IMMUTABLE
name = "john Waston"
print("name:", name, type(name))

print(num1[1])
print(num2[2])
print(name[2])
# print(num3[3]) # error

# num1[1] = 11 # err
num2[1] = 11  # ok
# num3[1] = # err
# name[1] = "k" # err
print(name)


#DICTIONARY : KEY AND VALUE PAIR | MUTABLE
# On the web terminology it is JSON : Java Script Object Notation

customer = {
                "name": "John",
                "age": 30,
                "email": "John@examole.com",
                "rating": 4.5,
                "loyalityPoints": 5133
           }

customer["name"] = "John Watson"
customer["Phone"] = "+91 98888 99999"
customer["email"] = "abc@gmail.com"
print(customer, type(customer))




