import random

class Jugador:
    def __init__(self, nombre, equipo, posicion):
        self.nombre = nombre
        self.equipo = equipo
        self.posicion = posicion

# Lista inicial de jugadores de fútbol
jugadores = [
    Jugador("Lionel Messi", "Paris Saint-Germain", "Delantero"),
    Jugador("Cristiano Ronaldo", "Manchester United", "Delantero"),
    Jugador("Neymar Jr.", "Paris Saint-Germain", "Delantero"),
    Jugador("Kevin De Bruyne", "Manchester City", "Centrocampista"),
    Jugador("Robert Lewandowski", "Bayern Munich", "Delantero"),
    Jugador("Virgil van Dijk", "Liverpool", "Defensa"),
    Jugador("Kylian Mbappé", "Paris Saint-Germain", "Delantero"),
    Jugador("Sergio Ramos", "Paris Saint-Germain", "Defensa"),
    Jugador("Mohamed Salah", "Liverpool", "Delantero"),
    Jugador("Luka Modric", "Real Madrid", "Centrocampista")
]

def seleccionar_jugador(jugadores):
    return random.choice(jugadores)

def agregar_jugador():
    print("\n[+] AGREGAR JUGADOR: ")
    nombre = input("Nombre del jugador: ")
    equipo = input("Equipo del jugador: ")
    posicion = input("Posición del jugador: ")
    jugadores.append(Jugador(nombre, equipo, posicion))
    print("¡El jugador ha sido agregado a la base de datos!")

def encontrar_jugador(nombre_ingresado):
    for jugador in jugadores:
        if nombre_ingresado.lower() in jugador.nombre.lower():
            return jugador
    return None

def jugar_adivina_quien():
    print("\n=====================================")
    print(" Bienvenido a Adivina Quién - Futbol Edition!")
    print("=====================================")
    print(" Estoy pensando en un jugador de fútbol...")
    print(" ¿Puedes adivinar quién es?")
    jugador_secreto = seleccionar_jugador(jugadores)
    print("\nPista: Juega en el equipo", jugador_secreto.equipo)
    pista_utilizada = False
    while True:
        print("\n-------------------------------------")
        nombre = input("¿Quién crees que es el jugador?: ")
        jugador_adivinado = encontrar_jugador(nombre)
        if jugador_adivinado and jugador_adivinado.nombre.lower() == jugador_secreto.nombre.lower():
            print("\n¡Felicidades! ¡Has adivinado el jugador!")
            break
        elif jugador_adivinado:
            print("\nEl jugador que has adivinado está en la base de datos, pero no es el correcto.")
            if not pista_utilizada:
                print("Aquí tienes una pista adicional: juega en la posición de", jugador_secreto.posicion)
                pista_utilizada = True
        else:
            print("\nEl jugador que has adivinado no está en la base de datos.")
            opcion = input("¿Quieres agregar información sobre este jugador? (si/no): ")
            if opcion.lower() == 'si':
                agregar_jugador()

def aprender_informacion(jugadores):
    print("\n=====================================")
    print(" Información de Jugadores de Fútbol")
    print("=====================================")
    print("\nAquí tienes algunos jugadores y sus equipos:")
    for jugador in jugadores:
        print(f"Nombre: {jugador.nombre} | Equipo: {jugador.equipo} | Posición: {jugador.posicion}")

# Main
if __name__ == "__main__":
    jugar_adivina_quien()
    aprender_informacion(jugadores)
