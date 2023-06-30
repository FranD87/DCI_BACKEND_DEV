''' Theory
- backward compatible with unittest
- testing framework
- mature package, been around for a long time.
- rich pluggings system, if you want to customize something, there is most likely pluggings to assist.
'''

''' Install
- python -m pip install pytest
- file naming convensions
'''

''' Define Tests
- in pytest you write plain assert statements 
# define a function

#define test function
def test_add():
    assert ... (some expression that must be true), ... (some error message)

- change function to actual values
- run the test 
- show an another example
- show example that test a class
- show example that test unittest


- show different outputs using different display statements
    - pytest !$
    - pytest test_add.py (-v) optional
    - pytest test_add.py -s
    - display output of a print statement
'''

''' Coverage
- coverage
    - python3 -m pip install pytest-cov
    - python3 -m pytest --cov .
    - python3 -m pytest --cov-report html --cov .

- coverage 2
    - python3 -m pip install coverage
    - coverage run <filename>
    - coverage report (-m)
    - PYTEST: coverage run -m pytest
'''

''' Parameters
- features - @pytest.fixtures
- parametarized features - @pytest.mark.parameterized

- doctest
    - python3 -m doctest <filename> (-v)
'''

def add(a, b):
    if b == 0:
        return ValueError
    return a + b

def div(a, b):
    return a/b

#print(add(2, 0))
#print(add(2, 3))
#print(div(4, 2))