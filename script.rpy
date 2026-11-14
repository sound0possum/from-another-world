
define mc = Character("Stacy", color="#F2A6C8")
define r = Character("Reon", color="#82B9F2")
define n = Character(None)
define w = Character("Witch", color="#B69BEB")

image medieval_3:
    "images/medieval_3.png"
    xysize (config.screen_width, config.screen_height)

image forest:
    "images/forest.png"
    xysize (config.screen_width, config.screen_height)

transform male_position:
    zoom 0.25
    xalign 0.7
    yalign 1.0

transform girl_position:
    zoom 0.5
    xalign 0.2
    yalign 0.9

transform crate_position:
    zoom 0.5
    xalign 0.1
    yalign 0.3

transform witch_position:
    zoom 0.5
    xalign 0.8
    yalign 0.9

transform smooth_enter_left:
    xalign -0.5
    alpha 0.0
    ease 0.8 xalign 0.2 alpha 1.0

transform smooth_enter_right:
    xalign 1.5
    alpha 0.0
    ease 0.8 xalign 0.8 alpha 1.0

transform subtle_breathing:
    yoffset 0
    ease 1.5 yoffset -3
    ease 1.5 yoffset 0
    repeat

transform witch_entrance:
    zoom 0.4
    xalign 0.8
    yalign 0.9
    alpha 0.0
    ease 0.8 alpha 1.0 zoom 0.5

label start:

    play music "audio/tuff music.mp3" fadein 3.0

    scene black
    with fade

    pause 0.8

    scene medieval_3
    with dissolve

    n " Several shipments have recently arrived from overseas. Wooden crates, barrels, and sacks of spices are scattered throughout the room."

    show male at male_position
    with moveinright

    r "Let's see... preserved meats, exotic spices, fabrics..."

    show sad girl at girl_position
    with dissolve

    n "Reon examines the inventory list before approaching a pirate who has a girl under capture hes made her a part of his crew"

    r "what is theis blasphemy that my eyes see how dare you have such a young women working on a damn pirate ship"

    show crate at crate_position
    with dissolve

    n " the pirates in shock at how frustrated the royalty is but he knows the royalty is curious as to where he procured her"

    r "release her AT ONCE OR I SHALL HAVE YOUR HEAD AT THE STAKE"

    with hpunch

    n " the pirates jump back in shock and release the girl at once ."

    hide crate
    with dissolve

    n " the girl once freed from the pirates runs towards reon"

    show sad girl:
        zoom 0.5
        xalign 0.2
        yalign 0.9
        ease 0.7 xalign 0.55
    with dissolve

    r "What in the...?! what have you done to this poor girl her hands are red and scarred"

    n "The girl looks up at him, tears streaming down her face."

    mc "thank you so much for saving me "

    r "its what a price would do dont worry lady"

    n "Reon quickly reaches for his sheath and removes the rope tied to his hands after drawing his dagger."

    r "Hold still. I'll get you out of here."

    mc " please do the pirates made me clean the ship all on my own"

    show sad girl:
        zoom 0.5
        xalign 0.55
        yalign 0.9
        ease 0.3 xalign 0.6

    n "Reon pulls her close to him , shes pale as a ghost her lips and fingertips a faint red from hunger"

    r " what in gods name happened to you how did you end up in the pirates shipment did they hurt you ?"

    n " reon exclaims surprised by the abusurdity of how a girl who seems like a noble ended up in the hands of pirates "

    mc " I-I WAS CAPTURED FORCED TO WORK AND TRAPPED AND FED SCRAPS FOR DAYS "

    r " calm down okay relax im a prince i wont hurt you me and my royal navy saved you from those wrethced pirates "

    mc " are you sure you wont harm me ?"

    r "i promise i wont "

    n " the pirates make a run for it trying to avoid legal trouble"

    r" explain to me at once why your with these pirates how did you get in their hands"

    mc" okay so this might be hard to take in okay but im not from this world i come from another world im like from a place thats far more advanced than yours "

    r" hmmm considering magic exists in this world that isnt the most suprising, go on"

    mc " im a scientist a article scientist to be precise i was part of an worldwide accident where the our collider got into a massive explosion of sorts we pushed the infrastructure too hard the particles started to fuse with one another essentially creating a fuision bomb , i expected to die but yet here i am alive and well well to an extent"

    mc" the pirates found me in the forest cold and shivereing they asked if i wanted to be a part of their crew i said yes expecting warmth and shelter yet they made me WORK LIKE A DOG DAY AND NIGHT "

    mc" i was on a routine ship but i guess your navy intercepted them to search their belonginrgs "

    n "reon cant belive himself all these words he's hearing he dosent know what any of them mean hadron colider ?"

    n " fuision bomb what in gods tarnation is she saying but he knows one thing for sure he needs to get her back to where ever she came from "

    r" so in conclusion you need to get to another dimension "

    mc" yes can you please please help me ?"

    r" dont worry sweetheart ill do whatever i can "

    show smile girl:
        zoom 0.5
        xalign 0.65
        yalign 0.9
        ease 0.5 xalign 0.6
    with dissolve

    mc " thank you so much i really appreiciate i really do "

    stop music fadeout 2.0

    pause 1.0

    scene forest
    with fade

    play music "audio/tuff music.mp3" fadein 3.0

    show male at male_position
    with dissolve

    show girl:
        zoom 0.5
        xalign 0.55
        yalign 0.9
        alpha 0.0
        ease 0.8 alpha 1.0

    n " the 2 of them make their way through a forest walking over rocks and twigs the air is humid wet and reeks of soil and earth "

    mc" why are we going through this it seems like a quite a dangerous path no ?"

    r" dont worry i have a freind who lives here and she can help "

    mc" whom "

    r" you dont need to ask me shes right there "

    pause 0.5

    show witch at witch_entrance

    pause 0.5
 
    w " hmm what brings you here reon and who might this girl be ? "
    r " shes a companion of mine you see shes not from this universe shes experienced a time warp basically i need you to send her back "
    hide witch 
    " the witch teleports away maintaing a safe distance from the girl "
    w " you know how dangerous that is harbouring someone from another dimension ?"
    r " im aware im just trying to get her back to her own universe "
    show smile witch : 
        zoom 0.5
        ease 0.5 xalign 0.2 yalign 0.9
    with dissolve
    w"hmmmm i see okay just drink this potion and you shal return to your own universe its as simple as that but this is only a one time favour reon never again "
    mc " well then reon thank you so much for your help i really appreciated it "


    hide girl 

    "she drinks the potion and fades away back into her own universe the end "

return
