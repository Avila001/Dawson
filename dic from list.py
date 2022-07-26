lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
print(lst_in)
lst_new = [i.split() for i in lst_in]
print(lst_new)
print(lst_new[0])
d = {lst_new[i][0]: lst_new[i][1] for i in range(len(lst_new))}
m = {int(key): [value]for key, value in lst_new}
print(d)
print(m)
if 'test' in m:
    m[3].append('test')
print(m)
#for i in range(len(lst_new)):

lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
lst_new = [i.split() for i in lst_in]
print(lst_new)
dic = {}
for i in lst_in:
    lenght = len(i.split()[0])
    print(lenght)
    print(i)
    dic.setdefault(int(i[:lenght]), []).append(i[lenght:])
print('setdefault', dic)
print(*sorted(dic.items()))

for d in dic:
    print(f'{d}:', end = '')
    print(*dic[d], sep=',')