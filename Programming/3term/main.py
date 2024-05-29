import math
import calc_print

PARAMS = {'precision': None,
        'output_type': None,
        'possible_types': None,
        'dest': None}


def load_params(file="params.ini"):
    """
        Функция записи параметров из файла в словарь PARAMS
        На вход поступает имя файла, в процессе выполнения
        Параметры построчно записываются в PARAMS.
    """
    global PARAMS
    try:
        f = open(file, mode='r', errors='strict')
        lines = f.readlines()
        for l in lines:
            param = l.split('=')
            param[1] = param[1].strip('\n')

            if param[0] != 'dest':
                param[1] = eval(param[1])

            PARAMS[param[0]] = param[1]
    except FileNotFoundError:
        print("Файл с параметрами не найден")
        sys.exit()


def convert_precision(precision):
    """
    Конвертирует точность вида float(ex.:0.001)
    в целочисленный выд
    """
    if precision is None:
        precision = '0.001'
    if type(precision) is float:
        precision = str(f'{precision:f}')
    for i in range(len(str(precision))):
        if float(precision) * 10**i >= 1:
            return i


def convert_precision_alt(**kwargs):
    """
    Альтернативная функция конвертации точности,
    здесь аргумент берется из словаря с заданной точностью
    вместо обычного числа или строки
    """
    precision = kwargs.get('precision')
    if precision is None:
        precision = '0.001'
    if type(precision) is float:
        precision = str(precision)
    for i in range(len(precision)):
        if float(precision) * 10**i >= 1:
            return i


def standard_deviation(*args, **kwargs):
    """
    Функция вычисляет среднеквадратическое отклонение из
    произвольного числа аргументов в виде кортежа
    """
    precision = convert_precision(kwargs['precision'])
    arith_mean = 0
    sum_squares = 0
    for arg in args:
        arith_mean += arg
    arith_mean /= len(args)
    for arg in args:
        sum_squares += (arg - arith_mean)**2
    deviation = math.sqrt(sum_squares / len(args))
    return round(deviation, precision)


def user_input():
    args = []
    values_counter = input("Введите кол-во значений для вычисления: ")
    for counter in range(0, int(values_counter)):
        value = input("Введите значение: ")
        try:
            if value == "":
                break
            value = float(value)
        except ValueError:
            print("Введите число в правильном формате (разделитель дробной части '.'")
        else:
            args.append(value)

    print(args)
    if len(args) <= 1:
        return "Недостаточно аргументов для вычисления"

    print("Введите действие \n"
          "Доступные действия: +, -, *, /, ^, //, %")
    action = input()
    result = calculate(*args, action, **PARAMS)
    calc_print.print_results(*args, action=action, result=result)
    calc_print.write_log(*args, action=action, result=result, file=PARAMS['dest'])


def digits_round(result, precision):
    """
    Функция позволяет округлять вещественные числа 
    по точности precision
    """
    if type(result) == float and not result.is_integer():
        result = round(result, precision)
        return result
    else:
        return result


def calculate(*args, **kwargs):
    """
    Просто калькулятор)
    """
    precision = convert_precision(kwargs['precision'])
    output_type = kwargs['output_type']
    act = args[-1]

    if act == "+":
        res = sum(args[0:len(args) - 1])

    elif act == "-":
        res = args[0]
        for n in args[1:len(args) - 1]:
            res -= n

    elif act == "*":
        res = 1
        for n in args[0:len(args) - 1]:
            res *= n

    elif act == "/":
        res = args[0]
        for n in args[1:len(args) - 1]:
            if n == 0:
                print("Деление на ноль невозможно")
                return None
            res /= n

    elif act == "^":
        res = args[0]
        for n in args[1:len(args) - 1]:
            if n % 1 != 0:
                print("Возведение в вещественную степень невозможно")
                return None
            res **= n

    # Целочисленное деление
    elif act == "//":
        res = args[0]
        for n in args[1:len(args) - 1]:
            if n == 0:
                print("Деление на ноль невозможно")
                return None
            res //= n

    # Остаток от деления
    elif act == "%":
        res = args[0]
        for n in args[1:len(args) - 1]:
            if n == 0:
                print("Деление на ноль невозможно")
                return None
            res %= n

    else:
        print("Операция не распознана")
        return None

    res = digits_round(res, precision)
    if isinstance(res, float) and res.is_integer():
        res = int(res)
    return res


if __name__ == '__main__':
    """
         main позволяет ввести значения с клавиатуры
         и запустить вычисление действия калькулятора
    """
    load_params()
    user_input()
