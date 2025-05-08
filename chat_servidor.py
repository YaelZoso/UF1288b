from flask import Flask, request, jsonify

app = Flask(__name__)

# lista para almacenar los mensajes
mensajes = []


@app.route("/enviar", methods=["POST"])
def enviar():
    # para que el cliente envie mensajes, 
    # recibe un JSON con el mensaje y el usuario
    datos = request.get_json()
    mensaje = datos.get("mensaje")
    usuario = datos.get("usuario")

    if mensaje and usuario:
        mensajes.append({
            "usuario": usuario,
            "mensaje": mensaje
        })
        # confirma que el mensaje fue recibido
        return jsonify({"estado": "mensaje recibido"})
    else:
        # devuelve error si faltan datos
        return jsonify({"error": "faltan datos"})

@app.route("/mensajes", methods=["GET"])
def obtener_mensajes():
    # devuelve la lista de mensajes en formato JSON
    return jsonify(mensajes)


if __name__ == "__main__":
    # ejecuta el servidor
    app.run(host="0.0.0.0", port=5000)
