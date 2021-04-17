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

        elif command == "CLASS" and len(elems)>1:
            my_manager.insert(elems)

        elif command == "DESCRIBIR" and len(elems)>1:
            response=my_manager.search_methods(elems[1])
            if response:
                print(response)
            else:
                print(f"No se consiguieron métodos para {elems[1]}\n")

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