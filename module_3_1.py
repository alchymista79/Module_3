calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    argument = (len(string), string.upper(), string.lower())
    count_calls()
    return argument

def is_contains(string,list_to_search ):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            output = True
            break
        else:
            output = False
            continue
    return output


print(string_info('колонна'))
print(string_info('теплообменник'))
print(string_info('печь'))
print(is_contains('бЕнЗин', ['неФть', 'дизеЛЬ', 'Бензин']))
print(is_contains('битум', ['УВГ', 'катализат', 'гудроН', 'гАзОЙль']))
print(calls)