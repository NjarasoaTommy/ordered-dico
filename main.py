from ordered.dictionnary.dico import Dico

print("=============================================================")
dic = {"matiere": "anglais", "prof": "Bertin"}
d = Dico(dic)
print("===================")
d2 = Dico(nom="Koto", age=42)
print("===================")
d2 = Dico(dic, nom="Koto", age=42)
print("=============================================================")