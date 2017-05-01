# Pythoniex, bot de trading configurable para Poloniex

El sistema funciona a base de un stop-loss de protección móvil, sin mostrar sus cartas al mercado, aunque también se puede configurar para que haga compras y ventas con la estrategia de ping-pong.

Es un bot de trading automático mediante línea de comandos escrito en Python 2.7, con una base de datos sqlite3. El código, los comentarios y la interfaz de línea de comandos están completamente en español.

Tiene advertencias de depuración para analizar fallos en el código. Úsalo con cuidado, pues no garantizo el 100% de fiabilidad en su funcionamiento (recomiendo trabajar con cable de red).

Si alguien quiere mejorar el código es libre de hacerlo y se puede utilizar el bot, aunque nunca venderlo. Yo he llegado a ganar entre un 5% a un 15% diario, aunque depende de tu suerte, la estrategia que uses y cómo lo configures.

Aquí ofrezco una guía paso a paso para comenzar a usarlo y sacarle el mayor rendimiento entendiendo cómo funciona, aunque la mejor documentación es el propio código.

### Instalación

1. [Instala Python 2.7](https://www.python.org/downloads/release/python-279/) si no lo tienes.

2. [Descarga la carpeta del proyecto desde Github](https://github.com/mondeja/pythoniex). Puedes guardarla donde quieras en tu ordenador.

3. Ve al archivo `config.py`, dentro de la carpeta modules y escribe la ruta a tu base de datos, el APIKey y el APISecret de tu cuenta de Poloniex. Abajo tienes más información sobre todos los parámetros configurables desde ese archivo.

4. Ve al archivo `setup.py`, dentro de la carpeta principal y ejecútalo. Te dirá que 'las tablas se han creado correctamente'. Si no es así revisa que tienes instalado sqlite3 y que hayas escrito bien la ruta a la base de datos. Si en algún momento borras la base de datos, vuelve a crearla ejecutando `setup.py`.

### Funcionamiento

Ahora, si corres el archivo `main.py`, empezará a ejecutarse. Lo primero que te pedirá es que insertes el mercado donde quieres tradear. Inserta STEEM, SBD, BTS o el mercado que quieras (no importa si lo escribes en minúsculas) y pulsa intro. Pythoniex sólo tradea en base al BTC.

Entonces te pedirá que insertes el rango mínimo de soporte. Si en este momento introduces `info` y pulsas intro, se abrirá una pestaña del navegador que te llevará a la página en Poloniex del mercado que has elegido. El rango de soporte es la zona donde intentará comprar Pythoniex. Debes introducir un precio mínimo y un precio máximo (siempre en BTC).

<center>http://www.siglo25.com/img/posts/pythoniex_1.png</center>

Luego introduce el rango de resistencia. Pythoniex no intentará vender en esa zona, simplemente es un indicador para que calcule los checkpoints. Si pulsas enter después de introducir el rango máximo de resistencia, te mostrará una serie de checkpoints. Estos son los precios en los que Pythoniex, si son superados, subirá el stop-loss móvil, teniendo en cuenta el porcentaje introducido en la variable `stop_loss_movil` en el archivo de configuración (ver abajo).

Para calcular los checkpoints, Pythoniex calcula primero la media del rango de soporte y luego la de resistencia. La diferencia entre esos dos precios los divide por el número de checkpoints introducidos en el archivo de configuración, entonces, partiendo de la media de soporte va introduciendo checkpoints hasta la media de resistencia. 

<center>http://www.siglo25.com/img/posts/pythoniex_2.png</center>

Después de esto te preguntará si quieres empezar el trade y, seguidamente, qué es lo que deseas hacer, si comprar, vender o dejar a Pythoniex elegir. Si lo dejas elegir Pythoniex comprobará si tienes de la moneda que has elegido, si no intentará comprar en rango de soporte. Si ya tienes, consultará si el precio actual es mayor que los checkpoints y, si es así, intentará vender.

### Configuración

En el archivo `config.py`, que se encuentra en la carpeta modules se encuentran los siguientes parámetros configurables. Edítalo a tu gusto. Los parámetros son:

- **keypublic** = El APIKey pública de tu cuenta de Poloniex (entre comillas).
- **keysecret** = La contraseña o APIKey secret de tu cuenta de Poloniex (entre comillas).
- **ruta_base_datos** = Es la ruta completa hacia la carpeta de tu ordenador donde se guardará la base de datos, por ejemplo: `'C:/User/Desktop/pythoniex/database/base_datos.db'` Fíjate que acaba en `base_datos.db`. 
- **enviar_mails_operacion** = Elige entre True o False si quieres que el bot te envíe un correo cada vez que venda o compre.
- **enviar_mails_checkpoint** = Elige entre True o False si quieres que el bot te envíe un correo cada vez que superes un checkpoint.
- **mail_to** = Indica al mail donde lo quieres enviar (entre comillas)
- **mail_from** = Indica el mail desde el cual lo quieres enviar (entre comillas). Recomiendo usar un mail el cual no utilices, así no pones en riesgo una contraseña valiosa.
- **contra** = Aquí la contraseña del mail desde donde envias los correos (entre comillas).
- **nombre** y **version** = Es algo puramente de estilo, puedes renombrar el bot como quieras
- **reiniciar** = Indica True o False si quieres que se reinicie el proceso de compra después de vender. La compra se hará en los márgenes de soporte.
- **comprar** y **vender** = Elige bids o asks en cada uno de los campos. Esto indica al bot si quieres comprar o vender en precios de compra o de venta. Por ejemplo, si colocas bids a compra, intentará comprar al precio de compra actual + 1 satoshi, pero si lo colocas en asks, comprará automáticamente a precio de mercado (ambos si se encuentra el precio en rango de soporte).
- **stop_loss** = El primer stop_loss de protección se coloca a un porcentaje por debajo del rango mínimo de soporte, indicado por un número que debes introducir en este campo.
- **numero_checkpoints** = Es el número de checkpoints que se colocan entre la media de los soportes y la media de las resistencias. Cuanto mayor sea el número, más cerca estarán entre sí y viceversa, dependiendo también de la diferencia entre los rangos.
- **stop_loss_movil** = Cada vez que el precio llega a un checkpoint superior, el bot calcula la diferencia entre el checkpoint anterior y el nuevo. De esa diferencia calcula un porcentaje representado por este número y sube el stop de protección al nivel del porcentaje. Introduce un número del 1 al 100.
- **espera** = Un número que representa la cantidad de segundos que transcurre el bot esperando, desde un intento de compra o de venta a otro. Si pones un número muy bajo corres el riesgo de que Poloniex banee tu IP, ya que sólo se permiten 6 órdenes por segundo.
- **min_btc** = Cantidad mínima en BTC que necesita Pythoniex para empezar el trading.

### Estrategias

- **Stop-loss móvil**: Compra en rango de resistencia y configura la cantidad de checkpoints, el stop-loss de protección y el porcentaje de subida del stop-loss móvil entre checkpoints. Hazlo con cabeza, teniendo en cuenta si vas a tradear a largo, medio o corto plazo y la volatilidad del mercado.
- **Ping-pong**: Compra a precio de compra y vende a precio de venta, coloca los checkpoints bien juntos y haz la variable reiniciar = True para que Pythoniex esté constantemente comprando y vendiendo. 

### Advertencias
Pythoniex sólo tradea con una moneda a la vez, e intentará comprar la mayor cantidad posible con respecto a la cantidad de BTC que tengas. Pythoniex no venderá si la venta no es rentable (considerando siempre que la comisión de compra es de un 0.25%), en ese caso cancelará la orden de venta esperará a que suba el precio.
Para un correcto funcionamiento no metas BTC y la moneda que compres a la vez en la cuenta de Poloniex. Recomiendo crear una cuenta de Poloniex única para el bot si ya tienes una.

Si te ha servido, puedes enviarme una donación a mi monedero Bitcoin, se agradece!
19Tx4p2T66pqqQSJCAPTz7ttgBDpw8caMR

Álvaro Mondéjar Rubio 18/12/2016
# pythoniex
