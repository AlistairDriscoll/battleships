import os
from random import randrange


def check_ok(boat, taken):
    boat.sort()
    for pos in boat:
        if pos in taken or pos < 0 or pos > 99:
            return None

    for i in range(len(boat) - 1):
        diff = boat[i + 1] - boat[i]
        if diff not in [1, 10]:
            return None

    for i in range(len(boat) - 1):
        if boat[i] % 10 == 9 and boat[i + 1] % 10 == 0:
            return None

    return boat


def check_boat(length, start, direction, taken):
    boat = []
    for i in range(length):
        if direction == 1:
            boat.append(start - i * 10)  # Up
        elif direction == 2:
            boat.append(start + i)  # Right
        elif direction == 3:
            boat.append(start + i * 10)  # Down
        elif direction == 4:
            boat.append(start - i)  # Left

    return check_ok(boat, taken)


def create_boats():
    ships = []
    taken = []
    boats = [5, 4, 3, 3, 2, 2]

    for b in boats:
        attempts = 0
        boat = None
        while boat is None:
            if attempts > 1000:
                raise Exception("Failed to place boat after 1000 attempts.")
            boat_start = randrange(100)
            boat_direction = randrange(1, 5)
            boat = check_boat(b, boat_start, boat_direction, taken)
            attempts += 1
        ships.append(boat)
        taken.extend(boat)

    return ships


def get_player_ship(length, taken):
    while True:
        ship = []
        print(f"Place your ship of length {length}:")
        for i in range(length):
            while True:
                try:
                    pos = int(input(f"Enter position {i+1} (0-99): "))
                    if pos < 0 or pos > 99:
                        print("Invalid position. Try again.")
                        continue
                    ship.append(pos)
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")
        ship = check_ok(ship, taken)
        if ship:
            taken.extend(ship)
            return ship
        else:
            print("Invalid ship placement. Try again.")


def create_player_ships():
    ships = []
    taken = []
    boats = [5, 4, 4, 3, 3, 2, 2]

    for b in boats:
        ship = get_player_ship(b, taken)
        ships.append(ship)

    return ships


def show_board(hit, miss, comp):
    print("            BATTLESHIPS          \n")
    print("     0  1  2  3  4  5  6  7  8  9")
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "
            else:
                ch = " _ "
            row += ch
            place += 1
        print(f"{x}  {row}")


def display_choices():
    """Displays choices for user to select in the menu"""

    print("Please press '1' for single player against the computer")
    print("\nPress '2' for a PVP game")
    print("\nPress 3 to view the rules")
    print("\nPress 4 to exit the game.")


def display_menu():
    """Displays menu for user"""

    choices = ["1", "2", "3", "4"]
    display_choices()

    choice = input("\nChoose an option here...")

    while choice not in choices:
        os.system("clear")
        print("Incorrect choice!\n")
        display_choices()
        choice = input("\nChoose an option here...")

    return choice


def display_rules():
    os.system("clear")
    print(
        """Battleships is a game of trying to sink your opponents ships before
        your opponent sinks yours! Each player has a ship that takes up five
        spaces on their board, and two ships that take up four spaces, three
        spaces and two spaces. The board consists of ten rows of ten and so is
        100 spaces in total and you will have to guess the coordinates of each
        ship. If the coordinates you guess make a hit then the space will be
        displayed as a 'o', a miss will be displayed as a 'x' and a sunken ship
        will be displayed as a 'O'. Each player is allowed 50 guesses and the
        first to sink all their opponents ship wins! You can either choose to
        play a two player game or a 1 player game against the computer."""
          )

    go_back_to_menu = input("\nNow please press 'b' to go back to the menu...")

    while go_back_to_menu.lower != 'b':
        print("Incorrect input!")
        go_back_to_menu = input(
            "\nNow please press 'b' to go back to the menu..."
            )


def player_vs_player():
    """Function called to do a player vs player game"""

    os.system("clear")
    print("You chose to do a player vs player game!")


def player_vs_computer():
    """Function called to do a player vs computer game"""

    os.system("clear")
    print("You chose to play against the computer!")


def main():
    print("Welcome to Battleships!")

    player_choice = display_menu()
    while int(player_choice) != 4:
        if int(player_choice) == 1:
            print("You chose to play the computer!")
            player_vs_computer()
        elif int(player_choice) == 2:
            player_vs_player()
        elif int(player_choice) == 3:
            display_rules()

        os.system("clear")
        player_choice = display_menu()


# Example setup usage
if __name__ == "__main__":
    main()
