
import unittest 
from kaprekar_constant import get_number, lower_number, higher_number, subtract

class KaprekarCheck(unittest.TestCase):

    @unittest.expectedFailure 
    def test_0_get_number(self):

        n = '8902'
        self.assertEqual(get_number(), '2334')

    # skip test for wrong input 
    # our function get_number() contains a while loop that will accept only the correct input
    def test_1_get_number(self):

        n = '12'
        if len(n) != 4:
            self.skipTest('Wrong Input. Number should contain 4 digits')

        self.assertEqual(get_number(), '12')

    # skip test for another example of a wrong input 
    def test_2_get_number(self):

        n = '2222'
        d = set(x for x in n)
        if len(d) < 2:
            self.skipTest('Need at least two different digits')

        self.assertTrue(get_number(), '2222')

    def test_3_lower_number(self):

        n = '3405'
        self.assertEqual(lower_number(n), 345)

    def test_4_higher_number(self):

        n = '3405'
        self.assertEqual(higher_number(n), 5430)
        
    def test_5_subtract(self):

        n = 345
        k = 5430
        self.assertEqual(subtract(n, k), '5085')

if __name__ == '__main__':
    unittest.main()
