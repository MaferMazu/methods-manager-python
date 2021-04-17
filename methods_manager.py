
class MethodsManager:
    """ Methods Manager Class """
    def __init__(self):
        self.heap = {}

    def insert(self, name, super_class, *kwargs):
        elem = {"super":super_class, "methods":[*kwargs]}
        self.heap[name]=elem

    def have(self, name):
        try:
            self.heap[name]
            return True
        except:
            return False

    def search_methods(self, name):
        base = self.heap[name]
        ancestors=[name]
        while base["super"]!=None:
            ancestors.append(base["super"])
            base=self.heap[base["super"]]

        ancestors=ancestors[::-1]
        methods_with_ancestor={}
        for ancestor in ancestors:
            methods=self.heap[ancestor]["methods"]
            for method in methods:
                methods_with_ancestor[method]=ancestor

        for method in methods_with_ancestor:
            print(f"{method} -> {methods_with_ancestor[method]} :: {method}")


    def __str__(self):
        return str(self.heap)
     

manager=MethodsManager()
manager.insert("A",None,1,2,3,4,5,6,7)
manager.insert("B","A",3,7)
print(manager)
manager.search_methods("B")


    
