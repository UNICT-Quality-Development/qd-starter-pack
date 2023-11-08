
##Write a software that verifies if a number is present in a pre-defined array.
##Output example:
##Insert number 3
##The number 3 is [not] present in the array.
##
success_test_array = [2,4,6,8,10,12,14,16,18,20]
fail_test_array = range(35,100)
import sys
sys.path.append('../src')

import verify

def test_verify():
    for i in success_test_array:
        assert verify.is_element_in_list(i) == True
    for i in fail_test_array:
        if i not in success_test_array:
            assert verify.is_element_in_list(i) == False    
