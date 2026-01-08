import math
x = math.pi / 6
value = math.exp(x)
app_value = 1 + x
print()
print("Value of e^x: ", value)
print()
print("Approximation with 2 terms: ", app_value)
print()
print("Truncation error: ", abs(value - app_value))