n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = "" # empty string
    for item in words:
        result += item # cannot use append() on string only lists so use the old i=i+ smth
    return result

print join_strings(n)
