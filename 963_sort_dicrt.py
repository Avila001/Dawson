
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}

def get_sort(d):
    res = [d[i] for i in sorted(d, reverse=True)]
    print(res)

get_sort(d)