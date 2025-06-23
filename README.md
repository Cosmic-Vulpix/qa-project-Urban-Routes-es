# Proyecto 8 - Miguel Angel Ruiz Santana : 29no Grupo
Este proyecto cuenta con dos archivos principales: *main.py* y *data.py*. En data se encuentran los datos que utilizaremos en las pruebas.


El archivo *main.py* prueba varias funciones de la app Urban Routes:  
**1**.- Establecer una ruta  
**2**.- Seleccionar la tarifa "Comfort"  
**3**.- Agregar un número de teléfono  
**4**.- Agregar una nueva tarjeta  
**5**.- Escribir un mensaje al conductor  
**6**.- Agregar mantas y pañuelos  
**7**.- Agregar helados  
**8**.- Pedir taxi  
**9**.- Esperar a la información del conductor

## Estructura

El código se forma de dos clases UrbanRoutesPage, que tiene como atributos todos los elementos de la página y como métodos las funciones que interactuan con dichos elementos.  
La segunda clase es TestUrbanRoutes que es donde se encuentra el decorador del servidor para llamarlo en todas la pruebas que hagamos y también aquí se hacen las pruebas.

Los elementos de la página se buscan por sus localizadores, utilicé tres tipos: CSS_SELECT, CLASS_NAME, XPATH y ID.  

También se usaron intervalos de espera como time.sleep o *esperas implícita y explícitas* para hacer las pruebas más suaves y entendibles

## Correr las pruebas

Para empezar con lo bueno, dirígete a la clase TestUrbanRoutes del archivo 
*main.py*, ahí puedes correr las pruebas individualmente 
en el botón "play" del lateral izquierdo de cada 
prueba, si quieres hacerlo por función inserta 
breakpoints haciendo click en los números de las líneas de código 
en las que quieras pausar y corre en modo depuración(el del bichito) 
haciendo click derecho en el botón "play".  
O bien puedes correr todas la pruebas seguidas en el botón
"play" de la parte superior de la ventana de Pycharm (De igual manera puedes
entrar en modo depuración en el botón "bug").

#### Gracias, y buena suerte C: