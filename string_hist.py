# Creates a "Histogram" dictionary from a string (could be converted to xcel)

def histogram(s):
    d = dict()
    for i in s:
        val = d.get(i, 0)
        d[i] = val + 1
    return d

def get_input():
    g = raw_input("What would you like to count the letters of? \n")
    return g

x = get_input()

print histogram(x)
