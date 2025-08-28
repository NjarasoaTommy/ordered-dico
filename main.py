from ordered.dictionnary.dico import Dico

dic = {"matiere": "anglais", "prof": "Bertin", "coefficient": 3, "ue": "base", "faculative": False}
d = Dico(dic)

d2 = Dico(sport="Foot", post="middle player", number=14)
print(d)
d + d2
print(d)