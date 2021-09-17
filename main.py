from Transaction import Transaction
import csv
import Transaction

CSV_FILE_NAME = 'SIMPLII.csv'

def main():
    transactions = read_csv()

    total_expense = get_total_expense(transactions)

    print(total_expense)
    total_deposit = get_total_deposit(transactions)

    print(total_deposit)
    net_deposit = total_deposit - total_expense

    print("You have a net deposit of {0}".format(net_deposit))

def read_csv():

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

class Transaction:

    def __init__(self, date, details, expense, deposit):
        self.date = date
        self.details = details
        self.expense = expense
        self.deposit = deposit
    
    def to_csv_format(self):
        
        return '{date}, {details}, {expense}, {deposit}'.format(
            date = self.date, 
            details = 
            self.details, 
            expense = self.expense, 
            deposit = self.deposit
        )

if __name__ == '__main__':
    main()