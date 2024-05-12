import numpy as np
from sympy import *
from math import factorial as fact


# The roots of the equation cos(B*L) * cosh(B*L) + 1 = 0 are the eigenvalues of the beam equation. 
# L is the length of the beam and B is the root/roots. 
# Depending on the order of the equation, the number of roots will vary. 
# The higher the order of cos and cosh in taylor series, the more roots will be there.
def rootsGen(n):
    x = Symbol('x')

    expr1 = 1
    expr2 = 1
    for i in range(1, n+1, 1):
        temp = x**(2*i)/fact(2*i)
        if i%2==0:
            expr1 = expr1 + temp
        else:
            expr1 = expr1 - temp
        expr2 = expr2 + temp

    # exp1 indicates taylor series of cos(x)
    # exp2 indicates taylor series of cosh(x)
    expr = (expr1)*(expr2)+1

    S = simplify(expr)

    P = Poly(S, x)

    coeff = P.coeffs()
    
    ans = []
    for i in np.roots(coeff)**(1/4):
        if re(i)>=0 and im(i)==0:
            ans.append(i)

    return expr, S, ans

def printer(n):
    expr, S, ans = rootsGen(n)

    print(' ')
    print(' ')
    print('##############################################')
    print('The order of expression is', n)
    print(' ')
    print('The expression is:')
    print(expr)
    print(' ')
    print('The simplified expression is:')
    print(S)
    print(' ')
    print('The positive real roots are:')
    print(ans)
    print('##############################################')

# for i in range(1, 31):
#     printer(i)