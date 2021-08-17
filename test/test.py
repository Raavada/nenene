#from pyfil import tota1l

# file_2.py
import sys
sys.path.append('pyfil')

#import file1

from file1 import *


#import pyfil
#from pyfil import *

import unittest 


print(tota1l(2,3))


class Tese(unittest.TestCase):

    def test1(self):
        tot= tota1l(2,3)
        self.assertEqual(tot,5,"equal")


if __name__ == '__main__':
    unittest.main()

