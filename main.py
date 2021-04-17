from sys import exit
from methods_manager import MethodsManager

def main():

    print("*"*30)
    print("""Welcome to this methods manager simulator :D Happy coding\n""")
    my_manager = MethodsManager()

    while True:
        my_input = input(">> ")
        elems = my_input.split(" ")
        command = elems[0].upper()

        if command == "SALIR":
            print("Nos vemos pronto :D\n")
            exit(0)

        elif command == "CLASS" and len(elems)>2:
            if elems[1][0].isupper():
                name = elems[1]
                if ":" in elems[2:]:
                    if my_manager.have(elems[3]):
                        super_class = elems[3]
                        if len(elems) > 4:
                            methods = elems[4:]
                        else:
                            methods = []

                        my_manager.insert(name, super_class, *methods)
                        str_methods = ' '.join(map(str, methods))
                        print(f"Se creo {name} con sus métodos {str_methods}\n")
                    else:
                        print(f"Error: {elems[3]} no es una clase declarada\n")
                    
                else:
                    super_class = None
                    methods = elems[2:]

                    my_manager.insert(name, super_class, *methods)
                    str_methods = ' '.join(map(str, methods))
                    print(f"Se creo {name} con sus métodos {str_methods}\n")

            else:
                print("Error: El nombre de las clases debe ser en mayúsculas\n")
                

        elif command == "DESCRIBIR" and len(elems)>1:
            my_manager.search_methods(elems[1])
            print("")

        else:
            print_help()

def print_help():
    """ Print help for user """

    response = """Las opciones válidas son:

        CLASS <tipo> [<nombre>]
        Crea una clase con tipo <tipo> y define métodos
        El <tipo> puede ser:
        • Un nombre, que establece un tipo que no hereda de ningún otro.
        • Una expresión de la forma <nombre> : <super>, que establece el 
        nombre del tipo y el hecho de que este tipo hereda del tipo con nombre <super>.
        Ej: CLASS A f g y CLASS B : A f h

        DESCRIBIR <nombre>
        Muestra los métodos de <nombre>.
        
        SALIR
        Salir del simulador.\n"""

    print(response)


if __name__  ==  "__main__":
    
    main()