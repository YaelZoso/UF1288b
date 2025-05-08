import requests

#direccion del servidor
SERVIDOR = "http://192.168.1.20:5000"

#solicita nombre de usuario
usuario = input("nombre de usuario: ")

#bucle para enviar mensajes
while True:
    texto = input("escribe un mensaje: ")

    if texto.lower() =="ver":
        #solicita los mensajes al servidor
        respuesta = requests.get(SERVIDOR + "/mensajes")
        mensajes = respuesta.json()

        #muestra mensajes uno por uno
        for mensaje in mensajes:
            print(f"{mensaje["usuario"]}: {mensaje[mensaje]}")
    else:
        #enviar mensaje al servidor
        detos = {"usuario": usuario, "mensaje": texto}
        respuesta = requests.post(SERVIDOR + "/enviar", json=datos)

        #muestra respuesta del servidor
        print(respuesta.json().get("estado", "error))