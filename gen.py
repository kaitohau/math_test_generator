# from latexfile import LatexFile
import sympy as sym
import numpy as np
import random
from gen import gen_Expand, gen_Factor, gen_Quadratic, LatexFile

def main(exam_num=50, test_type="Quadratic"):
    eqs = []

    if test_type == "Quadratic":
        for i in range(exam_num):
            eq = gen_Quadratic(eqs)
            eqs.append(eq)

    elif test_type == "Factor":
        for i in range(exam_num):
            eq = gen_Factor(eqs)
            eqs.append(eq)

    exam = LatexFile(test_type + '_exam', title='計算ドリル', point=9)
    sol = LatexFile(test_type + '_solution', title='計算ドリル答え', point=9)
    exam.begin_cols()
    sol.begin_cols()
    for e in eqs:
        exam.add_eq(' ' + sym.latex(e.exps))
        sol.add_eq(' ' + sym.latex(e.equation()))
    exam.end_cols()
    sol.end_cols()
    exam.compile()
    sol.compile()

if __name__ == '__main__':
    main(50, test_type="Quadratic")
