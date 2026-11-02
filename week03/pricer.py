# type(5) returned int because 5 in a integer as it is a whole number
# type(5.0) returned a float because it is a number with a decimal
# type("5") returned str because it is a text so a string
# type(True) returned bool because True and False is a boolean value
# "5" + "3" gives back 53 because both values are strings so Python puts them together
# 5 + 3 gives the value 8 because both numbers are integers so the program adds them together
#1. WHen I forgot to convert the price, I got a TypeError since it can do math operations between a string and a number. The price was considered a text instead of a number.
#2. Python gave back 52 because "5" and "3" are both strings, hence python joins the numbers together because of the plus sign. Values from input() must be converted to int or float before the math is done because input() gives back a string.
#3. In my future finance career, I can use these cariables and types to create a tool that could help me budget money. The tool coulduse number bariables to do math calculations and can then display the text with the calculations.
# Exercise #1: Variables and Types

product = "Notebook"
unit_price = 4.99
quantity = 12
in_stock = True

# print(type(product)); #<class 'str'>
# print(type(unit_price)); # <class 'float'>
# print(type(quantity)); #<class 'int"> 
# print(type(in_stock)); #<class 'bool'>

# # Exercise #2: String Formatting

# print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${unit_price * quantity:.2f}")

# Exercise #3: Input functions

# product_in = input("Product Name: ")
# price_in = float(input("Unit Price: ")) # Converts string to float
# quantity_in = int(input("Quantity: ")) # Converts string to int

# print(f"{quantity_in} units of {product_in} at ${price_in:.2f} each = ${price_in * quantity_in:.2f}")

# #Exercise #4: Product Card

unit_cost = 3.29
revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100

print(f"Product: {product}")
print(f"Revenue: ${revenue:.2f}")
print(f"Cost: ${unit_cost:.2f}")
print(f"Margin: {margin:.2f}%")
#\n = new Line
print("=" * 20)
print(f"product: {product}\nRevenue: ${revenue:.2f}\nCost: ${unit_cost:.2f}\nMargin: {margin:.2f}%")
