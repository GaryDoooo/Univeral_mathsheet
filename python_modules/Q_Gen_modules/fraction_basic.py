from random import randint, choice
from fractions import Fraction

function_list = ["1step_plus", "1step_minus", "1step_times", "1step_div"]
abstract = "One step fraction calculation, including plus, minus, multiplication, division, mixed numbers."
list_name = "Fraction 1 step calc."


def equation_1step_plus():
    types = ["two single digits", "one single digit", "two double digits"]
    franction_type = choice(types)
    if franction_type == "two single digits":
        denominator1 = randint(2, 9)
        var1 = Fraction(randint(1, denominator1 - 1), denominator1)
        denominator2 = randint(2, 9)
        var2 = Fraction(randint(1, denominator2 - 1), denominator2)
    elif franction_type == "one single digit":
        denominator1 = randint(2, 9)
        var1 = Fraction(randint(1, denominator1 - 1), denominator1)
        denominator2 = randint(2, 9) * denominator1
        var2 = Fraction(randint(1, int(denominator2 / 2) + 1), denominator2)
    else:
        factor1 = randint(2, 6)
        factor2 = randint(2, 6)
        factor3 = randint(2, 6)
        denominator1 = factor1 * factor2
        denominator2 = factor2 * factor3
        var1 = Fraction(randint(1, denominator1 - 1), denominator1)
        var2 = Fraction(randint(1, denominator2 - 1), denominator2)
    question = "/frac{%s}{%s}+/frac{%s}{%s}=" % (
        var1.numerator, var1.denominator, var2.numerator, var2.denominator)
    answer = var1 + var2
    return question, question + mixed_number_simplify(answer)


def equation_1step_minus():
    types = ["two single digits", "one single digit", "two double digits"]
    franction_type = choice(types)
    while True:
        if franction_type == "two single digits":
            denominator1 = randint(2, 9)
            var1 = Fraction(randint(1, denominator1 - 1), denominator1)
            denominator2 = randint(2, 9)
            var2 = Fraction(randint(1, denominator2 - 1), denominator2)
        elif franction_type == "one single digit":
            denominator1 = randint(2, 9)
            var1 = Fraction(randint(1, denominator1 - 1), denominator1)
            denominator2 = randint(2, 9) * denominator1
            var2 = Fraction(
                randint(
                    1, int(
                        denominator2 / 2) + 1), denominator2)
        else:
            factor1 = randint(2, 6)
            factor2 = randint(2, 6)
            factor3 = randint(2, 6)
            denominator1 = factor1 * factor2
            denominator2 = factor2 * factor3
            var1 = Fraction(randint(1, denominator1 - 1), denominator1)
            var2 = Fraction(randint(1, denominator2 - 1), denominator2)
        question = "/frac{%s}{%s}-/frac{%s}{%s}=" % (
            var1.numerator, var1.denominator, var2.numerator, var2.denominator)
        answer = var1 - var2
        if answer != 0:
            return question, question + mixed_number_simplify(answer)


def equation_1step_times():
    types = [
        "two single digits",
        "one remove",
        "two remove",
        "four remove"]
    franction_type = choice(types)
    while True:
        if franction_type == "two single digits":
            denominator1 = randint(2, 9)
            denominator2 = randint(2, 9)
            numerator1 = randint(1, 9)
            numerator2 = randint(1, 9)
        elif franction_type == "one remove":
            denominator1 = randint(2, 9)
            numerator1 = randint(1, 9)
            numerator2 = randint(1, 9) * denominator1
            denominator2 = randint(2, 9)
            if randint(0, 1) == 1 and denominator1 > 1:
                denominator1, numerator2 = numerator2, denominator1
            if randint(0, 1) == 1:
                denominator1, denominator2 = denominator2, denominator1
                numerator1, numerator2 = numerator2, numerator1
        elif franction_type == "two remove":
            denominator1 = randint(2, 9)
            denominator2 = randint(2, 9)
            numerator1 = randint(1, 9) * denominator2
            numerator2 = randint(1, 9) * denominator1
            if randint(0, 1) == 1 and denominator1 > 1:
                denominator1, numerator2 = numerator2, denominator1
            if randint(0, 1) == 1 and denominator2 > 1:
                denominator2, numerator1 = numerator1, denominator2
        else:
            factor1 = randint(2, 6)
            factor2 = randint(2, 6)
            factor3 = randint(2, 6)
            factor4 = randint(2, 6)
            remove1 = randint(2, 6)
            remove2 = randint(2, 6)
            denominator1 = factor1 * remove1
            denominator2 = factor2 * remove2
            numerator1 = factor3 * remove2
            numerator2 = factor4 * remove1
        if no_one_no_both_integers(
                numerator1,
                denominator1,
                numerator2,
                denominator2):
            break
    var1 = Fraction(numerator1, denominator1)
    var2 = Fraction(numerator2, denominator2)
    answer = var1 * var2
    question = mixed_number_simplify(
        var1) + "/times " + mixed_number_simplify(var2) + "="
    return question, question + mixed_number_simplify(answer)


def no_one_no_both_integers(
        numerator1,
        denominator1,
        numerator2,
        denominator2):
    if numerator1 == denominator1 or numerator2 == denominator2:
        return False
    if numerator1 % denominator1 == 0 and denominator2 % denominator2 == 0:
        return False
    return True


def equation_1step_div():
    types = [
        "two single digits",
        "one remove",
        "two remove",
        "four remove"]
    franction_type = choice(types)
    while True:
        if franction_type == "two single digits":
            denominator1 = randint(2, 9)
            denominator2 = randint(2, 9)
            numerator1 = randint(1, 9)
            numerator2 = randint(1, 9)
        elif franction_type == "one remove":
            denominator1 = randint(2, 9)
            numerator1 = randint(1, 9)
            numerator2 = randint(1, 9) * denominator1
            denominator2 = randint(2, 9)
            if randint(0, 1) == 1 and denominator1 > 1:
                denominator1, numerator2 = numerator2, denominator1
            if randint(0, 1) == 1:
                denominator1, denominator2 = denominator2, denominator1
                numerator1, numerator2 = numerator2, numerator1
        elif franction_type == "two remove":
            denominator1 = randint(2, 9)
            denominator2 = randint(2, 9)
            numerator1 = randint(1, 9) * denominator2
            numerator2 = randint(1, 9) * denominator1
            if randint(0, 1) == 1 and denominator1 > 1:
                denominator1, numerator2 = numerator2, denominator1
            if randint(0, 1) == 1 and denominator2 > 1:
                denominator2, numerator1 = numerator1, denominator2
        else:
            factor1 = randint(2, 6)
            factor2 = randint(2, 6)
            factor3 = randint(2, 6)
            factor4 = randint(2, 6)
            remove1 = randint(2, 6)
            remove2 = randint(2, 6)
            denominator1 = factor1 * remove1
            denominator2 = factor2 * remove2
            numerator1 = factor3 * remove2
            numerator2 = factor4 * remove1
        if no_one_no_both_integers(
                numerator1,
                denominator1,
                numerator2,
                denominator2) and numerator2 > 1:
            break
    var1 = Fraction(numerator1, denominator1)
    var2 = Fraction(denominator2, numerator2)
    answer = var1 / var2
    question = mixed_number_simplify(
        var1) + "/div " + mixed_number_simplify(var2) + "="
    return question, question + mixed_number_simplify(answer)


def mixed_number_simplify(input_fraction):
    result = ""
    if input_fraction.numerator < 0:
        input_fraction = -input_fraction
        result += "-"
    if input_fraction.numerator < input_fraction.denominator:
        result += "/frac{%s}{%s}" % (input_fraction.numerator,
                                     input_fraction.denominator)
    #  elif input_fraction.numerator==input_fraction.denominator:
        #  result=prefix+"1"
    else:
        integer = int(input_fraction.numerator / input_fraction.denominator)
        residue = input_fraction.numerator % input_fraction.denominator
        result += str(integer)
        if residue > 0:
            result += "/frac{%s}{%s}" % (residue, input_fraction.denominator)
    return result


if __name__ == "__main__":
    print(equation_1step_plus())
    print(equation_1step_minus())
    print(equation_1step_times())
    print(equation_1step_div())
