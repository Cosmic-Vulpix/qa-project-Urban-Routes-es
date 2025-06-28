# Proyecto 8 - Miguel Angel Ruiz Santana : 29no Grupo
Este proyecto cuenta con cinco archivos: *data.py*, *Helpers.py*, *TestsUrbanRoutes.py*, *UrbanRoutes.py* y *WaitHelpers.py*

#### Data.py:
    En este archivo se guardan los datos que se ingresaran en las pruebas
#### Helpers.py:
    Aqui encontraremos el método que nos ayuda a interceptar el código SMS
#### TestUrbanRoutes.py
    El archivo *main.py* prueba varias funciones de la app Urban Routes:  
    1.- Establecer una ruta  
    2.- Seleccionar la tarifa "Comfort"  
    3.- Agregar un número de teléfono  
    4.- Agregar una nueva tarjeta  
    5.- Escribir un mensaje al conductor  
    6.- Agregar mantas y pañuelos  
    7.- Agregar helados  
    8.- Pedir taxi  
    9.- Esperar a la información del conductor
#### UrbanRoutes.py
    Este código contiene la clase los localizadores y los métodos para interactuar con la página.
#### WaitHelpers.py
    Contiene las esperas explicitas

## Estructura y tecnologías

El código en general se conforma de varias clases en diferentes archivos, todas son llamadas en el archivo
para las pruebas. 

Se puede destacar el uso de localizadores que, para su mejor versatilidad se usaron 4 tipos: CLASS_NAME, XPATH, ID y CSS_SELECTOR . Los localizadores son utilizados mediante funciones juntos que también hacen interacciones con ellos, como hacer click e introducir datos.

También hacen presencia las esperas explicítas e implícitas que nos ayudan que el sistema haga pausas en busca de elementos en carga, o como el exclusivo caso
de esperar un contador. Ya para las pruebas tenemos los assert, que son la válidaciones que estamos buscando en cada prueba

## Correr las pruebas

**Antes de empezar recuerda tener instalados los paquetes *pytest* y *selenium* en tu programa Pycharm***

    Considera que este proyecto fue diseñado solo para el navegador Chrome v138.07... por lo que deberás tenerlo instalado y actualizado
    a esa versión

Ahora sí con lo bueno, dirígete a la clase TestUrbanRoutes del archivo 
*TestUrbanRoutes*, ahí puedes correr las pruebas individualmente 
en el botón "play" del lateral izquierdo de cada 
prueba, si quieres hacerlo por función inserta 
breakpoints haciendo click en los números de las líneas de código 
en las que quieras pausar y corre en modo depuración(el del bichito) 
haciendo click derecho en el botón "play".  
O bien puedes correr todas la pruebas seguidas en el botón
"play" de la parte superior de la ventana de Pycharm (De igual manera puedes
entrar en modo depuración en el botón "bug").

#### Gracias, y buena suerte C: