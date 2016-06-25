﻿"""Создание словарей"""

# Все эти примеры создают одинаковые словари
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

# Те, кто имел опыт программирования на Си-подобных языках, могут
# подумать, что в этой строке ошибка (потому что в них операции
# сравнения связывались бы слева направо), однако в Python такое
# сравнение абсолютно корректно и действительно проверяет все
# значения на равенство друг другу. Здесь действуют те же правила,
# что мы рассматривали для двойных сравнений во втором уроке
# курса Python Starter (все последовательные операции сравнения
# и проверки равенства объединяются при помощи операции and).
print(a == b == c == d == e)

print(a)

print()

# Использование включений словарей (аналогично списковым включениям)
print({string: string.upper() for string in ('one', 'two', 'three')})