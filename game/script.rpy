# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Grob = Character("Grob")
define Emma = Character("Emma")
define Daniel = Character("Daniel")
# Offis
define Ava = Character("Ava")
define Ethan = Character("Ethan")

label start:

    scene bg park1

    "You" "Wat was my name agen?"

    $ player_name  = renpy.input("wats your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $player_name="John"

    $ player = Character(player_name)
    
    player "Right, it was %(player_name)s."
    
    show male Sprite
    Ethan "Are you lost?"

    player "I am new her"

    Ethan "new blood?"

    return
