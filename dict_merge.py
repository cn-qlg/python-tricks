"""合并两个dict"""

# dict.update()，本地更新，键相同，则更新
d1 = {"a": 1, "b": 2}
d2 = {"b": 22, "c": 3}
print("Before")
print(d1, id(d1))
print(d2, id(d2))
d1.update(d2)
print("After")
print(d1, id(d1))
print(d2, id(d2))

# 直接新建一个新的dict
d1 = {"a": 1, "b": 2}
d2 = {"b": 22, "c": 3}
d3 = {**d1, **d2}
print(id(d1), id(d2), id(d3))
print(d3)
