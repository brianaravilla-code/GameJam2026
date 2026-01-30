# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Mariana", color="#47dd4e")
define l = Character("Lunacello", color="#e68302")
define w = Character("Wyatt", color="#ffee00")
define j = Character("Jecyka", color= "#ff0000")
define c = Character("Cillstead", color= "#0000ff")
define host = Character("Sir Veridan, The Altruist")
define pov = Character("[povname]")

default mari_trust = 0
default luna_trust = 0
default wyatt_trust = 0
default jecyka_trust = 0
default cill_trust = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show johnsanili normal

    # These display lines of dialogue.

    e "So You've finally decided to show up"

    e "Come The others are waiting"

    e "Are you coming or not?"
    

    menu:
        "-follow her-":
            jump choices1_a
        "-stay there":
            jump choices1_b

    label choices1_a:
        scene bg bloodslash2_big
        with fade
        p "Your finally mine"
        p "HAHAHAHAHAHAHAHAHA"
        scene bg single_bedroom
        show phillow smile2
        with fade
        p "HEY! WAKE UP"

    return


    label choices1_b:
        scene bg office40
        show phillow angry 
        with fade
        p "OH"
        p "Why you stay?"


    return

    # This ends the game.

    return
