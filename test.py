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

print("========================================")
legumes = Dico(carotte = 26, haricot = 48)
print(legumes)
print(len(legumes))

print("========================================")
legumes.reverse()
fruits = fruits + legumes
print(fruits)

print("========================================")
del fruits['haricot']
print('haricot' in fruits)
print(legumes['haricot'])

print("========================================")
for cle in legumes:
     print(cle)

print(legumes.keys())
print(legumes.values())
for nom, qtt in legumes.items():
    print("{0} ({1})".format(nom, qtt))