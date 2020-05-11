from random import randint, choice
import sympy

function_list = [
    "square",
    "yici_2xiang",
    #  "with_exponent_four_operator",
    "equation_two_bracket_square",
    "equation_yici_2xiang_with_number",
    "equation_x_square_minus_y_square_with_number",
    "equation_square_with_number",
    "equation_two_bracket_square_with_number",
    "equation_x_square_minus_y_square"]
abstract = "Expand symbolic expressions into polynomials."
list_name = "Symbolic expansion I"


def equation_square_with_number():
    a, b, symbol_a, symbol_b = get_two_symbols()
    while True:
        m = randint(-5, 5)
        n = randint(-5, 5)
        if m * n != 0:
            break
    term1 = gen_term(a, m)
    term2 = gen_number_term(n)
    symbol_b = 1
    if randint(0, 1) == 1:
        term1, term2 = term2, term1
        symbol_a, symbol_b = symbol_b, symbol_a
        m, n = n, m
    bracket, _ = one_bracket(term1, term2, 1, 1, "+")
    question = "(" + bracket + ")^2="
    result = sympy.latex(sympy.expand(
        (m * symbol_a + n * symbol_b)**2)).replace("\\", "/")
    return question, question + result


def equation_square():
    a, b, symbol_a, symbol_b = get_two_symbols()
    while True:
        m = randint(-5, 5)
        n = randint(-5, 5)
        if m * n != 0:
            break
    term1 = gen_term(a, m)
    term2 = gen_term(b, n)
    bracket, _ = one_bracket(term1, term2, 1, 1, "+")
    question = "(" + bracket + ")^2="
    result = sympy.latex(sympy.expand(
        (m * symbol_a + n * symbol_b)**2)).replace("\\", "/")
    return question, question + result


def equation_yici_2xiang_with_number():
    [m1, n1, m2, n2] = get_four_xishu()
    a, b, symbol_a, symbol_b = get_two_symbols()
    term1 = gen_term(a, m1)
    symbol_term1 = m1 * symbol_a
    term2 = gen_term(b, n1)
    symbol_term2 = n1 * symbol_b
    term3 = gen_term(a, m2)
    symbol_term3 = m2 * symbol_a
    term4 = gen_term(b, n2)
    symbol_term4 = n2 * symbol_b

    if randint(0, 1) == 1:
        term2 = gen_number_term(n1)
        symbol_term2 = n1
        if randint(0, 1) == 1:
            term4 = gen_number_term(n2)
            symbol_term4 = n2
    else:
        term4 = gen_number_term(n2)
        symbol_term4 = n2

    if randint(0, 1) == 1:
        term1, term2 = term2, term1
        symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    if randint(0, 1) == 1:
        term3, term4 = term4, term3
        symbol_term3, symbol_term4 = symbol_term4, symbol_term3

    bracket1, symbol_bracket1 = one_bracket(
        term1=term1, term2=term2, symbol_term1=symbol_term1, symbol_term2=symbol_term2, operator="+")
    bracket2, symbol_bracket2 = one_bracket(
        term1=term3, term2=term4, symbol_term1=symbol_term3, symbol_term2=symbol_term4, operator="+")
    expression = symbol_bracket1 * symbol_bracket2
    if "+" in bracket1 or ("-" in bracket1 and bracket1[0] != "-") or bracket1.count(
            "-") > 1 or "/div" in bracket1:
        question = "(" + bracket1 + ")(" + bracket2 + ")="
    else:
        question = bracket1 + "(" + bracket2 + ")="
    if m2 * n2 == 0:
        question = bracket2 + "(" + bracket1 + ")="
    #  expression = (m1 * symbol_a + n1 * symbol_b) * \
        #  (m2 * symbol_a + n2 * symbol_b)
    result = sympy.latex(sympy.expand(expression)).replace("\\", "/")
    return question, question + result


def equation_yici_2xiang():
    [m1, n1, m2, n2] = get_four_xishu()
    a, b, symbol_a, symbol_b = get_two_symbols()
    term1 = gen_term(a, m1)
    term2 = gen_term(b, n1)
    term3 = gen_term(a, m2)
    term4 = gen_term(b, n2)
    symbol_term1 = m1 * symbol_a
    symbol_term2 = n1 * symbol_b
    symbol_term3 = m2 * symbol_a
    symbol_term4 = n2 * symbol_b
    if randint(0, 1) == 1:
        term1, term2 = term2, term1
        symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    bracket1, symbol_bracket1 = one_bracket(
        term1=term1, term2=term2, symbol_term1=symbol_term1, symbol_term2=symbol_term2, operator="+")
    bracket2, symbol_bracket2 = one_bracket(
        term1=term3, term2=term4, symbol_term1=symbol_term3, symbol_term2=symbol_term4, operator="+")
    expression = symbol_bracket1 * symbol_bracket2
    if "+" in bracket1 or ("-" in bracket1 and bracket1[0] != "-") or bracket1.count(
            "-") > 1 or "/div" in bracket1:
        question = "(" + bracket1 + ")(" + bracket2 + ")="
    else:
        question = bracket1 + "(" + bracket2 + ")="
    if m2 * n2 == 0:
        question = bracket2 + "(" + bracket1 + ")="
    expression = (m1 * symbol_a + n1 * symbol_b) * \
        (m2 * symbol_a + n2 * symbol_b)
    result = sympy.latex(sympy.expand(expression)).replace("\\", "/")
    return question, question + result

    #  if randint(0, 1) == 1:
    #  term2 = gen_number_term(n1)
    #  symbol_term2 = n1
    #  if randint(0, 1) == 1:
    #  term4 = gen_number_term(n2)
    #  symbol_term4 = n2
    #  else:
    #  term4 = gen_number_term(n2)
    #  symbol_term4 = n2


def equation_two_bracket_square_with_number():
    a, b, symbol_a, symbol_b = get_two_symbols()
    while True:
        [m1, n1, _, _] = get_four_xishu()
        #  [e1, e2, _, _] = get_four_exponents()
        e1, e2 = 1, 1
        if not (e1 == 0 and e2 == 0) and m1 * n1 != 0:
            break
    if randint(0, 2) < 2:
        term1 = gen_term(a, m1, e1)
        term2 = gen_term(b, n1, e2)
        term3 = gen_term(a, -m1, e1)
        term4 = gen_term(b, -n1, e2)
        symbol_term1 = m1 * symbol_a**e1
        symbol_term2 = n1 * symbol_b**e2
        symbol_term3 = -m1 * symbol_a**e1
        symbol_term4 = -n1 * symbol_b**e2

        term2 = gen_number_term(n1)
        symbol_term2 = n1
        term4 = gen_number_term(-n1)
        symbol_term4 = -n1

        if randint(0, 1) == 1:
            term1, term2 = term2, term1
            symbol_term1, symbol_term2 = symbol_term2, symbol_term1
        if randint(0, 1) == 1:
            term3, term4 = term4, term3
            symbol_term3, symbol_term4 = symbol_term4, symbol_term3
    else:
        term1 = gen_term(a, m1, e1)
        term2 = gen_term(b, n1, e2)
        term3 = gen_term(a, m1, e1)
        term4 = gen_term(b, n1, e2)
        symbol_term1 = m1 * symbol_a**e1
        symbol_term2 = n1 * symbol_b**e2
        symbol_term3 = m1 * symbol_a**e1
        symbol_term4 = n1 * symbol_b**e2
        #  term1, term2 = term2, term1
        #  symbol_term1, symbol_term2 = symbol_term2, symbol_term1

        term2 = gen_number_term(n1)
        symbol_term2 = n1
        term4 = gen_number_term(n1)
        symbol_term4 = n1

        if randint(0, 1) == 1:
            term1, term2 = term2, term1
            symbol_term1, symbol_term2 = symbol_term2, symbol_term1
        if randint(0, 1) == 1:
            term3, term4 = term4, term3
            symbol_term3, symbol_term4 = symbol_term4, symbol_term3

    bracket1, symbol_bracket1 = one_bracket(
        term1=term1, term2=term2, symbol_term1=symbol_term1, symbol_term2=symbol_term2, operator="+")
    bracket2, symbol_bracket2 = one_bracket(
        term1=term3, term2=term4, symbol_term1=symbol_term3, symbol_term2=symbol_term4, operator="+")
    expression = symbol_bracket1 * symbol_bracket2
    question = "(" + bracket1 + ")(" + bracket2 + ")="
    result = sympy.latex(sympy.expand(expression)).replace("\\", "/")
    return question, question + result


def equation_two_bracket_square():
    a, b, symbol_a, symbol_b = get_two_symbols()
    while True:
        [m1, n1, _, _] = get_four_xishu()
        #  [e1, e2, _, _] = get_four_exponents()
        e1, e2 = 1, 1
        if not (e1 == 0 and e2 == 0) and m1 * n1 != 0:
            break
    if randint(0, 2) < 2:
        term1 = gen_term(a, m1, e1)
        term2 = gen_term(b, n1, e2)
        term3 = gen_term(a, -m1, e1)
        term4 = gen_term(b, -n1, e2)
        symbol_term1 = m1 * symbol_a**e1
        symbol_term2 = n1 * symbol_b**e2
        symbol_term3 = -m1 * symbol_a**e1
        symbol_term4 = -n1 * symbol_b**e2
        if randint(0, 1) == 1:
            term1, term2 = term2, term1
            symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    else:
        term1 = gen_term(a, m1, e1)
        term2 = gen_term(b, n1, e2)
        term3 = gen_term(a, m1, e1)
        term4 = gen_term(b, n1, e2)
        symbol_term1 = m1 * symbol_a**e1
        symbol_term2 = n1 * symbol_b**e2
        symbol_term3 = m1 * symbol_a**e1
        symbol_term4 = n1 * symbol_b**e2
        term1, term2 = term2, term1
        symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    bracket1, symbol_bracket1 = one_bracket(
        term1=term1, term2=term2, symbol_term1=symbol_term1, symbol_term2=symbol_term2, operator="+")
    bracket2, symbol_bracket2 = one_bracket(
        term1=term3, term2=term4, symbol_term1=symbol_term3, symbol_term2=symbol_term4, operator="+")
    expression = symbol_bracket1 * symbol_bracket2
    question = "(" + bracket1 + ")(" + bracket2 + ")="
    result = sympy.latex(sympy.expand(expression)).replace("\\", "/")
    return question, question + result


def equation_x_square_minus_y_square_with_number():
    a, b, symbol_a, symbol_b = get_two_symbols()
    while True:
        [m1, n1, _, _] = get_four_xishu()
        #  [e1, e2, _, _] = get_four_exponents()
        e1, e2 = 1, 1
        if not (e1 == 0 and e2 == 0) and m1 * n1 != 0:
            break
    term1 = gen_term(a, m1, e1)
    term2 = gen_term(b, n1, e2)
    term3 = gen_term(a, m1, e1)
    term4 = gen_term(b, -n1, e2)
    symbol_term1 = m1 * symbol_a**e1
    symbol_term2 = n1 * symbol_b**e2
    symbol_term3 = m1 * symbol_a**e1
    symbol_term4 = -n1 * symbol_b**e2

    if randint(0, 1) == 1:
        term2 = gen_number_term(n1)
        symbol_term2 = n1
        term4 = gen_number_term(-n1)
        symbol_term4 = -n1
    else:
        term1 = gen_number_term(m1)
        symbol_term1 = m1
        term3 = gen_number_term(m1)
        symbol_term3 = m1

    if randint(0, 1) == 1:
        term1, term2 = term2, term1
        symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    if randint(0, 1) == 1:
        term3, term4 = term4, term3
        symbol_term3, symbol_term4 = symbol_term4, symbol_term3
    #
    #  if randint(0, 1) == 1:
        #  term1, term2 = term2, term1
        #  symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    bracket1, symbol_bracket1 = one_bracket(
        term1=term1, term2=term2, symbol_term1=symbol_term1, symbol_term2=symbol_term2, operator="+")
    bracket2, symbol_bracket2 = one_bracket(
        term1=term3, term2=term4, symbol_term1=symbol_term3, symbol_term2=symbol_term4, operator="+")
    expression = symbol_bracket1 * symbol_bracket2
    question = "(" + bracket1 + ")(" + bracket2 + ")="
    result = sympy.latex(sympy.expand(expression)).replace("\\", "/")
    return question, question + result


def equation_x_square_minus_y_square():
    a, b, symbol_a, symbol_b = get_two_symbols()
    while True:
        [m1, n1, _, _] = get_four_xishu()
        #  [e1, e2, _, _] = get_four_exponents()
        e1, e2 = 1, 1
        if not (e1 == 0 and e2 == 0) and m1 * n1 != 0:
            break
    term1 = gen_term(a, m1, e1)
    term2 = gen_term(b, n1, e2)
    term3 = gen_term(a, m1, e1)
    term4 = gen_term(b, -n1, e2)
    symbol_term1 = m1 * symbol_a**e1
    symbol_term2 = n1 * symbol_b**e2
    symbol_term3 = m1 * symbol_a**e1
    symbol_term4 = -n1 * symbol_b**e2
    if randint(0, 1) == 1:
        term1, term2 = term2, term1
        symbol_term1, symbol_term2 = symbol_term2, symbol_term1
    bracket1, symbol_bracket1 = one_bracket(
        term1=term1, term2=term2, symbol_term1=symbol_term1, symbol_term2=symbol_term2, operator="+")
    bracket2, symbol_bracket2 = one_bracket(
        term1=term3, term2=term4, symbol_term1=symbol_term3, symbol_term2=symbol_term4, operator="+")
    expression = symbol_bracket1 * symbol_bracket2
    question = "(" + bracket1 + ")(" + bracket2 + ")="
    result = sympy.latex(sympy.expand(expression)).replace("\\", "/")
    return question, question + result


def gen_number_term(m):
    if m < 0:
        result = "-"
        m = -m
    elif m == 0:
        return "{}"
    else:
        result = " "
    result += str(m)
    return result


def gen_term(a, m, e=1):
    if m < 0:
        result = "-"
        m = -m
    elif m == 0:
        return "{}"
    else:
        result = " "
    if m == 1:
        str_m = " "
    else:
        str_m = str(m)
    if e == 1:
        #  if randint(0, 3) > 2:
        #  result += str_m + a + "^{1}"
        #  else:
        result += str_m + a
    elif e < 0:
        if randint(0, 1) == 1:  # if to print in fraction
            if e == -1:
                result += "/frac{" + str(m) + "}{%s}" % a
            else:
                result += "/frac{" + str(m) + "}{%s^{%s}}" % (a, str(-e))
        else:
            result += str_m + a + "^{%s}" % e
    elif e == 0:
        if randint(0, 2) > 1:
            result += str_m
            if str_m == " ":
                result += "1"
        else:
            result += str_m + a + "^{%s}" % e
    else:
        result += str_m + a + "^{%s}" % e
    return result


def one_bracket(
        term1=" ",
        term2=" ",
        symbol_term1=0,
        symbol_term2=0,
        operator="+"):
    if term2 == "{}":
        return term1, symbol_term1
    if term1 == "{}":
        return term2, symbol_term2
    result = term1
    if term2[0] == "-":
        if operator != "+":
            result += operator + "(" + term2 + ")"
        else:
            result += term2
    else:
        result += operator + term2
    if operator == "+":
        symbol_result = symbol_term1 + symbol_term2
    elif operator == "-":
        symbol_result = symbol_term1 - symbol_term2
    elif operator == "/times":
        symbol_result = symbol_term1 * symbol_term2
    else:
        symbol_result = symbol_term1 / symbol_term2
    return result, symbol_result


def get_two_operators():
    pool = ['+', '-', '/times', '/div', '+', '-', '+', '-', '+', '-', '+']
    return choice(pool), choice(pool)


def get_four_xishu():
    pool = [1, 1, 1, -1, -1, -1, 0, -2, -2, 2, 2, -3, -4, 3, 4]
    while True:
        result = []
        for _ in range(4):
            result.append(choice(pool))
        if [_ == 0 for _ in result].count(True) < 2:
            break
    return result


def get_four_exponents():
    pool = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2,
            1.5, -0.5, -1, 0.5, 3, 4, -1.5, -2, 0]
    while True:
        result = []
        for _ in range(4):
            result.append(choice(pool))
        if [_ == 0 for _ in result].count(True) < 2:
            break
    return result


def get_two_symbols():
    pool = [['a', 'b'], ['x', 'y']]
    #  while True:
    #  a = choice(pool)
    #  b = choice(pool)
    #  if a != b:
    #  break
    [a, b] = choice(pool)
    symbol_a = sympy.Symbol(a)
    symbol_b = sympy.Symbol(b)
    return a, b, symbol_a, symbol_b


if __name__ == "__main__":
    for _ in range(10):
        #  print(equation_square())
        #  print(equation_yici_2xiang())
        #  print(equation_with_exponent_four_operator()[1])
        #  print(equation_x_square_minus_y_square()[1])
        #  print(equation_two_bracket_square()[1])
        print(equation_yici_2xiang_with_number()[1])
        #  print(equation_square_with_number()[1])
        #  print(equation_two_bracket_square_with_number()[1])
        #  print(equation_x_square_minus_y_square_with_number()[1])
