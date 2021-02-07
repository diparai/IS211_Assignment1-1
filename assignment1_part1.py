
def listDivide(numbers=[], divide=2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """
    newNumber = [x % divide for x in numbers]
    answer = newNumber.count(0)
    return answer

class ListDivideException(Exception):
    def __init__(self, message):
        self.message = message

def testListDivide():
    """
    Test listDivide
    """
    result = listDivide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Failed")
    result = listDivide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Failed")
    result = listDivide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Failed")
    result = listDivide([])
    if result != 0:
        raise ListDivideException("Failed")
    result = listDivide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Failed")

testListDivide()

