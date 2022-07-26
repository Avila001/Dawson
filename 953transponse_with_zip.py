import sys

# считывание списка из входного потока
lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']

# здесь продолжайте программу (используйте список строк lst_in)
lst_in = [line.split() for line in lst_in]
print(lst_in)
first = zip(*lst_in)
print(*first)
