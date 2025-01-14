# Tema 2: Manejo de datos y optimización

## <span style="color:green">2.1 Colecciones de datos<span>


### <span style="color:gray">2.1.1 Tuplas<span>
***
Una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. Se representan escribiendo los eleemntos entre paréntesis y separados por comas.
    
```python
tupla = ("Hola", 8,-5, [2,4,6])
tupla
```
_**Index**_ y _**Slicing**_ en tuplas
```python
tupla[0]
tupla[-1]
tupla[2:]
tupla[3][0]
```
**Inmutalidad** en las tuplas   
Las tuplas son como las listas pero con la pecularidad de que son inmutables.
```python
tupla[0] = 0
```
La función **`len()`**
```python
len(tupla)
len(tupla[0])
```
**Métodos** integrados   
    
**`index():`**
Para buscar un elemento y conocer su posición dentro de la tupla. Si no encuentra el elemento dentro de la tupla, devuelve un error
    
```python
tupla.index(8)
tupla.index("Hola")
tupla.index("otro")
```

**`count()`**: 
Cuenta el número de veces que aparece el elemento en la tupla

```python
tupla.count(8)
tupla.count("otro")
tupla = (8,5,8,2,8,3,8)
tupla.count(8)
```
Al ser inmutables, las tuplas no disponene de métodos para modificar su contenido
### <span style="color:gray">2.1.2 Conjuntos<span>
***
En python, un conjunto es una colección no ordenada de objetos únicos   

```python
conjunto = set() # creando  un conjunto vacío
print(conjunto)
conjunto = {1,2,3} # conjunto de tres elementos
print(conjunto)
conjunto = {1,2,3,1,2,3}
print(conjunto)
```

**Métodos** integrados     
    
**`add()`** y **`discard()`**: 
Los conjuntos son objetos mutables y podemos añadir o eliminar un elemento con estos métodos, indicando el elemento como argumento.

```python
s = {1, 2, 3, 4}
print(s)
s.add(5)
print(s)
s.discard(1)
print(s)
```
Los conjuntos son colecciones desordenadas, python gestiona de forma automática la posición de sus elementos en lugar de conservarlos en la posición que nosotros los añadimos.

```python
s.add("H")
print(s)
s.add("A")
print(s)
s.add("Z")
print(s)
```
pertenecia a un grupo con **in**

```python
grupo = {'Juan', 'María', 'Mario'}
'Juan' in grupo
'Paco' in grupo 
'Pa'
'Mario' in grupo
``` 

autoeliminación de elementos duplicados
```python
test = {'Héctor', 'Héctor', 'Héctor'}
test
```
    
Pasar de lista a conjunto y de conjunto a lista
Es muy útil para cuando queremos eliminar los elementos duplicados de una lista
```python
l = [1,2,3,3,2,1]
c = set(l)
print(c)
l = list(c)
print(l)
```
```python
l = [1,2,3,3,2,1]
# en una línea
l = list( set(l))
    print(l)
```

Podemos crear un conjunto con los caracteres de una cadena
```python
s = "Al pan pan y al vino vino"
set(s)
```

### <span style="color:gray">2.1.3 Diccionarios<span>
***
Los diccionarios se basan en una estructura mapeada donde cada elemento de la colección se encuentra identificado con una clave única

```python
conjunto = {}
print(conjunto)
type(conjunto)
```
Para cada elemento se define la estructura **clave:valor**
```python
colores = {"amarillo":"yellow", "azul":"blue"}
colores
```

Podemos añadir elementos sobre la marcha
```python
colores['verde'] = 'green'
colores
```
Consultamos los valore por la clave **`diccionario["clave"]`** y nos devuelve el valor correspondiente a esa clave
```python
colores['azul']
colores['amarillo']
```
Las claves también pueden ser números 
```python
numeros = {10:'diez', 20:'veinte'}
numeros[10]
```
Podemos modificar el valor a partir de la clave
```python
colores['amarillo'] = 'white'
colores
```
- La función **`del()`** en diccionarios
```python
del(colores['amarillo'])
colores
```

Podemos trabajar directamente con los registros
```python
edades = {'Hector':27,'Juan':45,'Maria':34}
print(edades)
edades['Hector'] += 1
print(edades)
edades['Juan'] + edades['Maria']
```

- Recorremos los elementos del diccionario con **'for ... in ...'**

```python
for edad in edades:
    print(edad) 
```
Pero esto me devuelve las claves. Para que me devuelva los valores:

```python
for clave in edades:
    print(edades[clave]) 
```

- el método **`items()`**     
Nos facilita la lectura **`clave valor`** de los elementos por que devuelve ambos valores en cada iteracción.
```python
for clave, valor in edades.items():
    print(clave, valor)
```
    
    
- **ejemplo:** Diccionarios y listas
    
Podemos crear nuestras propias estructuras avanzadas mezclando tipos de colecciones como diccionarios y listas. Mientras loa diccionarios manejan las propiedades individuales de los registros, las listas nos permiten manejarlos todos en conjunto.
```python
personajes = [] #lista vacía
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Istar'} # un personaje
personajes.append(p) # añede el personaje a la lista de personajes
personajes
```
```python
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p) #añadimos otro personaje
personajes
```
```python
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p) #añadimos otro personaje
personajes
```
```python
for p in personajes:
    print(p["Nombre"], p["Clase"], p["Raza"])
```
### <span style="color:gray">2.1.4 Pilas y colas con listas <span>
***
- **Las pilas** son colecciones de elementos ordenados que únicamente permiten dos acciones:   
    - Añadir un elemento a la pila
    - Sacar un elemento de la pila   
    
 La peculiaridad es que el último elemento en entrar es el primero en salir. Estructura LIFO (_last In First Out_)

Para incluir los elementos usamos **`append()`**

```python
pila = [3,4,5]
pila.append(6)
pila.append(7)
pila
```

Para sacar un elemento de la pila usamos  **`pop()`**   
```python
pila.pop()
pila
```
**`pila.pop()`** nos extrae el último elemento de la pila y lo borra, si queremos trabajar con el debemos guardarlo en una variable.
```python
n = pila.pop()
print(n)
print(pila)
```
Si hacemos **`pila.pop()`** de una lista vacía, nos devuelve un error.
```python
pila.pop()
pila.pop()
pila.pop()
pila.pop()
```

- **Las colas** son colecciones de elementos ordenados que únicamente permiten dos acciones:
    - Añadir un elemento a la cola
    - Sacar un elemento de la cola   
La peculiaridad es que el primer elemento en entrar es el primero en salir. Estructura FIFO (_First In First Out_)    

Para trabajar con colas importamos la librería **_deque_**
```python
from collections import deque
```
Podemos crear una cola vacía
```python
cola = deque()
cola
```
o crear una cola con elementos pasandole una lista al crearla
```python
cola = deque(['Hector','Juan','Miguel'])
cola
```
también podemos usar el método **`append()`**
```python
cola.append("Maria")
cola.append("Pedro")
cola
```
para sacar los elementos de la cola usamos **`popleft()`**
```python
cola.popleft()
cola
```
si queremos trabajar con el elemento que sale de la cola, debemos almacenarlo en una variable.
```python
p = cola.popleft()
print(p)
print(cola)
```
si hacemos **`popleft()`** de una cola vacía nos devuelve un error
```python
cola.popleft()
```
    
### <span style="color:gray">2.1.4 Ejercicios complementarios <span>
***

**1) Realiza un programa que siga las siguientes instrucciones:**
- Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
- Crea un conjunto llamado administradores con los administradores Juan y Marta.
- Borra al administrador Juan del conjunto de administradores.
- Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
- Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
> Los conjuntos se pueden recorrer dinámicamente  utilizando el bucle for de forma similar a una lista. También cuentan con el método **`discard(elemento)`** que sirve para borrar un elemento

```python 

    
    
```

**2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:**
- El caballero tiene el doble de vida y defensa que un guerrero.
- El guerrero tiene el doble de ataque y alcance que un caballero.
- El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
- Muestra como quedan las propiedades de los tres personajes.


```python 

    
    
```

    
**3) Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad)   
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?**

>Para ordenar automáticamente una lista podemos utilizar el método **`sort()`**   
    
```python
    
    
    
    
    
    
    


    
    
```
