# Tema 2: Manejo de datos y optimización

## <span style="color:green">2.4 Gestión de errores<span>


### <span style="color:gray">2.4.1 Errores<span>
***

- **Errores de sintaxis:** <span style="color:red"> SyntaxError <span>   

Son errores de código, por ejemplo cuando nos quedamos un paréntesis sin cerrar
```python
print("Hola"
```


- **Errores de nombre:** <span style="color:red"> NameError <span>    
<span style="color:black">El sistema interpreta que debe ejecutar alguna función o método pero no lo encuentra definido <span>

```python
pint("Hola")
```

- **Errores Semánticos**
Son los más difíciles de identificar ya que van ligados al sentido del funcionamiento y dependen de la situación.   
    
 Ejemplos:
    
    **.`pop()`** con una lista vacía
    ```python
    l = [1,2,3]
    l.pop()
    l.pop()
    l.pop()
    l.pop()
    
    ```
    
    
- Podemos **prevenir estos errores** utilizando la función **`len()`**
       
```python
l = [1,2,3]
if len(l) > 0:
    print(l)
    l.pop()
    print(l)
else:
    print("la cadena está vacía")
```

    
- **Error de tipo** <span style="color:red"> TypeError <span>   
<span style="color:black">Nos devuelve este error cuando una operación o función se aplica a un objeto de tipo no apropiado.
```python 
n = input("Introduce un número")
m = 4 
print("{}/{} = {}".format(n, m, n/m))
```

```python 
n = float(input("Introduce un número"))
m = 4 
print("{}/{} = {}".format(n, m, n/m))
```

¿Qué pasará si el usuario introduce una cadena de caracteres?

### <span style="color:gray">2.4.2 Excepciones <span>
***
Los errores detectados durante la ejecución se llaman excepciones, y no son incondicionalmente fatales, podemos manejarlos en los programas de python. 

- Bloques **`try`** y **`except`**     
    
Para crear la excepción y prevenir el error debemos poner el código propenso al error en el bloque **`try`** y encadenar un bloque **`except`** para trata la excepción

```python
try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")
```

Utilizamos el bucle **`while`** podemos repetir la lectura hasta que el usuario lo introduzca de forma correcta, y entonces rompemos el bucle con **`break`**
```python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        break  # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")
```

- Bloque **`else`**   
Es posible encadenar un bloque **`else`** después de **`except`** para ejecutar en el caso de que todo funcione correctamente (no se ejecuta la excepción)

```python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
```

- Bloque **`finally`**
Por último, es posible utilizar un bloque **`finally`** que se ejecute al final del código, ocurra o no ocurra un error.

```python
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta
```

### <span style="color:gray">2.4.3 Excepciones multiples <span>
***

- **Guardado de excepciones**   
Cuando ocurre un error dentro del bloque **`try`** se produce la excepción, y cada excepción tiene su propio identificador que podemos guardar dentro de una variable

```python
try:
    n = input("Introduce un número: ")
    5/n
except Exception as e:
    print( type(e).__name__ )
```

- **Excepciones encadenadas**   
Gracias a los identificadores de errores podemos crear múltiples comprobaciones, siempre que dejemos en último lugar la excepción por defecto Excepcion que engloba cualquier tipo de error (si la pusiéramos al principio, las demas excepciones nunca se ejecutarían):

```python
try:
    n = float(input("Introduce un número: "))
    5/n
except TypeError:
    print("No se puede dividir el número por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print( type(e).__name__ )
```
### <span style="color:gray">2.4.4 Ejemplo: Invocación de excepciones<span>
***
```python
def mi_funcion(algo=None):
    if algo is None:
        print("Error, no se permite un valor nulo")

mi_funcion()        
```

```python
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error!, no se permite un valor nulo")
    except ValueError:
        print("Error!, No se permite un valor nulo (desde la excepción)")

mi_funcion() 
```

### <span style="color:gray">2.4.5 Ejercicios complementarios <span>
***

**1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python 
# Completar
resultado = 10/0
    
    
    
    
    
```

**2) Localiza el error en el siguiente bloque de código.  Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
# Completar

lista = [1, 2, 3, 4, 5]
lista[10]

    
    
    
    
```

**3) Localiza el error en el siguiente bloque de código.  Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
# Completar
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
colores['blanco']
    
    
    


```

**4) Localiza el error en el siguiente bloque de código.  Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:**

```python
# Completar
resultado = 15

    

    
    
    
```

**5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:**


```python
elementos = [1, 5, -2]

# Completar

    
    
    
    
    
```
    