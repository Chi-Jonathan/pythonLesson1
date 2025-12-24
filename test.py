import unittest
import main

class unit_test_calculator(unittest.TestCase):
    def setUp(self):
        self.num1List = [-23213432, -23, -10, 0, 1, 9, 1000, 243243243]
        self.num2List = [-63413432, -73, -10, 0, 1, 7, 1000, 784332432]
    
    def test_add(self):
        for num1 in self.num1List:
            for num2 in self.num2List:
                self.assertEqual(main.add(num1, num2), num1+num2)

    def test_subtract(self):
        for num1 in self.num1List:
            for num2 in self.num2List:
                self.assertEqual(main.subtract(num1, num2), num1-num2)

    def test_multiply(self):
        for num1 in self.num1List:
            for num2 in self.num2List:
                self.assertEqual(main.multiply(num1, num2), num1*num2)
    
    def test_divide(self):
        for num1 in self.num1List:
            for num2 in self.num2List:
                if num2 == 0:
                    self.assertEqual(main.divide(num1, num2).lower(), "invalid denominator")
                else:
                    self.assertEqual(main.divide(num1, num2), num1/num2)


if __name__ == '__main__':
    unittest.main()