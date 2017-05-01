''' El siguiente código de ejemplo simula una operación en un bucle
de 20 iteraciones al bloquear por una cantidad de segundos aleatorios
entre 1 y 5 utilizando la función time.sleep. '''

from tqdm import tqdm
from time import sleep
from random import randint
for i in tqdm(range(20)):
    sleep(randint(1, 5))

# Texto en pantalla al 40%:

''' |####------| 8/20 40% [elapsed: 00:23 left: 00:34, 0.35 iters/sec] '''

# Puede utilizarse la función trange como atajo para tqdm(range()):

    from tqdm import trange
    ...
    for i in trange(20):
        sleep(randint(1, 5))

''' Como toda barra de progreso, no es matemáticamente exacta,
pues el tiempo de proceso de cada una de las iteraciones del bucle
puede generar diversos intervalos. Aún así no deja de ser una buena opción. '''
