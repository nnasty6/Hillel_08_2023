# Псевдокод
from threading import Thread


def fetch_from_pokeapi(pokemon):
    ...


def save_to_database(data):
    pass


def process(pokemon):
    data = fetch_from_pokeapi(pokemon)
    save_to_database(data)


def main():
    user_input = input("enter pokemons list: ")
    pokemons = user_input.split(",")
    threads = [Thread(target=process, args=(pokemon,)) for pokemon in pokemons]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # poke = database.get(pokemons[0])
