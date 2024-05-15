import random
import tkinter as tk
from tkinter import messagebox, Scrollbar
from PIL import Image, ImageTk

class Character:
    def __init__(self, name, traits, image_path):
        self.name = name
        self.traits = traits
        self.image_path = image_path

class AvengersGuessWho:
    def __init__(self, characters):
        self.characters = characters
        self.questions_asked = set()
        self.character_images = {}
        self.user_character = None
        self.root = tk.Tk()  # Crear la ventana principal

    def ask_question(self):
        if len(self.characters) == 1:
            self.guess_character()
            return

        trait = self.get_random_trait()
        related_characters = [char for char in self.characters if trait in char.traits]

        if not related_characters:
            trait = self.get_random_trait()  # Retry with another trait if no character found
            related_characters = [char for char in self.characters if trait in char.traits]

        self.show_question_window(trait, related_characters)

    def get_random_trait(self):
        # Choose a random trait from all the characters
        all_traits = [trait for char in self.characters for trait in char.traits]
        return random.choice(all_traits)

    def show_question_window(self, trait, related_characters):
        if hasattr(self, "question_window") and self.question_window:
            self.question_window.destroy()

        self.current_related_characters = related_characters  # Guardar los personajes relacionados

        self.question_window = tk.Toplevel(self.root)
        self.question_window.title("Pregunta")

        question_label = tk.Label(self.question_window, text=f"¿El personaje en el que estas pensando tiene la característica '{trait}'?")
        question_label.pack()

        canvas = tk.Canvas(self.question_window)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(self.question_window, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0,0), window=frame, anchor="nw")

        for character in related_characters:
            image_label = tk.Label(frame, image=self.character_images[character.name])
            image_label.pack()

        frame.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))

        yes_button = tk.Button(self.question_window, text="Sí", command=lambda: self.process_answer(1))
        yes_button.pack(side=tk.LEFT, padx=10)

        no_button = tk.Button(self.question_window, text="No", command=lambda: self.process_answer(0))
        no_button.pack(side=tk.LEFT, padx=10)

    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def process_answer(self, answer):
        self.question_window.destroy()

        if answer == 1:
            self.characters = [char for char in self.characters if char in self.current_related_characters]
        else:
            self.characters = [char for char in self.characters if char not in self.current_related_characters]

        self.ask_question()  # Llamar a ask_question() para mostrar la siguiente pregunta

    def update_character_info(self):
        if not self.characters:  # Si no hay personajes restantes
            messagebox.showinfo("Adivinación", "No hay personajes que coincidan con esas características.")
            self.root.destroy()
            return

        # Mostrar las características de todos los personajes en la ventana principal
        characters_info = "\n".join([f"{char.name}: {', '.join(char.traits)}" for char in self.characters])

        if hasattr(self, "characters_label") and self.characters_label:
            self.characters_label.destroy()

        self.characters_label = tk.Label(self.root, text=characters_info, justify="left")
        self.characters_label.pack()

    def guess_character(self):
        if len(self.characters) == 1:
            guessed_character = self.characters[0]
            messagebox.showinfo("Adivinación", f"Adivino que tu personaje es {guessed_character.name}.")
            self.user_character = guessed_character
            self.root.destroy()
        elif len(self.characters) == 0:
            messagebox.showinfo("Adivinación", "No hay personajes que coincidan con esas características.")
            self.root.destroy()

    def load_images(self):
        # Cargar todas las imágenes
        for character in self.characters:
            image = Image.open(character.image_path)
            image = image.resize((150, 150), Image.LANCZOS)  # Usar LANCZOS para evitar la advertencia de deprecación
            self.character_images[character.name] = ImageTk.PhotoImage(image)

    def play(self):
        self.root.title("Adivina el Vengador")
        self.load_images()  # Cargar las imágenes antes de crear la ventana principal
        self.update_character_info()  # Mostrar las características de los personajes en la ventana principal
        self.ask_question()  # Mostrar la primera pregunta
        self.root.mainloop()

# Definir los personajes y sus características
iron_man = Character("Iron Man", ["ingeniero", "tiene un traje", "tiene inteligencia artificial", "líder", "inteligente", "ha usado las gemas del infinito", "rico""\n"], "iron_man.jpg")
thor = Character("Thor", ["dios", "ha usado un martillo/hacha", "tiene un traje", "fuerza sobrehumana", "tiene hermano malvado""\n"], "thor.jpg")
hulk = Character("Hulk", ["fuerza sobrehumana", "ha usado las gemas del infinito", "verde", "se transforma", "científico", "resistente a daños""\n"], "hulk.jpg")
black_widow = Character("Viuda Negra", ["espía", "acrobátic@", "combate cuerpo a cuerpo", "tiene un traje", "usa pistolas""\n"], "black_widow.jpg")
captain_america = Character("Capitán América", ["ha usado un martillo/hacha", "líder", "lucha por la justicia", "fuerza sobrehumana", "combate cuerpo a cuerpo", "tiene un traje", "usa escudo""\n"], "captain_america.jpg")
spider_man = Character("Spider-Man", ["tiene un traje", "joven", "combate cuerpo a cuerpo", "inteligente", "fuerza sobrehumana", "acrobatic@", "sentido arácnido""\n"], "spider_man.jpg")
thanos = Character("Thanos", ["titán", "ha usado un martillo/hacha", "ha usado las gemas del infinito", "fuerza sobrehumana", "inteligente", "busca el equilibrio""\n"], "thanos.jpg")

characters = [iron_man, thor, hulk, black_widow, captain_america, spider_man, thanos]

# Iniciar el juego
game = AvengersGuessWho(characters)
game.play()
