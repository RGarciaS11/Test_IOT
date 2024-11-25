#*******************************#
#                               #
# Test IOT Modificado           #
# Conjetura de Collatz          #
# Autor: Rubén García Saldívar  #
# Fecha: 24 - noviembre - 2024  #
#                               #
#*******************************#


### Cargamos todas las bibliotecas que usaremos en el programa
from Adafruit_IO import Client, RequestError, Feed  # Conexión con Adafruit IO
import time

### Configuramos la conexión con Adafruit IO
ADAFRUIT_IO_USERNAME = "IO_USERNAME"  
ADAFRUIT_IO_KEY = "IO_KEY"
# Creamos una instancia para que trabaje como el cliente de conexión
con_aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Creamos los feeds donde alojaremos los datos de las diferentes funciones
# Usamos el try - catch para crear el "feed" en caso de no existir

try: # Creamos el feed para los valores de la función seno
    collatz = con_aio.feeds('collatz')
except:
    feed = Feed(name = 'Collatz')
    collatz = con_aio.create_feed(feed)

c = int(input('Introduce un número para simular la congetura de Collatz: \t'))
con_aio.send_data(collatz.key, c)
time.sleep(2)

## Creamos un ciclo para enviar los datos a Adafruit IO
while c != 1:
    if c % 2 == 0:
        c = c / 2
    else:
        c = (3 * c) + 1

    con_aio.send_data(collatz.key, c)
    #  Debido a que la plataforma tiene una limitación en los datos que se pueden enviar por minuto,
    # definimos el tiempo adecuado para obtener la mayor cantidad de datos continuos, en este caso, como se 
    time.sleep(2)

