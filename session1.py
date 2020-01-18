# ecommerce probelem

# model
# container creation statements
# 1. single value storage containers
sellingpriceamazon = 15000
sellingpriceflipkart =14800

profitsamazon = 3800.33
profitsflipkart = 4000.12

taxes = 18

# 2. multi value storage containers
#               0     1     2
salesamazon = [1200, 4200, 300]
salesflipkart = [1350, 8349, 1977]

# printing/reading statements
print("sellingpriceamazon:", sellingpriceamazon, type(sellingpriceamazon))
print("sellingpriceflipkart:", sellingpriceflipkart, type(sellingpriceflipkart))

print()

print("profitsamazon:", profitsamazon, type(profitsamazon))
print("profitflipkart:", profitsflipkart, type(profitsflipkart))

print()

print("taxes:", taxes, type(taxes))

print()

print("salesamazon:", salesamazon, type(salesamazon))
print("salesflipkart:", salesflipkart, type(salesflipkart))

# controller
# computational statement | maths
totalsalesamazon = (salesamazon[0] + salesamazon[1] + salesamazon[2]) * sellingpriceamazon
totalsalesflipkart = (salesflipkart[0] + salesflipkart[1] + salesflipkart[2]) * sellingpriceflipkart

totalprofitsamazon = (salesamazon[0] + salesamazon[1] + salesamazon[2]) * profitsamazon
totalprofitsflipkart = (salesflipkart[0] + salesflipkart[1] + salesflipkart[2]) * profitsflipkart


print()

print("totalsalesamazon:", totalsalesamazon, type(totalsalesamazon))
print("totalsalesflipkart:", totalsalesflipkart, type(totalsalesflipkart))

print()

print("totalprofitsamazon:", totalprofitsamazon, type(totalprofitsamazon))
print("totalprofitsflipkart:", totalprofitsflipkart, type(totalprofitsflipkart))



# MI totalsalesamazon > totalsalesflipkart:
# who so ever sold more product will be paid 1000 extra per product as incentive

if totalprofitsamazon > totalprofitsflipkart:
    print(">> amazon made more sales")
else:
    print(">>flipkart made more sales")



incentive = totalsalesflipkart * 1000
print("incentive", incentive, type(incentive))

incentive = totalprofitsamazon * 1000
print("incentive:", incentive, type(incentive))

# taxes

taxes_amazon = totalprofitsamazon/100*18
taxes_flipkart = totalprofitsflipkart/100*18

print()

print("taxes_amazon:", taxes_amazon, type(taxes_amazon))
print("taxes_flipkart:", taxes_flipkart, type(taxes_flipkart))