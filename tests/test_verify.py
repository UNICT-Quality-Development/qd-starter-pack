
##Write a software that verifies if a number is present in a pre-defined array.
##Output example:
##Insert number 3
##The number 3 is [not] present in the array.
##
test_array = [2,4,6,8,10,12,14,16,18,20]
import sys
sys.path.append('../src')

import verify

def test_verify():
    for i in test_array:
        assert verify.verify(i) == True
    for i in range(35,55):
        if i not in test_array:
            assert verify.verify(i) == False    
