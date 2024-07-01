# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Grob = Character("Grob")

label start:
    "snak snak snak"
    Grob "yoyo alt bra?"

    Grob "giga test Grob test hei på deg test etter rart merke"

    return

# label sprites:
#     Grob "but wait haha"

#     Grob "tehrs more"

#     Grob "mohahaha"
    
# label background:
    
#     Grob  "Lets go!!!"
#     scene bg park1

#     Grob "wat you want?"

# label choices:

#     define obidiant = false
#     Grob "can we stopp now?"
#     menu :
#         "Yes":
#             jump choices1_a
#         "No":
#             jump choices1_b

# label choices1_a:

#     $ obidiant = True
#     Grob "good"
#     jump choices1_common

# label choices1_b:
    
#     Grob "You wat skrub?"
#     jump choices1_common

# label choices1_common:
    
#     if obidiant:
#     Grob "Be gone"
#     else:
#     Grob "Dont desturb me!"