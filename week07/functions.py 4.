# 1. The first bug that I found was the total = sales. I realized that it was not adding the sales together and instead was replacing hte total amount. I found htis immediately without the use of AI as it stood out to me. This tells me that some of the debugging is instinctual in that I immediately realized what was wrong
#2. This takes the inputs which are the price and the discount tier and uses the tier to determine which discount should be applied. After, it returns the price after the discount was applied. A colleague could as long as they understood what the price and tier were
#3. My disclosure comment would be I used AI (which AI specifically would be stated) to help with debugging and I reviewed the suggestions made and fixed them. The use of AI built my understanding because I was able to identify why the code was wrong by myself and used AI to identify the code. If i didn't understand why, then AI was able to explain it to me; therefore, I was able to understand the mistake and why it was wrong.

# Exercise 1

#Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price



original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f"final_price(200,0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
   total = final_price(price, rate, tier)
   print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# For this part I changed total + sale to total += sale so it adds the sales up
#Then I added : after for sale in sales which would hten indent the code
# I then made it i < len(sales) so it doesn't go past the index at the end
