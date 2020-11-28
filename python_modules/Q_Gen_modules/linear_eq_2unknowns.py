import sympy
from linear_eq_1unknown import gen_constant, gen_constant_positive, choice


try:
    from Q_Gen_modules.my_random import my_randint
    #  from Q_Gen_modules.fraction_basic import mixed_number_simplify
except BaseException:
    #  from fraction_basic import mixed_number_simplify
    from my_random import my_randint

function_list = [
    "linear_eq_1unknown_depth1"
]
abstract = "Linear equation with one unknown, whose solution should be integers or fractions."
list_name = "Linear equation: 1 unknown"
#  note = "All symbols in the exponent consolidation problems are positive."

randint = my_randint(100)


def gen_single_x_term():
    if randint(0, 1) == 0:
        symbol = 'x'
    else:
        symbol = 'y'
    constant, constant_str = gen_constant()
    res = constant * sympy.symbols(symbol)
    if constant == 1:
        res_str = symbol
    elif constant == -1:
        res_str = "-" + symbol
    else:
        res_str = constant_str + " " + symbol
    operation = 'multiply' if constant >= 0 else 'substract'
    return res, res_str, operation


def gen_xterm(depth=0):
    if depth == 0:
        return gen_single_x_term()
    xterm, xterm_str, xterm_operation = gen_xterm(depth - 1)
    constant, constant_str = gen_constant_positive()
    if xterm_operation == "multiply" or depth == 1:
        operation_pool = ['add', 'substract'] * 5 + ['divide']
    else:
        operation_pool = ['add', 'substract', 'multiply'] * 5 + ['divide']
    operation = choice(operation_pool)
    if operation == 'add':
        if randint(0, 1) == 0:  # if use xterm instead of constant
            res = xterm + constant
            if randint(0, 1) == 0:  # if switch sequence
                xterm_str, constant_str = constant_str, xterm_str
            if constant_str[0] == '-':
                res_str = xterm_str + "-" + constant_str[1:]
            else:
                res_str = xterm_str + "+" + constant_str
        else:
            xterm2, xterm_str2, xterm_operation2 = gen_xterm(depth - 1)
            res = xterm2 + xterm
            if xterm_str2[0] == '-':
                res_str = xterm_str + "-" + xterm_str2[1:]
            else:
                res_str = xterm_str + "+" + xterm_str2
    elif operation == 'substract':
        if randint(0, 1) == 0:  # if use xterm instead of constant
            if randint(0, 1) == 0:
                res = xterm - constant
                res_str = xterm_str + "-" + constant_str
            else:
                res = constant - xterm
                if xterm_operation in ['add', 'substract']:
                    res_str = constant_str + "-(" + xterm_str + ")"
                else:
                    res_str = constant_str + '-' + xterm_str
        else:
            xterm2, xterm_str2, xterm_operation2 = gen_xterm(depth - 1)
            res = xterm2 - xterm
            if xterm_operation in ['add', 'substract']:
                res_str = xterm_str2 + "- (" + xterm_str + ")"
            else:
                res_str = xterm_str2 + "-" + xterm_str
    elif operation == 'multiply':
        while constant**2 == 1:
            constant, constant_str = gen_constant_positive()
        res = xterm * constant
        if xterm_operation in ['add', 'substract']:
            res_str = constant_str + "/times (" + xterm_str + ")"
        else:
            res_str = constant_str + '/times' + xterm_str
    elif operation == 'divide':
        while constant**2 == 1:
            constant, constant_str = gen_constant_positive()
        res = xterm / constant
        if randint(0, 1) == 0:
            if xterm_operation in ['add', 'substract']:
                #  constant_str=constant_str if constant>=0 else "(%s)"%constant_str
                res_str = "(" + xterm_str + ") /div" + constant_str
            else:
                res_str = xterm_str + "/div " + constant_str
        else:
            res_str = "/dfrac{%s}{%s}" % (xterm_str, constant_str)
    return res, res_str, operation

def linear_eq_2unknowns(depth=2):
    type_pool = ["xt1/xt2=c", "c/xt1=c"] + ["xt1=c", "xt1=xt2+c"] * 3
    equation_type = choice(type_pool)
    while True:
        if equation_type == "xt1/xt2=c":
            while True:
                equation1, equation_str1, _ = gen_xterm(randint(0, depth))
                equation2, equation_str2, _ = gen_xterm(randint(0, depth))
                if equation1 * equation2 != 0:
                    break
            constant, constant_str = gen_constant()
            equation = sympy.Eq(equation1, equation2 * constant)
            question = "/dfrac{%s}{%s} = %s" % (
                equation_str1, equation_str2, constant_str)
        elif equation_type == "xt1=c":
            equation1, equation_str1, _ = gen_xterm(randint(1, depth + 1))
            constant, constant_str = gen_constant()
            equation = sympy.Eq(equation1, constant)
            question = "%s = %s" % (
                equation_str1, constant_str)
        elif equation_type == "xt1=xt2+c":
            equation1, equation_str1, _ = gen_xterm(randint(0, depth))
            equation2, equation_str2, _ = gen_xterm(randint(0, depth))
            constant, constant_str = gen_constant()
            equation = sympy.Eq(equation1 - equation2, constant)
            if constant >= 0:
                question = "%s = %s + %s" % (
                    equation_str1, equation_str2, constant_str)
            else:
                question = "%s = %s - %s" % (
                    equation_str1, equation_str2, constant_str[1:])
        elif equation_type == "c/xt1=c":
            while True:
                equation1, equation_str1, _ = gen_xterm(randint(1, depth + 1))
                if equation1 != 0:
                    break
            constant, constant_str = gen_constant()
            constant2, constant_str2 = gen_constant()
            equation = sympy.Eq(equation1 * constant, constant2)
            question = "/dfrac{%s}{%s} = %s" % (
                constant_str2, equation_str1, constant_str)

        #  print(equation1, equation2, constant, equation)
        try:  # in some case the Eq function will return False instead of an equation
            solution = str(sympy.solve(equation)[0])
            if meet_solution_requirements(solution) and solution != "0":
                break
        except Exception:
            pass

    #  print(equation)
    solution = make_mix_number(solution)
    question = random_flip(question)
    return question, "/tiny{%s}../normalsize{x=%s}" % (question, solution)



if __name__ == '__main__':
    print(gen_xterm(depth=1))
