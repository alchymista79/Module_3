def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['oil', 23, True]
values_dict = {'a': 41, 'b': 'gas', 'c': False}
values_list_2 = [8, 88]


print_params()
print_params(2, 4)
print_params('string', False)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)