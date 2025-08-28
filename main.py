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

for k in d:
    print(k)