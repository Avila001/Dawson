t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
    'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
def foo(s, sep = '-'):
    s = s.split()
    new_s = []
    for i in s:
        for j in i:
            new_s.append(t[j] if (t.get(j) or (j=='ъ' or j=='ь')) else j)
        new_s.append(' ')
    return ''.join(new_s).replace(' ', sep).strip(sep)

s = 'Лучший курс по Pythonъ!'.lower()

print(foo(s))
print(foo(s, '+'))