from src.calculator import *

assert sum(3, 5) == 8
assert difference(8, 4) == 4
assert multiplication(2, 6) == 12
assert division(6, 2) == "3"
assert division(4, 0) == "Can't divide by 0"
assert division(5.2, 2.1) == "Make a or b integer"
