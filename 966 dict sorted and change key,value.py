


s = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

s = {int(key): value for value, key in (i.split(':') for i in s)}
# print(s)
# s = {value: key for key, value in s.items()}
print(s)
s = dict(sorted(s.items()))
print(s)
for value in list(s.values())[:3]:
    print(value, end=' ')

#{v:k for k, v in e2f.items()}

# s = sorted(s.items())
# print(s)
#s = dict(zip(s.values(), s.keys())) - reverse keys|values
#print(s)