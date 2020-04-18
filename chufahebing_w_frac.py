from random import randint


def latex_div(a, b):
    a = str(a)
    b = str(b)
    equation = []
    equation.append(a + "/div " + b)
    equation.append(a + "/times /frac{1}{" + b + "}")
    equation.append("/frac{" + a + "}{" + b + "}")
    return equation[randint(0, 2)]


def equation_chufahebing_minus_w_frac():
    var1 = randint(2, 9)
    answer = randint(2, 9)
    product = var1 * answer
    var2 = randint(product + 1, 100)
    var3 = var2 - product
    if randint(0, 1) == 0:
        var2, var3 = var3, var2
        answer = -answer
    question = latex_div(var2, var1) + "-" + latex_div(var3, var1) + "="
    # answer = str((var2+ var3 )/var1)
    return question, question + str(answer)


def equation_chufahebing_plus_w_frac():
    # equation = "VAR2\div VAR1+VAR3\div VAR1="
    var1 = randint(2, 9)
    answer = randint(2, 9)
    product = var1 * answer
    var2 = randint(1, product - 1)
    var3 = product - var2
    question = latex_div(var2, var1) + "+" + latex_div(var3, var1) + "="
    # answer = str((var2+ var3 )/var1)
    return question, question + str(answer)


function_list = [
    "chufahebing_plus_w_frac", "chufahebing_minus_w_frac"]

# sample1, _ = equation_chufahebing_plus_w_frac()
# sample2, _ = equation_chufahebing_minus_w_frac()
abstract = "Use distributive law of division to calculate quickly. Calculation involves division and fractions."
# e.g. <br><latex>" + \
#     sample1 + "</latex><br><latex>" + sample2 + "</latex>"
list_name = "Division dist. with fractions"
