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
        # print(self.keys_array)
        # print(self.values_array)

    def __len__(self):
        return self.length
    
    def __delitem__(self, key):
        del_index = self.keys_array.index(key)
        del self.keys_array[del_index]
        del self.values_array[del_index]
        self.length -= 1

    def __str__(self):
        if len(self.keys_array) == 0:
            return '{}'
        s =  '{ "' + str(self.keys_array[0]) + "\" : "
        if isinstance(self.values_array[0], str):
            s += "\"" + str(self.values_array[0]) + '"'
        else:
            s += str(self.values_array[0])
        i = 1
        while i < len(self.keys_array):
            s +=  ", \"" + str(self.keys_array[i]) + "\" : "
            if isinstance(self.values_array[i], str):
                s += "\"" + str(self.values_array[i]) + '"'
            else:
                s += str(self.values_array[i])
            i += 1
        s += ' }'
        return s

    def __setitem__(self, key, value):
        if key in self.keys_array:
            change_index = self.keys_array.index(key)
            self.values_array[change_index] = value
        else:
            self.keys_array.append(key)
            self.values_array.append(value)

    def sort(self):
        old_key = self.keys_array.copy()
        old_values = self.values_array.copy()
        self.keys_array.sort()
        i = 0
        while i < len(self.keys_array):
            self.values_array[i] = old_values[old_key.index(self.keys_array[i])]
            i += 1
    
    def reverse(self):
        old_key = self.keys_array.copy()
        old_values = self.values_array.copy()
        self.keys_array.reverse()
        i = 0
        while i < len(self.keys_array):
            self.values_array[i] = old_values[old_key.index(self.keys_array[i])]
            i += 1

    def __iter__(self):
        return ItKeys(self.keys_array)
    
    def keys(self):
        for i in self.keys_array:
            yield i
    
    def values(self):
        for i in self.values_array:
            yield i
    
    def items(self):
        for i in range(len(self.keys_array)):
            yield (self.keys_array[i], self.values_array[i])

    def __add__(self, other_dic):
        self.keys_array.extend(list(other_dic.keys()))
        self.values_array.extend(list(other_dic.values()))
        return self

class ItKeys():
    def __init__(self, keys):
        self.list_keys = keys
        self.position = len(self.list_keys)
    def __next__(self):
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.list_keys[self.position]