from random import randint


def equation_chufahebing_minus():
    equation = r'VAR2/div VAR1-VAR3/div VAR1='
    var1 = randint(2, 9)
    answer = randint(2, 9)
    product = var1 * answer
    var2 = randint(product + 1, 100)
    var3 = var2 - product
    if randint(0, 1) == 0:
        var2, var3 = var3, var2
        answer = -answer
    # print(equation)
    # print(repr(equation))
    question = equation.replace(
        "VAR1",
        str(var1)).replace(
        "VAR2",
        str(var2)).replace(
            "VAR3",
        str(var3))
    # answer = str((var2+ var3 )/var1)
    # print(question)
    return question, question + str(answer)


def equation_chufahebing_plus():
    equation = r'VAR2/div VAR1+VAR3/div VAR1='
    var1 = randint(2, 9)
    answer = randint(2, 9)
    product = var1 * answer
    var2 = randint(1, product - 1)
    var3 = product - var2
    # print(repr(equation))
    # print(equation)
    question = equation.replace(
        "VAR1",
        str(var1)).replace(
        "VAR2",
        str(var2)).replace(
            "VAR3",
        str(var3))
    # answer = str((var2+ var3 )/var1)
    # print(question)
    return question, question + str(answer)

function_list = [
    "chufahebing_plus", "chufahebing_minus"]

# sample1, _ = equation_chufahebing_plus()
# sample2, _ = equation_chufahebing_minus()
abstract = "Use distributive law of division to calculate quickly."
# e.g. <br><latex>" + \
#     sample1 + "</latex><br><latex>" + sample2 + "</latex>"
list_name = "Division distribution"
