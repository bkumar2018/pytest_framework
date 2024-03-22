import pytest

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0

# Now, we have the files test_div_by_3_6.py and test_div_by_13.py making use of the fixture 
   # defined in conftest.py.
   