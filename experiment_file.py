from sympy import *

x, y = symbols("x,y")

# Create a string that is a factorised expression
# expr = "2*(x+1)*(3*x-5)"
expr = "2*x*(x+1)"
print(expr)

# Seperate it into its factors
expr_factors = factor_list(expr)
print(expr_factors)
# expr = "2*(2*x+1)*(x-3)"
expr = "2*x*(x+1)"
factors = expr.split("*(")
new_factors = []
for n in factors:
    new_factors.append(simplify(n.translate({ord(c): None for c in ' ()'})))

print(new_factors)
