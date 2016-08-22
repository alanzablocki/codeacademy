
price = {
    "banana":  4,
    "apple" :  2,
    "orange":  1.5,
    "pear"  :  3
}

stock = {
    "banana":  6,
    "apple" :  0,
    "orange":  32,
    "pear"  :  15
}

# ??? 
# the order is weird

for key in price:
    print key
    print "price: %s" % price[key]
    print "stock: %s" % stock[key]
