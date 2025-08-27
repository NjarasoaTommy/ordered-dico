from ordered.dictionnary.dico import Dico

dic = {"matiere": "anglais", "prof": "Bertin"}
d = Dico(dic)

print(len(d))
del d["prof"]
print(len(d))