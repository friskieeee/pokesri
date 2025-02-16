import aiohttp  # A library for asynchronous HTTP requests
import random
import datetime

class Pokemon:
    pokemons = {}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.ability = None
        self.hp = random.randint(100, 1000)
        self.power = random.randint(10, 50)
        
    
        
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['forms'][0]['name']  # Returning a Pokémon's name
                else:
                    return "Pikachu"  # Return the default name if the request fails

    async def info(self):
        # A method that returns information about the pokémon
        if not self.name:
            self.name = await self.get_name()  # Retrieving a name if it has not yet been uploaded
            self.ability = await self.get_power()
        return f"The name of your Pokémon: {self.name} {self.ability}  {self.hp}  {self.power} "   # Returning the string with the Pokémon's name

    async def show_img(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['sprites']['front_default']  # Returning a Pokémon's name
                else:
                    return "gada fotonya"  # Return the default name if the request fails
    async def get_power(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['abilities'][0]['ability']["name"] # Returning a Pokémon's name
                else:
                    return "ga ada"  # Return the default name if the request fails
    async def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.current()  
        delta_time = datetime.timedelta(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {current_time+delta_time}"  
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Memeriksa apakah musuh adalah tipe data Wizard (merupakan instance dari kelas Wizard)
            chance = random.randint(1,5)
            if chance == 1:
                return "Pokémon Penyihir menggunakan perisai selama pertempuran!"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pelatih Pokemon @{self.pokemon_trainer} menyerang @{enemy.pokemon_trainer}\nkesehatan @{enemy.pokemon_trainer} sekarang menjadi {enemy.hp}"
        else:
            enemy.hp = 0
            return f"Pelatih Pokemon @{self.pokemon_trainer} mengalahkan @{enemy.pokemon_trainer}!"
class Wizard(Pokemon):

    def attack(self, enemy):
        return super().attack(enemy)
    async def feed(self, feed_interval = 10, hp_increase = 10 ):
        current_time = datetime.current()  
        delta_time = datetime.timedelta(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {current_time+delta_time}"  
class Fighter(Pokemon):
    def attack(self, enemy):
        superboost = random.randint(5,15)
        self.power += superboost
        result = super().attack(enemy)
        self.power -= superboost
        return result + f"\Pokémon Petarung menggunakan serangan super. Kekuatan yang ditambahkan adalah:{superboost} "
    async def feed(self, feed_interval = 20, hp_increase = 20 ):
        current_time = datetime.current()  
        delta_time = datetime.timedelta(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {current_time+delta_time}"  
        
