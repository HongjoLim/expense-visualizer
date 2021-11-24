import unittest
import parse_expenditure as parse

class TestParseExpenditure(unittest.TestCase):
    
    def test_strip_non_numeric_chars(self):
        entries = ['0.00', '-0.33PendingPending', '-$3.54', '−$19.13PendingPending']
        result = parse.strip_non_numeric_chars(entries=entries)
        self.assertEqual(result, ['0.00', '-0.33', '-3.54', '19.13'])

    def test_add_all_entries(self):
        entries = [0.00, 0.33, 3.54]
        result = parse.add_all_entries(entries=entries)
        self.assertEqual(result, 3.87)

    def test_convert_to_abs(self):
        entries = ['0.00', '-0.33', '-3.54']
        result = parse.convert_to_abs(entries=entries)
        self.assertEqual(result, [0.00, 0.33, 3.54])

if __name__ == '__main__':
    unittest.main()