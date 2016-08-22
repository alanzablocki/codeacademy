def cube(number):
    result = number**3
    """print "%d cubed is $d" % (number,result)"""
    return result
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print cube(3)
print by_three(3)
