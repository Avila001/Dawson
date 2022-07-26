


s = ['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']

s = {key: int(value) for key, value in (line.split('=') for line in s)}

print(s)

s = dict(sorted(s.items(), key=lambda item: item[1], reverse=True))
#s = sorted(s, key=lambda x: int(s.get(x)), reverse=True)


print(*s.keys())
