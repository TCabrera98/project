from django.shortcuts import render
from .utils import obtener_respuestas_chatbot


# Vista para manejar las preguntas del chatbot
def chatbot(request):
    pregunta = ""
    respuesta = ""

    if request.method == "POST":
        # Obtenemos la pregunta enviada por el usuaro
        pregunta = request.POST.get("pregunta", "")
        # Obtenemos la respuesta
        respuesta = obtener_respuestas_chatbot(pregunta)

    return render(request, "chatbot/chatbot.html", {
        "respuesta": respuesta,
        "pregunta": pregunta,
    })
