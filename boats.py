from random import randrange


def check_ok(boat, taken):

    for i in range(len(boat)):
        num = boat[i]
        if num in taken:
            boat = [-1]
            break
        if num < 0 or num > 99:
            boat = [-1]
            break
        elif num % 10 == 9 and i < len(boat) - 1:
            if boat[i + 1] % 10 == 0:
                boat = [-1]
                break

    return boat


def check_boat(b, start, dirn, taken):
    boat = []
    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)

    boat = check_ok(boat, taken)

    return boat


def create_boats():
    taken = []
    ships = []
    boats = [5, 4, 3, 3, 2, 2]
    for b in boats:
        print(f"Trying to find a position for the {b} length boat")
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1, 4)
            boat = check_boat(b, boat_start, boat_direction, taken)
        ships.append(boat)
        print(ships)
        taken = taken + boat

    return ships, taken


def show_board(taken):
    print("            BATTLESHIPS          ")
    print()
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in taken:
                ch = " x "
            row = row + ch
            place = place + 1
        print(x, " ", row)


boats, taken = create_boats()
print("All boats taken")
show_board(taken)
