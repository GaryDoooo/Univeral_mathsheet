# Copyright 2017 Garry Du
from gen import question_gen
#  import random
#  from page_key import page_key_compress as encode_key
#  from page_key import page_key_decompress as decode_key
#


def html_output(problem_list="", answer_list="", page_key="", num_of_col=5):
    problem_output = ''
    table_head = '<table BORDERCOLOR=white width="100%"><tr><th colspan="5">ANSWER KEY:  ' + \
        page_key + '</th></tr><tr>'
    table_end = "  </tr></table>"
    answer_output = problem_output
    counter = 0
    answer_output += table_head
    problem_output += table_head
    num_of_col = int(num_of_col)
    if not (0 < num_of_col < 11):
        num_of_col = 5
    for problem, answer in zip(problem_list, answer_list):
        problem_output += '<td>' + problem + '</td>'
        answer_output += '<td>' + answer + '</td>'
        counter += 1
        if (counter % num_of_col) == 0:
            problem_output += "</tr><tr><td><br></td></tr><tr>"
            answer_output += "</tr><tr><td><br></td></tr><tr>"
    answer_output += table_end
    problem_output += table_end
    return problem_output, answer_output


def dispatch(question_type_list_string="chengfahebing", problem_num=5,
             page_key="new"):
    #  max_list = [  # 20000,  # problem list max 20k
    #  2000,  # num min and max both have -1000 to 1000 range thus 0-1999
    #  2000,
    #  2000,
    #  2000,
    #  1000001,  # result max in 1M
    #  5,  # operator 1-4
    #  65535  # max of rand seed
    #  ]
    #  if page_key == "new":
    #  randseed = random.randint(0, 65534)
    #  page_key = encode_key([1, randseed
    #  ], max_list)
    #  else:
    #  [_, randseed] = decode_key(page_key, max_list)
    if not (0 < problem_num <= 2000):
        problem_num = 100
    ##### Generate problems. #####
    problem_list, answer_list, page_key = question_gen(
        question_type_list_string, problem_num, page_key)

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


def main():
    r1, r2, r3 = dispatch()
    print(r1, r2, r3)


if __name__ == "__main__":
    main()
    # TabNine::semSemantic completion enabled.
