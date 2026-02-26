def handle_message(texto):

    texto = texto.lower().strip()

    if texto in ["hola", "buenas", "buenos dias"]:
        return (
            "👋 Hola.\n\n"
            "Ahora puedo ayudarte a buscar:\n\n"
            "1️⃣ Número de póliza\n"
            "2️⃣ Nombre del cliente\n\n"
            "Escribe 1 o 2 para continuar."
        )

    if texto == "1":
        return "Por favor escribe el número de póliza."

    if texto == "2":
        return "Por favor escribe el nombre del cliente."

    return "No entendí tu mensaje. Escribe *hola* para comenzar."