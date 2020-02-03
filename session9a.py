employee = {
    "name": "John",
    "eid": 101,
    "salary": 3000,
    "rating": 4.5
}

print(employee, type(employee))
print(len(employee))
print(max(employee))
print(min(employee))

#Update
employee["name"] = "john Watson"

print(employee)

# Add a new Key value pair
employee["address"] = "Redwood Shores"

print(employee)

# Delete a Key value pair
del employee["eid"]

print(employee)

# Deletion : Container deleted from memory
# del employee
# print(employee) # error

# Keys = employee.keys()
# values = employee.values()

keys = list(employee.keys())
values = list(employee.values())

print(">> Keys is:", keys, type(keys))
print(">> values is:", values, type(values))
