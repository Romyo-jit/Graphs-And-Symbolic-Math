import sympy as sp

x, y = sp.symbols('x y')

fx = sp.sin(x)**2 + sp.cos(x)**2 + 2*sp.sin(x**6) + 1

dev_wrt_x = sp.diff(fx, x)

print("Function: f(x)\n")
sp.pprint(fx)
print("")
print("Derivative:\n")
sp.pprint(dev_wrt_x)
