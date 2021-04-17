# :sunny: Manejador de métodos
Este es un manejador de tipos de métodos en Python.

## :computer: Requerimientos

Python3 and pip3.

Crear tu entorno virtual:

```shell
python3 -m venv env
```

Activar el entorno:

- Unix/macOS

```shell
source env/bin/activate
```

- Windows

```shell
./env\Script\activate
```

### Instalar requerimientos:

```shell
pip3 install -r requirements.txt
```

## :fire: Para correr

```shell
python3 main.py
```

## :bulb: Cómo usar

i. CLASS \<nombre> \[\<representacion>]

Crea una clase con tipo <tipo> y define métodos
El \<tipo> puede ser:
• Un nombre, que establece un tipo que no hereda de ningún otro.
• Una expresión de la forma \<nombre> : \<super>, que establece el nombre del tipo y el hecho de que este tipo hereda del tipo con nombre \<super>.
Ej: CLASS A f g y CLASS B : A f h


ii. DESCRIBIR \<nombre>

Muestra los métodos de \<nombre>.

Define un nuevo registro de nombre \<nombre>. La definición de los campos del registro viene dada por la lista en \[\<tipo>].

iii. SALIR

Para salir del simulador.

## :mag: For run the tests

```shell
cd tests
coverage3 run --source=methods_manager -m unittest test_methods_manager.py
```

#### Coverage of the tests

```shell
coverage3 report -m
```

| Module | Coverage |
|:----:|:--:|
| MethodsManager| 96% |