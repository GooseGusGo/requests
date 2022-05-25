import requests

class Superhero:

    def __init__(self, name):
        self.name = name

    def get_id_superhero(self):
        url = f"https://superheroapi.com/api/2619421814940190/search/{self.name}"
        response = requests.get(url)
        id = response.json()["results"]
        return id[0]["id"]

    def get_int_superhero(self):
        url = f"https://superheroapi.com/api/2619421814940190/{self.get_id_superhero()}/powerstats"
        response = requests.get(url)
        stats = response.json()
        intelligence = stats['intelligence']
        return intelligence

def superhero_int_range(*heroes):
    for superhero in heroes:
        max_int = 0
        intelligence = int(superhero.get_int_superhero())
        if intelligence >= max_int:
            max_int = intelligence
            winner = superhero.name
    print(f"Самый умный супергерой - {winner} с интелектом - {max_int}")

if __name__ == '__main__':
    hulk = Superhero("Hulk")
    captain_america = Superhero("Captain America")
    thanos = Superhero("Thanos")
    superhero_int_range(hulk, captain_america, thanos)
