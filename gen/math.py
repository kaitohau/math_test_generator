import sympy as sym

class Quadratic:
    
    def __init__(self, a, b, c):

        # define x 
        sym.var('x')

        # strict to use rational有理数のこと
        self.a = sym.Rational(a)
        self.b = sym.Rational(b)
        self.c = sym.Rational(c)
        
        # Quadratic func
        self.exps = self.a*x**2 + self.b*x + self.c
        
    # return vule
    def value(self, t):
        return self.exps.subs(x, t)

    def vertex(self):
        xv = -self.b / (2*self.a)
        yv = (-self.b**2 + 4*self.a*self.c)/(4*self.a)
        return(xv, yv)
    
    # return solution
    def equation(self):
        eq = sym.Eq(self.exps, 0)
        return sym.solve(eq)


class Factor:
    def __init__(self, a, b, c):

        # define x
        sym.var('x')

        # strict to use rational有理数のこと
        self.a = sym.Rational(a)
        self.b = sym.Rational(b)
        self.c = sym.Rational(c)

        # Quadratic func
        self.exps = self.a * x**2 + self.b * x + self.c

    # return factor
    def equation(self):
        eq = sym.factor(self.exps)
        return eq


class Expand:
    def __init__(self, eq):

        # 記号xを定義
        sym.var('x')

        self.a = sym.Rational(a)
        self.b = sym.Rational(b)
        self.c = sym.Rational(c)

        self.exps = self.a * x**2 + self.b * x + self.c

    # return expand
    def equation(self):
        eq = sym.Expand(self.exps)
        return eq
