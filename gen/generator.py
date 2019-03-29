import random
import sympy as sym
import gen.math as math

def gen_Quadratic(eqs):
    eq = 0
    stop_step = 0
    while True:
        stop_step += 1
        flag_same_eq = False
        C1, C2, C3 = random.randint(1, 2), random.randint(
            1, 9), random.randint(1, 9)
        eq = math.Quadratic(C1, C2, C3)
        for i in eqs:
            if i.exps == eq.exps:
                flag_same_eq = True
                break
        if not flag_same_eq:
            try:
                if eq.equation()[0].is_real and eq.equation()[1].is_real:
                    return eq
            except:
                if eq.equation()[0].is_real:
                    return eq
        if stop_step > 100:
            raise Exception('Its inf loop ! Too many exam_num')


def gen_Factor(eqs):
    stop_step = 0
    eq = 0
    while True:
        stop_step += 1
        flag_same_eq = False
        C1, C2, C3 = random.randint(1, 9), random.randint(
            0, 50), random.randint(1, 50)
        eq = math.Factor(C1, C2, C3)
        for i in eqs:
            if i.exps == eq.exps:
                flag_same_eq = True
                break
        if not flag_same_eq and not eq.exps == eq.equation():
            return eq
        if stop_step > 100:
            raise Exception('Its inf loop ! Too many exam_num')


def gen_Expand(eqs):
    stop_step = 0
    eq = 0
    while True:
        stop_step += 1
        flag_same_eq = False
        C1, C2, C3 = random.randint(1, 9), random.randint(
            0, 50), random.randint(1, 50)
        eq = math.Expand(C1, C2, C3)
        for i in eqs:
            if i.exps == eq.exps:
                flag_same_eq = True
                break
        if not flag_same_eq and not eq.exps == eq.equation():
            return eq
        if stop_step > 100:
            raise Exception('Its inf loop ! Too many exam_num')
