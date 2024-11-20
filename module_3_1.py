def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string,list_to_search ):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if i.lower() == string:
            return True
    return False


calls = 0
print(string_info('колонна'))
print(string_info('теплообменник'))
print(string_info('печь'))
print(is_contains('бЕнЗин', ['неФть', 'дизеЛЬ', 'Бензин']))
print(is_contains('битум', ['УВГ', 'катализат', 'гудроН', 'гАзОЙль']))
print(calls)