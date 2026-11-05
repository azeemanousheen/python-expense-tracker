print("WELCOME TO MY EXPENSE TRACKER")

expenses = []

while True:
	name = input("Enter expense name (or done): ")

	if name.lower() == "done":
		break

	amount = float(input("Enter amount: ₹"))
	expenses.append((name, amount))

total = 0

print("\nYOUR EXPENSES")

for name, amount in expenses:
	print(name, ":", amount)
	total += amount

print("\nTotal spending: ₹", total)
