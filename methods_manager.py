
class MethodsManager:
    """ Methods Manager Class """
    def __init__(self):
        self.heap = {}

    def insert(self, elems):
        if elems[1][0].isupper():
            name = elems[1]
            if ":" in elems[2:]:
                if self.have(elems[3]):
                    super_class = elems[3]
                    if len(elems) > 3:
                        methods = elems[4:]
                    else:
                        methods = []

                    self.insert_simple(name, super_class, *methods)
                    str_methods = ' '.join(map(str, methods))
                    print(f"Se creo {name} con sus métodos {str_methods}\n")
                else:
                    print(f"Error: {elems[3]} no es una clase declarada\n")
                
            else:
                super_class = None
                if len(elems)>1:
                    print("here")
                    methods = elems[2:]
                else:
                    print("vacio")
                    methods=[]

                self.insert_simple(name, super_class, *methods)
                str_methods = ' '.join(map(str, methods))
                print(f"Se creo {name} con sus métodos {str_methods}\n")

        else:
            print("Error: El nombre de las clases debe ser en mayúsculas\n")


    def insert_simple(self, name, super_class, *kwargs):
        elem = {"super":super_class, "methods":[*kwargs]}
        self.heap[name]=elem

    def have(self, name):
        try:
            self.heap[name]
            return True
        except:
            return False

    def search_methods(self, name):
        if self.have(name):
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

            response = ""
            for method in methods_with_ancestor:
                response = response + f"{method} -> {methods_with_ancestor[method]} :: {method}\n"

            return response
        else:
            return None


    def __str__(self):
        return str(self.heap)


    
