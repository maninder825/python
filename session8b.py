# Built In APIs i.e. Functions

# string are IMMUTABLE
# Manipulation operations will create a new String in memory
# old string will not be modified

name = "Fionna Flynn"
print(">> name is:", name)
newName = name.upper()
print(">> name now is :", name)
print(">> newName  is:", newName)

authorName = "john watson"
print(authorName, hex(id(authorName)))
# We are creating a new string and reference it in our old ref var
#newAuthorName = authorName.capitalize()
#print(">> newAuthorName is:", newAutorName)
#print(">> authorName is:", authorName)
authorName = authorName.capitalize()
print(authorName, hex(id(authorName)))

names = "John, Jennie, jim, John, Jack, Joe"
print(names[0])
print(names[len(names)-1])
#idx = names.index("0")
idx = names.index("Jennie")
print(idx)

newNames = names.replace('j', 'k')
print(names)
print(newNames)

#num = name.count("j", 0, len(names)
num = names.count("john", 0, len(names))
print(">> num is:", num)

#HW:
quotes = """work hard, get luckier
search the candles, rather than cursing the darkness
"""

def count(data, word, start, end):
    c = 0
    j = 0
    for i in range(start, end):
        print(data[i] == word[j])

        return c

print(">> the occcurs: ", count(quotes, "the", 0, len(quotes)))