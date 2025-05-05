import re


def obtener_respuestas_chatbot(pregunta):
    # Respuestas predefinidas del chatbot
    respuestas = {
        "horario": "Nuestro horario de atención es de lunes a viernes de 9 a 12:00 por la mañana y por la tarde de 4 a 7.30, y los sábados por la mañana.",
        "contacto": "Puedes contactarnos al número de teléfono (3329) 426-287 o escribirnos a cabrerautomotores@gmail.com.",
        "autos": "Sí, tenemos autos nuevos y usados seleccionados. Puedes verlos en nuestra página web o el stock físico en nuestros concesionarios.",
        "financian": "Actualmente no contamos con planes de financiación.",
        "ubicacion": "Nos encontramos en Avenida Sarmiento 1845 y Caseros 725, en la ciudad de San Pedro, Buenos Aires. Te esperamos en nuestros locales.",
    }

    # Normalizamos la pregunta: la convertimos a minúsculas, eliminamos caracteres extra
    pregunta_normalizada = pregunta.strip().lower()

    # Verificar si la pregunta coincide exactamente con una palabra clave
    if pregunta_normalizada in respuestas:
        return respuestas[pregunta_normalizada]

    # Definimos patrones de búsqueda más generales y flexibles
    patrones = {
        "horario": r"\b(horarios?|hora|tiempo|cuando|abren|abierto)\b",
        "contacto": r"\b(contacto?|comunicar|llamar|telefono|número|escribir|contactar|contactarlos)\b",
        "autos": r"\b(autos?|disponibles|vehículos?|tienen|stock|modelo)\b",
        "financian": r"\b(financian?|financiamento|financiación|financiacion|cuotas|plan de pago|planes)\b",
        "ubicacion": r"\b(donde|ubicación|dirección|encontrarlos?|encuentro|sucursal(es)?|están ubicados|ubico)\b",
    }

    # Iteramos sobre los patrones para ver si alguno coincide con la pregunta
    for clave, patron in patrones.items():
        if re.search(patron, pregunta_normalizada):
            # Usamos get para evitar KeyError
            return respuestas.get(clave, "Lo siento, no entendí tu pregunta.")

    return "Lo siento, no entendí tu pregunta."
