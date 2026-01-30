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

image davidend = Movie(play="David.webm",size=(1920,1080),loop=False)
# The game starts here.

label start:
    play music "Roblox Meep City_ The Playground Theme (Day Time).mp3" volume 0.2

    scene bg black
    with dissolve

    show johnsanili normal
    with fade

    host "Ah finally you've arrived"

    host "Allow me to welcome you to this lovely Institute"

    host "Come The others are waiting"

    scene bg spawn
    with dissolve

    show johnsanili normal at left
    with moveinleft

    host "Greetings everyone, our final associate has arrived!"
    
    show fhaeris annoyed at right
    with moveinright
    m "finally"

    host "Please come and sit, have you decided on a title yet?"

    label name:
    $ povname = renpy.input("What is your name", length=32)
    $ povname = povname.strip()
    pov "Hello you may call me [povname]"
if povname == "The Altruist":
    host "Haha"
    host "No. Try Again"
    jump name
elif povname == "The Scouter":
    m "Tch. Already taken"
    jump name
elif povname == "The Conductor":
    l "I do believe if anyone deserves that title it should be me."
    jump name
elif povname == "The Dungeon Master":
    w "Hey Sorry but I got that."
    jump name
elif povname == "The Coach":
    j ""
    jump name
elif povname == "The Agent":
    c "Hmph, denied"
    jump name
elif povname == "David","Lucy":
        with fade
        $ renpy.movie_cutscene("images/movies/david.webm") 
        return
else:
    host "So now that's everyone accounted for"
    host "Welcome to the playground"    

       
