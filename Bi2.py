import math

def f(x):
    return math.exp(x) - x - 2

a = 0
b = 2
tol = 0.0001

if f(a) * f(b) >= 0:
    print("Invalid interval")
else:
    for i in range(50):
        c = (a + b) / 2
        print("Iteration", i+1, "c =", c, "f(c) =", f(c))

        if abs(f(c)) < tol:
            print("Root =", c)
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c