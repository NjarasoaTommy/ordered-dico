from ordered.dictionnary.dico import Dico

dic = {"matiere": "anglais", "prof": "Bertin", "coefficient": 3, "ue": "base", "faculative": False}
d = Dico(dic)
print(d)
d.reverse()
print(d)