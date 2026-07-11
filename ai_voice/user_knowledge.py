from memory import guardar_perfil

def analizar_usuario(texto):

    texto_lower = texto.lower()

    if "me encanta" in texto_lower:

        interes = texto_lower.replace(
            "me encanta",
            ""
        ).strip()

        guardar_perfil("pasiones", interes)

        return True

    if "me cuesta" in texto_lower:

        debilidad = texto_lower.replace(
            "me cuesta",
            ""
        ).strip()

        guardar_perfil("debilidades", debilidad)

        return True

    if "soy bueno en" in texto_lower:

        fortaleza = texto_lower.replace(
            "soy bueno en",
            ""
        ).strip()

        guardar_perfil("fortalezas", fortaleza)

        return True

    if "quiero aprender" in texto_lower:

        interes = texto_lower.replace(
            "quiero aprender",
            ""
        ).strip()

        guardar_perfil("intereses", interes)

        return True

    return False