import sympy as sp
from sympy import E as e, sin, cos, tan, cot, sec, csc, log, exp, sqrt, pi

x, y = sp.symbols('x y')

fx = (sp.E**x)*sp.sin(x)*sp.cos(x)**2

dev_wrt_x = sp.diff(fx, x)

print("Function: f(x)\n")
sp.pprint(fx)
print("")
print("Derivative:\n")
sp.pprint(dev_wrt_x.simplify())
