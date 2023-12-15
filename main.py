from flask import Flask  #Importar libreria de flask

app = Flask(__name__)  #El name es para pasarle el parametro por otro medio de entrada como la terminal

#Inicializar parametros para servidor (se hace por la terminal)
#En windows:
#set FLASK_APP=main.py

#Comando para ejecutar el servidor
#flask --app main run

#Todo se ejecuta en el servidor web propio del sistema operativo, en un puerto especifico:  * Running on http://127.0.0.1:5000    esto es lo mismo que http://localhost:5000
#A veces este puerto esta ocupado por otro programa. Para ejecutarlo en otro puerto hay que usar otro comando: flask --app main run -p 5002   Si se cambia hay que cambiarlo en las url para ejecutar las funciones

#Comando para ejecutar el servidor en modo debug y ejecutar cambios en tiempo real
#flask --app main --debug run

@app.route("/hola")  #El decorador sirve para llamar a la funcion que sigue luego de llamar al link con el / que defina. En este caso si pongo http://127.0.0.1:5000/hola va a llamar a la funcion hola_mundo
def hola_mundo():
    return "Hola mundo flask, esto es flask, hoy es viernes"