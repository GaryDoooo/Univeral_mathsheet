# Copyright 2017 Garry Du
from int_gen import two_number_operation
import random
from page_key import page_key_compress as encode_key
from page_key import page_key_decompress as decode_key


def html_output(problem_list, answer_list, page_key):
    problem_output = ''
    table_head = '<table BORDERCOLOR=white><tr><th colspan="5">ANSWER KEY:  ' + \
        page_key + '</th></tr><tr>'
    table_end = "  </tr></table>"
    answer_output = problem_output
    counter = 0
    answer_output += table_head
    problem_output += table_head
    for problem, answer in zip(problem_list, answer_list):
        problem_output += '<td>' + problem + '</td>'
        answer_output += '<td>' + answer + '</td>'
        counter += 1
        if (counter % 5) == 0:
            problem_output += "</tr><tr><td><br></td></tr><tr>"
            answer_output += "</tr><tr><td><br></td></tr><tr>"
    answer_output += "  </tr></table>"
    return problem_output, answer_output


def dispatch(first_num_max,
             second_num_max,
             result_max,
             first_num_min,
             second_num_min,
             operator,
             problem_num,
             page_key):
    max_list = [  # 20000,  # problem list max 20k
        2000,  # num min and max both have -1000 to 1000 range thus 0-1999
        2000,
        2000,
        2000,
        1000001,  # result max in 1M
        5,  # operator 1-4
        65535  # max of rand seed
    ]
    if page_key == "new":
        randseed = random.randint(0, 65534)
        operator_in_number = 1  # 1 is add
        if (operator == "s"):
            operator_in_number = 2  # 2 is sub
        elif (operator == "m"):
            operator_in_number = 3  # 3 is mul
        elif (operator == "d"):
            operator_in_number = 4  # 4 is div
        [first_num_max,
            second_num_max,
            result_max,
            first_num_min,
            second_num_min,
            operator_in_number,
            problem_num] = check_input(first_num_max,
                                       second_num_max,
                                       result_max,
                                       first_num_min,
                                       second_num_min,
                                       operator_in_number,
                                       problem_num
                                       )
        page_key = encode_key([first_num_min + 1000, first_num_max + 999, second_num_min + 1000,
                               second_num_max + 999, result_max, operator_in_number, randseed
                               ], max_list)
    else:
        [first_num_min, first_num_max, second_num_min,
         second_num_max, result_max, operator_in_number, randseed] = decode_key(page_key, max_list)
        first_num_min = first_num_min - 1000
        first_num_max = first_num_max - 999
        second_num_min = second_num_min - 1000
        second_num_max = second_num_max - 999
        # problem_num = 1000
        [first_num_max,
            second_num_max,
            result_max,
            first_num_min,
            second_num_min,
            operator_in_number,
            problem_num] = check_input(first_num_max,
                                       second_num_max,
                                       result_max,
                                       first_num_min,
                                       second_num_min,
                                       operator_in_number,
                                       problem_num
                                       )
    ##### Generate problems. #####
    problem_list, answer_list = two_number_operation(
        first_num_max, second_num_max, result_max,
        first_num_min, second_num_min, operator_in_number, problem_num, randseed)

    return problem_list, answer_list, page_key


def check_input(first_num_max,
                second_num_max,
                result_max,
                first_num_min,
                second_num_min,
                operator_in_number,
                problem_num
                ):
    if not (-1e3 < first_num_max <= 1e3):
        first_num_max = 100
    if not (-1e3 < second_num_max <= 1e3):
        second_num_max = 100
    if not (-1e3 <= second_num_min < 1e3):
        second_num_min = 2
    if not (-1e3 <= first_num_min < 1e3):
        first_num_min = 2
    if first_num_min >= first_num_max:
        first_num_max = 100
        first_num_min = 2
    if second_num_min >= second_num_max:
        second_num_max = 100
        second_num_min = 2
    if (result_max == 0):
        result_max = first_num_max * second_num_max
    if not (0 < result_max <= 1e6):
        result_max == 1e6
    if not(1 <= operator_in_number <= 4):
        operator_in_number = 1
    if not (0 < problem_num <= 20000):
        problem_num = 100

    return [first_num_max,
            second_num_max,
            result_max,
            first_num_min,
            second_num_min,
            operator_in_number,
            problem_num]
