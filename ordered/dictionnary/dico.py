class Dico(dict):
    

    def __init__(self,*dic, **items):
        if len(dic) == 0 and len(items) == 0:
            self.keys_array = []
            self.values_array = []
        elif len(dic) == 1 and len(items) == 0:
            self.keys_array = dic[0].keys()
            self.values_array = dic[0].values()
        elif len(dic) == 0 and len(items) > 0:
            self.keys_array = items.keys()
            self.values_array = items.values()
        else:
            print("Paramètre incorrect")
            exit(0)
        print(self.keys_array)
        print(self.values_array)
