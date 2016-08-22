# only makes sense to define or carry out for types int or float

def distance_from_zero(arg):
    if type(arg) == type(5) or type(arg) == type(10.1):
        return abs(arg)
    else:
        return "Not numeric"

print distance_from_zero("str")
