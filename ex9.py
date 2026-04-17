import math

# differential equation
def f(x, y):
    return x**3 + y

# exact solution
def exact(x):
    return -x**3 - 3*x**2 - 6*x - 6 + 8*math.exp(x)

# RK4 Method
def runge_kutta_4(x0, y0, x_end, h):
    x = x0
    y = y0

    print("x\tRK4 y\t\tExact y\t\tError")

    while x <= x_end:
        exact_val = exact(x)
        error = abs(exact_val - y)

        print(f"{x:.1f}\t{y:.6f}\t{exact_val:.6f}\t{error:.6f}")

        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

# initial values
runge_kutta_4(0, 2, 0.6, 0.2)