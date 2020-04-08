import random


def two_number_add(
        first_num_max, first_num_min, second_num_max, second_num_min, result_max):
    result_max = max(result_max, first_num_min + second_num_min)
    timer = 0
    while (timer < 10000):
        timer += 1
        a = random.randint(first_num_min, first_num_max)
        b = random.randint(second_num_min, second_num_max)
        if a + b <= result_max:
            break
    new_problem = "%d + %d = " % (a, b)
    new_answer = new_problem + "%d" % (a + b)
    return new_problem, new_answer


def two_number_sub(
        first_num_max, first_num_min, second_num_max, second_num_min):
    a = random.randint(first_num_min, first_num_max)
    b = random.randint(second_num_min, second_num_max)
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
    result_max = max(result_max, first_num_min * second_num_min)
    timer = 0
    while (timer < 10000):
        timer += 1
        a = random.randint(first_num_min, first_num_max)
        b = random.randint(second_num_min, second_num_max)
        if a != 1 and b != 1 and a * b <= result_max:
            break
        if not no_one:
            break
    new_problem = "%d x %d = " % (a, b)
    new_answer = new_problem + "%d" % (a * b)
    return new_problem, new_answer


def two_number_div(
        first_num_max, first_num_min, second_num_max, second_num_min, no_one=True):
    a = random.randint(first_num_min, first_num_max)
    timer = 0
    while (timer < 10000):
        timer += 1
        b = random.randint(second_num_min, second_num_max)
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
        randseed=100,
        no_one=True
):
    problem_list = []
    answer_list = []
    random.seed(randseed)
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
