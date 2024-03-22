import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0

# Here, we have a fixture function named input_value, which supplies the input to the tests. To access the fixture function, the tests have to mention the fixture name as input parameter.
# Pytest while the test is getting executed, will see the fixture name as input parameter. It then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test.
# Execute the test using the following command −
# pytest -k divisible -v <filename>
   
# However, the approach comes with its own limitation. 
# A fixture function defined inside a test file has a scope within the test file only. 
# We cannot use that fixture in another test file. 
# To make a fixture available to multiple test files, we have to define the fixture function 
   #in a file called conftest.py. conftest.py is explained in the next chapter.
   # Create a new file conftest.py and add the below code into it −

