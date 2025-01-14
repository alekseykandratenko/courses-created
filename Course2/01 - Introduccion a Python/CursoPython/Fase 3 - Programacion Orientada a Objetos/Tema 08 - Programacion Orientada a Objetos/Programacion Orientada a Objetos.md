# Tema 3: Programación Orientada a Objetos
Paradigma de solución de problemas que identifica entidades de la realidad y los traslada a clases y objetos.
Respecto a la programación clásica, la POO es más ágil, más intuitiva, mas organizable y más escalable.
## <span style="color:green">3.1 Programación Estructurada vs POO <span>
Nos piden crear un registro para manejar los clientes de una empresa, con su nombre, sus apellidos y su dni. El programa debe permitirnos mostrar los datos de los clientes o borrarlos a partir de su dni
    
### <span style="color:gray">3.1.1 Ejemplo con Programación Estructurada<span>
***

```python
clientes= [
    {'Nombre': 'Victor',  'Apellidos':'Serrano Rodriguez',      'dni':'11111100A'},
    {'Nombre': 'Maria',    'Apellidos':'Gonzalez Álvarez',  'dni':'22222200B'} 
]
```

```python
def mostrar_cliente(cliente, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return
    print('Cliente no encontrado')
```

```python
mostrar_cliente(clientes, '11111100A')
```

```python
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return
        
    print('Cliente no encontrado')
```

```python
print("==LISTADO DE CLIENTES==")
print(clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111100A')
mostrar_cliente(clientes, '11111100Z')

print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222200V')
borrar_cliente(clientes, '22222200B')

print("\n==LISTADO DE CLIENTES==")
print(clientes)
```

### <span style="color:gray">3.1.1 Ejemplo con Programación Orientada a Objetos<span>
***
```python
# Estructura para los clientes
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)
    

# Estructura para las empresas
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")
```

```python
# Creamos los clientes
Victor = Cliente(nombre="Victor", apellidos="Serrano Rodriguez", dni="11111100A")
Maria = Cliente("22222200B", "Maria", "Gonzalez Álvarez")

# Creamos la empresa con los clientes ya creados
empresa = Empresa(clientes=[Victor, Maria])

# Mostramos el listado de clientes en la empresa
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)
print("\n==MOSTRAR CLIENTES POR DNI==")
    
# Consultamos los clientes por su dni
empresa.mostrar_cliente("11111100A")
empresa.mostrar_cliente("11111100Z")

# Borro clientes por DNI
print("\n==BORRAR CLIENTES POR DNI==")
empresa.borrar_cliente("22222200V")
empresa.borrar_cliente("22222200B")

# Mostramos el listado de clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)
```
## <span style="color:green"> 3.2 Clases y Objetos <span>

<center><img src = "galletas.jpg"></center>

- **Objeto:** Los objetos son la base de la POO , son un tipo de dato cuya definición viene dada en una estructura llamada clase.
- **Clase:**  Una clase es un guión sobre como deben ser los objetos que se crearan en ella. Las clases son los moldes de los objetos
   
Como todas las galletas se hacen con el mismo molde (clase) comparten unos atributos pero cada una de estas galletas (objetos) son únicas

```python
'''Creamos la clase Galleta'''
class Galleta:
    pass
```
```python
'''Creamos los objetos una_galleta y otra_galleta de la clase Galleta'''
una_galleta = Galleta()
otra_galleta = Galleta()
```
Este proceso de crear un objeto a partir de su clase se denomina instanciación, de echo un objeto también se conoce como una instancia de clase. Todo se crea a partir de una clase
    
```python
'''Podemos saber la clase de un objeto o valor'''
type(una_galleta)
```
```python
type(10)
type(3.014)
type("Hola")
type([])
type({})
```
```python
def hola():
    pass
```
```python
type(hola)
```
## <span style="color:green"> 3.3 Atributos y Métodos de clase <span>
- **Atributos:** Son las características individuales que diferencian un objeto de otro y determinan su apariencia, estado u otras cualidades. Se guardan en variables denominadas de instancia, y cada objeto particular puede tener valores distintos para estas variables.
- **Métodos:** Los métodos describen el comportamiento de los objetos de una clase. representan las operaciones que se pueden realizar con los objetos de la clase.   
    
### <span style="color:gray">3.3.1 Atributos<span>
***
El valor de los atributos es lo que diferencia a un objeto (instancia) de otro y lo que las hace únicas. Un objeto también puede tener sus propios atributos.
```python
class Galleta:
    pass
'''Creamos una galleta'''
una_galleta = Galleta()
```
- Atributos de instancia
Si el atributo no existe se creará automáticamente dentro de la instancia del objeto y podremos utilizarlo.
```python
una_galleta.sabor = 'Salado'
una_galleta.color = 'Marrón'
```
```python
print("El sabor de esta galleta es", una_galleta.sabor)
print("El color de esta galleta es", una_galleta.color)
```
   
    
- Atributos de clase
```python
class Galleta:
    chocolate = False #Por defecto ninguna galleta tiene chocolate
```
```python
g = Galleta()
g.chocolate
```   
Podemos cambiar su valor en cualquier momento
```python
g.chocolate = True
g.chocolate
```
Lo interesante es establecer los atributos en el momento de crear el objeto y no tener que definirlos uno a uno. Para mostrar como hacerlo, necesitamos primero introducir el método especial llamado _**init**_ y la palabra reservada _**Self**_

### <span style="color:gray">3.3.2 Métodos<span>
***
Los métodos son "funciones" y nos permiten definir funcionalidades para llamarlas desde las instancias. 
    
```python
class Galleta:
    chocolate = False
    
    def saludar():
        print("Hola, soy una galleta muy sabrosa")

# galleta = Galleta()
# galleta.saludar()
'''Al ser una instancia de clase llamando a la clase en lugar del objeto'''
Galleta.saludar()
```


- El argumento **_Self_**. Cuando se ejecuta un método desde un objeto, se envía un primer argumento implícito que hace referencia al propio objeto. Como este argumento hace referencia al objeto en sí mismo por convención se le llama **self**

```python
class Galleta:
    chocolate = False

    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galleta muy sabrosa")
        print(soy_el_propio_objeto)

galleta = Galleta()
galleta.saludar()
```

El poder acceder al propio objeto desde un método nos permite acceder a sus atributos

```python
class Galleta():
    chocolate = False

    def chocolatear(self):
        self.chocolate = True

galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)
```
    
    
- El método **_init_** es un método **constructor**, un método especial que se ejecuta automáticamente al crear un objeto (se comparte con todos los métodos de la misma clase) y permite enviar argumentos durante la instantciación.   
- La palabra self hace referencia al propio objeto

    
```python
class Galleta():
    chocolate = False
    def __init__(self):
        print("Seacaba de crear una galleta")

g = Galleta()
```