from flask import Flask, render_template  #Importar libreria de flask

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

#Ej: crear una ruta que devuelva una lista de frutas, el path seria /frutas

@app.route("/frutas")
def lista_frutas():
    list_fruta = ['Platano', 'Fresa', 'Piña', 'Melon', 'Naranja']
    return list_fruta

@app.route("/nombre/<name>")  #Lo que esta entre <> lo toma como una variable que se puede usar mas abajo
def tunombre(name):
    return f"hola {name} como estas"

#Ej: realizar una ruta que devuelva el cuadrado de un numero dado, /numero/<parametro>

@app.route("/numero/<int:parametro>")  #Se pone <int:parametro> porque por default el parametro es tomado como str, por lo que daria error al hacer el cuadrado
def cuadrado(parametro):
    return f"El parametro de {parametro} es {parametro*parametro}"

#Ej: realizar una ruta que dinamicamente pueda solicitar o realizar operaciones de +, -, *, / segun los parametros pasados en la ruta (en una ruta se pueden pasar varios parametros)

@app.route("/calculadora/<operacion>/<int:n1>-<int:n2>")
def operacion(operacion, n1, n2):
    if operacion == "suma":
        return f"La {operacion} de {n1} + {n2} da {n1 + n2}"
    elif operacion == "resta":
        return f"La {operacion} de {n1} - {n2} da {n1 - n2}"
    elif operacion == "multiplicacion":
        return f"La {operacion} de {n1} x {n2} da {n1 * n2}"
    elif operacion == "division":
        return f"La {operacion} de {n1} / {n2} da {n1 / n2}"
    else:
        return "Elija una operacion valida entre suma, resta, multiplicacion o division, y utilice numeros enteros"

@app.route("/<dato>")
def mihtml(dato):
    list_fruta = ['Platano', 'Fresa', 'Piña', 'Melon', 'Naranja']
    return render_template("hola.html", variable = dato, frutas = list_fruta)  #Esto hace que el parametro <dato> se pase al html y se pueda usar ahi (en este caso linea 23 de hola.html)