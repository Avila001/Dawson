from tkinter import S
from turtle import xcor


s = ["Атос=лейтенант","Портос=прапорщик","д'Артаньян=капитан","Арамис=лейтенант","Балакирев=рядовой"]

order = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник']

s = list(i.split('=') for i in s)
print(s)

s = sorted(s, key=lambda x: order.index(x[1]))

print(s)