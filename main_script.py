# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define m = Character("Mariana", color="#47dd4e")
define l = Character("Lunacello", color="#e68302")
define w = Character("Wyatt", color="#ffee00")
define j = Character("Jecyka", color= "#ff0000")
define c = Character("Cillstead", color= "#0000ff")

define host = Character("Sir Veridan, The Altruist")
define pov = Character("The [povname]")

default mari_trust = 0
default luna_trust = 0
default wyatt_trust = 0
default jecyka_trust = 0
default cill_trust = 0

image davidend = Movie(play="David.webm",size=(1920,1080),loop=False)
# The game starts here.

label start:
  

    scene bg black
    
    with dissolve
    play music "images/Roblox Meep City_ The Playground Theme (Day Time).mp3" volume 0.2
    show johnsanili normal
    with fade

    host "Ah finally you've arrived"

    host "Allow me to welcome you to this lovely Institute"

    host "Come The others are waiting"

    hide bg black

    show bg spawn behind johnsanili
    with fade

    show johnsanili normal at left
    with moveinleft

    host "Greetings everyone, our final associate has arrived!"
    
    show fhaeris annoyed at right
    with moveinright
    m "finally"

    host "Please come and sit, have you decided on a title yet?"

    label name:
    $ povname = renpy.input("Which title would you like to go by: The", length=32)
    $ povname = povname.strip()
    $ povname = povname.capitalize()
if povname == "Altruist":
    pov "Hello you may call me The [povname]"
    host "Haha. No, Try again"
    jump name
elif povname == "Scouter":
    pov "Hello you may call me The [povname]"
    host "Hehe Apologies but that title has been taken"
    jump name
elif povname == "Conductor":
    pov "Hello you may call me The [povname]"
    host "Woops but that title has been taken"
    jump name
elif povname == "Dungeon Master":
    pov "Hello you may call me The [povname]"
    host "Sorry but that title is in use"
    jump name
elif povname == "Coach":
    pov "Hello you may call me The [povname]"
    host "Ooh that's being used by someone else"
    jump name
elif povname == "Agent":
    pov "Hello you may call me The [povname]"
    host "Nope it's being used"
    jump name
elif povname == "David":
        with fade
        $ renpy.movie_cutscene("images/movies/david.webm") 
        return
elif povname == "Lucy":
        with fade
        $ renpy.movie_cutscene("images/movies/david.webm") 
        return
else:
    host "So now that's everyone accounted for"
    host "Welcome to the playground" 
    jump Meeting
    

label Meeting:
    host "First things first to discuss matters of payment"
    host "I'll gladly acce-"
    "*Ring Ring*{w} *Ring Ring* {w} *Ring Ring*"
    host "Excuse me I have to take this"
    host "Yes?{w} mhm mhm {w} Okay {w} Right away I'll be right there"
    host "Apologies, but I must go for a moment, there are pressing matters I must attend to"
    host "Please wait here while I have a few things sorted"

