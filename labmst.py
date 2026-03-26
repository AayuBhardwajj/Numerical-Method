def f(x):
    return 2*x**3 + x**2 - 20*x + 12


a = 0      # starting interval
b = 1
tol = 0.0001

if f(a) * f(b) >= 0:
    print("Bisection method fails. Choose another interval.")
else:
    while (b - a) / 2 > tol:
        c = (a + b) / 2

        if f(c) == 0:
            break

        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Root is:", c)