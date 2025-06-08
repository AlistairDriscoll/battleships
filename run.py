def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Incorrect number, please try again")
            elif shot in guesses:
                print(
                    "you have already tried this number, please select another"
                    )
            else:
                ok = "y"
                break
        except ValueError:
            print("incorrect entry, please enter again")
    return shot


def show_board(hit, miss, comp):
    print("            BATTLESHIPS          ")
    print()
    print("     0  1  2  3  4  5  6  7  8  9")

    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "
            row = row + ch
            place = place + 1
        print(x, " ", row)


def check_shot(shot, boat1, boat2, hit, miss, comp):

    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)

    return boat1, boat2, hit, miss, comp


boat1 = [45, 46, 47]
boat2 = [6, 16, 26]
hit = []
miss = []
comp = []


for guess in range(10):
    guesses = hit + miss + comp

    shot = get_shot(guesses)
    boat1, boat2, hit, miss, comp = check_shot(
        shot, boat1, boat2, hit, miss, comp)
    show_board(hit, miss, comp)

    if len(boat1) < 1 and len(boat2) < 1:
        print("You've won!")
        break
print("Finished")
