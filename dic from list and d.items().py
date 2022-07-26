lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']

d = {}

for i in lst_in:
    key, value = i.split()
    d.setdefault(key, []).append(value)
print(d)
for key, value in d.items():
    print(f"{key}: {', '.join(value)}")

