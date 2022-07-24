from re import I


s = ['Пушкин: Сказака о рыбаке и рыбке', 
'Есенин: Письмо к женщине',
'Тургенев: Муму',
'Пушкин: Евгений Онегин',
'Есенин: Русь']

k = [i.split(': ') for i in s]
print(k)
d = {}
for i in k:
    d.setdefault(i[0], set()).add(i[1])
print(d)


