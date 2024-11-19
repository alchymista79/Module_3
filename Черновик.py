# Домашняя работа по уроку "Пространство имён"

# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен
# подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# 1. Создать переменную calls = 0 вне функций.
# 2. Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных
# двух функциях.
# 3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# 4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# 6. Вывести значение переменной calls на экран(в консоль).

# Примечания:
# Для использования глобальной переменной внутри функции используйте оператор global.
# Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.

# ~_Р_Е_Ш_Е_Н_И_Е_~
calls = 0   # 1
def count_calls():  #2
    global calls
    calls += 1

def string_info(string):    #3
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Kalinka'))
print(string_info('Cavaleria'))
print(is_contains('cube', ['recycling', 'cyclic', 'sphere'])) # No matches
print(is_contains('GaZEL', ['List', 'Snow', 'Gazelist', 'gAzeL'])) # Urban ~ urBAN

print(calls)