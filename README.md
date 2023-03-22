# RETO 6


## Primer punto 

Dado la figura de la imagen, desarrolle:

![68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67](https://user-images.githubusercontent.com/124607325/226735474-d6f739ca-631b-4831-992c-63b1b035a493.png)

Para poder hallar el volumen y el área superficial de las imagenes de la figura se debera: 

1. Importar la funcion Math para poder usar la funcion math.pi (representa al numero pi (3.1415)
2. Se define cuatro funciones para calcular el volumen y área superficial de la esfera y el cono (se usan las formulas ya establecidas) , respectivamente. y en la funcion se podran variables que se pediran  y se remplazaran mas adelantee.

![Primer punto reto 6 1](https://user-images.githubusercontent.com/124607325/226743460-22ebb37c-0646-4c76-8b0a-8d57e583a14e.png)

(Se utiliza la condición if __name__ == "__main__": para indicar que el código debajo sólo se ejecutará si se está ejecutando el archivo directamente)

3. Con la funcion imput se pide ingresar los valores del radio de la esfera, el radio de la base del cono, y la altura del cono

![Primer punto reto 6 imprimir](https://user-images.githubusercontent.com/124607325/226757391-4fe1d2aa-20f1-492f-b584-6cba5490ba80.png)

4. Se utiliza cada una de las funciones previamente definidas para calcular el volumen y área superficial de la esfera y el cono, respectivamente, utilizando los valores ingresados por el usuario. Cada resultado se almacena en una variable diferente.
5. Se imprimaran los resultados del volumen y área superficial de la esfera y el cono


## Segundo Punto 
Dada la figura de la imagen desarrolle: 

![68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67](https://user-images.githubusercontent.com/124607325/226761470-1c312c29-8d81-4d7c-a1b9-0e9cc2a99faa.png)

1. se Importa el módulo math, el cual se utiliza para usar a la constante pi y la función exponencial.

2. se definen e dos funciones para poder calcular el area y perimetro, y tomaran como como entrada  r (radio del circulo), a y b(base y altura del rectangulo)

![Segundo punto 1](https://user-images.githubusercontent.com/124607325/226783460-a9cc38b6-9911-4d77-95bb-b8c91e1b9fd5.png)

3. En la funcion para calcular el perimetro y area del circulo  se usan las fórmulas  pi * r**2 para el area , y la fórmula 2 * pi * r  para el perimetro.

4. En la funcion para calcular el perimetro y area del circulo  se usan las fórmula a * b, para el area y la formula 2 * (a + b) para el perimetro.

(Se utiliza la condición if __name__ == "__main__": para indicar que el código debajo sólo se ejecutará si se está ejecutando el archivo directamente)

5. Se pide al usuario  con la función imput que ingrese los valores del radio del círculo, la base y la altura del rectángulo.

![segundo punto 2](https://user-images.githubusercontent.com/124607325/226783991-f85dbd46-56f7-445b-aa50-9e9e4d2e4dca.png)

6. Se llama a la función calcular_area_perimetro_circulo con los valores ingresados y se almacena el resultado en la variable resultado_circulo y se imprime el área y el perímetro del círculo, utilizando los valores almacenados en resultado_circulo.

7. Se llama a la función calcular_area_perimetro_rectangulo con los valores ingresados y se almacena el resultado en la variable resultado_rectangulo y se imprime el área y el perímetro del rectángulo, utilizando los valores almacenados en resultado_rectangulo.



## Tercer Punto 
 Función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
 
 para hallar esta funcion se debe: 
 
1. Se define una función llamada calcular_cantidad_carne que usa tres   entradas N, M, K. en ella se calcula la cantidad de kilos de carne que hay multiplicando el número de aves que hay por los kilos de que pesaria, N serian gallinas, M gallos y K pollitos . Estos valores se almacenan en variables separadas.

![Tercer punto 1](https://user-images.githubusercontent.com/124607325/226786330-7bd8c1e1-2f58-4f36-a231-1e044344baa1.png)

2. Para calcular la cantidad todal de kilos de carne de aves que hay se supan la cantidad de kilos obtenidos segun cada tipo de ave.

3. Se pide que se ingrese la cantidad de gallinas, gallos y pollitos  que se tienen  se almacenan y  se llama a la función calcular_cantidad_carne con estos valores como argumentos.

![tercer punto 2](https://user-images.githubusercontent.com/124607325/226786540-ae4d516f-52f8-43d1-9d88-242ecbbb8a89.png)

4. El resultado de la función se almacena en la variable resultado.

5. Y se imprime en la pantalla la cantidad de carne obtenida de cada tipo de ave, así como la cantidad total de carne.



## Cuarto Punto 
Hallar respuesta a el problema: 
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.


1. se define una función para calcular el total de la compra, que toma como entrada la cantidad de panes (P), la cantidad de leche (M), la cantidad de huevos (H) y el dinero que se lleva (B). Y con ellas se calcula el total de lo gastado en cada artículo, el total de la compra.

![Cuarto punto 1](https://user-images.githubusercontent.com/124607325/226789236-e801e391-d75c-49a5-af55-d528cd5bd2bd.png)

2. Se define una segunda función para calcular las vueltas o la deuda, que toma como entrada el total de la compra y el dinero que lleva el cliente, y determina si se tiene que recibir vueltas o si se tiene que pagar una deuda.

![Cuarto punto 2](https://user-images.githubusercontent.com/124607325/226789332-52d89f51-64b8-4ebb-b12f-77c86ae255d6.png)

3. Se pide ingresar la cantidad de panes, leche, huevos y dinero que lleva. Luego, se llama a la función calcular_total_compra() con los valores ingresados y se muestra por pantalla el costo de cada artículo y el total de la compra.

![Cuarto punto 3](https://user-images.githubusercontent.com/124607325/226789352-9782f22a-86ab-4f8a-8a1e-728201325410.png)

4. Finalmente, se llama a la función calcular_vueltas_o_deuda() con el total de la compra y el dinero que lleva el cliente, y se muestra por pantalla si el cliente debe recibir vueltas o si tiene que pagar una deuda.

![Cuarto punto 4](https://user-images.githubusercontent.com/124607325/226789366-42c8f85f-c636-4cb9-8a83-0d70a14e3893.png)



## Quinto Punto
Hacer un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

1. Se define una función para calcular el valor del prestamo, y se usan tres entradas  C, que es el valor del préstamo, I, que es la tasa de interés anual, y n, que es la cantidad de meses del préstamo. La función calcula el valor total del préstamo con interés compuesto. Y Se devuelve el valor calculado de Valor_Prestamo mediante la instrucción return.

![Quinto punto 1](https://user-images.githubusercontent.com/124607325/226791844-8de7dc0e-5a2d-4235-a19b-13be81a3ad8f.png)

2. En la sección if __name__ == "__main__":, se solicita ingresar el valor del préstamo C, la tasa de interés anual en decimal i, y la cantidad de meses del préstamo n.

3. Luego se llama a la función calcular_Valor_Prestamo con los parámetros C, i/12, y n. El valor de i/12 se utiliza para convertir la tasa de interés anual en tasa mensual.

![Quinto punto 2](https://user-images.githubusercontent.com/124607325/226791870-eedbca8d-ed1e-4059-b419-4ce7eae83d23.png)


4. Se imprime el resultado de la función calcular_Valor_Prestamo, que es el valor total del préstamo con interés compuesto.



## Sexto punto 
Hallar el número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.


1. Se define la función para calcular contagios que recibe dos entradas  C numero actual de contagiados  y D Días. Se calcula el número total de contagios proyectados  multiplicando el número actual de contagiados C por 2 elevado a la D, que representa el número de días a proyectar.

![Sexto punto 1](https://user-images.githubusercontent.com/124607325/226793116-dd90d291-1ccb-42e9-8a04-49bd05977121.png)

2. Se solicita ingresar el número actual de contagiados C y la cantidad de días a proyectar D.

![Sexto punto 2](https://user-images.githubusercontent.com/124607325/226793236-c96bd660-5118-4a40-bb8d-37466d9539e3.png)

3.Se llama a la función calcular_contagios pasando como argumentos los valores de C y D, y se guarda el resultado en la variable total_contagios. Y se imprime en pantalla el mensaje indicando el número total de personas contagiadas después de D días, el cual corresponde al valor de total_contagios.



## Septimo Punto 
1. Se define la función calcular_promedio que recibe cinco números de tipo float y devuelve el promedio de estos números.

![Promedio](https://user-images.githubusercontent.com/124607325/226794312-dd9d74ed-e122-4f40-bd33-f9f0a3e815ce.png)

2. Se define la función calcular_la_mediana que recibe cinco números de tipo float y devuelve la mediana de estos números.

![Mediana](https://user-images.githubusercontent.com/124607325/226794366-59cb280f-2083-477a-a931-951f4c544360.png)

3. Se define la función Calcular_el_promedio_multiplicativo que recibe cinco números de tipo float y devuelve el promedio multiplicativo de estos números.

![Promedio multiplicativo](https://user-images.githubusercontent.com/124607325/226794432-3cc0f9fe-b6c0-4fae-a1ad-46df5e487d8e.png)

4.Se define la función Numeros_ordenar_ascendente que recibe cinco números de tipo float y devuelve la lista de números ordenados de menor a mayor. Para esto se comparar dos números a la vez y, si el primero es mayor que el segundo, intercambiarlos de lugar. Este proceso se repite varias veces hasta que se logran ordenar los números.

![Resultados numeros forma ascendente](https://user-images.githubusercontent.com/124607325/226794462-d2bb95e6-093f-489f-847c-b2515e81b5a4.png)

5.Se define la función Numeros_ordenar_descendente que recibe cinco números de tipo float y devuelve la lista de números ordenados de mayor a menor. ´Para esto se  comparan dos números a la vez y, si el primero es menor que el segundo, intercambiarlos de lugar. Este proceso se repite varias veces hasta que se logra ordenarlos.

![Resultados forma descendente](https://user-images.githubusercontent.com/124607325/226795106-10d682bd-4db8-4bac-8f5c-987626931b30.png)

6. Se define la función Calcular_potencia que recibe cinco números de tipo float y devuelve la potencia del mayor número elevado al menor número.
![Potencia](https://user-images.githubusercontent.com/124607325/226795234-66010fdb-25ef-406a-85d8-8c3046ca61f3.png)


7. Se define la función calcular_raíz que recibe cinco números de tipo float y devuelve la raíz cúbica del menor número.
![Raiz cubica](https://user-images.githubusercontent.com/124607325/226795278-6bbea25a-aad7-4b07-876d-92244ff08c35.png)


8. En el bloque if __name__ == "__main__":, se le pide al usuario que ingrese cinco números de tipo float.
![Ingresar valores](https://user-images.githubusercontent.com/124607325/226795375-28e59581-3192-4100-a976-dc3ef400f469.png)

9. Luego, se llaman a las funciones definidas anteriormente: 
 
- Función calcular_promedio con los cinco números ingresados y se imprime el resultado.
 
 ![Resultado Promedio Multuplicativo](https://user-images.githubusercontent.com/124607325/226795621-87dfff4f-a838-4f2e-a267-5248cc9bdfcd.png)

 
- Función calcular_la_mediana con los cinco números ingresados y se imprime la mediana, así como la lista de números ordenados y la lista original.

![Resultado mediana](https://user-images.githubusercontent.com/124607325/226795593-bba43bb5-45cf-45a0-9a7d-32d26b1e7ef1.png)


- Función Calcular_el_promedio_multiplicativo con los cinco números ingresados y se imprime el resultado.

![Resultado Promedio Multuplicativo](https://user-images.githubusercontent.com/124607325/226795636-782baf0a-9351-4556-b186-c7f3ebb39297.png)

- Función Numeros_ordenar_ascendente con los cinco números ingresados y se imprime la lista de números ordenados de menor a mayor.

![Resultados numeros forma ascendente](https://user-images.githubusercontent.com/124607325/226795685-819818df-59f4-453b-a4e2-cfaf0fe41745.png)

- Función Numeros_ordenar_descendente con los cinco números ingresados y se imprime la lista de números ordenados de mayor a menor.

![Resultados forma descendente](https://user-images.githubusercontent.com/124607325/226795715-dcd8b614-0d71-4fd8-ba84-2f5c3646e520.png)


- Función Calcular_potencia con los cinco números ingresados y se imprime la potencia del mayor número elevado al menor número.

![Resultado potencia](https://user-images.githubusercontent.com/124607325/226795764-14a1ce40-63d2-48a9-a3b6-cb9849c76e76.png)


- Función calcular_raíz con los cinco números ingresados y se imprime la raíz cúbica del menor número.

![Resultado raíz](https://user-images.githubusercontent.com/124607325/226795801-e7ae2af0-e7f4-4a3e-a35b-6e44604fa842.png)

## Noveno y Decimo Punto
## ¿Qué es y cómo funciona pip en python?

PIP "Python Package Index" es un administrador de paquetes para Python, lo que significa que es una herramienta que se utiliza para instalar y administrar paquetes de software (bibliotecas, módulos, frameworks, etc.) escritos en Python.
pip es el acrónimo de "Python Package Index" y se utiliza para buscar, descargar e instalar paquetes de la base de datos PyPI (Python Package Index). PyPI es un repositorio de paquetes que contiene miles de paquetes que pueden ser utilizados por los desarrolladores de Python para agregar funcionalidades a sus proyectos de software.

### Comó funciona PIP en python 

Para usar PIP es neceario instalarlo en tu sistema si aún no se encuentra instalado. Para hacerlo, abre una terminal o línea de comandos y escribe:

    $ pip install pip

Al ya estar instalado, se peude empezar a instalar paquetes para python de la siguiente forma 

    $ pip install nombre_del_paquete

pip es un administrador de paquetes para Python, lo que significa que es una herramienta que se utiliza para instalar y administrar paquetes de software (bibliotecas, módulos, frameworks, etc.) escritos en Python para agregar funcionalidades a sus proyectos de software.

#### Para usar pip, primero debes instalarlo en tu sistema si aún no lo tienes instalado. Para hacerlo, abre una terminal o línea de comandos y escribe:
    $ pip install pip

Una vez que pip esté instalado, puedes utilizarlo para instalar paquetes de la siguiente manera:
    
    $ pip install nombre_del_paquete

Si necesitas desinstalar un paquete, puedes hacerlo utilizando el siguiente comando:
        
    $ pip uninstall nombre_del_paquete

Y se pueden ver los paquetes instalados en tu sistema utilizando:

     $ pip list

### Listado de módulos populares python 

- Matplotlib: eneran una gran variedad de gráficos de calidad para publicar online o en papel y sin emplear muchas líneas de código. 

      $ pip install matplotlib

Ejemplos : Diagramas de barras, histogramas, series temporales, espectros de potencia…

- TensorFlow: biblioteca popular de Python para aprendizaje automático y redes neuronales. Se utiliza para construir modelos de aprendizaje profundo y realizar tareas de procesamiento de imágenes, texto y voz.

      $ pip install tensorflow

- Pandas: Es una biblioteca para análisis de datos. Se utiliza para leer, manipular y analizar datos en diferentes formatos, como CSV, Excel y SQL. Para instalar Pandas, escriba en la línea de comandos:

      $ pip install pandas
  

- BeautifulSoup: Es una biblioteca popular de Python para análisis de HTML y XML. Se utiliza para extraer información de páginas web y realizar tareas de web scraping. Para instalar BeautifulSoup, escriba en la línea de comandos:

      $ pip install beautifulsoup4


- Flask: Es un popular marco de aplicaciones web de Python. Se utiliza para construir aplicaciones web y APIs. Para instalar Flask, escriba en la línea de comandos:

      $ pip install flask

- Django: Es otro popular marco de aplicaciones web de Python. Se utiliza para construir aplicaciones web y APIs más complejas que Flask. Para instalar Django, escriba en la línea de comandos:

     $ pip install Django
