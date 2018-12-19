from sympy import *

x, y = symbols("x,y")

def list_of_factors(fl):
    """Produce a list of factors of an expression
    with multiple entries when a factor occurs more
    than once.
    fl is a factor list
    """
    mf = []
    for i in fl:
        if not isinstance(i, list):
            if i != 1:
                mf.append(i)
        else:
            for n in i:
                for m in range(n[1]):
                    mf.append(n[0])
    return mf


def str_to_list_of_factors(expr):
    after = expr
    factors = []
    present = False
    if '*(' in after:
        present = True
    while(present):
        i = after.index('*(')
        before = after[:i]
        factors.append(simplify(before))
        after = after[i + 1:]
        if not '*(' in after:
            present = False
    factors.append(simplify(after))
    result = []
    for f in factors:
        if str(f)[-3:-1] == "**":
            power = int(str(f)[-1])
            inside = simplify(str(f)[1:-4])
            for n in range(power):
                result.append(inside)
        elif '+' in str(f) or '-' in str(f):
            result.append(f)
        else:
            temp = str(f).split('*')
            for t in temp:
                result.append(simplify(t))
    return result


def compare_factors(quest, ans):
    ql = quest
    al = ans
    if len(al) != len(ql):
        return False
    size = len(al)
    correct = True
    for i in al:
        if i in ql:
            del ql[ql.index(i)]
        else:
            return False
    return correct
