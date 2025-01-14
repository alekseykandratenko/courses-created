# Tema 2: Manejo de datos y optimización

## <span style="color:green">2.2 Entradas y salidas de datos<span>

- **Entradas:** Forma de capturar información desde el exterior
- **Salidas:** Forma de presentar la información al exterior
    
### <span style="color:gray">2.2.1 Entradas<span>
***
- Entradas por teclado: la función **`input()`**

```python
decimal = float( input("Introduce un número decimal con punto: ") )
valores = []
print("Introduce 3 valores")
for x in range(3):
    valores.append( input("Introduce un valor >") )
```

- Uso de la **terminal** y el editor **Spyder**    
    
    - Podemos ejecutar un script desde la terminal del sistema. En windows debemos usar Anaconda Promot que es un CMD especial con el entorno de Anaconda.
    - Spyder es una de las herramientas incluidas en la suite de anaconda, se trata de un IDE (Integrated Development enviroment) para python.  
    
![Prompt](promt.png)   
    
![Spyder](spyder.png)

### <span style="color:gray">2.2.2 Scripts<span>
***
    
Un scripts es un fichero con un nombre propio que se ejecuta desde el intérprete de python. Se trata de un guión con instrucciónes en código que se ejecutan de arriba a abajo. En el momento de la ejecución pueden necesitart la entrada de información (argumentos)
    
- Ejecutar Scripts desde el sistema operativo
> Con la línea de comando en el directorio donde tengo el archivo.py, escribo:    **`python NombreScript.py`**
- Enviar datos al scripts (argumentos) desde la línea de comandos
> Para poder capturar los argumentos que se mandan desde la línea de comandos al script tenemos que importar la librería de sistemas llamada **`sys`** y con ella podremos interactuar con las distintas funcionalidades del sistema operativo. La función del sistema **`sys.argv`** nos devuleve una lista con los argumentos que le hemos pasado.


### <span style="color:gray">2.2.3 Salidas<span>
***

- La función **`print()`**    
La función print() es la forma general de mostrar información por pantalla. Generalmente podemos mostrar cadenas de texto y variables conjuntamente separándolos por comas.

```python
v = "otro texto"
n = 10
print("Un texto", v, "y un número", n)
```

- El método **`.format()`**    
Es una funcionalidad de las cadenas de texto que nos permite incluir información (variables) en una cadena cómodamente utilizando identificadores referenciados.

```python
c = "Un texto '{}' y un número '{}'".format(v,n)
c
```
también podemos referenciar a partir de la posición de los valores utilizando índices
```python
print( "Un texto '{1}' y un número '{0}'".format(v,n) )
```
o podemos utilizar un identificador con una clave
```python
print( "Un texto '{v}' y un número '{n}'".format(n=n,v=v) )
print("{v},{v},{v}".format(v=v))
```

Alinear texto
```python
print("{:>30}".format("palabra") )
print("{:30}".format("palabra"))
print("{:^30}".format("palabra"))
```

Truncar texto
```python
print("{:.5}".format("palabra"))
```

Alinear y truncar
```python
print( "{:>30.3}".format("palabra") )
```

Rellenar número enteros con espacios
```python
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
```

Rellenar números enteros con ceros
```python
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
```

Rellenar números lotantes con espacios
```python
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))
```

Rellenar números flotantes con ceros
```python
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))
```
    
### <span style="color:gray">2.2.4 Ejercicios complementarios<span>
***

**1) Formatea los siguientes valores para mostrar el resultado indicado:**
   
- "Hola Mundo" → Alineado a la derecha en 20 caracteres
- "Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
- "Hola Mundo" → Alineamiento al centro en 20 caracteres con - - truncamiento en el segundo carácter (índice 1)
- 150 → Formateo a 5 números enteros rellenados con ceros
- 7887 → Formateo a 7 números enteros rellenados con espacios
- 20.02 → Formateo a 3 números enteros y 3 números decimales

```python

    
    
```

**2) Crea un script llamado tabla.py que realice las siguientes tareas:**
- Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
- El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
- En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
- El script contendrá un bucle for que itere el número de veces del primer argumento.
- Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
- Dentro del segundo for ejecuta una instrucción ** print(" * ", end='')**, (end='' evita el salto de línea).
- Ejecuta el código y observa el resultado.

Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.
   
> Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo **`sys`** y su lista **`argv`**.   
    
```python
import sys
print(sys.argv) # argumentos enviados
# completar
    
```

**3) Crea un script llamado descomposicion.py que realice las siguientes tareas:**   
- Debe tomar 1 argumento que será un número entero positivo.
- En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.   
    
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:

 -  3647

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

-  0007   
- 0040    
- 0600    
- 3000

>Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa