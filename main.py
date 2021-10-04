import csv
from transaction import Transaction
import calculate_transactions

CSV_FILE_NAME_DEBIT = 'SIMPLII-debit.csv'
CSV_FILE_NAME_CREDIT = 'SIMPLII-credit.csv'

def main():
    transactions = []

    debit_transactions = read_csv(CSV_FILE_NAME_DEBIT)
    credit_transactions = read_csv(CSV_FILE_NAME_CREDIT)

    total_expense_debit = calculate_transactions.get_total_expense(debit_transactions)
    total_expense_credit = calculate_transactions.get_total_expense(credit_transactions)

    total_deposit = calculate_transactions.get_total_deposit(debit_transactions)
    net_deposit = total_deposit - total_expense_debit - total_expense_credit

    print("You have a net deposit of {0}".format(net_deposit))
    print("Your total expense on the credit card is {0}".format(total_expense_credit))

def read_csv(CSV_FILE_NAME):

    transactions = []

    with open(CSV_FILE_NAME) as f:
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

if __name__ == '__main__':
    main()