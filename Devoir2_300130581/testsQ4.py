#pyunit test pour Q4 de Devoir 2
#pour l'excuter, appuetre Run Module
import unittest
import D2Q4

class Test_Template(unittest.TestCase):

    def test_q4(self):
        """
        Test question 4
        """
        print("Test question 4")

        p = D2Q4.palindrome("laval")
        self.assertTrue(p == True)

        p = D2Q4.palindrome("hello")
        self.assertTrue(p == False)


if __name__ == '__main__':
    unittest.main()

