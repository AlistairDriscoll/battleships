def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Incorrect number, please try again")
            elif shot in guesses:
                print("you have already tried this number, please select another")
            else:
                ok = "y"
                break
        except:
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
        print(x," ",row)


hit = [21,22]
miss = [20,24,12,13]
comp = [23]

guesses = hit + miss + comp

shot = get_shot(guesses)
show_board(hit, miss, comp)