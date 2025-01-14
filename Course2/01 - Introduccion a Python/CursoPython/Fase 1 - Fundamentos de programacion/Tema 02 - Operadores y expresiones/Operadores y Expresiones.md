# Tema 1: Fundamentos de la programación

## <span style="color:green">1.2 Operadores y Expresiones<span>


### <span style="color:gray">1.2.1 El tipo lógico <span>
***

Representa la mínima expresión racional representada por dos valores:   

- Verdadero (True)
- Falso (False)
    
```python
1 + 1 == 3
    ```
```python 
1 + 1 == 2
```
    
### <span style="color:gray">1.2.2 Operadores relacionales <span>
***
Los operadores relacionales sirven para comparar dos valores, dependiendo del resultado de la comparación se devolverá:
- Verdadero (True), si es cierta
- Falso (Fasle), si no es cierta

|Operación|Operador|Ejemplo|Significado|Resultado|
|:--------|:----:|:-------:|:----------|:--------|
|Igualdad|  ==  |  4 == 5 | 4 es igual a 5| False|
|Desigualdad| !=|5!=7    |5 es distinto de 7|True|
|Mayor    |>     | 8>15  |8 mayor que 215  |False|
|Mayor o igual| >=| 15>=8|15 es mayor o igual que 8|True|
|Menor    |<     |2<6    |2 es menor que 6|True
|Menor o igual que|<=|7<=7|5 es menor o igual que 7|True|

>No debemos confundir el operador de igualdad (==) con el de asignación (=)
    
También podemos comparar variables
    
```python
x1 = 8
x2 = 2
x2 < x1
```
       
```python
x1 != x2
```
```python
x1 ==4*x2
```
y otros tipos de datos como cadenas, listas, el resultado de algunas funciones o los propios tipos lógicos
- **Cadenas**   
       
```python
"Python" == "Python"
```
```python
"Python" != "Python"
```
```python
p = "Python"
```
```python
p[1] == "y"
```
```python
p[-1] == "n"
```
    
       
- **Listas**   
       
```python
l1 = [0,1,2]
l2 = [2,3,4]
l1 == l2
```
```python(
len(l1) == len(l2)
```
```python
l1[-1] == l2[0]
```   
- **Lógicos**
       
```python
True == True
```
```python
False == True
```
```python
False != True
```
```python
True > False
```
```python
False > True
```
> La representación aritmética de True y False equivalen a 1 y 0 respectivamente

```python
True * 3
False / 5
True * False
```

### <span style="color:gray">1.2.3 Operadores lógicos <span>
***
- **_Not_**: Negación. Niega un valor o expresión.
- **_And_**: Conjunción. Devuelve verdadero sólo cuando todas las condiciones son ciertas.
- **_Or_**: Disyunción. Devuelve verdadero si se cumple al menos una condición.

- **Not**
```python
not True
```
```python
not False
```
```python
not True == False
```

    
- **And**
    
```python
True and True
```
```python
True and False
```
```python
False and True
```
```python
False and False
```
```python
x = 8
x > 5 and x < 10
```
```python
p = "Python"
len(p) <= 6 and p[1] == "y"
```
- **Or**
    
```python
True or True
```
```python
True or False
```
```python
False or True
```
```python
False or False
```
```python
p = "Python"
p == "Py" or p == "thon"
```
```python
p = "Python"
p == "Py" or p == "thon" or p == "Python"
```

### <span style="color:gray">1.2.4 Expresiones anidadas <span>
***
En python tenemos un montón de expresiones distintas con las que podemos crear combinaciones entre ellas, esto es lo que se conoce como expresiones anidadas. Podemos definir grandes expresiones con multitud de operadores y operandos. 
    
```python
x1 = 8
x2 = 4
x1 * x2 - 2**x1 and not (x1 % x2) != 0
```
Las normas de precedencia nos enseñana como se resuelven las expresiones complejas con distintos tipos de operadores   

Cómo funcionan las **reglas de precedencia**:
1. Expresiones entre paréntesis
- Expresiones aritméticas por sus propias reglas:
    - exponentes
    - raíces
    - multiplicación
    - división
    - suma
    - resta
- Expresiones relacionales (de izquierda a derecha)
- Expresiones lógicas (de izquierda a derecha)
    
```python
```

### <span style="color:gray">1.2.5 Operadores de asignación <span>
***
Los operadores de asignación son aquellos quecon los que le asignamos un valor a una variable, lesta, ect.

|Operación|Operador|Ejemplo|Resultado|
|:--------|:------:|:-----:|:-------:|
|Asignación|  =  |  x1 = 2 | x1 vale 2|
|Suma en signación| += | x1 += 2 | Cada vez que se ejecuta esta instrucción se le suma 2 a x1|
|Resta en asignación| -= | x1 -=1  | Cada vez que se ejecuta esta instrucción se le resta 1 a x1|
|Multiplicación en asignación| *= | x1 *=3| Cada vez que se ejecuta esta instrucción se multiplica x1*3|
|División en asignación| /= | x1 /=5 | Cada vez que se ejecuta esta instrucción se divide x1 entre 5|
|Módulo en asignación| %= | x1 %= 2|Cada vez que se ejecute esta instrucción x1 se dividirá por dos y se le asignará el valor del resultado|
|Potencia en asignación| **= | x1 **=2 | Cada vez que se ejecute esta instrucción x1 se expondrá por 2 y se le asignará el valor del resultado|

```python
x = 7
x
```
```python
x += 8
x
```
```python
x -= 6
x
```
```python
x *= 2
x
```
```python
x /= 9
x
```
```python
x %= 2
x
```
```python
x **= 2
x
```
### <span style="color:gray">1.2.6 Ejemplo <span>
***
```python
n = 0
while n < 10:
    if (n % 2) == 0:
        print(n) 
    else:
        print(n)
    n += 1
```
¿Qué expresiones podemos identificar?

### <span style="color:gray">1.2.7 Ejercicios complementarios <span>
***
1) Realizar un programa que lea dos números por teclado y determine si los siguientes aspectos son Verdaderos o Falsos.
    - Si los dos números son iguales
    - Si los dos número son diferentes
    - Si el primero es mayor que el segundo
    - Si el segundo es mayor o igual que el primero
```python 
    
    
    
    
    
    
    
    
```
2) Utilizando operadores lógicos, determinar si una cadena de texto introducida por el usuario tiene una longuitud mayor o igual que 3 y a su vez es menor que 10
```python 
    
    
    
    
    
    
    
    
```
3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
- Guarda en una variable numero_magico el valor 12345679 (sin el 8)
- Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
- Multiplica el numero_usuario por 9 en sí mismo
- Multiplica el numero_magico por el numero_usuario en sí mismo
- Finalmente muestra el valor final del numero_magico por pantalla

