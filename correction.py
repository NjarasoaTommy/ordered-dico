class Dico:
    def __init__(self, base={}, **donnees):
        self._cles = []
        self._valeurs = []

        if type(base) not in (dict, Dico):
            raise TypeError("le type attendu est un dictionnaire (usuel ou ordonné)")
        
        for cle in base:
            self[cle] = base[cle]

        for cle in donnees:
            self[cle] = donnees[cle]

    def __setitem__(self, key, value):
        if key in self._cles:
            self._valeurs[self._cles.index(key)] = value
        else:
            self._cles.append(key)
            self._valeurs.append(value)

    def __str__(self):
        if len(self._cles) == 0:
            return '{}'
        s =  '{ "' + str(self._cles[0]) + "\" : "
        if isinstance(self._valeurs[0], str):
            s += "\"" + str(self._valeurs[0]) + '"'
        else:
            s += str(self._valeurs[0])
        i = 1
        while i < len(self._cles):
            s +=  ", \"" + str(self._cles[i]) + "\" : "
            if isinstance(self._valeurs[i], str):
                s += "\"" + str(self._valeurs[i]) + '"'
            else:
                s += str(self._valeurs[i])
            i += 1
        s += ' }'
        return s
    
    def __repr__(self):
        return self.__str__(self)
    
    def __contains__(self, key):
        return key in self._cles

dic = {"nom": "Toky", "poste": "Attaquant"}
d = Dico(dic)
print(d)
print(d._cles)
print(d._valeurs)

print("=========================")
print("nom" in d)
print("sport" in d)