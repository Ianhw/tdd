import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        print(camper_age_input.convert_to_months(72))
        self.assertEqual(6,camper_age_input.convert_to_months(72))





if __name__ == '__main__':
    unittest.main()