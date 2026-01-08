# Implemented the taylors series
import math;
x=math.pi/6
value=math.sin(x)
app_value= x-(x**3)/math.factorial(3)
print()
print("Value of sin(x) ", value)
print()
print("approximation with 2 terms: ", app_value)
print()
print("truncation error: ",abs(value-app_value))
