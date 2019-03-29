import sympy as sym

class Quadratic:
    
    def __init__(self, a, b, c):

        # 記号xを定義
        sym.var('x')

        # a, b, c を有理数型に変換>小数点にしない
        self.a = sym.Rational(a)
        self.b = sym.Rational(b)
        self.c = sym.Rational(c)
        
        # 2次関数の表式
        self.exps = self.a*x**2 + self.b*x + self.c
        
    # 2次関数の値を返すメソッド
    def value(self, t):
        return self.exps.subs(x, t)
    
    # 頂点の座標を返すメソッド
    def vertex(self):
        xv = -self.b / (2*self.a)
        yv = (-self.b**2 + 4*self.a*self.c)/(4*self.a)
        return(xv, yv)
    
    # 2次方程式と解を返すメソッド
    def equation(self):
        eq = sym.Eq(self.exps, 0)
        return sym.solve(eq)


class Factor:
    def __init__(self, a, b, c):

        # 記号xを定義
        sym.var('x')

        # a, b, c を有理数型に変換>小数点にしない
        self.a = sym.Rational(a)
        self.b = sym.Rational(b)
        self.c = sym.Rational(c)

        # 2次関数の表式
        self.exps = self.a * x**2 + self.b * x + self.c

    # 因数分解
    def equation(self):
        eq = sym.factor(self.exps)
        return eq


class Expand:
    def __init__(self, eq):

        # 記号xを定義
        sym.var('x')

        # a, b, c を有理数型に変換>小数点にしない
        self.a = sym.Rational(a)
        self.b = sym.Rational(b)
        self.c = sym.Rational(c)

        # 2次関数の表式
        self.exps = self.a * x**2 + self.b * x + self.c

    # 因数分解
    def equation(self):
        eq = sym.Expand(self.exps)
        return eq
