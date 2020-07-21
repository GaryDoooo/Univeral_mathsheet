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
def test_qlist_gen_triple(question_type_list_string, seeds, repeat):
    for i in range(seeds):
        seed = random.randint(0, 4294967295)
        print(test_gen_list_triple(question_type_list_string, seed, repeat))


def test_gen_list_triple(
        question_type_list_string,
        seed=0,
        repeat=2,
        problem_num=100):
    res = []
    for i in range(repeat):
        ql1, al1, _, _ = question_gen_test_triple(
            question_type_list_string=question_type_list_string, problem_num=problem_num, seed=seed)
        ql2, al2, _, _ = question_gen_test_triple(
            question_type_list_string=question_type_list_string, problem_num=problem_num, seed=seed)
        res.append((i, ql1 == ql2, al1 == al2))
        if ql1 != ql2:
            print([(i, j) for (i, j) in zip(ql1, ql2) if i != j])
    return res


def question_gen_test_triple(
        question_type_list_string="chengfahebing",
        problem_num=10,
        page_key="There_is_no_page_key_input",
        no_one=True,
        seed=0
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
    random.seed(seed)
    # Gen and store rand seed for each question
    seed = []
    for _ in range(problem_num):
        seed.append(random.randint(0, 4294967295))
    for i in range(1, problem_num + 1):
        # a string of name of the question type
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
        # Repeat the same thing again to avoid random lib error.
        #  random.seed(seed[i - 1])
        #  question_type = random.choice(question_type_list)
        #  new_problem, new_answer = equations.generate_a_question(question_type)

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


def test_qlist_gen_single(question_type_list_string, seeds, repeat):
    for i in range(seeds):
        seed = random.randint(0, 4294967295)
        print(test_gen_list_single(question_type_list_string, seed, repeat))


def test_gen_list_single(
        question_type_list_string,
        seed=0,
        repeat=2,
        problem_num=100):
    res = []
    for i in range(repeat):
        ql1, al1, _, _ = question_gen_test_single(
            question_type_list_string=question_type_list_string, problem_num=problem_num, seed=seed)
        ql2, al2, _, _ = question_gen_test_single(
            question_type_list_string=question_type_list_string, problem_num=problem_num, seed=seed)
        res.append((i, ql1 == ql2, al1 == al2))
        if ql1 != ql2:
            print([(i, j) for (i, j) in zip(ql1, ql2) if i != j])
    return res


def test_qlist_gen(question_type_list_string, seeds, repeat):
    for i in range(seeds):
        seed = random.randint(0, 4294967295)
        print(test_gen_list(question_type_list_string, seed, repeat))


def test_gen_list(
        question_type_list_string,
        seed=0,
        repeat=2,
        problem_num=100):
    res = []
    for i in range(repeat):
        ql1, al1, _, _ = question_gen_test(
            question_type_list_string=question_type_list_string, problem_num=problem_num, seed=seed)
        ql2, al2, _, _ = question_gen_test(
            question_type_list_string=question_type_list_string, problem_num=problem_num, seed=seed)
        res.append((i, ql1 == ql2, al1 == al2))
        if ql1 != ql2:
            print([(i, j) for (i, j) in zip(ql1, ql2) if i != j])
    return res


def question_gen_test_single(
        question_type_list_string="chengfahebing",
        problem_num=10,
        page_key="There_is_no_page_key_input",
        no_one=True,
        seed=0
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
    random.seed(seed)
    # Gen and store rand seed for each question
    seed = []
    for _ in range(problem_num):
        seed.append(random.randint(0, 4294967295))
    for i in range(1, problem_num + 1):
        # a string of name of the question type
        #  random.seed(seed[i - 1])
        #  question_type = random.choice(question_type_list)
        #  new_problem, new_answer = equations.generate_a_question(question_type)
        # Repeat the same thing again to avoid random lib error.
        random.seed(seed[i - 1])
        question_type = random.choice(question_type_list)
        new_problem, new_answer = equations.generate_a_question(question_type)

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


def question_gen_test(
        question_type_list_string="chengfahebing",
        problem_num=10,
        page_key="There_is_no_page_key_input",
        no_one=True,
        seed=0
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
    random.seed(seed)
    # Gen and store rand seed for each question
    seed = []
    for _ in range(problem_num):
        seed.append(random.randint(0, 4294967295))
    for i in range(1, problem_num + 1):
        # a string of name of the question type
        random.seed(seed[i - 1])
        question_type = random.choice(question_type_list)
        new_problem, new_answer = equations.generate_a_question(question_type)
        # Repeat the same thing again to avoid random lib error.
        random.seed(seed[i - 1])
        question_type = random.choice(question_type_list)
        new_problem, new_answer = equations.generate_a_question(question_type)

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


def _test(question_type_list_string="chengfahebing", seed=10):
    #  seed=random.randint(0, 4294967295)
    equations = equation()
    question_type_list = question_type_list_string.split(",")
    random.seed(seed)
    question_type = random.choice(question_type_list)
    new_problem, new_answer = equations.generate_a_question(question_type)
    return new_problem, new_answer


def compare2_2(question_type_list_string, seed):
    _ = _test(question_type_list_string, seed)
    p1, a1 = _test(question_type_list_string, seed)
    p2, a2 = _test(question_type_list_string, seed)
    if p1 != p2:
        #  print(p1, p2)
        return "Q1 " + p1 + " Q2 " + p2
    if a1 != a2:
        #  print(a1, a2)
        return "A1 " + a1 + " A2 " + a2
    return "same"


def compare2(question_type_list_string, seed):
    p1, a1 = _test(question_type_list_string, seed)
    p2, a2 = _test(question_type_list_string, seed)
    if p1 != p2:
        #  print(p1, p2)
        return "Q1 " + p1 + " Q2 " + p2
    if a1 != a2:
        #  print(a1, a2)
        return "A1 " + a1 + " A2 " + a2
    return "same"


def testgen(question_type_list_string, seeds=10, repeat=10):
    for _ in range(seeds):
        seed = random.randint(0, 4294967295)
        #  print(_, "\t seed %d" % seed, end=" ")
        same = True
        errors = ""
        for __ in range(repeat):
            res = compare2(question_type_list_string, seed)
            if "same" != res:
                same = False
                errors += res
        print(_, "\t seed %d" % seed, "tested same:", same, errors)


def testgen2(question_type_list_string, seeds=10, repeat=10):
    for _ in range(seeds):
        seed = random.randint(0, 4294967295)
        #  print(_, "\t seed %d" % seed, end=" ")
        same = True
        errors = ""
        for __ in range(repeat):
            res = compare2_2(question_type_list_string, seed)
            if "same" != res:
                same = False
                errors += "#" + str(__) + " " + res
        print(_, "\t seed %d" % seed, "tested same:", same, errors)


def checkseeds(question_type_list_string, seed_file="", repeat=10):
    for _ in open(seed_file):
        print("From File:", _)
        try:
            print(_.strip())
            seed = int(_.strip().replace("\n", ""))
        except BaseException:
            print("convert int error")
            pass
        same = True
        errors = ""
        for __ in range(repeat):
            res = compare2(question_type_list_string, seed)
            if "same" != res:
                same = False
                errors += str(__) + ">>>" + res
        print(_, "\t seed %d" % seed, "tested same:", same, errors)


def print_seed_results(question_type_list_string, seed_file="", repeat=10):
    for _ in open(seed_file):
        print("From File:", _)
        try:
            print(_.strip())
            seed = int(_.strip().replace("\n", ""))
        except BaseException:
            print("convert int error")
            pass
        for __ in range(repeat):
            #  res = compare2(question_type_list_string, seed)
            p1, a1 = _test(question_type_list_string, seed)
            print("#", __, p1)
        #  print(_, "\t seed %d" % seed, "tested same:", same, errors)


if __name__ == '__main__':
    print("main test")
    #  print(question_gen(
    #  question_type_list_string="chengfahebing,chufahebing", problem_num=10))
    #  testgen(
    #  question_type_list_string="exponent_consolidate2",
    #  seeds=100,
    #  repeat=100)
    #  checkseeds(question_type_list_string="exponent_consolidate2",
    #  seed_file="100x100ec_false_seeds", repeat=100)
    #  print_seed_results(question_type_list_string="exponent_consolidate2",
    #  seed_file="100x100ec_false_seeds", repeat=5)
    #  testgen2(
    #  question_type_list_string="exponent_consolidate2",
    #  seeds=10000,
    #  repeat=5)
    #  test_qlist_gen_single(
    #  question_type_list_string="exponent_compare,two_symbol_expand2,exponent_consolidate2",
    #  seeds=20,
    #  repeat=5)
    test_qlist_gen_triple(
        question_type_list_string="exponent_compare,two_symbol_expand2,exponent_consolidate2",
        seeds=2000,
        repeat=3)
    #  test_qlist_gen(
    #  question_type_list_string="exponent_compare,two_symbol_expand2,exponent_consolidate2",
    #  seeds=20,
    #  repeat=5)
