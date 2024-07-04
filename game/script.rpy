# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Grob = Character("Grob")
define Emma = Character("Emma")
define Daniel = Character("Daniel")
# Office
define Ava = Character("Ava")
define Ethan = Character("Ethan")

label start:

    scene bg park

    "You" "What was my name again?"

    $ player_name = renpy.input("What's your name?")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "John"

    $ player = Character(player_name)

    player "Right, it was %(player_name)s."

    "Do you prefer men or Men or women?"
menu:
        "Women":
            $ coworker = Ava
            $ fcoworker = True
            jump office

        "Men":
            $ coworker = Ethan
            $ fcoworker = False
            jump office

        "Non":
            jump end

label office:

    scene bg offis

    if fcoworker == True:
        show woman office brunet  passiv
    elif fcoworker == False:
        show male office silver passiv

    coworker "Are you lost?"

    player "I am new here."

    coworker "New hire? Welcome aboard!"

    player "Thanks. I'm still trying to find my way around."

    coworker "Understandable. This place can be a bit of a maze at first."

    player "Any tips for a newcomer?"

    coworker "Sure! First things first, the coffee machine in the break room is your best friend. Trust me."

    player "Good to know. Anything else?"

    coworker "The boss loves punctuality, so always be on time for meetings. And don't hesitate to ask if you need help with anything."

    player "I'll keep that in mind. Thanks for the advice."

    coworker "No problem. By the way, we have team lunches every Thursday. It's a great way to get to know everyone."

    player "Sounds great! I'll be there."

    coworker "Awesome. Well, I've got to get back to work, but it was nice meeting you, %(player_name)s."

    player "Nice meeting you too, %(coworker)s."

    coworker "See you around the office!"
# not speld checed
    "You continue your first day in the office."

    "After hours, you finish your first day and take your leave."

label street:

    scene bg caffestreet

    "You walk through the street after a long first day."

label end:

    "Thanks for playing"
    return
