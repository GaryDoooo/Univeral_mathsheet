from random import randint


def latex_times(a, b):
    a = str(a)
    b = str(b)
    equation = []
    equation.append(a + "/times " + b)
    equation.append(b + "/times " + a)
    equation.append(a + "/div /frac{1}{" + b + "}")
    equation.append(a + "/div /frac{1}{" + b + "}")
    return equation[randint(0, 3)]


def equation_chengfahebing_w_frac_plus_10():
    var1 = randint(5, 30)
    var2 = randint(1, 9)
    var3 = 10 - var2
    question = latex_times(var1, var2) + "+" + latex_times(var3, var1) + "="
    answer = str(var1 * var2 + var3 * var1)
    return question, question + answer


def equation_chengfahebing_w_frac_plus_10s():
    var1 = randint(2, 9)
    s = randint(1, 9) * 10  # sum of var2 and var3
    var2 = randint(1, s - 1)
    var3 = s - var2
    question = latex_times(var1, var2) + "+" + latex_times(var3, var1) + "="
    answer = str(var1 * var2 + var3 * var1)
    return question, question + answer


def equation_chengfahebing_w_frac_minus_10():
    var1 = randint(5, 30)
    var2 = randint(11, 99)
    var3 = var2 - 10
    if randint(0, 1) == 0:
        var2, var3 = var3, var2
    question = latex_times(var1, var2) + "-" + latex_times(var3, var1) + "="
    answer = str(var1 * var2 - var3 * var1)
    return question, question + answer


def equation_chengfahebing_w_frac_minus_10s():
    var1 = randint(2, 9)
    d1 = randint(1, 9)  # digit at 1
    d2 = randint(1, 9)  # digit at 10
    var2 = d2 * 10 + d1
    var3 = randint(0, d2 - 1) * 10 + d1
    if randint(0, 1) == 0:
        var2, var3 = var3, var2
    question = latex_times(var1, var2) + "-" + latex_times(var3, var1) + "="
    answer = str(var1 * var2 - var3 * var1)
    return question, question + answer


function_list = [
    "chengfahebing_w_frac_plus_10",
    "chengfahebing_w_frac_plus_10s",
    "chengfahebing_w_frac_minus_10",
    "chengfahebing_w_frac_minus_10s"]

# sample1, _ = equation_chengfahebing_w_frac_plus_10()
# sample2, _ = equation_chengfahebing_w_frac_minus_10s()
abstract = "Use distributive law of multiplication to calculate quickly. But in this case, the multiplication includes division and fractions."
# " e.g. <br><latex>" + \
#     sample1 + "</latex><br><latex>" + sample2 + "</latex>"
list_name = "Multiplication dist. with fractions"
