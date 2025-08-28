from ordered.dictionnary.dico import Dico
fruits = Dico()
print(fruits)
fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
print(fruits)

print("========================================")
fruits.sort()
print(fruits)
