#1. It is a way to continue using the loop to keep track of the end result. There are three main steps. The first step is to initialize which is to create a variable that has a value that it starts with. Next is to Accumulate. This is when you go through each item that is in the loop and you add them to the accumulator. Then you use the reselt. So after the loop finishes, you print the final value that you get.
#2. I noticed that the while loop sum was longer than the for loop because you have to set it up and then do it. A for loop is shorter and easier to read especially when using a list. A while loop requires more code but allows you to continue the loop until the condition that you placed is met.
#3. As a finance major, I could use this to keep the sales of my company and keep track of htem monthly.The list would have the sales made. I could use a loop to add the sales and then at the end I could ask the program to print the total sales for the year.
#Exercise 1
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
for sale in sales:
    total += sale   # update
print(f"Total: ${total}")
# Exercise 2
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")
#Exercise 3
current_max = 0 #or sales[0], to be safe with negative numbers
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")
#Exercise 4
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")
#Exercise 5
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")
#Exercise 6
total = 0
i = 0 # index
while i < len(sales):
    total += sales [i]
    i += 1

print(f"Total(while loop): ${total}")
# Exercise 7
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1- discount)
    print(
        f"${sale}-> {discount * 100:.0f}% discount ->"
        f"${discounted_price:.2f}"
)
