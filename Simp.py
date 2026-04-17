
import math
def f(x):
    return math.exp(math.sin(x))
def simpson_one_third(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even")
    h = (b - a) / n
    result = f(a) + f(b)
    print("x\tf(x)")
    for i in range(0, n+1):
        x = a + i*h
        print(round(x,4), "\t", round(f(x),4))

    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
    result *= h / 3
    return result
a = 0
b = math.pi / 2
n = 4
ans = simpson_one_third(a, b, n)
print("\nFinal Answer =", round(ans, 4))
