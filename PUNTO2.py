from collections import deque
avengers = [
    {
        "nombre_superheroe": "Capitan America",
        "nombre_personaje": "Steve Rogers",
        "grupo": "Avengers",
        "anio_aparicion": 1941
    },
    {
        "nombre_superheroe": "Iron Man",
        "nombre_personaje": "Tony Stark",
        "grupo": "Avengers",
        "anio_aparicion": 1963
    },
    {
        "nombre_superheroe": "Thor",
        "nombre_personaje": "Thor Odinson",
        "grupo": "Avengers",
        "anio_aparicion": 1962
    },
    {
        "nombre_superheroe": "Hulk",
        "nombre_personaje": "Bruce Banner",
        "grupo": "Avengers",
        "anio_aparicion": 1962
    },
    {
        "nombre_superheroe": "Black Widow",
        "nombre_personaje": "Natasha Romanoff",
        "grupo": "Avengers",
        "anio_aparicion": 1964
    },
    {
        "nombre_superheroe": "Hawkeye",
        "nombre_personaje": "Clint Barton",
        "grupo": "Avengers",
        "anio_aparicion": 1964
    },
    {
        "nombre_superheroe": "Sr. Fantastico",
        "nombre_personaje": "Reed Richards",
        "grupo": "Los cuatro fantásticos",
        "anio_aparicion": 1961
    },
    {
        "nombre_superheroe": "Mujer invisible",
        "nombre_personaje": "Susan Storm",
        "grupo": "Los cuatro fantásticos",
        "anio_aparicion": 1961
    },
    {
        "nombre_superheroe": "Antorcha Humana",
        "nombre_personaje": "Johnny Storm",
        "grupo": "Los cuatro fantásticos",
        "anio_aparicion": 1961
    },
    {
        "nombre_superheroe": "La Mole",
        "nombre_personaje": "Ben Grimm",
        "grupo": "Los cuatro fantásticos",
        "anio_aparicion": 1961
    },
    {
        "nombre_superheroe": "Black Cat",
        "nombre_personaje": "Felicia Hardy",
        "grupo": "",
        "anio_aparicion": 1979
    },
    {
        "nombre_superheroe": "Hulk",
        "nombre_personaje": "Bruce Banner",
        "grupo": "Avengers",
        "anio_aparicion": 1962
    },
    {
        "nombre_superheroe": "Rocket Racoonn",
        "nombre_personaje": "",
        "grupo": "Guardianes de la galaxia",
        "anio_aparicion": 1976
    },
    {
        "nombre_superheroe": "Loki",
        "nombre_personaje": "",
        "grupo": "",
        "anio_aparicion": 1962
    },
    {
        "nombre_superheroe": "Groot",
        "nombre_personaje": "",
        "grupo": "Guardianes de la galaxia",
        "anio_aparicion": 1960
    },
    {
        "nombre_superheroe": "Star-Lord",
        "nombre_personaje": "",
        "grupo": "Guardianes de la galaxia",
        "anio_aparicion": 1976
    },
    {
        "nombre_superheroe": "Gamora",
        "nombre_personaje": "",
        "grupo": "Guardianes de la galaxia",
        "anio_aparicion": 1975
    },
    {
        "nombre_superheroe": "Thanos",
        "nombre_personaje": "",
        "grupo": "avengers",
        "anio_aparicion": 1973
    },
    {
        "nombre_superheroe": "Spiderman",
        "nombre_personaje": "Peter Parker",
        "grupo": "",
        "anio_aparicion": 1962
    },
    {
        "nombre_superheroe": "Superman",
        "nombre_personaje": "Clark Kent",
        "grupo": "",
        "anio_aparicion": 1978
    },
]
encontrada = False
nombre_personaje = ""
for heroe in avengers:
    if heroe["nombre_superheroe"] == "Capitana Marvel":
        encontrada = True
        nombre_personaje = heroe["nombre_personaje"]
        break

if encontrada:
    print(f"Capitana Marvel - Nombre de personaje: {nombre_personaje}")
else:
    print("Capitana Marvel no se encuentra en la lista")
guardianes_de_la_galaxia = deque()
for heroe in avengers:
    if heroe["grupo"] == "Guardianes de la galaxia":
        guardianes_de_la_galaxia.append(heroe)

print(f"Hay {len(guardianes_de_la_galaxia)} superhéroes en el grupo 'Guardianes de la galaxia'.")

grupos = ["Los cuatro fantásticos", "Guardianes de la galaxia"]
for grupo in grupos:
    print(f"Superhéroes en el grupo '{grupo}':")
    for heroe in reversed(avengers):
        if heroe["grupo"] == grupo:
            print(heroe["nombre_superheroe"])
    print()

print("Superhéroes con nombre de personaje cuyo año de aparición es posterior a 1960:")
for heroe in avengers:
    if heroe["nombre_personaje"] != "" and heroe["anio_aparicion"] > 1960:
        print(heroe["nombre_superheroe"])

for heroe in avengers:
    if heroe["nombre_superheroe"] == "Vlanck Widow":
        heroe["nombre_superheroe"] = "Black Widow"
        break

lista_auxiliar = [
    {
        "nombre_superheroe": "Black Cat",
        "nombre_personaje": "Felicia Hardy",
        "grupo": "",
        "anio_aparicion": 1979
    },
    {
        "nombre_superheroe": "Hulk",
        "nombre_personaje": "Bruce Banner",
        "grupo": "Avengers",
        "anio_aparicion": 1962
    },
    {
        "nombre_superheroe": "Rocket Racoonn",
        "nombre_personaje": "",
        "grupo": "Guardianes de la galaxia",
        "anio_aparicion": 1976
    },
    {
        "nombre_superheroe": "Loki",
        "nombre_personaje": "",
        "grupo": "",
        "anio_aparicion": 1962
    },
]
for heroe_nuevo in lista_auxiliar:
    encontrado = False
    for heroe in avengers:
        if heroe["nombre_superheroe"] == heroe_nuevo["nombre_superheroe"]:
            encontrado = True
            break
    if not encontrado:
        avengers.append(heroe_nuevo)
letras_iniciales = ["C", "P", "S"]
print("Personajes que comienzan con C, P o S:")
for heroe in avengers:
    if heroe["nombre_personaje"] and heroe["nombre_personaje"][0] in letras_iniciales:
        print(heroe["nombre_personaje"])
