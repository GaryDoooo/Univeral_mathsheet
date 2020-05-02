from random import randint, choice
from fractions import Fraction
import sympy
try:
    from Q_Gen_modules.fraction_basic import mixed_number_simplify
except BaseException:
    from fraction_basic import mixed_number_simplify

function_list = [
    "equation_one_var_simple",
    #  "equation_one_var_with_xishu_fraction",
    #  "equation_one_var_simple_fraction",
    "equation_one_var_with_xishu"
]
abstract = "Consolidate the expression into one single exponent. It includes different exponent caculations."
list_name = "Exponent consolidate I"
#  note = "All symbols in the exponent consolidation problems are positive."


def equation_one_var_with_xishu_fraction():
    pool = ["times", "divide"]
    term_latex_list, term_symbol_list = gen_terms(2, 3)
    result_latex = ""
    result_symbol = 1
    for (term_latex, term_symbol) in zip(term_latex_list, term_symbol_list):
        operator = choice(pool)
        xishu = randint(2, 12)
        if xishu < 5:
            term_latex = str(xishu) + term_latex
            term_symbol = term_symbol * xishu
            #  with_xishu = True
        #  else:
            #  with_xishu = False
        if operator == "times":
            if len(result_latex) > 0:
                result_latex += "/times " + term_latex
            else:
                result_latex = term_latex
            result_symbol = result_symbol * term_symbol
        elif operator == "divide":
            if len(result_latex) > 0:
                result_latex = "/frac{%s}{%s}" % (result_latex, term_latex)
                result_symbol = result_symbol / term_symbol
            else:
                if randint(0, 3) == 1:
                    # in a few cases put 1 / xxxxx in the beginning
                    result_latex = "/frac{%s}{%s}" % ("1", term_latex)
                    result_symbol = 1 / term_symbol
                else:
                    result_symbol = term_symbol
                    result_latex = term_latex
    question = result_latex + "="
    answer = sympy.latex(sympy.simplify(result_symbol)).replace("\\", "/")
    return question, question + answer


def equation_one_var_simple_fraction():
    pool = ["times", "divide"]
    term_latex_list, term_symbol_list = gen_terms(2, 3)
    result_latex = ""
    result_symbol = 1
    for (term_latex, term_symbol) in zip(term_latex_list, term_symbol_list):
        operator = choice(pool)
        if operator == "times":
            if len(result_latex) > 0:
                result_latex += "/times " + term_latex
            else:
                result_latex = term_latex
            result_symbol = result_symbol * term_symbol
        elif operator == "divide":
            if len(result_latex) > 0:
                result_latex = "/frac{%s}{%s}" % (result_latex, term_latex)
                result_symbol = result_symbol / term_symbol
            else:
                if randint(0, 3) == 1:
                    # in a few cases put 1 / xxxxx in the beginning
                    result_latex = "/frac{%s}{%s}" % ("1", term_latex)
                    result_symbol = 1 / term_symbol
                else:
                    result_symbol = term_symbol
                    result_latex = term_latex
    question = result_latex + "="
    answer = sympy.latex(sympy.simplify(result_symbol)).replace("\\", "/")
    return question, question + answer


def equation_one_var_with_xishu():
    pool = ["times", "divide"]
    term_latex_list, term_symbol_list = gen_terms(2, 4)
    result_latex = ""
    result_symbol = 1
    for (term_latex, term_symbol) in zip(term_latex_list, term_symbol_list):
        operator = choice(pool)
        xishu = randint(2, 12)
        if xishu < 5:
            term_latex = str(xishu) + term_latex
            term_symbol = term_symbol * xishu
            with_xishu = True
        else:
            with_xishu = False
        if operator == "times":
            if len(result_latex) > 0:
                result_latex += "/times " + term_latex
            else:
                result_latex = term_latex
            result_symbol = result_symbol * term_symbol
        elif operator == "divide":
            if len(result_latex) > 0:
                if with_xishu:
                    result_latex += "/div (" + term_latex + ") "
                else:
                    result_latex += "/div " + term_latex
                result_symbol = result_symbol / term_symbol
            else:
                if randint(0, 3) == 1:
                    # in a few cases put 1 / xxxxx in the beginning
                    if with_xishu:
                        result_latex += "1/div (" + term_latex + ") "
                    else:
                        result_latex += "1/div " + term_latex
                    result_symbol = 1 / term_symbol
                else:
                    result_symbol = term_symbol
                    result_latex = term_latex
    question = result_latex + "="
    answer = sympy.latex(sympy.simplify(result_symbol)).replace("\\", "/")
    return question, question + answer


def equation_one_var_simple():
    pool = ["times", "divide"]
    term_latex_list, term_symbol_list = gen_terms(2, 4)
    result_latex = ""
    result_symbol = 1
    for (term_latex, term_symbol) in zip(term_latex_list, term_symbol_list):
        operator = choice(pool)
        if operator == "times":
            if len(result_latex) > 0:
                result_latex += "/times " + term_latex
            else:
                result_latex = term_latex
            result_symbol = result_symbol * term_symbol
        elif operator == "divide":
            if len(result_latex) > 0:
                result_latex += "/div " + term_latex
                result_symbol = result_symbol / term_symbol
            else:
                if randint(0, 3) == 1:
                    # in a few cases put 1 / xxxxx in the beginning
                    result_latex = "1/div " + term_latex
                    result_symbol = 1 / term_symbol
                else:
                    result_symbol = term_symbol
                    result_latex = term_latex
    question = result_latex + "="
    answer = sympy.latex(sympy.simplify(result_symbol)).replace("\\", "/")
    return question, question + answer


def gen_terms(minimun=2, maximun=5):
    num_of_terms = randint(minimun, maximun)
    a, _, symbol_a, _ = get_two_symbols()
    term_latex_list = [a] * num_of_terms
    term_symbol_list = [symbol_a] * num_of_terms
    for i in range(num_of_terms):
        exp = get_exponent()
        if exp == int(exp):  # if it's an integer
            if exp != 1:
                term_latex_list[i] = term_latex_list[i] + "^{" + str(exp) + "}"
            else:
                term_latex_list[i] = term_latex_list[i]
        else:
            if randint(0, 1) == 0:  # if print as fraction
                term_latex_list[i] = term_latex_list[i] + "^{" + str(exp) + "}"
            else:
                frac = Fraction(int(exp * 100), 100)
                if randint(0, 1) == 0:  # if print as mix number
                    term_latex_list[i] = term_latex_list[i] + \
                        "^{" + mixed_number_simplify(frac) + "}"
                else:
                    term_latex_list[i] = term_latex_list[i] + \
                        "^{" + "/frac{%s}{%s}" % (frac.numerator,
                                                  frac.denominator) + "}"
        term_symbol_list[i] = term_symbol_list[i]**exp
    return term_latex_list, term_symbol_list


def get_exponent():
    pool = [1, 1, 1, 2, 2, 0.5, 1, 1, 1, 2, 2, 0.5, 1.5, 2.5, 0]
    if randint(0, 3) == 0:  # possibility of negative
        a = -1
    else:
        a = 1
    return choice(pool) * a


def get_two_symbols():
    pool = ['a', 'b', 'r', 't']
    while True:
        a = choice(pool)
        b = choice(pool)
        if a != b:
            break
    symbol_a = sympy.Symbol(a)
    symbol_b = sympy.Symbol(b)
    return a, b, symbol_a, symbol_b


if __name__ == "__main__":
    for _ in range(10):
        #  print(generate_two_exp())
        #  print(equation_same_exp_compare())
        #  print(equation_same_base_compare())
        #  print(equation_one_var_simple()[1])
        print(equation_one_var_with_xishu_fraction()[1])
        print(equation_one_var_simple_fraction()[1])
