from random import randint, choice
from fractions import Fraction
from Q_Gen_modules.fraction_basic import mixed_number_simplify

function_list = ['same_exp_compare', 'same_base_compare']
abstract = "Compare two exponential expressions, and fill the relationship with greater than or less than or equal. There is no additional calculation step for either side."
list_name = "Exponent comparison"


#  def generate_base():
#  types = [
#  "base<1",
#  "1<base<2",
#  "base>2",
#  "base<1 fraction",
#  "base>1 fraction"]

def equation_same_exp_compare():
    # Generate two bases both >0 and not 1
    while True:
        base1, base2 = generate_two_exp()
        if base1 > 0 and base2 > 0 and base1 != 1 and base2 != 1:
            break
    exp, _ = generate_two_exp()
    question, answer = get_output(base1, exp, base2, exp)
    return question, answer


def equation_same_base_compare():
    # Generate a base 0< and not 1
    while True:
        base, _ = generate_two_exp()
        if base > 0 and base != 1:
            break
    exp1, exp2 = generate_two_exp()
    question, answer = get_output(base, exp1, base, exp2)
    return question, answer


def print_exp_with_fraction(base, exp):
    if isinstance(base, Fraction):
        return "(" + print_rational_number(base) + ")" + \
            "^{" + print_rational_number(exp) + "}"
    else:
        return "{" + print_rational_number(base) + "}" + \
            "^{" + print_rational_number(exp) + "}"


def get_output(base1, exp1, base2, exp2):
    var1 = print_exp_with_fraction(base1, exp1)
    var2 = print_exp_with_fraction(base2, exp2)
    question = var1 + '/;/;/;' + var2
    if base1**exp1 > base2**exp2:
        answer = var1 + ">" + var2
    elif base1**exp1 == base2**exp2:
        answer = var1 + "=" + var2
    else:
        answer = var1 + "<" + var2
    return question, answer


def print_rational_number(i):
    if isinstance(i, Fraction):
        return mixed_number_simplify(i)
    else:
        return str(i)


def generate_two_exp():
    types = ["0<two<1", "two>1", "positive and negative", ">1 and <1"]
    fraction = choice([True, False])
    exp_type = choice(types)
    while True:
        if exp_type == "0<two<1":
            if fraction:
                if randint(0, 1) == 1:  # same numerator or same denominator
                    denominator1 = randint(2, 9)
                    denominator2 = denominator1
                    numerator1 = randint(0, denominator1 - 1)
                    numerator2 = randint(1, denominator1 - 1)
                else:
                    while True:
                        numerator1 = randint(1, 9)
                        numerator2 = numerator1
                        denominator1 = randint(2, 9)
                        denominator2 = randint(2, 9)
                        if denominator1 > numerator1 and denominator2 > numerator2:
                            break
                exp1 = Fraction(numerator1, denominator1)
                exp2 = Fraction(numerator2, denominator2)
            else:
                exp1 = randint(0, 10) / 10
                exp2 = randint(0, 10) / 10

        elif exp_type == "two>1":
            if fraction:
                if randint(0, 1) == 1:  # same numerator or same denominator
                    denominator1 = randint(2, 9)
                    denominator2 = denominator1
                    numerator1 = randint(denominator1 + 1, denominator1 * 5)
                    numerator2 = randint(denominator1 + 1, denominator1 * 5)
                else:
                    while True:
                        numerator1 = randint(1, 45)
                        numerator2 = numerator1
                        denominator1 = randint(2, 9)
                        denominator2 = randint(2, 9)
                        if denominator1 < numerator1 and denominator2 < numerator2:
                            break
                exp1 = Fraction(numerator1, denominator1)
                exp2 = Fraction(numerator2, denominator2)
            else:
                exp1 = randint(11, 100) / 10
                exp2 = randint(11, 100) / 10
        elif exp_type == "positive and negative":
            if randint(0, 1) == 1:
                exp1 = -randint(0, 20) / 10
            else:
                exp1 = -Fraction(randint(0, 19), randint(2, 9))
            if randint(0, 1) == 1:
                exp2 = randint(0, 20) / 10
            else:
                exp2 = Fraction(randint(0, 19), randint(2, 9))
            if randint(0, 1) == 1:
                exp1, exp2 = exp2, exp1
        elif exp_type == ">1 and <1":
            if randint(0, 1) == 1:
                exp1 = randint(11, 100) / 10
            else:
                denominator = randint(2, 9)
                numerator = randint(denominator + 1, denominator * 5)
                exp1 = Fraction(numerator, denominator)
            if randint(0, 1) == 1:
                exp2 = randint(1, 10) / 10
            else:
                denominator = randint(2, 9)
                numerator = randint(1, denominator - 1)
                exp2 = Fraction(numerator, denominator)
            if randint(0, 1) == 1:
                exp1, exp2 = exp2, exp1
        if exp1 != exp2:
            break
    if randint(0, 2) == 1:
        exp1 = -exp1
        exp2 = -exp2
    if randint(0, 1) == 1:
        exp1, exp2 = exp2, exp1
    return exp1, exp2


if __name__ == "__main__":
    for _ in range(100):
        #  print(generate_two_exp())
        #  print(equation_same_exp_compare())
        print(equation_same_base_compare())
