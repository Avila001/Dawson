# put your python code here
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

N = 10 * 1000
weight = 0
sorted_things = {}
sorted_things2 = {}
lst = []
i = 0
sorted_things = sorted(things.items(), key=lambda item: -item[1])
print(sorted_things)
for i in sorted_things:
    if i[1] <= N:
        lst.append(i[0])
        N -= i[1]
print(lst)
# sorted_things2 = sorted(things, key=things.get)
# print(sorted_things2)

# while weight < N:

#     weight += 