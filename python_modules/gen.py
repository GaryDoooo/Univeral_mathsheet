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
        page_key="There_is_no_page_key_input",
        no_one=True
):
    problem_list = []
    answer_list = []
    equations = equation()
    if page_key == "There_is_no_page_key_input":
        randseed = random.randint(0, 65534)
        question_type_list = question_type_list_string.split(",")
        page_key = equations.encode_key(question_type_list, randseed)
    else:
        question_type_list, randseed = equations.decode_key(
            page_key.replace(" ", ""))
    question_type_list = equations.sort_question_list(question_type_list)
    page_note = equations.get_page_note(question_type_list)
    random.seed(randseed)
    # Gen and store rand seed for each question
    seed = []
    for _ in range(problem_num):
        seed.append(random.randint(0, 4294967295))
    for i in range(1, problem_num + 1):
        # a string of name of the question type
        ####################################################
        # while loop to two identical question generated
        # It's somehow filter out the random generation errors
        random.seed(seed[i - 1])
        question_type = random.choice(question_type_list)
        new_problem_previous, new_answer_previous = equations.generate_a_question(
            question_type)
        while True:
            random.seed(seed[i - 1])
            question_type = random.choice(question_type_list)
            new_problem, new_answer = equations.generate_a_question(
                question_type)
            if new_problem == new_problem_previous and new_answer == new_answer_previous:
                break
            else:
                new_problem_previous, new_answer_previous = new_problem, new_answer
        ###################################################
        problem_list.append(("[%d] " % i) +
                            ("<latex>%s</latex>" % new_problem))
        answer_list.append(("[%d] " % i) + ("<latex>%s</latex>" %
                                            # .replace(r"\\\\", r"\\")
                                            new_answer
                                            ))
        # problem_list.append(("[%d] " % i) +
        #                     ("$$%s$$" % new_problem))
        # answer_list.append(("[%d] " % i) + ("$$%s$$" %
        #                                     # .replace(r"\\\\", r"\\")
        #                                     new_answer
        #                                     ))
    return problem_list, answer_list, page_key, page_note


def get_random_by_seed(seed=1, index=0, total=100):
    random.seed(seed)
    seeds = []
    for _ in range(total):
        seeds.append(random.randint(0, 4294967295))
    return seeds[index]


def test_gen_by_seed(seed=0, question_type_list=['chengfahebing']):
    equations = equation()
    random.seed(seed)
    question_type = random.choice(question_type_list)
    new_problem_previous, new_answer_previous = equations.generate_a_question(
        question_type)
    return new_problem_previous, new_answer_previous


if __name__ == '__main__':
    print("main test")
    #  print(question_gen(
    #  question_type_list_string="chengfahebing,chufahebing", problem_num=10))
    print(get_random_by_seed(16558, 34))
    print(
        test_gen_by_seed(
            get_random_by_seed(
                16558,
                34),
            ['linear_eq_1unknown']))
