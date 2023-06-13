def contar_palabra(vector, palabra, indice=0, contador=0):
    if indice == len(vector):
        return contador
    elif vector[indice] == palabra:
        contador += 1
    return contar_palabra(vector, palabra, indice + 1, contador)
vector = ["Santiago", "Santiago", "Esteban", "Santiago", "Diego", "Luis"]
palabra = "Santiago"
resultado = contar_palabra(vector, palabra)
print(f"La palabra '{palabra}' aparece {resultado} veces en el vector.")
