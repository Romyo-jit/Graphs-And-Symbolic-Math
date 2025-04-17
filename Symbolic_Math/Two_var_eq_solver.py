import sympy as sp

x, y = sp.symbols('x y')

def eq_solver(eq1, eq2): ### CAN BE IMPORTED ###
    solved = sp.solve([eq1, eq2], (x, y))
    return solved

eq1 = sp.Eq(5*x + 2*y, 12)
eq2 = sp.Eq(2*x + 5*y, 9)

print("Equation:\n")
print(eq1.lhs, '=', eq1.rhs)
print(eq2.lhs, '=', eq2.rhs)
print("")
print("Solution:", end='\n\n')

sp.pprint(eq_solver(eq1, eq2), use_unicode=True)