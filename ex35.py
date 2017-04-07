from sys import exit

def gold_room():
    print "This room is full of gold, how much do u take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int (choice)
    else:
        dead("man, learn to type a number")
    if how_much < 50:
        print "you win"
        exit(0)
    else:
        dead("u gready")

def bear_room():
    print """ there is a bear here
            the bear has a bunch of huney
            how to move bear"""
    bear_moved = False

    while True:
        choice = raw_input("> ")
        if choice == "take honey":
            dead("eat you")
        elif choice == "taunt bear" and not bear_moved:
            print  "good job"
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "bye "
def  cthulu_room():
    print "flee or head"
    choice = raw_input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("really")
    else:
        cthulu_room()

def dead(why):
    print why, "good job"
    exit(0)

def start():
    print "left or right"
    choice = raw_input("> ")
    if "left" in choice:
        bear_room()
    elif "right" in choice:
        cthulu_room()
    else:
        dead("bye")

start()
