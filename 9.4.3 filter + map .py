lst_in = ['зонт=1000',
          'палатка=10000',
          'спички=22',
          'котелок=543']

tpl = list(map(tuple, (line.split('=') for line in lst_in)))
print(*tpl)

# for i in tpl:
#     print(i[0])

tpl_filter = filter(lambda x: int(x[1]) >= 500, tpl)
for i in tpl_filter:
    print(i[0], end = ' ')
#print(*tpl_filter[0][0])