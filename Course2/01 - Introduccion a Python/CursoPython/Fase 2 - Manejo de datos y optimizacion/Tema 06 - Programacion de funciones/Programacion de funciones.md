# Tema 2: Manejo de datos y optimización

## <span style="color:green">2.3 Programación de funciones<span>

Las funciones son fragmentos de código que podemos ejecutar múltiples veces y pueden recibir y devolver información para comunicarse con el proceso principal.
    
### <span style="color:gray">2.3.1 Definición de funciones<span>
***

- Definición y llamada    
    
```python
# definición
def saludar():
    print("este print() se llama desde la función saludar")

# llamada
saludar()
```

- dentro  de una función podemos utilizar variables y sentencias de control

```python
def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i, i*5))
``` 

- Ámbito de las variables
Una variable que declaramos dentro de una función sólo existe dentro de esa función, y no en el proceso principal
    
```python
def test():
    n = 10
test()
print(n)
```
Sin embargo, una variable que se declare fuera de la función sí es accesible desde la función.    
    
```python
m = 10
def test():
    print(m)
test()
```
Siempre que declaremos la variable antes de la ejecución de la función podremos acceder a ella desde dentro.
```python
def test():
    print(l)
l = 10
test()
```
en el caso en que declaremos de nuevo una variable en la función, se creará una copia de la  misma que sólo funcionará dentro de la función. Por tanto, no podemos modificar una variable externa dentro de la función

```python
def test():
    n = 5
    print(n)
test()

o = 10
test()
print(o)
```

- La instrucción **`global`**   
Para poder modificar una variable externa desde la función, debemos indicar que es global 

```python
def test():
    global o
    o = 5
    print(o)
test()

o=10
test()
print(o)
```
    
### <span style="color:gray">2.3.2 Retorno de valores<span>
***
Gracias a la instrucción **`return`** las funciones pueden devolver valores al proceso principal para comunicarse con el exterior. La función finaliza en el momento de devolver un valor.

- Retorno simple
    
```python
def test():
    return "La función test() devuelve esta cadena"
test()
```

Los valores devueltos por una función se tratan como valores literales directos del tipo de dato retornado.
```python
print(test())
c = test()
print(c)
type(c)
c = test() + 10
type(c)
``` 

```python 
def test():
    return [1,2,3,4,5]
print(test())
print(test()[-1])
print(test()[1:4])
l = test()
l[-1]
```
    
- Retorno múltiple    

Una característica interesante es la posibilidad de devolver múltiples valores separados por comas.

```python
def test():
    return "Una cadena", 20, [1,2,3]

test()
```
Estos valores se tratan en conjunto, como una tupla inmutable, y se pueden reasignar a distintas variables.

```python
c,n,l = test()
print(c)
print(n)
print(l)
```

### <span style="color:gray">2.3.3 Envío de valores<span>
***

Para comunicarse con el exterior las funciones no solo pueden devolver valores, también pueden recibir.    

```python
def suma(a,b):
    return a+b
r = suma(2,4)
print(r)
```

- Parámetros y argumentos    
En la definición de una función los valores que se reciben se denominan parámetros, pero durante la llamada los valores que se envían se denominan argumentos.

### <span style="color:gray">2.3.4 Argumentos y parámetros<span>
***
- Argumentos por posición    
Cuando enviamos argumentos a una función, estos se definen por orden en los parámetros definidos. 
    
```python
def resta(a,b)
    return a-b

resta(8,10)
# argumento 8 => posición 0 => parámetro a
# argumento 10 => posición 1 => parámetro b
```

- Argumentos por nombre    
Sin embargo es posible evadir el orden de los parámetros si indicamos durante la llamada que valor tiene cada parámetro a partir de su nombre
    
```python
resta(b=8 , a=10)
```

- Llamada sin argumentos    
Al llamar una función que tiene definidos unos parámetros, si no pasamos los argumentos correctamente provocará un error
    
```python
resta()
```
    
- Parámetros por defecto    
Para solucionarlo podemos asignar uos valores por defecto nulos a los parámetros, de esa forma podríamos hacer una comprobación antes de ejecutar el código de la función:
    
```python
def resta(a=None,b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b
resta(1,5)
```

### <span style="color:gray">2.3.5 Argumentos por valor y referencia<span>
***
Dependiendo del tipo de dato que enviemos a la función, podemos diferenciar dos comportamientos:
- Paso por valor: Se crea una copia local de la variable dentro de la función. Por valor se suelen pasar los tipos simples como enteros, flotantes, cadenas, lógicos...
- Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro de la función le afectaran también fuera. Por referencia se suelen pasar  los tipos compuestos, listas, diccionarios, conjuntos...

- **Paso por valor**   

    
```python
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)
```

- **Paso por referencia**

```python
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns)
```
No es posible indicar a python cuando queremos pasar un argumento por valor o referencia, en otros lenguajes si se puede. Podemos utilizar trucos, por ejemplo devolver el valor modificado dentro de la función y volverlo a asignar a la variable

- Truco con valores   
Podemos volver a asignar a la variable el valor modificado dentro de la función.

```python
def doblar_valor(numero):
    numero *= 2
    return(numero)
    
n = 10
n = doblar_valor(n)
n
```

- Truco con referencias     
Creando una copia  prevenimos  que dentro de la función se pueda modificar la lista original ya que lo que mandamos es una copia.   
    
```python
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2


ns = [10, 50, 100]
doblar_valores(ns[:]) #creando una copia
ns
```
    
### <span style="color:gray">2.3.6 Argumentos y parámetros indeterminados<span>
***

¿Qué pasaría se queremos mandar un número indeterminado de valores a una función?, mandar un número indeterminado de argumentos y tratarlos como un número indeterminado de parámetros.   
Dado que tenemos dos maneras de enviar y recibir datos, por posición y por nombre, python implementa dos formas distintas 

Para manejar los argumentos por posición lo que debemos hacer es indicar un parámetro iterable de la siguiente forma: **`*args`**. Ponemos primero el asterísco y por norma general se le suele llamar _args_, de argumentos
    
```python
#devuelve una tupla
def indeterminados_posicion(*args):
    #print(args)
    for arg in args:
        print(arg)
    
indeterminados_posicion(5, "Hola", [1,2,3])
```
    
   
En los argumentos por nombre, en lugar de un iterable python puede gestionar un diccionario. Es decir, en lugar de una tupla, un diccionario. Para indicarles que queremos crear estos argumentos en clave y valor tenemos que ponerle dos astericos delante. Devemos indecarlos con **`**kwargs`**

    
```python
#devuelve un diccionario
def indeterminados_nombre(**kwargs):
    print(kwargs)
    
indeterminados_nombre(n=5, c="Hola", l=[1,2,3])
``` 

```python
#devuelve un diccionario
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "-", kwargs[kwarg])
    
indeterminados_nombre(n=5, c="Hola", l=[1,2,3])
```
    
Con argumentos indeterminados por posición y por clave.
```python
def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("Sumatorio indeterminado", t)
    for kwarg in kwargs:
        print(kwarg, "-", kwargs[kwarg])

super_funcion(10,50,-1,1.56,200,5, nombre="Hector", edad=27)
```

### <span style="color:gray">2.3.7 Funciones recursivas <span>
***
    
Se trata de funciones que se llaman a sí misma durante su propia ejcución. Funcionan de forma similar a las iteraciones y debemos de encargarnos de planificar el momento en que una función recursiva deja de llamarse para no tener una función recursiva infinita.
    
Suele usarse para dividir una tarea en subtareas más simples de forma que sea más fácil abordar el problema y solucionarlo.

- Función recursiva sin retorno

```python
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)
```
    
- Función recursiva con retorno    

```python
def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num

factorial(5)
```


### <span style="color:gray">2.3.8 Funciones integradas <span>
***
    
- **`int():`** Se usa para devolver un número entero.
    
```python
n = int("10")
n
```
- **`float():`** Se usa para devolver un número de coma flotante. El método acepta un número entero o un número de coma flotante, o una cadena que contenga números.  

```python
f = float("10.5")
f
```
- **`str():`** Transforma cualquier valor a una cadena.

```python
c = "Un texto y un número " + str(10) + " " + str(3.14)
c
```
- **`bin():`** Convierte y devuelve la cadena binaria equivalente de un entero dado.
    
```python
bin(10)
```
- **`hex():`** Convierte un número entero a la cadena hexadecimal correspondiente.

```python 
hex(10)
```

- **`int()`** con base:
```python
```
- **`abs():`** Valor absoluto de un número.
- **`round():`**Devuelve el número de coma flotante redondeado a los digitos dados después del punto decimal.
- **`eval():`** Analiza la expresión pasada y la ejecuta 
- **`len():`** Longitud de una colección o cadena
- **`help():`** Para invocar el menú de ayuda del interprete de Python.