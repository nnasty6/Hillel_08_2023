from pprint import pprint as print

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    """This function should print all players to the client"""
    print(sorted(team, key=lambda item: item["number"]))


def add_player(num: int, name: str, age: int) -> None:
    """This function adds the new player."""
    for new_plaer in team:
        if new_plaer["number"] == num:
            print("The team can't have two identical numbers")
            break
    else:
        new_plaer = {"name": name, "age": age, "number": num}
        team.append(new_plaer)
        print(team)


def remove_player(players: list[dict], num: int) -> None:
    """This function removes the player by his/her number."""

    index = 0
    while True:
        if index >= len(players):
            break
        if players[index]["number"] == num:
            del players[index]
            index -= 1

        index += 1
    print(players)


def main():
    print("---Show all team")
    show_players(team)
    print("---Show team with new players")
    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    print("---Show team with deleted players")
    remove_player(players=team, num=17)
    print("---Show all team with changes")
    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
