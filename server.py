
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    titulo = "Inicio"
    mensaje = "Bienvenido a la Biblioteca Universitaria"
    return render_template("index.html", titulo=titulo, mensaje=mensaje)


@app.route("/catalogo")
def catalogo():
    titulo = "Catálogo"
    mensaje = "Consulta los materiales disponibles en nuestra biblioteca."
    return render_template("catalogo.html", titulo=titulo, mensaje=mensaje)


@app.route("/servicios")
def servicios():
    titulo = "Servicios"
    mensaje = "Conoce los servicios de nuestra biblioteca."
    return render_template("servicios.html", titulo=titulo, mensaje=mensaje)


@app.route("/contacto")
def contacto():
    titulo = "Contacto"
    mensaje = "Aquí puedes encontrar nuestros medios de contacto."
    return render_template("contacto.html", titulo=titulo, mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True , port=5000)
