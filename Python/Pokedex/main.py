import requests
import json
import customtkinter as ctk
from PIL import Image
from io import BytesIO
from pathlib import Path
class PokemonNotFoundError(Exception):
    pass

class PokedexApp:
    def __init__(self):
        self.okno = ctk.CTk()
        self.okno.configure(fg_color="#0F172A")
        self.saved_pokemons = []
        self.json_path = Path(__file__).parent / "pokemon.json"
        with open(self.json_path, "r") as file:
             self.saved_pokemons = json.load(file)
        self.okno.title("Pokédex")
        self.okno.geometry("1200x900")
        self.title = ctk.CTkLabel(
            self.okno,
            text="POKÉDEX",
            font=("Arial", 28, "bold"),
            fg_color="transparent",
            text_color="#F5F0E6"
        )

        self.title.pack(pady=20)

        self.subtitle = ctk.CTkLabel(
            self.okno,
            text = "Discover your Pokémon",
            font = ("Arial", 16, "bold"),
            fg_color = "#0F172A",
            text_color = "#F5F0E6"
        )

        self.subtitle.pack(pady=20)


        self.search_input = ctk.CTkEntry(
            self.okno,
            width = 250,
            font = ("Arial", 14, "bold"),
            fg_color = "#1E293B",
            text_color = "#F5F0E6",
            corner_radius = 15
            )
        
        self.search_input.pack(pady=20)

        self.result = ctk.CTkLabel(
            self.okno,
            text = "Enter Pokemon Name",
            fg_color = "transparent",
            text_color = "#F5F0E6",
            font = ("Arial", 18, "bold")
        )

        self.result.pack(pady=15)

        self.search_input.bind("<Return>", self.search_pokemon)

        self.search_button = ctk.CTkButton(
            self.okno,
            command = self.search_pokemon,
            text = "Search",
            font = ("Arial", 25, "bold"),
            fg_color = "#A78BFA",
            text_color = "#F5F0E6",
            corner_radius = 15,
            hover_color = "#8B5CF6"
        )

        self.search_button.pack(pady=10)

        self.cards_frame = ctk.CTkScrollableFrame(
            self.okno,
            fg_color = "transparent",
            width = 1160,
            height = 450
        )

        self.cards_frame.pack(pady=25)

        self.show_cards()

    def search_pokemon(self, event = None):
        pokemon_name = self.search_input.get()
        pokemon_name = pokemon_name.lower()
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}", timeout = 5)
            if response.status_code == 404:
                raise PokemonNotFoundError("Pokemon Was Not Found")
        except requests.exceptions.RequestException:
            self.result.configure(text = "Connection error")
            return 
        except PokemonNotFoundError as error:
            self.result.configure(text = str(error))
            return
        if response.status_code == 200:
            data = response.json()
            pokemon_id = data["id"]
            pokemon_height = data["height"] * 10
            pokemon_weight = data["weight"] / 10
            pokemon_types = []
            for item in data["types"]:
                pokemon_types.append(item["type"]["name"])
            pokemon_types_text = ", ".join(pokemon_types)
            pokemon_data = {
                 "name": data["name"],
                 "id": pokemon_id,
                 "height": pokemon_height,
                 "weight": pokemon_weight,
                 "types": pokemon_types
            }

            already_saved = False

            for pokemon in self.saved_pokemons:
                if pokemon_id == pokemon["id"]:
                    already_saved = True

            if already_saved == False: 
                self.saved_pokemons.append(pokemon_data)
                with open("pokemon.json", "w") as file:
                    json.dump(self.saved_pokemons, file)
                self.show_cards()
            self.result.configure(text = "Pokémon: " + data["name"] + "\nID: " + str(pokemon_id) + "\nHeight: " + str(pokemon_height) + " cm" + "\nWeight: " + str(pokemon_weight) + " kg" + "\nType: " + pokemon_types_text)

        else:
            self.result.configure(text="Pokemon Was Not Found")

    def show_cards(self):
        for card in self.cards_frame.winfo_children():
            card.destroy()  

        row = 0
        column = 0
        
        for pokemon in self.saved_pokemons:
                self.card = ctk.CTkFrame(
                    self.cards_frame,
                    fg_color = "#1E293B",
                    width = 270,
                    height = 310,
                    corner_radius = 20
                )
    
                self.card.grid(row = row, column = column, padx=10, pady=5)
                self.card.pack_propagate(False)
    
                self.card_name = ctk.CTkLabel(
                    self.card,
                    text = pokemon["name"],
                    font = ("Arial", 20, "bold"),
                    text_color = "#F5F0E6",
                    fg_color = "transparent"
                )
    
                self.card_name.pack(pady=10)
    
                self.card_id = ctk.CTkLabel(
                    self.card,
                    text = "#" + str(pokemon["id"]),
                    font = ("Arial", 14),
                    text_color = "#94A3B8",
                    fg_color = "transparent"
                )
    
                self.card_id.pack(pady=5)
    
                image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon["id"]}.png"
                try:
                    image_response = requests.get(image_url, timeout = 5)
                    image_data = BytesIO(image_response.content)
                    pokemon_image = Image.open(image_data)
                except (requests.exceptions.RequestException, OSError):
                    pokemon_image = None

                if pokemon_image is not None:
                    self.card_image = ctk.CTkImage(
                            light_image = pokemon_image,
                            size = (140, 140)
                    )
        
                    self.card_image_label = ctk.CTkLabel(
                        self.card,
                        image = self.card_image,
                        text = ""
                    )
        
                    self.card_image_label.pack(pady=5)

                if column < 3:
                    column += 1
                else:
                    column = 0
                    row += 1

                self.remove_button = ctk.CTkButton(
                    self.card,
                    text = "Remove",
                    font = ("Arial", 12, "bold"),
                    fg_color = "#991B1B",
                    hover_color = "#B91C1C",
                    text_color = "#F5F0E6",
                    corner_radius = 15,
                    command = lambda pid=pokemon["id"]: self.remove_pokemon(pid)
                )

                self.remove_button.pack(pady=5)

    def remove_pokemon(self, pokemon_id):
        for pokemon in self.saved_pokemons:
            if pokemon_id == pokemon["id"]:
                self.saved_pokemons.remove(pokemon)
                break

        with open("pokemon.json", "w") as file:
            json.dump(self.saved_pokemons, file)
        self.show_cards()

    def start(self):
            self.okno.mainloop()


aplikace = PokedexApp()
aplikace.start()