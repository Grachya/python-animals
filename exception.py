def polish_sum(value):
    try:
        return int(value[1]) + int(value[2])
    except TypeError:
        print('Не верный тип данных')


def polish_mult(value):
    try:
        return int(value[1]) * int(value[2])
    except TypeError:
        print('Не верный тип данных')


def polish_div(value):
    try:
        return int(value[1]) / int(value[2])
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except TypeError:
        print('Не верный тип данных')


def polish_substr(value):
    try:
        return int(value[1]) - int(value[2])
    except TypeError:
        print('Не верный тип данных')


expression = input('Введите выражение: ')
expression_list = expression.split()
operators = ['+', '-', '*', '/']


def is_operator(operator):
    try:
        operators.index(operator)
        return True
    except ValueError:
        return False


assert is_operator(expression_list[0]), 'Первая операция не в списке доступных.'
assert len(expression_list) == 3, 'Не верный формат'

if expression_list[0] == '+':
    print(polish_sum(expression_list))
elif expression_list[0] == '-':
    print(polish_substr(expression_list))
elif expression_list[0] == '*':
    print(polish_mult(expression_list))
elif expression_list[0] == '/':
    print(polish_div(expression_list))
