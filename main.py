import csv
from transaction import Transaction
import calculate_transactions

CSV_FILE_NAME = 'SIMPLII.csv'

def main():
    transactions = read_csv(CSV_FILE_NAME)

    total_expense = get_total_expense(transactions)
    total_deposit = get_total_deposit(transactions)
    net_deposit = total_deposit - total_expense

    print("You have a net deposit of {0}".format(net_deposit))

def read_csv(file_name):

    transactions = []

    with open(file_name) as f:
        lines = csv.DictReader(f, delimiter= ',')

        for line in lines:
            date = line[lines.fieldnames[0]]
            details = line[lines.fieldnames[1]]
            expense = to_num(line[lines.fieldnames[2]]) 
            deposit = to_num(line[lines.fieldnames[3]]) 
            transactions.append(Transaction(date, details, expense, deposit))

    return transactions

def to_num(str_amount):
    try:
        return float(str_amount)
    except:
        return 0

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

if __name__ == '__main__':
    main()