#1.  Python would not crash and would just provide a wrong answer silently. This is because Python would assume that the 10 is a value that is 10 times the price instead of a discount. The output would be incorrect because the percentage would not be a decimal conversion
#2. A scenario could be when you are putting the inventory into shipping boxes. If there were 65 products and each box could hold 15, 65 // 15 would show that there are 4 boxes that are full while 60%15 would say that there was still 5 products left over so we would know how many boxes are full and how much would be left and need to be put into a seperate box
#3. I feel least confident about when to use input() and I get confused between int() and float() at times which just requires practice to strengthen.
# Revenue, Margins and Discount Calculator

# Exercise 1:
price = 50
quantity = 12
revenue = price + quantity

print(f"Revenue: ${revenue:,.2f}")

# Exercise 2:

cost = 32
price = 50
margin = (price-cost) / price
print(f"Margin: {margin:.1%}")

# Exercise 3: Boolean Logic

#Product A wins if margin_a > margin_b
# Product A margin 60%, Product B (80-60)/80 = 25%
margin_a = 0.60
margin_b = 0.25
product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Exercise 4: Logic Combo

is_premium = price > 100 and margin > 0.3

price = 150
margin = 0.35
is_premium = price > 100 and margin > 0.3

# Exercise 5: Division + Mod

print(17/5) # 3.4 This is regular division which is used when you need an exact result such as looking at an average cost per person
print(17//5) # 3 This is floor division which gives you the whole number and can be used when you want to know how mnay full groups of 5 can be made from 17
print(17%5)# 2 This only gives the remainder which you could use to find how many are left over after putting everything into equal groups
# Exercise 6:

def calc_discount(price, rate):
    return price * (1- rate)
discounted_pct = 20
discounted_rev = revenue * (1 - discounted_pct / 100)

product = input("A product name: ")
retail_price = float(input("Enter the retail price: "))
quantity_sold = int(input("Enter the quantity sold: "))
discount_pct = int(input("Enter the discount percentages: "))
cost = float(input("Enter the cost: "))
print("=" * 50)
revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1-discounted_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost * quantity_sold)


print(discounted_rev)

# Exercise 7:

BOX_SIZE = 24 
items_ordered = int(input("Numbers of items ordered: "))
full_boxes = items_ordered // BOX_SIZE
loose_items = items_ordered % BOX_SIZE
exact_fit = loose_items == 0
print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")


# Stretch A
# unpaid = 1
# retail_price = 50
# cost = 32
# fixed_costs = 10000.0
# contribution = retail_price - cost
# whole_units = int(fixed_costs // contribution)

# print(f"Whole units: {whole_units} ")
