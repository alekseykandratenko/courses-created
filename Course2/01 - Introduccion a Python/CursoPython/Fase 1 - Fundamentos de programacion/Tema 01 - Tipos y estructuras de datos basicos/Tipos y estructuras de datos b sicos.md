# Tema 1: Fundamentos de la programación

## <span style="color:green">1.1 Tipos y estructuras de datos básicos<span>


### <span style="color:gray">1.1.1 Números<span>
***
Python distingue entre enteros, números  de punto flotante y números complejos

|Clase|Tipo|Notas|Ejemplo|
|:----|:---|:----|:------|
|int|Números|Número entero con precisión fija|8|
|float|Números|Coma flotante de doble precisión|3.1415927|
|complex|Números|parte real y parte imaginaria j|(4.5 + 3j)|

#Utilizando el interprete como una **calculadora**

```python
3 + 2
3 - 2
3 * 2```

Para escribir **comentarios** en el código usamos "#" delante del texto

```python
#División
3 / 2
#Módulo
3 % 2
#Potencia
3 ** 2
```

Podemos realizar **operaciones más complejas**
```python
3 - 2 + 4 * 10
```

Las **variables**. Concepto fundamental en la programación en el cual se define un identificador y se le asigna un valor. Es un nombre que se refiere a un objeto que reside en la memoria. Cada variable debe tener un nombre único llamado identificador

```python
n = 3
n
n + 3
n * 3
m = 10
n * m
n = 10 
m = 15
n + m
```

```python
nota1 = 5
nota2 = 8
nota_media = (nota1 + nota2) / 2
nota_media
```



### <span style="color:gray"> 1.1.2 Textos - Cadenas de caracteres
***

**Cadenas cortas.** Son caracteres encerrados entre comillas simples (') o dobles (")
```python
'Hola mundo'
"Hola mundo"
```

**Cadenas largas.** Son caracteres encerrados entre grupo comillas triples (''') o dobles (""").
```python
'''Así podemos escribir un parrafo completo, 
con varias líneas'''
```
Texto que **incluye comillas**
```python
'Este texto incluye unas "" '
'Esta "palabra" se encuentra escrita entre comillas'
"Esta \"palabra\" se encuentra escrita entre comillas"
'Esta \'palabra\' se encuentra escrita entre comillas'
```

La función **print()** nos permite mostrar el valor de una cadena u otros valores/variables por pantalla.

```python
"una cadena"
"otra cadena"
"otra cadena más"
```

```python
print("una cadena")
print("otra cadena")
print("otra cadena más")
```

Acepta **caracteres especiales** como las tabulaciones **\t** o los saltos de línea **\n**
```python
print("un texto \tuna tabulación")
print("un texto \nuna nueva línea")
```

Para evitar los caracteres especiales debemos indicar que una cadena es **_raw_**

```python
print("C:\nombre\directorio")
print(r"C:\nombre\directorio")
```

Podemos usar la tiple comilla para cadenas multilínea
```python
print("""Una línea
otra línea
otra línea \tuna tabulación""")
```

También es posible asignar una cadena de caracteres a una variable y después emprimir la cadena en pantalla
```python
c = "Esto es una cadena \n con dos líneas"
c
print(c)
```

**Operaciones con cadenas**
Una de las operaciones más utilizadas con las cadenas es la concatenación

- **suma de cadenas**
```python
c + c
```
```python
print(c + c)
```
```python
s = "Una cadena" "compuesta de dos cadenas"
print(s)
```
```python
c1 = "Una cadena "
c2 = "otra cadena "
print(c1 + c2 + "otra cadena más")
```

- **multiplicación de cadenas**
```python
diez_espacios = " " * 10
print(diez_espacios + "un texto a diez espacios")
```

_**Index**_ de cadenas.
Nos permiten posicionarnos en un caracter específico de una cadena. escribimos **a[i]** para posicionarnos en el carácter **i-ésimo** de la cadena **a***

|cadena|P|y|t|h|o|n|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
Index positivo|0|1|2|3|4|5|
Index negativo|-6|-5|-4|-3|-2|-1|

```python
palabra = "Python"
palabra[0]
palabra[3]
palabra[-1]
```
Si el índice se encuentra fuera del rango de la cadena nos devuelve un error
```python
palabra[99]
```

_**Slicing**_ de cadenas. Para acceder a un rango de caracteres de la cadena. Si queremos imprimir la subcadena **Py** 

```python
print(palabra[0:2])
print(palabra[2:])
print(palabra[:2])
```
Si no se indica el número de índice se toma por defecto el principio y el final (incluidos)
```python
print(palabra[:])
```
```python
palabra[:2] + palabra[2:]
```
```python
palabra[-2:]
```
Si se especifica un slicin fuera de rango simplemente se ignora el espacio vacío
```python
palabra[:99]
palabra[99:]
```
**Inmutabilidad** de las cadenas. Una propiedad de las cadenas es que son inmutables, no se pueden modificar. Si intentamos reasignar un carácter no nos dejará
```python
palabra[0] = "N"
```
Sin embargo, utilizando slicing y concatenación podemos generar nuevas palabras facilmente
```python
palabra = "N" + palabra[1:]
```
**Funciones** útiles para cadenas
Un ejemplo de función útil que soportan las cadenas es _**len()**_, que nos permite saber su longuitud (número de caracteres que contiene)
```python
len(palabra)
```

### <span style="color:gray">1.1.3 Listas
***
Una lista es una estructura de datos que puede almacenar distintos tipos de datos, llamados ítems, ordenados entre corchetes y separados por coma.
```python
lista = [4, "Una cadena", -15, 3.14, "otra cadena"]
```

**_Index_** y **_Slicing_** en cadenas 
```python
lista[0] #-index positivo
lista[-1] #-index negativo
lista[:2] #-slicing positivo
lista[-2:] #-slicing negativo
```

**Suma de listas**
Da como resultado una nueva lista que incluye todos los ítems
```python
lista1 = [1,2,3]
lista2 = [4,5,6]
lista1 + lista2
```
**Son mutables.** En las listas podemos modificar sus ítems utilizando _index_
```python
pares = [2,4,5,8,10]
pares[2] = 6
pares
```
O también podemos modificar varios ítems en conjunto usando _slicing_
```python
letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3]
letras[:3] = ['A', 'B', 'C']
letras
```
Asignar una lista vacía equivale a borrar los ítems de la lista o sublista
```python
letras[:3] = []
letras
letras = []
letras
```


**Funciones y métodos** para trabajar con listas
- **len():** Contar los elementos de una lista
```python
len(lista)
```
- **.append():** Añadir un elemento al final de una lista
```python
lista1.append(4)
```
- **.extend():** Añadir varios elementos al final de una lista
```python
lista2.extend([7,8,9])
```

**Listas anidadas.**
Podemos manioular fácilmente este tipo de estructura utilizando múltiples índices, como si nos refiriéramos a las filas y columnas de una tabla.
```python
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
```
```python
r[0] #-primera sublista
r[-1] #-última sublista
r[0][0] #-primer ítem de la primera sublista
r[1][1] #-segundo ítem de la segunda lista
r[-1][-1] #-último ítem de la última lista
```

### <span style="color:gray">1.1.4 Entrada/lectura por teclado
***
**La función _input()_** nos permite obtener texto escrito por teclado. Al llegar a la función el programa se detiene esperando que se escriba algo.

```python
entrada = input()
entrada
print(entrada)
```
Podemos especificar un texto para que se muestre en pantalla
```python
entrada = input("Introduce un valor: ")
```
La función input, de forma predeterminada, convierte la entrada en una cadena, aunque escribamos un número.
```python
valor + 100
```
Si queremos que python interprete la entrada como un número entero, debemos utilizar la función **_int()_** de la siguiente manera:
```python
entrada = int(input("Introduce un valor: "))
entrada + 100
```
Si el usuario escribe un número decimal, la función **_int()_** producirá un error. Para que Python interprete la entrada como un número decimal, se debe utilizar la función **_float()_** de la siguiente manera:
```python
entrada = float(input("Introduce un valor: "))
entrada + 100
```
Pero si el usuario escribe un número entero, la función **_float()_** no producirá un error, aunque el número se escribirá con parte decimal (.0):
```python
entrada = float(input("Introduce un valor: "))
entrada
```

### <span style="color:gray"> 1.1.5 Ejemplo: Primer programa
***
Intenta deducir que hace este programa

```python
lista1=[]
lista2=[]
n = 0
while n < 10:
    if (n % 2) == 0:
        lista1.append(n)
    else:
        lista2.append(n)
    n = n + 1
print(lista1, lista2)
```

### <span style="color:gray"> 1.1.6 Ejercicios complementarios
***
1) Identifica el tipo de dato (int, float, string o list) de los siguientes valores
```python
"Hola Mundo"
[1, 10, 100]
-25
1.167
["Hola", "Mundo"]
' '
```

2) Determina mentalmente (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:

```python
a = 10
b = -5
c = "Hola "
d = [1, 2, 3]
```
```python
print(a * 5)
print(a - b)
print(c + "Mundo")
print(c * 2)
print(c[-1])
print(c[1:])
print(d + d)
```

3) El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?
```python
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = numero_1 + numero_2 + numero_3 / 3
print("La nota media es", media)
```

4) A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota final. El problema es que cada nota tiene un valor porcentual:
- La primera nota vale un 15% del total
- La segunda nota vale un 35% del total
- La tercera nota vale un 50% del total   

Desarrollar un programa para calcular perfectamente la nota final

```python
nota_1 = 10
nota_2 = 7
nota_3 = 4

```
5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

>Ayuda: La función **_sum(lista)_** devuelve la suma de todos los elementos de la lista

```python
matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

```

6) Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:
- **Nombre Apellido** ha sacado un **Nota** de nota
> Ayuda: Para invertir el orden de una cadena rápidamente podemos hacerlo usando slicing, utilizando un tercer índice -1

```python
cadena = "zeréP nauJ,01"

```