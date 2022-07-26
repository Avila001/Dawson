'''Фишка функции-генератора в том, что она возвращается в замороженный цикл, значения перед циклом не "обнуляются"'''
def foo(N):
    a, b, c = 1, 1, 1
    for i in range(N):
        yield a
        a, b, c = b, c, a + b + c


N = 7
a = foo(N)
# for i in a:
#     print(i, end = ' ')
# print(a)
# [print(next(a), end=' ') for _ in range(N)]
print(*(a))
