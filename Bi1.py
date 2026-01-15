def f(x):
    return x*x - 4

a = 0
b = 3

for i in range(10):
    c = (a + b) / 2
    print("Step", i+1, ": c =", c)

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root is approximately:", c)