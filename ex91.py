# function dy/dx = f(x, y)
def f(x, y):
    return x + y

# RK4 Method
def runge_kutta_4(x0, y0, x, h):
    n = int((x - x0) / h)
    y = y0

    for i in range(n):
        k1 = h * f(x0, y)
        k2 = h * f(x0 + h/2, y + k1/2)
        k3 = h * f(x0 + h/2, y + k2/2)
        k4 = h * f(x0 + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 = x0 + h

    return y

# Initial values
x0 = 0
y0 = 1
x = 0.2
h = 0.1

y_val = runge_kutta_4(x0, y0, x, h)
print("Solution at x =", x, "is", y_val)