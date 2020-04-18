from equations_class import equation
import random

# def call(function_name_suffix, var_list=None):
#     if var_list is None:
#         return globals()["equation_" + function_name_suffix]()
#     else:
#         return globals()["equation_" + function_name_suffix](var_list)


# def call(module, function_name_suffix, var_list=None):
#     # this is an importance methode: to call a function inside a module by its
#     # name in a string
#     function_to_run = getattr(module, "equation_" + function_name_suffix)
#     if var_list is None:
#         return function_to_run()
#     else:
#         return function_to_run(var_list)


def question_gen(
        question_type_list_string="chengfahebing",
        problem_num=10,
        randseed=100,
        no_one=True
):
    problem_list = []
    answer_list = []
    random.seed(randseed)
    equations = equation()
    question_type_list = question_type_list_string.split(",")
    for i in range(1, problem_num + 1):
        # a string of name of the question type
        question_type = random.choice(question_type_list)

        new_problem, new_answer = equations.generate_a_question(question_type)

        problem_list.append(("[%d] " % i) +
                            ("<latex>%s</latex>" % new_problem))
        answer_list.append(("[%d] " % i) + ("<latex>%s</latex>" %
                                            # .replace(r"\\\\", r"\\")
                                            new_answer
                                            ))

    return problem_list, answer_list


if __name__ == '__main__':
    print("main test")
    print(question_gen(
        question_type_list_string="chengfahebing,chufahebing", problem_num=10))
