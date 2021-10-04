import unittest
import calculate_transactions
from transaction import Transaction

class TestCalculateTransactions(unittest.TestCase):

    def test_get_total_deposit(self):
        transactions = [Transaction('2020/01/01', 'dummy', 3.14, 0), Transaction('2020/01/01', 'dummy2', 3.43, 0), Transaction('2020/02/03', 'dummy3', 0, 4.5)]
        result = calculate_transactions.get_total_deposit(transactions)
        self.assertEqual(result, 4.5)


    def test_get_total_expense(self):
        transactions = [Transaction('2020/01/01', 'dummy', 3.14, 0), Transaction('2020/01/01', 'dummy2', 3.43, 0), Transaction('2020/02/03', 'dummy3', 0, 4.5)]
        result = calculate_transactions.get_total_expense(transactions)
        self.assertEqual(result, 6.57)

if __name__ == '__main__':
    unittest.main()