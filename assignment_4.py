expenses = []

while True:
    expense = float(input("Enter an expense or 0 to finish: "))

    if expense == 0:
        break
    elif expense < 0:
        print("Expense cannot be negative. Please enter a valid expense.")
    else:
        expenses.append(expense)

# Calculate results from user input
total_expenses = sum(expenses)
number_of_expenses = len(expenses)
average_expense = total_expenses / number_of_expenses

smallest_expense = min(expenses)
largest_expense = max(expenses)
small_expenses = 0
moderate_expenses = 0
large_expenses = 0

# Classify each expense
for expense in expenses:
    if expense < 25:
        small_expenses += 1
    elif expense <= 100:
        moderate_expenses += 1
    else:
        large_expenses += 1

# Display results for user in list
print("\nExpense Summary")
print("-------------------------")
print(f"Total number of expenses: {number_of_expenses}")
print(f"Total expenses: ${total_expenses:,.2f}")
print(f"Average expense: ${average_expense:,.2f}")
print(f"Smallest expense: ${smallest_expense:,.2f}")
print(f"Largest expense: ${largest_expense:,.2f}")
print(f"Small expenses (< $25): {small_expenses}")
print(f"Moderate expenses ($25 - $100): {moderate_expenses}")
print(f"Large expenses (> $100): {large_expenses}")