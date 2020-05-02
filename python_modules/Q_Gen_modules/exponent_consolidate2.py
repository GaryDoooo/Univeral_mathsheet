from random import randint, choice, shuffle
from fractions import Fraction
import sympy
try:
    from Q_Gen_modules.fraction_basic import mixed_number_simplify
except BaseException:
    from fraction_basic import mixed_number_simplify

function_list = [
    "equation_two_var_simple_fraction",
    "equation_one_var_with_exponent_root"
]
abstract = "Consolidate the expression into one single exponent for one variable. It includes different exponent caculations, and may include two variables."
list_name = "Exponent consolidate II"
note = "All symbols in the exponent consolidation problems are positive."


def equation_one_var_with_exponent_root():
    term_latex_list, term_symbol_list = gen_one_terms(2, 4)
    pool = ["exponent", "root"]
    num_of_tricks = randint(1, 2)
    for _ in range(num_of_tricks):
        length = len(term_symbol_list)
        start_point = randint(0, length - 1)
        end_point = randint(start_point + 1, length)
        prefix_latex_list = term_latex_list[:start_point]
        prefix_symbol_list = term_symbol_list[:start_point]
        suffix_latex_list = term_latex_list[end_point:]
        suffix_symbol_list = term_symbol_list[end_point:]
        trick_latex_list = term_latex_list[start_point:end_point]
        trick_symbol_list = term_symbol_list[start_point:end_point]
        new_latex, new_symbol = combine_terms_into_one(
            trick_latex_list, trick_symbol_list)
        trick = choice(pool)
        if trick == "exponent":
            new_latex, new_symbol = add_exponent(new_latex, new_symbol)
        elif trick == "root":
            new_latex, new_symbol = add_root(new_latex, new_symbol)
        prefix_latex_list.append(new_latex)
        prefix_symbol_list.append(new_symbol)
        prefix_latex_list.extend(suffix_latex_list)
        prefix_symbol_list.extend(suffix_symbol_list)
        term_latex_list = prefix_latex_list
        term_symbol_list = prefix_symbol_list
    result_latex, result_symbol = combine_terms_into_one(
        term_latex_list, term_symbol_list)
    question = result_latex + "="
    answer = sympy.latex(sympy.simplify(result_symbol)).replace(
        "\\", "/").replace(".0", "")
    return question, question + answer


def equation_two_var_simple_fraction():
    term_latex_list, term_symbol_list = gen_terms(3, 4)
    result_latex, result_symbol = combine_terms_into_one(
        term_latex_list, term_symbol_list)
    question = result_latex + "="
    answer = sympy.latex(sympy.simplify(result_symbol)).replace(
        "\\", "/").replace(".0", "")
    return question, question + answer


def add_exponent(term_latex, term_symbol):
    pool = [-1, -0.5, 0, 1, 2, 0.5, 2, 2, 4, 4, 2, 4]
    exp = choice(pool)
    term_latex = "(" + term_latex + ")^{%s}" % str(exp)
    term_symbol = term_symbol**exp
    return term_latex, term_symbol


def add_root(term_latex, term_symbol):
    pool = [1, 2, 0.5, 2, 2, 4]
    exp = choice(pool)
    if exp == 2:
        term_latex = "/sqrt{%s}" % term_latex
    else:
        term_latex = "/sqrt[%s]{%s}" % (str(exp), term_latex)
    term_symbol = term_symbol**(1 / exp)
    return term_latex, term_symbol


def combine_terms_into_one(term_latex_list, term_symbol_list):
    if len(term_latex_list) == 1:
        return term_latex_list[0], term_symbol_list[0]
    pool = ["times", "divide"]
    result_latex = ""
    result_symbol = 1
    for (term_latex, term_symbol) in zip(term_latex_list, term_symbol_list):
        operator = choice(pool)
        if randint(0, 1) == 0:  # if print as fraction for dividens
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
        else:
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
    return result_latex, result_symbol


def gen_terms(minimun=2, maximun=5):
    num_of_terms = randint(minimun, maximun)
    a, b, symbol_a, symbol_b = get_two_symbols()
    term_latex_list = [a, b] * num_of_terms
    term_symbol_list = [symbol_a, symbol_b] * num_of_terms
    shuffle(term_symbol_list)
    shuffle(term_latex_list)
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
    return term_latex_list[:num_of_terms], term_symbol_list[:num_of_terms]


def gen_one_terms(minimun=2, maximun=5):
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
    symbol_a = sympy.Symbol(a, positive=True)
    symbol_b = sympy.Symbol(b, positive=True)
    return a, b, symbol_a, symbol_b


if __name__ == "__main__":
    for _ in range(10):
        #  print(generate_two_exp())
        #  print(equation_same_exp_compare())
        #  print(equation_same_base_compare())
        #  print(equation_one_var_simple()[1])
        #  print(equation_one_var_with_xishu_fraction()[1])
        #  print(equation_one_var_simple_fraction()[1])
        print(equation_one_var_with_exponent_root()[1])
        print(equation_two_var_simple_fraction()[1])
