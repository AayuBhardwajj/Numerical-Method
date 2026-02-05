from sympy import*
x=symbols('x')
f=x**3-2*x-5 
f_prime=f.diff(x)
f=lambdify(x,f)
f_prime=lambdify(x,f_prime)
print(f(5))