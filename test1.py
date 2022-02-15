list = ['key1', 'key2'], ['value1', 'value2']
dict11 = {}

for i1, i2 in zip(*list):
    dict11[i1] = i2

print(dict11)