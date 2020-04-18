from random import randint


def equation_chengfahebing_plus_10():
    equation = []
    equation.append("VAR1\times VAR2+VAR1\times VAR3=")
    equation.append("VAR2\times VAR1+VAR3\times VAR1=")
    equation.append("VAR2\times VAR1+VAR3\times VAR1=")
    index_equation = randint(0, 2)
    var1 = randint(5, 30)
    var2 = randint(1, 9)
    var3 = 10 - var2
    question = equation[index_equation].replace(
        "VAR1",
        str(var1)).replace(
        "VAR2",
        str(var2)).replace(
            "VAR3",
        str(var3))
    answer = str(var1 * var2 + var3 * var1)
    return question, question + answer


def equation_chengfahebing_plus_10s():
    equation = []
    equation.append("VAR1\times VAR2+VAR1\times VAR3=")
    equation.append("VAR2\times VAR1+VAR3\times VAR1=")
    equation.append("VAR2\times VAR1+VAR3\times VAR1=")
    index_equation = randint(0, 2)
    var1 = randint(2, 9)
    s = randint(1, 9) * 10  # sum of var2 and var3
    var2 = randint(1, s - 1)
    var3 = s - var2
    question = equation[index_equation].replace(
        "VAR1",
        str(var1)).replace(
        "VAR2",
        str(var2)).replace(
            "VAR3",
        str(var3))
    answer = str(var1 * var2 + var3 * var1)
    return question, question + answer


def equation_chengfahebing_minus_10():
    equation = []
    equation.append("VAR1\times VAR2-VAR1\times VAR3=")
    equation.append("VAR2\times VAR1-VAR3\times VAR1=")
    equation.append("VAR2\times VAR1-VAR3\times VAR1=")
    index_equation = randint(0, 2)
    var1 = randint(5, 30)
    var2 = randint(11, 99)
    var3 = var2 - 10
    if randint(0, 1) == 0:
        var2, var3 = var3, var2
    question = equation[index_equation].replace(
        "VAR1",
        str(var1)).replace(
        "VAR2",
        str(var2)).replace(
            "VAR3",
        str(var3))
    answer = str(var1 * var2 - var3 * var1)
    return question, question + answer


def equation_chengfahebing_minus_10s():
    equation = []
    equation.append("VAR1\times VAR2-VAR1\times VAR3=")
    equation.append("VAR2\times VAR1-VAR3\times VAR1=")
    equation.append("VAR2\times VAR1-VAR3\times VAR1=")
    index_equation = randint(0, 2)
    var1 = randint(2, 9)
    d1 = randint(1, 9)  # digit at 1
    d2 = randint(1, 9)  # digit at 10
    var2 = d2 * 10 + d1
    var3 = randint(0, d2 - 1) * 10 + d1
    if randint(0, 1) == 0:
        var2, var3 = var3, var2
    question = equation[index_equation].replace(
        "VAR1",
        str(var1)).replace(
        "VAR2",
        str(var2)).replace(
            "VAR3",
        str(var3))
    answer = str(var1 * var2 - var3 * var1)
    return question, question + answer


function_list = [
    "chengfahebing_plus_10",
    "chengfahebing_plus_10s",
    "chengfahebing_minus_10",
    "chengfahebing_minus_10s"]

sample1, _ = equation_chengfahebing_plus_10()
sample2, _ = equation_chengfahebing_minus_10s()
abstract = "Use distributive law of multiplication to calculate quickly, e.g. <latex>" + \
    sample1 + "</latex><latex>" + sample2 + "</latex>"
list_name = "Multiplication distribution"
