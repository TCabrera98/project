def obtener_respuestas_chatbot(pregunta):
    # Respuestas predefinidas del chatbot
    respuestas = {
        "¿Cuál es el horario de atención?": "Nuestro horario de atención es de lunes a viernes de 9 a 12:00 por la mañana y por la tarde de 4 a 7.30, y los sábados por la mañana.",
        "¿Cómo puedo contactar con ustedes?": "Puedes contactarnos al número de teléfono (XXX) XXX-XXXX o escribirnos a contacto@cabrerautomotores.com.",
        "¿Tienen autos disponibles?": "Sí, tenemos autos nuevos y usados seleccionados. Puedes verlos en nuestra página web.",
        "¿Aceptan permutas?": "Sí, aceptamos permutas de autos. ¡Contáctanos para más detalles!",
        "¿Financian los autos?": "Actualmente no ofrecemos financiamiento, pero puedes pagar en efectivo.",
        "¿Cómo puedo comprar un auto?": "El proceso es simple, solo elige el auto, contáctanos y nosotros te ayudaremos con todo el trámite.",
        "¿Tienen garantía los autos?": "Sí, todos nuestros autos tienen garantía.",
    }

    # Convertimos la pregunta a minúsculas para una mejor comparación
    pregunta_normalizada = pregunta.strip().lower()

    # Comprobamos si la pregunta está en las respuestas predefinidas
    return respuestas.get(pregunta_normalizada, "Lo siento, no entendí tu pregunta.")
