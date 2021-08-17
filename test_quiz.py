from unittest.case import TestCase
import quiz
import unittest


class TestQuiz(unittest.TestCase):
    
    def testCasePositive(self):
        results = ["9","2","7","11"]
        self.assertEqual(quiz.print2largest(results),9)
        results = ["9","2","7","11"]
        self.assertEqual(quiz.print2largest(results),9)
        results = ["9","2","7","11"]
        self.assertEqual(quiz.print2largest(results),9)
        results = ["9","2","7","11"]
        self.assertEqual(quiz.print2largest(results),9)

    def testCaseNegative(self):
        results = ["9","2","7","11"]
        self.assertNotEqual(quiz.print2largest(results),2)        
        self.assertNotEqual(quiz.print2largest(results),7)        
        self.assertNotEqual(quiz.print2largest(results),1)        

    def sizeOfListgreaterthentwo(self):  
        results = ["9"]
        self.assertEqual(quiz.print2largest(results),-1) 

    def emptyListCheck(self):  
        results = []
        self.assertEqual(quiz.print2largest(results),-1) 



    



if __name__ == '__main__':
    unittest.main()