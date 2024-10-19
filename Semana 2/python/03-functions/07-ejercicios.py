# Palíndromo: Son aquellas palabras que leídas al revés tienen distinto significado. Por ejemplo: rotor. amar - rama.
# Realizar una función que te reconozca cuando una palabra/frase es palindromo

def no_space(texto):
    texto_retorno = ""
    for char in texto:
        if char != " ":
            texto_retorno += char
    return texto_retorno


def reverse(texto):
    texto_reves = ""
    for char in texto:
        texto_reves = char + texto_reves
    return texto_reves


def es_pal(palabra):
    palabra = no_space(palabra)
    cursor = len(palabra)
    texto_reves = reverse(palabra)
    return texto_reves.lower() == palabra.lower()


print(es_pal("Ammaa"))
