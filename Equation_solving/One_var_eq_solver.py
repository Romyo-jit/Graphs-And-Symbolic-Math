import sympy as sp

x = sp.symbols('x')

def eq_solver(eq): ### CAN BE IMPORTED ###
    solved = sp.solve(eq)
    return solved

eq = sp.Eq(x**2 + 9*x + 1, 0)

print("Equation:", end=' ')
print(eq.lhs, '=', eq.rhs)
print("Solution:", end='\n\n')
sp.pprint(eq_solver(eq))
   
