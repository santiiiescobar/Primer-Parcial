class Mision:
    def __init__(self, planeta, objetivo, recompensa):
        self.planeta = planeta
        self.objetivo = objetivo
        self.recompensa = recompensa
        
class Bitacora:
    def __init__(self):
        self.pila_misiones = []
    def agregar_mision(self, mision):
        self.pila_misiones.append(mision)
    def mostrar_planetas_visitados(self):
        planetas_visitados = []
        for mision in self.pila_misiones:
            planetas_visitados.append(mision.planeta)
        return planetas_visitados
    def calcular_recaudacion_total(self):
        total_recaudado = 0
        for mision in self.pila_misiones:
            total_recaudado += mision.recompensa
        return total_recaudado
    def buscar_mision_han_solo(self, objetivo):
        for i, mision in enumerate(self.pila_misiones, 1):
            if mision.objetivo == objetivo:
                return i, mision.planeta
        return None, None
bitacora_boba_fett = Bitacora()
bitacora_boba_fett.agregar_mision(Mision("Tatooine", "Bail Organa", 5000))
bitacora_boba_fett.agregar_mision(Mision("Naboo", "Padmé Amidala", 3000))
bitacora_boba_fett.agregar_mision(Mision("Coruscant", "Han Solo", 10000))
bitacora_boba_fett.agregar_mision(Mision("Kamino", "Jango Fett", 8000))

planetas_visitados = bitacora_boba_fett.mostrar_planetas_visitados()
print("Planetas visitados:")
for planeta in planetas_visitados:
    print(planeta)

recaudacion_total = bitacora_boba_fett.calcular_recaudacion_total()
print(f"Recaudación total: {recaudacion_total} créditos galácticos")

num_mision, planeta_captura = bitacora_boba_fett.buscar_mision_han_solo("Han Solo")
if num_mision:
    print(f"Han Solo fue capturado en la misión número {num_mision} en el planeta {planeta_captura}")
else:
    print("No se encontró la misión en la que se capturó a Han Solo")
