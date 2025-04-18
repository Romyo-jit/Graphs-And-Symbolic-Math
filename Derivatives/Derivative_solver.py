import sympy as sp

x, y = sp.symbols('x y')

fx = sp.asin(sp.E**x**2)

dev_wrt_x = sp.diff(fx, x)

print("Function: f(x)\n")
sp.pprint(fx)
print("")
print("Derivative:\n")
sp.pprint(dev_wrt_x.simplify())
