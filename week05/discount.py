# 1. The value of 350 goes throuhg an if/elif/else statement. It checks each tier starting with the highest tier which is 500. SInce 350 is lower than 500, this condition is not met so it moves on to the next one. The next tier is if the order is greater than or equal to 200. As 350 is greater than 200, this condition is met thus it does not continue down the condiitonal statements and the code is executed applying the dicount rate of 10%.
# 2. The statement if total > 100 and total < 500 checks the conditions at the same time. It checks if the total is greater than 100 and less than 500. When the if statements are sperated into two, Python checks both condition seperately. They would not produce the same result. The first one would work only when both conditions are true.
# 3. Online shopping is a good exmaple. For some stores free shipping is if the user spends $75+ but when spending below that amount, there will be a shipping fee. Taxes can work like that because a person's income can determine how they pay in taxes. If they more than a certain amount, they will move to the next tier. Now after using Python, I understand how htese systems calculate how much they would have to pay.

# Starter Code from Lab 5

total = float(input("Enter cart total: $"))

# Add your if/elif/else here
# Exercise 1
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0

# discount = 0
final = total * (1- discount)
print(f"Discount: {discount*100:.0f}%")


# Exercise 2
if final > 1000: #strictly greater than.
    status = "manager_approval_required"
else:
    status = "auto_approved"

# print(status)

# Exercise 3

region = "South"


if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")
else:
    extra_discount = 0


final = total * (1- (discount + extra_discount))
print (final)

# Exercise 4
customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03


# Exercise 5
amount = 0

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE -- REVIEW REQUIRED")

# Exercise 6

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False

vip_upgrade = True
if total_spent_this_year > 2000 or orders_this_year > 10:
    vip_upgrade = True
else:
    vip_upgrade = False

