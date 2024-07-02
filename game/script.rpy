# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Grob = Character("Grob")
# Offis
define Ava = Character("Ava")
define Ethan = Character("Ethan")

label start:

    scene bg park1

    Ethan "You got a name?"

    $ player_name  = renpy.input("wats your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $player_name="John"

    $ player = Character(player_name)

    show male Sprite
    Ethan "Are you lost?"

    player "I am new her"

    Ethan "new blood?"

    return
