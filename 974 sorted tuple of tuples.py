s =(("Номер;Имя;Оценка;Зачет"), ("1;Портос;5;Да"), ("2;Арамис;3;Да"), ("3;Атос;4;Да"), ("4;д'Артаньян;2;Нет"), ("5;Балакирев;1;Нет"))
order = ['Имя', 'Зачет', 'Оценка', 'Номер']
print(s)
s = list(list(int(i) if i.isdigit() else i for i in line.split(';')) for line in s)
print(s)
# new_s = []
# for i in s:
#     new_s.append(i.split(';'))

n = len(s)
# for i in range(1, len(new_s)):
#     for j
print(f'{n}: {s}')

number, name, grade, offset = zip(*s)
t_sorted = tuple(zip(name, offset, grade, number))
print(t_sorted)

# x = iter(new_s)
# print(*zip(x))

# x = iter([1,2,3,4,5,6,7,8,9])
# print(*zip(x, x, x))

# zip(*[iter(s)]*n)