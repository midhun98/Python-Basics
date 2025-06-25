# Print out the keys with duplicate values
# eg:  {'a':1, 'b':1 , 'c':2, 'd':3, 'e':2}
# out : {1:['a','b'], 2:['c', 'e']}

duplicates = {"a": 1, "b": 1, "c": 2, "d": 3, "e": 2}
out = {}
for key, value in duplicates.items():
    if value not in out:
        out[value] = [key]
    else:
        out[value].append(key)

res = {}
for key, value in out.items():
    if len(value) > 1:
        res[key] = value
print(res)
