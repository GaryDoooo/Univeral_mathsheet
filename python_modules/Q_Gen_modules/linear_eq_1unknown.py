from fractions import Fraction
import sympy
try:
    from Q_Gen_modules.my_random import my_randint
    from Q_Gen_modules.fraction_basic import mixed_number_simplify
except BaseException:
    from fraction_basic import mixed_number_simplify
    from my_random import my_randint

function_list = [
    "linear_eq_1unknown_depth1"
]
abstract = "Linear equation with one unknown, whose solution should be integers or fractions."
list_name = "Linear equation: 1 unknown"
#  note = "All symbols in the exponent consolidation problems are positive."

randint = my_randint(100)


def equation_linear_eq_1unknown_depth1():
    #  global randint
    #  init_random_list()
    #  randint = my_randint(100)
    randint.re_init(10000)
    return linear_eq_1unknown(depth=1)


def choice(input_list):
    #  print(input_list)
    return input_list[randint(0, len(input_list) - 1)]


def meet_solution_requirements(solution):
    if "/" in solution:
        # the solution is not a integer
        #  print(solution)
        [nominator, denominator] = solution.split("/")
        #  print(denominator)
        if int(denominator) > 10:
            return False
        if float(nominator) / float(denominator) > 100:
            return False
    elif int(solution)**2 > 10000:
        return False
    return True


def linear_eq_1unknown(depth=2):
    type_pool = ["xt1/xt2=c", "c/xt1=c"] + ["xt1=c", "xt1=xt2+c"] * 3
    equation_type = choice(type_pool)
    while True:
        if equation_type == "xt1/xt2=c":
            equation1, equation_str1, _ = gen_xterm(randint(0, depth))
            equation2, equation_str2, _ = gen_xterm(randint(0, depth))
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
            equation1, equation_str1, _ = gen_xterm(randint(1, depth + 1))
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

    solution = make_mix_number(solution)
    question = random_flip(question)
    return question, "/tiny{%s}../normalsize{x=%s}" % (question, solution)


def random_flip(question):
    if randint(0, 3) > 0:
        return question
    [left, right] = question.split("=")
    return right + " = " + left


def make_mix_number(rational_str):
    if "/" in rational_str:
        [nominator, denominator] = rational_str.split("/")
        return mixed_number_simplify(
            Fraction(int(nominator), int(denominator)))
    else:
        return rational_str


def gen_constant():
    denominator_pool = [2, 4, 5, 8, 10] * 4 + [100]
    type_pool = ["integer"] * 5 + ["fraction", "decimal"]
    gen_type = choice(type_pool)
    while True:
        res = randint(-10, 10)
        if res != 0:
            break
    if gen_type == "integer":
        res_str = str(res)
    else:
        nominator = res
        denominator = choice(denominator_pool)
        res = sympy.Rational(nominator, denominator)
        if gen_type == "fraction":
            if randint(0, 1) == 0:
                res_str = mixed_number_simplify(
                    Fraction(nominator, denominator))
            else:
                res_str = sympy.latex(
                    sympy.Rational(
                        nominator,
                        denominator)).replace(
                    "\\",
                    "/")
        elif gen_type == "decimal":
            res_str = str(nominator / denominator)
    if res_str.endswith(".0"):
        res_str = res_str[:-2]
    return res, res_str


def gen_constant_positive():
    while True:
        res, res_str = gen_constant()
        if res > 0:
            return res, res_str


def gen_single_x_term():
    constant, constant_str = gen_constant()
    res = constant * sympy.symbols('x')
    if constant == 1:
        res_str = "x"
    elif constant == -1:
        res_str = "-x"
    else:
        res_str = constant_str + " x"
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


if __name__ == '__main__':
    for _ in range(10):
        #  print(gen_xterm(2))
        print(equation_linear_eq_1unknown_depth1())
