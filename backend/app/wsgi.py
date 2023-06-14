from flask import Flask, render_template, jsonify

ejerciso = {
    "id": 1,
    "text": "¿Por qué deberías aprender Python?",
    "choices": [
        "es muy poderoso",
        "es bueno para el mente",
        "mi mamá me dijo que es bueno",
        "es bueno para las pruebas de software.",
    ],
}


def create_app():
    app = Flask(__name__)

    return app


app = create_app()


@app.route("/", methods=["GET"])
def inicio():
    return render_template("inicio.html")


@app.route("/next_exercise", methods=["GET"])
def proximo_ejercicio():
    return jsonify(ejerciso)


if __name__ == "__main__":
    app = create_app()
    app.run()
