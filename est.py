def f(x, y):
    return x + y

def rk4(x0, y0, h, xn):
    x = x0
    y = y0
    
    print("Step-by-step values:\n")
    
    while x < xn:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        
        print(f"x = {round(x,2)}, y = {round(y,6)}")
    
    return y


x0 = 0
y0 = 1
h = 0.1
xn = 0.3


result = rk4(x0, y0, h, xn)

print("\nFinal value of y at x = 0.3 is:", round(result, 6))