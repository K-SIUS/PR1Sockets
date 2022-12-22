# PR1Sockets
Práctica 1 sockets de la asignatura Arquitecturas avanzadas de Ander Sarrión Martín
Practica 1 Sockets. Ander Sarrión Martín

El resultado no es el esperado.
Las ejecuciones no finalizan y no parece contabilizar bien el sistema de ayudas.
Por otro lado, he logrado hacer el intercambio de mensajes de sockets utilizando una estructura similar a https://github.com/mittalmehul/socket-server
Tampoco creo que haya problemas en la clase Agente, pues todo el apartado de sincronismo, y tratamiento de ayudas tendría que ser implementado desde el servidor, y es ahí donde fracaso.


Problemas:
Por lo que he podido observar. Una conexión de stream TCP siempre envia los mensajes del buffer y tendría que implementar un método para descartar todos los mensajes mientras el servidor duerme, no he sido capaz. 

Tampoco he encontrado la manera de realizar sincronismo de peticiones entre agentes.
La semilla aleatoria funciona igual para todos los clientes nuevos conectados, es decir, mandan ayuda siempre a la vez.

También se me ha dificultado el hecho de conectar más de un agente al servidor, he tenido que hacer uso de un esqueleto nuevo al iniciado y hacer uso de la programación con hilos que hasta el momento pensé que no sería necesario.
