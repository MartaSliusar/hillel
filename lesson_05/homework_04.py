team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    for player in players:
        name = player["name"]
        age = player["age"]
        number = player["number"]
        print(f"name: {name}, age: {age},number: {number}")


def add_player(num: int, name: str, age: int) -> None:
    new_player = {"name": name, "age": age, "number": num}
    team.append(new_player)


def remove_player(players: list[dict], num: int) -> None:
    players_copy = players.copy()

    for player in players_copy:
        if player["number"] == num:
            players.remove(player)


def main():
    show_players(team)

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)
    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
