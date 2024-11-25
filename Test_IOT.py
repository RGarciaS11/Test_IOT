#*******************************#
#                               #
# Test IOT                      #
# Autor: Rubén García Saldívar  #
# Fecha: 24 - noviembre - 2024  #
#                               #
#*******************************#


### Cargamos todas las bibliotecas que usaremos en el programa
from Adafruit_IO import Client, RequestError, Feed  # Conexión con Adafruit IO
import math # Biblioteca de funciones matemáticas
import time # Biblioteca para funciones que requieran el uso de una variable que dependa del tiempo

### Definimos algunas constantes que usaremos en el código
PI = math.pi        # Constante pi
f1 = PI / 90.0     # Constante para cambiar valores de grados a radianes
f2 = f1 * 2.0       # Relación de variación de frecuencias entre las funciones 

### Configuramos la conexión con Adafruit IO
ADAFRUIT_IO_USERNAME = "IO_USERNAME"  
ADAFRUIT_IO_KEY = "IO_KEY"
# Creamos una instancia para que trabaje como el cliente de conexión
con_aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Creamos los feeds donde alojaremos los datos de las diferentes funciones
# Usamos el try - catch para crear el "feed" en caso de no existir

try: # Creamos el feed para los valores de la función seno
    seno = con_aio.feeds('seno')
except:
    feed = Feed(name = 'Seno')
    seno = con_aio.create_feed(feed)

try: # Creamos el feed para los valores de la función coseno
    coseno = con_aio.feeds('coseno')
except:
    feed = Feed(name = 'Coseno')
    coseno = con_aio.create_feed(feed)

try: # Creamos el feed para los valores de la función resultante de la suma
    resultado = con_aio.feeds('resultado')
except:
    feed = Feed(name = 'Resultado')
    resultado = con_aio.create_feed(feed)

## Creamos un ciclo para enviar los datos a Adafruit IO
for x in range(360):
    Sen = math.sin(f1 * x)      # Obtenemos el dato para la funcion "Seno"
    Cos = math.cos(f2 * x)      # Obtenemos el dato para la funcion "Coseno"
    Res = Sen + Cos             # Obtenemos el dato del resultado de sumar las dos funciones
    # Con las siguientes tres instrucciones enviamos los datos los feeds en Adafruit IO
    con_aio.send_data(seno.key, Sen)
    con_aio.send_data(coseno.key, Cos)
    con_aio.send_data(resultado.key, Res)
    #  Debido a que la plataforma tiene una limitación en los datos que se pueden enviar por minuto,
    # definimos el tiempo adecuado para obtener la mayor cantidad de datos continuos, en este caso, como se 
    time.sleep(6)

