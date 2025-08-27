class Dico(dict):
    

    def __init__(self,*dic, **items):
        if len(dic) == 0 and len(items) == 0:
            self.keys_array = []
            self.values_array = []
            self.length = 0
        elif len(dic) == 1 and len(items) == 0:
            self.keys_array = list(dic[0].keys())
            self.values_array = list(dic[0].values())
            self.length = len(dic[0])
        elif len(dic) == 0 and len(items) > 0:
            self.keys_array = list(items.keys())
            self.values_array = list(items.values())
            self.length = len(items)
        else:
            print("Paramètre incorrect")
            exit(0)
        print(self.keys_array)
        print(self.values_array)

    def __len__(self):
        return self.length
    
    def __delitem__(self, key):
        del_index = self.keys_array.index(key)
        del self.keys_array[del_index]
        del self.values_array[del_index]
        self.length -= 1

    def __str__(self):
        s =  '{' + str(self.keys_array[0]) + " : " + str(self.values_array[0])
        i = 1
        while i < len(self.keys_array):
            s +=  ", " + str(self.keys_array[i]) + " : " + str(self.values_array[i])
            i += 1
        s += '}'
        return s

    def __setitem__(self, key, value):
        if key in self.keys_array:
            change_index = self.keys_array.index(key)
            self.values_array[change_index] = value
        else:
            self.keys_array.append(key)
            self.values_array.append(value)
