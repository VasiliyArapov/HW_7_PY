# На вход программы поступает строка в формате:

# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:

# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

# Выводить на экран получившийся кортеж.

# Sample Input:

# house=дом car=машина men=человек tree=дерево
# Sample Output:

# ((house, дом), (car, машина), (men, человек), (tree, дерево))

input_string = input("Input your string: ").split()
# print(input_string)
proc_string = list((map(lambda x: x.split('='), input_string)))
# print(proc_string)
tuple_list = list(map(tuple, proc_string))
# print(tuple_list)
tp = tuple(tuple_list)
print(tp)
