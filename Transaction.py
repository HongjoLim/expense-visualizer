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