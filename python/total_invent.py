prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}
total = 0
for key in prices:
    print prices[key]*stock[key]
    total = total + prices[key]*stock[key]
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    
print total

def compute_bill(food):
    total = 0
    for item in food:
        total += prices[item]
    return total

# better yet

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] = stock[item]-1
    return total

