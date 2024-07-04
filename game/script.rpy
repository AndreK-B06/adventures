# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Grob = Character("Grob")
define Emma = Character("Emma")
define Daniel = Character("Daniel")
define Isabella = Character("Isabella")
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
            $ coffeeworker = Isabella
            $ fcoworker = True
            $ fcoffeeworker = True
            jump office

        "Men":
            $ coworker = Ethan
            $ coffeeworker = Daniel
            $ fcoworker = False
            $ fcoffeeworker = False
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

    "You continue your first day in the office."

    "After hours, you finish your first day and take your leave."

label street:

    scene bg caffestreet

    "As you walk through the street after a long first day, your mind starts to wander."

    player "Wat a day"

    "you think to yourself."

    player "I didn't expect my first day at the new job to be so exhausting. I could really use a break, something to take my mind off things."

    "You glance around, noticing the usual hustle and bustle of the city."

    player "Maybe I should grab a coffee or a snack"

    "Just then, a colorful sign catches your eye: Café Purrfection Cat Café. A smile tugs at your lips."

    player "A cat café, huh? That sounds interesting. I haven't been to one of those before."

    player "Maybe some furry company is just what I need to unwind. Plus, I did always love cats. They're so calming."

label caffe:

    scene bg catecoffe

    if fcoworker == True:
        show woman catcaffe pink passiv
    elif fcoworker == False:
        show male catcaffe blond passiv

    coffeeworker "How can I help you?"

menu:
    "One coffee, please?":
        $ coworker_feling = "Normal" 
        jump caffe_normal_path

    "Wow, nice place. Can I get a coffee?":
        $ coworker_feling = "Love" 
        jump caffe_love_path
    
    "What do you think? I want a freaking coffee.":
        $ coworker_feling = "Anger"
        jump caffe_angry_path
    
label caffe_normal_path:

    scene bg catecoffe

    if fcoworker == True:
        show woman catcaffe pink eyesclosed
    elif fcoworker == False:
        show male catcaffe blond eyesclosed

    "dey nods and start prepering your coffee"
    
    coffeeworker "That wil be €4.20"

    jump end

label caffe_love_path:

    scene bg catecoffe

    if fcoworker == True:
        show woman catcaffe pink smug
    elif fcoworker == False:
        show male catcaffe blond eyesclosed

    coffeeworker "why thank you"

    jump end

label caffe_angry_path:

    scene bg catecoffe

    if fcoworker == True:
        show woman catcaffe pink angry
    elif fcoworker == False:
        show male catcaffe blond angry

    coffeeworker "Leve now"

    jump end

label end:

    scene bg sakuratree

    "Thanks for playing"
    return
