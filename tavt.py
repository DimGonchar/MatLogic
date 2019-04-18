from math import fmod
import re
import itertools
"""Правила//
Позначення можливих логічних дій:
    унарна дія "не": "!"
    бінарні дії:
        диз'юнкція: "+"
        кон'юнкція: "*"
        імплікація: "-"
        еквіваленція: "="
        альтернатива: "&"
Всі формули повинні вводитися згідно визначень логіки висловлювань
Вигляд змінних: x1, x2, x3 і т.д.
Змінні вводити в порядку зростання індексів
"""

def result_binar_operation(a, b, act):
    if act == "*":
        return a * b
    if act == "+":
        return fmod((a * b + a + b), 2)
    if act == "-":
        return fmod((a * b + a + 1), 2)
    if act == "=":
        return fmod((a + b + 1), 2)
    if act == "&":
        return fmod((a + b), 2)
    return "Error in <result_binar_operation>: a=" + str(a)+", b="+str(b)+" act="+str(act)


def result_formul(str_form, vector):
    # print(str_form)
    # print(vector)
    if str_form.count("x") == 1:
        str_form=str_form.replace(")","").replace("(","")

        req = r"[+]?\d+(?:\.\d+)?"
        number_x = re.findall(req, str_form)[0]

        if fmod(str_form.count("!"), 2) == 1:
            # print("x", number_x, fmod(vector[int(number_x)-1]+1,2))
            return fmod(vector[int(number_x)-1]+1,2)
        else:
            # print("x", number_x,vector[int(number_x)-1])
            return vector[int(number_x)-1]
    ne1 = 0
    ne2 = 0

    if str_form[0] == "!":
        ne1 = 1
        str_form = str_form[1:]

    if str_form[0] == "(":
        count = 1
        i = 0
        while count != 0:
            i += 1
            if str_form[i] == "(":
                count += 1
            elif str_form[i] == ")":
                count += -1
        form1 = str_form[1:i]
        str_form = str_form[i+1:]
    else:
        req = r"[+]?\d+(?:\.\d+)?"
        number_x = re.findall(req, str_form)[0]
        form1 = str_form[0] + number_x
        str_form = str_form[len(form1):]


    if len(str_form) == 0:
        return fmod(result_formul(form1, vector)+ne1, 2)

    act=str_form[0]
    str_form = str_form[1:]

    # print("str_form", str_form)

    if str_form[0] == "!":
        ne2 = 1
        str_form = str_form[1:]

    if str_form[0] == "(":
        form2 = str_form[1:-1]
    else:
        form2 = str_form
    # print("form2", form2)

    a = fmod(result_formul(form1, vector)+ne1, 2)
    b = fmod(result_formul(form2, vector)+ne2, 2)
    # print("res",a,b,act)
    return result_binar_operation(a, b, act)


def check_tavt(str_form):

    n = count_zmin(str_form)
    l = [i for i in itertools.product([0, 1], repeat=n)]
    # print(l)
    tavt = 1
    i = 0
    while tavt == 1:
        # print("l", l[i])
        tavt = result_formul(str_form, l[i])
        i += 1
        if len(l) == i:
            break
    if tavt == 0:
        return "Не тавтологія"
    else:
        return "Тавтологія"


def tablista_istunnisti(str_form):
    n = count_zmin(str_form)
    l = [i for i in itertools.product([0, 1], repeat=n)]
    for i in l:
        print(i, result_formul(str_form, i))

def count_zmin(str_form):
    req = r"[+]?\d+(?:\.\d+)?"
    s = re.findall(req, str_form)
    s = [int(i) for i in s]
    return max(s)

formula = ""
if formula=="":
    formula = input("Введіть формулу: ")
print(check_tavt(formula))
# tablista_istunnisti(formula)
