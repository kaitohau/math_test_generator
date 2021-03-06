import sys
import sympy as sym
import numpy as np
import random
from gen import gen_Expand, gen_Factor, gen_Quadratic,gen_plus_minus, LatexFile

def main(exam_num=50, test_type="Quadratic"):
    """
    test_type: Quadratic or Factor
    
    """

    eqs = []# array of eqation 

    # genretor for each test type
    if test_type == "Quadratic":
        for i in range(exam_num):
            eq = gen_Quadratic(eqs)#genretor
            eqs.append(eq)

    elif test_type == "Factor":
        for i in range(exam_num):
            eq = gen_Factor(eqs)  # genretor
            eqs.append(eq)  
    elif test_type == "plus_minus":
        for i in range(exam_num):
            eq = gen_plus_minus(eqs)  # genretor
            eqs.append(eq)  

    # make Tex file
    exam = LatexFile(test_type + '_exam', title='計算ドリル', point=9)
    sol = LatexFile(test_type + '_solution', title='計算ドリル答え', point=9)
    exam.begin_cols()# add multicol
    sol.begin_cols()  # add multicol

    for e in eqs:  # add item to tex
        # sym.latex isconvert math eqation to tex
        exam.add_eq(' ' + sym.latex(e.exps))
        sol.add_eq(' ' + sym.latex(e.equation())) 

    exam.end_cols()  # add multicol
    sol.end_cols()

    exam.compile()  # make tex file and pdf
    sol.compile()

if __name__ == '__main__':
    num=50
    test_type = "Quadratic"
    if len(sys.argv)>1:
        if sys.argv[1]:
            num = int(sys.argv[1])
        if sys.argv[2]:
            test_type = sys.argv[2]
    main(num, test_type)
