def get_total_deposit(transactions):

    total_deposit = 0

    for transaction in transactions:
        total_deposit += transaction.deposit

    return total_deposit

def get_total_expense(transactions):

    total_expense = 0

    for transaction in transactions:
        total_expense += transaction.expense

    return total_expense