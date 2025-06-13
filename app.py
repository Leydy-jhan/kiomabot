from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def responder():
    mensaje = request.form.get('Body').lower()
    respuesta = MessagingResponse()
    mensaje_respuesta = respuesta.message()

    if "hola" in mensaje:
        mensaje_respuesta.body("¡Hola! Soy KiomaBot 👟 ¿Qué deseas hacer?\n1. Ver productos\n2. Hacer un pedido\n3. Hablar con un asesor")
    elif "1" in mensaje:
        mensaje_respuesta.body("👕 Polos dryfit\n🩳 Shorts deportivos\n👚 Conjuntos personalizados")
    elif "2" in mensaje:
        mensaje_respuesta.body("Por favor envíanos tu nombre completo, producto y talla 📦")
    elif "3" in mensaje:
        mensaje_respuesta.body("📞 Un asesor se comunicará contigo en breve.")
    else:
        mensaje_respuesta.body("Lo siento, no entendí. Por favor responde con 1, 2 o 3.")

    return str(respuesta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
