import sympy as sp

x = sp.symbols('x')

f_expr = sp.exp(x) - 2

f_prime_expr = sp.diff(f_expr, x)

f = sp.lambdify(x, f_expr)
f_prime = sp.lambdify(x, f_prime_expr)

x0 = float(input("Enter initial guess: "))
n = int(input("Enter number of iterations: "))

print("\nIteration\t x\t\t f(x)")

for i in range(1, n + 1):
    fx = f(x0)
    print(f"{i}\t\t {x0:.6f}\t {fx:.6f}")
    
    x1 = x0 - fx / f_prime(x0)
    x0 = x1

print("\nRoot correct to 3 decimal places:", round(x0, 3))