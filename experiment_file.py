from sympy import *

def list_of_factors(fl):
    mf = []
    for i in fl:
        if not isinstance(i, list):
            mf.append(i)
        else:
            for n in i:
                for m in range(n[1]):
                    mf.append(n[0])

    return mf

x, y = symbols("x,y")

# Create a string that is a factorised expression
# expr = "2*(x+1)*(3*x-5)"
# expr = "2*x*(x+1)"
# print(expr)
#
# # Seperate it into its factors
# expr_factors = factor_list(expr)
# print(expr_factors)
# expr = "2*(2*x+1)*(x-3)"
expr = "2*x*(x+1)"
factors = expr.split("*(")
new_factors = []
for n in factors:
    new_factors.append(simplify(n.translate({ord(c): None for c in ' ()'})))

print(new_factors)

result = []
for i in new_factors:
    if '+' in str(i) or '-' in str(i):
        result.append(i)
    else:
        result.append(factor_list(i))

print(result)
# Need to check for things like 2*x with + or - should be 2 and x
