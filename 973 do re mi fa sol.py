s = 'до фа соль до ре фа ля си'
s = s.split()
order =  ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

s = sorted(s, key=lambda x: order.index(x))

print(s)