# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Grob = Character("Grob")

label start:

    scene bg park1

    "You got a name?"

    $ player_name  = renpy.input("wats your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $player_name="John"

    $ player = Character(player_name)

    show male Sprite
    Grob "yoyo alt bra?"

    player "jada"

    Grob "Lol"

    return
