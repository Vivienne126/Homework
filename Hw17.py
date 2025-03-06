amount_paid=int(input("Enter the amount paid"))
total_bill=int(input("Enter the total bill"))
def calculate_change(amount_paid, total_bill):
    if amount_paid < total_bill:
        return"Amount is insuffincent"
    else:
        change=amount_paid - total_bill
        return change
        print("The change is:" , calculate_change(amount_paid, total_bill))