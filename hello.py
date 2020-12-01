from flask import Flask #importamos el objeto Flask

app = Flask(__name__) # creamos una instancia y le ponemos como nombre la del fichero
# Hay que definir los puntos de entrada: las peticiones a las que vamos a responder.
@app.route('/hello') # Esto es un "decorador" (@): ponemos la ruta o punto de entrada.
#El método 'route' comunica la petición 'hello' con la función hello_world

def hello_world():
    return 'Hola, mundo'
