from chengfahebing import function_list as chengfahebing_function_list
from chengfahebing import *
from chengfahebing_w_frac import function_list as chengfahebing_w_frac_function_list
from chengfahebing_w_frac import *
from chufahebing_w_frac import function_list as chufahebing_w_frac_function_list
from chufahebing_w_frac import *
from chufahebing import function_list as chufahebing_function_list
from chufahebing import *
import random


def get_function_list_to_use(question_type_list_string):
    function_list = []
    function_list.extend(chengfahebing_function_list)
    function_list.extend(chengfahebing_w_frac_function_list)
    function_list.extend(chufahebing_function_list)
    function_list.extend(chufahebing_w_frac_function_list)
    #  print(function_list)
    selected_question_types = question_type_list_string.split(',')
    function_list_to_use = []
    for function in function_list:
        selected = False
        for question_type in selected_question_types:
            if question_type in function:
                selected = True
        if selected:
            function_list_to_use.append(function)
    return function_list_to_use
#  print(function_list_to_use)
#  print(equation_chengfahebing_plus_10())

#  html_header="<html><head><title>Math Generator</title></head><body>"
#  table_header="<table style='width:100%'>"


def call(function_name_suffix, var_list=None):
    if var_list is None:
        return globals()["equation_" + function_name_suffix]()
    else:
        return globals()["equation_" + function_name_suffix](var_list)


def question_gen(
        question_type_list_string="chengfahebing",
        problem_num=10,
        randseed=100,
        no_one=True
):
    problem_list = []
    answer_list = []
    random.seed(randseed)
    function_list_to_use = get_function_list_to_use(question_type_list_string)
    # print(function_list_to_use)
    for i in range(1, problem_num + 1):
        index_function = random.randint(0, len(function_list_to_use) - 1)
        new_problem, new_answer = call(function_list_to_use[index_function])
        # print(repr(new_problem))
        # print(repr(new_answer))
        problem_list.append(("[%d] " % i) +
                            ("<latex>%s</latex>" % new_problem))
        answer_list.append(("[%d] " % i) + ("<latex>%s</latex>" %
                                            # .replace(r"\\\\", r"\\")
                                            new_answer
                                            ))
        # problem_list.append(("[%d] " % i) +
        #                     ("\[%s\]" % new_problem))
        # answer_list.append(("[%d] " % i) + ("\[%s\]" % new_answer))
    return problem_list, answer_list


if __name__ == '__main__':
    print("main test")
    print(question_gen(
        question_type_list_string="chengfahebing,chufahebing", problem_num=10))
# The brackets [ and ] are from MathJax, but it does not work with live
# update html contents.

#  <table style="width:100%">
  #  <tr>
    #  <th>Firstname</th>
    #  <th>Lastname</th>
    #  <th>Age</th>
  #  </tr>
  #  <tr>
    #  <td>Jill</td>
    #  <td>Smith</td>
    #  <td>50</td>
  #  </tr>
  #  <tr>
    #  <td>Eve</td>
    #  <td>Jackson</td>
    #  <td>94</td>
  #  </tr>
#  </table>
