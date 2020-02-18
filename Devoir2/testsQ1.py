#pyunit test pour Q1 de Devoir 2
#pour l'excuter, appuetre Run Module
import unittest
import D2Q1

class Test_Template(unittest.TestCase):

    def test_q1(self):
        """
        Test question 1
        """
        print("Test question 1")

        code = D2Q1.obtenirCodePrime(3,4,3,4,5)
        self.assertTrue(code == 2)

        code = D2Q1.obtenirCodePrime(3,4,25,4,2)
        self.assertTrue(code == 0)
        
        code=D2Q1.obtenirCodePrime(3,4,24,4,2)
        self.assertTrue(code == 1)

        code=D2Q1.obtenirCodePrime(21,4,5,56,6)
        self.assertTrue(code == 3)


if __name__ == '__main__':
    unittest.main()

