from ordered.dictionnary.dico import Dico

dic = {"matiere": "anglais", "prof": "Bertin", "coefficient": 3, "ue": "base", "faculative": False}
d = Dico(dic)

it = iter(d)

# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for k in d.keys():
    print(k)
print("=======================")
for v in d.values():
    print(v)
print("=======================")
for (k, v) in d.items():
    print(k, " => ", v)