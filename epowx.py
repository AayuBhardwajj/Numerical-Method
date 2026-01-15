# e ki power x, taylor series..
import math
x=math.pi/6
value=math.exp(x)
app_value=1+x/math.factorial(1)+x**2/math.factorial(2)+x**3/math.factorial(3)
print()
print("Value of e^x: ", value)
print()
print("Approximation with 3 terms: ", app_value)
print()
print("Truncation error: ", abs(value - app_value))
print()
