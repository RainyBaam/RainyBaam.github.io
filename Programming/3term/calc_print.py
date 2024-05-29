import datetime


def print_results(*args, action=None, result=None):
    """
    Вывод в табличном виде результатов вычислений
    """
    for arg in args:
        print("| " + str(arg), end=" ")
    print("| " + str(action) + " | ", end="")
    print("result: " + str(result) + " |")


def write_log(*args, action=None, result=None,
              file='output.txt'):
    with open(file, mode='a', errors='ignore') as output:
        now = datetime.datetime.now()
        now_time = now.strftime("%d.%m.%Y %H:%M")
        output.write(f"{now_time}, {action}, {args} = {result} \n")
