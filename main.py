from ordered.dictionnary.dico import Dico

dic = {"matiere": "anglais", "prof": "Bertin"}
d = Dico(dic)

print(d)
del d["prof"]
print(d)