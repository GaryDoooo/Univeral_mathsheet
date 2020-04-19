from fractions import Fraction
from numpy import random
import math
import numpy as np


def two_number_add(
        first_num_max, first_num_min, second_num_max, second_num_min, result_max):
    while True:
        a = random.randint(first_num_min, first_num_max + 1)
        b = random.randint(second_num_min, second_num_max + 1)
        if a + b <= result_max:
            break
    new_problem = "%d + %d = " % (a, b)
    new_answer = new_problem + "%d" % (a + b)
    return new_problem, new_answer


def two_number_sub(
        first_num_max, first_num_min, second_num_max, second_num_min):
    a = random.randint(first_num_min, first_num_max + 1)
    b = random.randint(second_num_min, second_num_max + 1)
    #  first_number, second_number):
    #  a = random.randint(10**(first_number - 1), 10**(first_number))
    #  b = random.randint(10**(second_number - 1), 10**second_number)
    big = max(a, b)
    small = min(a, b)
    new_problem = "%d - %d = " % (big, small)
    new_answer = new_problem + "%d" % (big - small)
    return new_problem, new_answer


def two_number_mul(
        first_num_max, first_num_min, second_num_max, second_num_min, result_max, no_one=True):
    while True:
        a = random.randint(first_num_min, first_num_max + 1)
        b = random.randint(second_num_min, second_num_max + 1)
        if a != 1 and b != 1 and a * b <= result_max:
            break
        if not no_one:
            break
    new_problem = "%d x %d = " % (a, b)
    new_answer = new_problem + "%d" % (a * b)
    return new_problem, new_answer


def two_number_div(
        first_num_max, first_num_min, second_num_max, second_num_min, no_one=True):
    a = random.randint(10**(first_number - 1), 10**first_number)
    while True:
        b = random.randint(10**(second_number - 1), 10**second_number)
        if b != 1:
            break
        if not no_one:
            break
    new_problem = "%d / %d = " % (a, b)
    shang = int(a / b)
    remain = a % b
    if remain == 0:
        new_answer = new_problem + "%d " % shang
    else:
        new_answer = new_problem + "%d R%d" % (shang, remain)
    return new_problem, new_answer

    #  problem_list, answer_list = generator.two_number_operation(
    #  first_num_max, second_num_max, result_max,
    #  first_num_min, second_num_min, operator_in_number, problem_num, no_one)


def two_number_operation(
        first_num_max=100,
        second_num_max=100,
        result_max=10000,
        first_num_min=2,
        second_num_min=2,
        operator=1,
        problem_num=10,
        no_one=True):
    problem_list = []
    answer_list = []
    for i in range(1, problem_num + 1):
        if operator == 1:
            new_problem, new_answer = two_number_add(
                first_num_max, first_num_min, second_num_max,
                second_num_min, result_max)
        elif operator == 2:
            new_problem, new_answer = two_number_sub(
                first_num_max, first_num_min, second_num_max, second_num_min)
        elif operator == 3:
            new_problem, new_answer = two_number_mul(
                first_num_max, first_num_min, second_num_max,
                second_num_min, result_max, no_one)
        elif operator == 4:
            new_problem, new_answer = two_number_div(
                first_num_max, first_num_min, second_num_max,
                second_num_min, no_one)
        problem_list.append(("[%d] " % i) + new_problem)
        answer_list.append(("[%d] " % i) + new_answer)
    return problem_list, answer_list

###### Krypto generator below ######


def cal_first_without_bracket(left_operator, right_operator):

    RIGHT_FIRST = 1
    LEFT_FIRST = 2
    DOESNT_MATTER = 0

    if left_operator >= 500 or right_operator >= 500:
        return DOESNT_MATTER

    left_operator = left_operator % 10
    right_operator = right_operator % 10

    if left_operator == 0:
        if right_operator <= 1:
            return DOESNT_MATTER
        elif 1 < right_operator < 4:
            return RIGHT_FIRST
    if left_operator == 1:
        if right_operator <= 1:
            return LEFT_FIRST
        elif 1 < right_operator < 4:
            return RIGHT_FIRST
    if left_operator == 2:
        if 1 < right_operator < 4:
            return DOESNT_MATTER
        elif right_operator <= 1:
            return LEFT_FIRST
    if left_operator == 3:
        return LEFT_FIRST


def krypto_print(numbers, operators, parent_right_operator=None, parent_left_operator=None):

    RIGHT_FIRST = 1
    LEFT_FIRST = 2
    # DOESNT_MATTER = 0

    if len(numbers) == 1:
        return "%d" % numbers[0]
    else:
        calculate_last = np.argmin(np.floor(operators / 2))
        answer_of_1st_part = krypto_print(numbers[:(calculate_last + 1)], operators[:(
            calculate_last)], parent_right_operator=operators[calculate_last])
        answer_of_2nd_part = krypto_print(numbers[(calculate_last + 1):], operators[(
            calculate_last + 1):], parent_left_operator=operators[calculate_last])
        if operators[calculate_last] >= 500:
            answer = answer_of_1st_part + answer_of_2nd_part
        else:
            operator = operators[calculate_last] % 10
            if operator == 0:
                answer = answer_of_1st_part + " + " + answer_of_2nd_part
            elif operator == 1:
                answer = answer_of_1st_part + " - " + answer_of_2nd_part
            elif operator == 2:
                answer = answer_of_1st_part + " x " + answer_of_2nd_part
            elif operator == 3:
                answer = answer_of_1st_part + " / " + answer_of_2nd_part
            if parent_right_operator is not None:
                if cal_first_without_bracket(operator, parent_right_operator) == RIGHT_FIRST:
                    answer = "(" + answer + ")"
            if parent_left_operator is not None:
                if cal_first_without_bracket(parent_left_operator, operator) == LEFT_FIRST:
                    answer = "(" + answer + ")"
        return answer


def krypto_cal(numbers, operators):
    #    print numbers, operators
    if len(numbers) == 1:
        return numbers[0]
    else:
        calculate_last = np.argmin(np.floor(operators / 2))
#        print calculate_last
        answer_of_1st_part = krypto_cal(
            numbers[:calculate_last + 1], operators[:(calculate_last)])
        answer_of_2nd_part = krypto_cal(
            numbers[(calculate_last + 1):], operators[(calculate_last + 1):])
#        print "Returned answer:", answer_of_1st_part, answer_of_2nd_part
        if math.isnan(answer_of_1st_part) or math.isnan(answer_of_2nd_part):
            return float('nan')
        if operators[calculate_last] >= 500:
            answer = answer_of_1st_part * \
                10**np.floor(1 + math.log10(answer_of_2nd_part)) + \
                answer_of_2nd_part
        else:
            operator = operators[calculate_last] % 10
            if operator == 0:
                answer = answer_of_1st_part + answer_of_2nd_part
            elif operator == 1:
                answer = answer_of_1st_part - answer_of_2nd_part
                if answer < 0:
                    answer = float('nan')
            elif operator == 2:
                answer = answer_of_1st_part * answer_of_2nd_part
            elif operator == 3:
                if answer_of_2nd_part == 0 or answer_of_1st_part < answer_of_2nd_part:
                    answer = float('nan')
                else:
                    answer = float(answer_of_1st_part) / \
                        float(answer_of_2nd_part)
                    if answer > np.floor(answer):
                        answer = float('nan')
        return answer


def krypto_gen(
        number_of_digits, enable_mul, enable_div, enable_num_combine, max_answer=100000):
    # define operator add 0, sub 1, mul 2, div 3, combine 500
    # operation sequence 00,10,20,30,40... upto 90 (10 problems)
    while True:
        numbers = np.zeros((number_of_digits))
        for i in range(number_of_digits):
            numbers[i] = random.randint(9) + 1
        operators = np.zeros((number_of_digits - 1))
        if enable_mul and enable_div:
            for i in range(number_of_digits - 1):
                operators[i] = np.random.randint(4)
        elif enable_mul and not enable_div:
            for i in range(number_of_digits - 1):
                operators[i] = np.random.randint(3)
        elif enable_div and not enable_mul:
            for i in range(number_of_digits - 1):
                operators[i] = np.random.randint(3)
                if operators[i] == 2:
                    operators[i] = 3
        else:
            for i in range(number_of_digits - 1):
                operators[i] = random.randint(2)

        sequence = np.arange(number_of_digits - 1) * 10
        combine = np.zeros((number_of_digits - 1))
        np.random.shuffle(sequence)
        if enable_num_combine and number_of_digits > 2:
            number_of_combine = int(number_of_digits / 3)
            for i in range(number_of_combine):
                combine[i] = 500
            np.random.shuffle(combine)
       #  print operators.shape, combine.shape, sequence.shape
        operators = operators + combine + sequence
        answer = krypto_cal(numbers, operators)
        if not math.isnan(answer) and max_answer > answer:
            break
    new_problem = ""
    for i in range(number_of_digits):
        new_problem = new_problem + " %d " % numbers[i]
    new_answer = krypto_print(numbers, operators)
    new_problem = new_problem + "= %d" % answer
    new_answer = new_answer + " = %d" % answer
    return new_problem, new_answer


def krypto(
        problem_num, number_of_digits, enable_mul, enable_div, enable_num_combine, max_answer):
    problem_list = []
    answer_list = []
    for i in range(1, problem_num + 1):
        new_problem, new_answer = krypto_gen(
            number_of_digits, enable_mul, enable_div, enable_num_combine, max_answer)
        problem_list.append(("[%d] " % i) + new_problem)
        answer_list.append(("[%d] " % i) + new_answer)
    return problem_list, answer_list


###### Fraction math generator below ######


def pairing_attach(str_list_a, str_list_b):
    # join elements with same index in two string lists
    return [i + j for i, j in zip(str_list_a, str_list_b)]


def print_fraction(numerator, denominator, mixed_numbers):
    if mixed_numbers and numerator > denominator:
        integer = int(numerator / denominator)
        numerator = numerator % denominator
    elif mixed_numbers:
        mixed_numbers = False
    a = " %d " % numerator
    b = " %d " % denominator
    c = "-" * max(len(a), len(b))
    if len(a) > len(b):
        b = " " * (len(a) - len(b)) + b
    else:
        a = " " * (len(b) - len(a)) + a
    frac_list = [a, c, b]
    if mixed_numbers:
        side = "%d" % integer
        side_list = [" " * len(side), side, " " * len(side)]
        frac_list = pairing_attach(side_list, frac_list)
    return frac_list


def fraction_gen(mixed_numbers, digits, same_denominator, operator_in_number):
    if mixed_numbers:
        n_digits = digits + 1
    else:
        n_digits = digits
    while True:
        Numerator1 = random.randint(10**n_digits - 1) + 1
        Denominator1 = random.randint(10**digits - 2) + 2
        Denominator2 = random.randint(10**digits - 2) + 2
        if same_denominator:
            Denominator2 = Denominator1
        Numerator2 = random.randint(10**n_digits - 1) + 1
        a = Fraction(Numerator1, Denominator1)
        b = Fraction(Numerator2, Denominator2)
        if a.denominator > 1 and b.denominator > 1:
            if same_denominator:
                if a.denominator == b.denominator:
                    break
            else:
                break

    add = ["   ", " + ", "   "]
    sub = ["   ", " - ", "   "]
    mul = ["   ", " x ", "   "]
    div = ["   ", " / ", "   "]
    #end=["\n","\n"," "]
    equal = ["   ", " = ", "   "]

    if operator_in_number == 1:
        answer = a + b
        operator = add
    elif operator_in_number == 2:
        answer = a - b
        operator = sub
        if answer < 0:
            c = a
            a = b
            b = c
            answer = -answer
    elif operator_in_number == 3:
        answer = a * b
        operator = mul
    elif operator_in_number == 4:
        answer = a / b
        operator = div

    a_list = print_fraction(a.numerator, a.denominator, mixed_numbers)
    b_list = print_fraction(b.numerator, b.denominator, mixed_numbers)
    ans_list = print_fraction(
        answer.numerator, answer.denominator, mixed_numbers)
    new_problem = pairing_attach(a_list, operator)
    new_problem = pairing_attach(new_problem, b_list)
    new_problem = pairing_attach(new_problem, equal)
    new_answer = pairing_attach(new_problem, ans_list)
    # new_problem=pairing_attach(new_problem,end)
    # new_answer=pairing_attach(new_answer,end)
    return new_problem, new_answer


def two_fraction_operation(
        mixed_numbers, digits, same_denominator, operator_in_number, problem_num):
    # a fraction number print out will be stored in a list of 3 str
    # i.e. 3 lines of the fraction print.
    problem_list = []
    answer_list = []
    for i in range(1, problem_num + 1):
        new_problem, new_answer = fraction_gen(
            mixed_numbers, digits, same_denominator, operator_in_number)
        index = "[%d] " % i
        index_list = [index, " " * len(index), " " * len(index)]
        new_problem = pairing_attach(index_list, new_problem)
        new_answer = pairing_attach(index_list, new_answer)
        problem_list.append("\n".join(new_problem))
        answer_list.append("\n".join(new_answer))
    return problem_list, answer_list
