# 1. The most suprising thing to me about Python lists is that that it is more straightforward to call something from the list even when the list is expanding
#2. One instance would be when I worked at a math tutor. I could have python to keep track of the students' names and the number of pages/problems they completed inctead of manually entering it into excel

#Exercise 1: Build a list
print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2: Index Practice

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) //2
print(inventory[middle])

print("--- Exercise 3: List Slicing ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---") 

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

print("--- Exercise 6: Average of a list of sales ---") 

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: {total}")
print(f"Number of Sales: {count}")
print(f"Average Sales: {average}")
print(f"Best Sale: {max(sales)}")
print(f"Worst Sale: {min(sales)}")

print("--- Exercise 7: Accumulator Pattern ---") 

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

print("--- Exercise 8: Filter above Threshold ---") 

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")


