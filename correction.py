class Dico:
    def __init__(self):
        self._cles = []
        self._valeurs = []

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

d = Dico()
d["nom"] = "TOM"
d["age"] = 12
d["sexe"] = 'Homme'
d["nom"] = "Blaise"
print(d)
print(d._cles)
print(d._valeurs)

print("=========================")
print("nom" in d)
print("sport" in d)