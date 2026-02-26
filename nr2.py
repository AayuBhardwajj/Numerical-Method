import math

def f(x):
    return math.exp(x) - 2

def f_prime(x):
    return math.exp(x)

x = float(input("Enter the initial value of x: "))
n = int(input("Enter the required correct decimal places: "))

i = 1
condition = True

while condition:
    x_new = x - (f(x) / f_prime(x))
    print("Iteration", i, ": x =", x_new, ", f(x) =", f(x_new))

    m = str(x_new)
    g = str(x)

    if m[0:n+2] == g[0:n+2]:
        condition = False
    else:
        x = x_new
        i += 1

print("\nRequired root is:", x_new)