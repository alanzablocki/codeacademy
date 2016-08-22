meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal*(1+tip)
print("%.2f" % total)
print("%.3f" % total)
