def due_amount(total_bill, paid_amount):
    return total_bill - paid_amount

bill = float(input("Enter the total bill amount: "))
paid = float(input("Enter the amount paid: "))

due = due_amount(bill, paid)

if due > 0:
    print("Due Amount =", due)
elif due == 0:
    print("No due amount. Payment completed.")
else:
    print("Extra Amount Paid =", abs(due))