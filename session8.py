"""

    String
    Set
    Dicitionary

"""

# johnsShop = ' Johns Coffee Shop'
# johnsShop = 'John's Coffee Shop' # err
# johnsShop = 'John/'s coffee Shop' # Escape Sequence [Google Them for More examples]
# johnsShop = "John's Coffee Shop"

# Raw String [which will ignore escape in a string]
johnsShop = r'John\'s Coffee Shop'
print(johnsShop, type(johnsShop))

# quote = "Work Hard, Get Luckier\n-Anonymous"
quote = r"Work Hard, Get Luckier\n-Anonymous"
print(quote)


message = "This is an Awesome Day"\
          "we will Code Together"\
          "Thank You :)"
print(message)



quote = """Work Hard, Get Luckier
Search the Candle, rather than cursinh the darkness
"""

print(quote, type(quote))

# HW: Likewise we have put r in Front of string , what else we can put :)