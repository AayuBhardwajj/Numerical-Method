def f(x):
    return x**3 - 5*x + 1


def regular_falsi(a, b, n):
    i = 1

    if f(a) * f(b) >= 0:
        print("Invalid initial guesses")
        return

    while i <= n:
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print("Iteration =", i, "x =", x, "f(x) =", f(x))

        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        i = i + 1

    print("Required root is:", x)


a = float(input("First approximate root: "))
b = float(input("Second approximate root: "))
n = int(input("No. of iterations: "))

regular_falsi(a, b, n)