# DAY -------------------------------------------------------------------------------------------------------------------------------------------

screen kitchen_day:
    modal True

    add "images/backgrounds/kitchen.png"
    image "images/overlay/ui/morning.png"

    hbox:
        xalign 0.99
        yalign 0.01
        spacing 5 

        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/status_idle.png"
                hover "images/overlay/ui/status_hover.png"
                action [Show("status"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]
        
        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/tasks_idle.png"
                hover "images/overlay/ui/tasks_hover.png"
                action [Show("tasks"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    imagebutton:
        xalign 0.9
        yalign 0.2
        focus_mask True
        at six_percent
        idle "images/overlay/ui/artifact_idle.png"
        hover "images/overlay/ui/artifact_hover.png"
        action [Show("artifacts"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")] # TODO: Add artifact screen

    imagebutton:
        xpos 582
        ypos 454
        idle "images/overlay/ui/kitchen/cook_idle.png"
        hover "images/overlay/ui/kitchen/cook_hover.png"
        at hover
        action [Hide("kitchen_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("kitchen_button_interact_day")] # Kitchen

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/robin_room_idle.png"
                hover "images/overlay/house_icons/day/robin_room_hover.png"
                action [Hide("kitchen_day"), Show("robin_room_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/bathroom_idle.png"
                hover "images/overlay/house_icons/day/bathroom_hover.png"
                action [Hide("kitchen_day"), Show("bathroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/mc_room_idle.png"
                hover "images/overlay/house_icons/day/mc_room_hover.png"
                action [Hide("kitchen_day"), Show("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/lr_idle.png"
                hover "images/overlay/house_icons/day/lr_hover.png"
                action [Hide("kitchen_day"), Show("livingroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

label kitchen_button_interact_day:

    if robin_progression_level == 0 and key_task == 0:
        scene kitchen
        play sound error_001
        system "You should probably complete your tasks before using the kitchen."
        call screen kitchen_day
    
    if robin_progression_level == 0 and key_task == 1:
        scene kitchen
        call screen kitchen_cook_menu_day

    if robin_progression_level >= 1:
        scene kitchen
        call screen kitchen_cook_menu_day

# AFTERNOON -------------------------------------------------------------------------------------------------------------------------------------------

screen kitchen_afternoon:
    modal True

    add "images/backgrounds/kitchen.png"
    image "images/overlay/ui/afternoon.png"

    hbox:
        xalign 0.99
        yalign 0.01
        spacing 5 

        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/status_idle.png"
                hover "images/overlay/ui/status_hover.png"
                action [Show("status"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]
        
        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/tasks_idle.png"
                hover "images/overlay/ui/tasks_hover.png"
                action [Show("tasks"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    imagebutton:
        xalign 0.9
        yalign 0.2
        focus_mask True
        at six_percent
        idle "images/overlay/ui/artifact_idle.png"
        hover "images/overlay/ui/artifact_hover.png"
        action [Show("artifacts"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")] # TODO: Add artifact screen

    imagebutton:
        xpos 582
        ypos 454
        idle "images/overlay/ui/kitchen/cook_idle.png"
        hover "images/overlay/ui/kitchen/cook_hover.png"
        at hover
        action [Hide("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("kitchen_button_interact_afternoon")] # Kitchen
   
    # Robin
    imagebutton:
        xpos 32
        ypos 252
        focus_mask True
        idle "images/overlay/house_icons/afternoon/robin_idle.png"
        hover "images/overlay/house_icons/afternoon/robin_hover.png"
        action [Hide("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_kitchen_interact")]

    # ARTIFACT 2
    if not artifact2:
        imagebutton:
            xpos 1429
            ypos 367
            at artifact2_zoom
            idle "images/overlay/artifacts/artifact2_idle.png"
            hover "images/overlay/artifacts/artifact2_hover.png"
            action [SetScreenVariable("artifact2_moving", True), SetVariable("artifact2", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact2_moving:
        default artifact_image = "images/overlay/artifacts/artifact2_idle.png"
        image artifact_image at unlock_artifact2
        timer 0.9 action [Hide("artifact2_moving")] 

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/robin_room_idle.png"
                hover "images/overlay/house_icons/afternoon/robin_room_hover.png"
                action [Hide("kitchen_afternoon"), Show("robin_room_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/bathroom_idle.png"
                hover "images/overlay/house_icons/afternoon/bathroom_hover.png"
                action [Hide("kitchen_afternoon"), Show("bathroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/mc_room_idle.png"
                hover "images/overlay/house_icons/afternoon/mc_room_hover.png"
                action [Hide("kitchen_afternoon"), Show("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/lr_idle.png"
                hover "images/overlay/house_icons/afternoon/lr_hover.png"
                action [Hide("kitchen_afternoon"), Show("livingroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

label kitchen_button_interact_afternoon:

    if robin_progression_level == 0 and key_task == 0:
        scene kitchen
        play sound error_001
        system "You should probably complete your tasks before using the kitchen."
        call screen kitchen_afternoon
    
    if robin_progression_level == 0 and key_task == 1:
        scene kitchen
        call screen kitchen_cook_menu_afternoon

    if robin_progression_level >= 1:
        scene kitchen
        call screen kitchen_cook_menu_afternoon

# EVENING -------------------------------------------------------------------------------------------------------------------------------------------

screen kitchen_evening:
    modal True

    add "images/backgrounds/kitchen.png"
    image "images/overlay/ui/evening.png"

    hbox:
        xalign 0.99
        yalign 0.01
        spacing 5 

        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/status_idle.png"
                hover "images/overlay/ui/status_hover.png"
                action [Show("status"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]
        
        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/tasks_idle.png"
                hover "images/overlay/ui/tasks_hover.png"
                action [Show("tasks"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    imagebutton:
        xalign 0.9
        yalign 0.2
        focus_mask True
        at six_percent
        idle "images/overlay/ui/artifact_idle.png"
        hover "images/overlay/ui/artifact_hover.png"
        action [Show("artifacts"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")] # TODO: Add artifact screen

    imagebutton:
        xpos 582
        ypos 454
        idle "images/overlay/ui/kitchen/cook_idle.png"
        hover "images/overlay/ui/kitchen/cook_hover.png"
        at hover
        action [Hide("kitchen_evening"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("kitchen_button_interact_evening")] # Kitchen

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/robin_room_idle.png"
                hover "images/overlay/house_icons/evening/robin_room_hover.png"
                action [Hide("kitchen_evening"), Show("robin_room_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/bathroom_idle.png"
                hover "images/overlay/house_icons/evening/bathroom_hover.png"
                action [Hide("kitchen_evening"), Show("bathroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/mc_room_idle.png"
                hover "images/overlay/house_icons/evening/mc_room_hover.png"
                action [Hide("kitchen_evening"), Show("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/lr_idle.png"
                hover "images/overlay/house_icons/evening/lr_hover.png"
                action [Hide("kitchen_evening"), Show("livingroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

label kitchen_button_interact_evening:

    if robin_progression_level == 0 and key_task == 0:
        scene kitchen
        play sound error_001
        system "You should probably complete your tasks before using the kitchen."
        call screen kitchen_evening
    
    if robin_progression_level == 0 and key_task == 1:
        scene kitchen
        call screen kitchen_cook_menu_evening

    if robin_progression_level >= 1:
        scene kitchen
        call screen kitchen_cook_menu_evening

# NIGHT -------------------------------------------------------------------------------------------------------------------------------------------

screen kitchen_night:
    modal True

    add "images/backgrounds/kitchen_night.png"
    image "images/overlay/ui/night.png"

    hbox:
        xalign 0.99
        yalign 0.01
        spacing 5 

        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/status_idle.png"
                hover "images/overlay/ui/status_hover.png"
                action [Show("status"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]
        
        vbox:
            imagebutton:
                focus_mask True
                idle "images/overlay/ui/tasks_idle.png"
                hover "images/overlay/ui/tasks_hover.png"
                action [Show("tasks"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    imagebutton:
        xalign 0.9
        yalign 0.2
        focus_mask True
        at six_percent
        idle "images/overlay/ui/artifact_idle.png"
        hover "images/overlay/ui/artifact_hover.png"
        action [Show("artifacts"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")] # TODO: Add artifact screen

    if robin_progression_level >= 1 and key_task >= 2:
        # Robin
        imagebutton:
            xpos 667
            ypos 373
            focus_mask True
            idle "images/overlay/house_icons/night/robin_idle.png"
            hover "images/overlay/house_icons/night/robin_hover.png"
            action [Hide("kitchen_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_kitchen_night")]

    # ARTIFACT 4
    if not artifact4:
        imagebutton:
            xpos 123
            ypos 666
            at artifact2_zoom
            idle "images/overlay/artifacts/artifact4_idle.png"
            hover "images/overlay/artifacts/artifact4_hover.png"
            action [SetScreenVariable("artifact4_moving", True), SetVariable("artifact4", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact4_moving:
        default artifact_image = "images/overlay/artifacts/artifact4_idle.png"
        image artifact_image at unlock_artifact4
        timer 0.9 action [Hide("artifact4_moving")] 


    # ARTIFACT 10
    if not artifact10 and robin_progression_level >= 4:
        imagebutton:
            xpos 175
            ypos 560
            at artifact10_zoom
            idle "images/overlay/artifacts/artifact10_idle.png"
            hover "images/overlay/artifacts/artifact10_hover.png"
            action [SetScreenVariable("artifact10_moving", True), SetVariable("artifact10", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact10_moving:
        default artifact_image = "images/overlay/artifacts/artifact10_idle.png"
        image artifact_image at unlock_artifact10
        timer 0.9 action [Hide("artifact10_moving")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/robin_room_idle.png"
                    hover "images/overlay/house_icons/afternoon/robin_room_hover.png"
                    action [Hide("kitchen_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/robin_room_idle.png"
                    hover "images/overlay/house_icons/night/robin_room_hover.png"
                    action [Hide("kitchen_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/bathroom_idle.png"
                hover "images/overlay/house_icons/night/bathroom_hover.png"
                action [Hide("kitchen_night"), Show("bathroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/mc_room_idle.png"
                hover "images/overlay/house_icons/night/mc_room_hover.png"
                action [Hide("kitchen_night"), Show("mc_bedroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/lr_idle.png"
                hover "images/overlay/house_icons/night/lr_hover.png"
                action [Hide("kitchen_night"), Show("livingroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

# ROBIN INTERACTION -------------------------------------------------------------------------------------------------------------------------------------------

label robin_kitchen_night:
    scene kitchen_night_1
    "What's Robin doing in the kitchen this late?"
    menu:
        "What should I do?"

        "Approach Robin (1)":
            scene kitchen_night with dissolve
            show robin tank with dissolve
            pro "Hey Robin, grabbing a late-night snack?"
            show robin tank open at jumper
            robin "Eep!"
            "He looks startled, and really sweaty too..."
            pro "Whoa, you alright? You're super sweaty..."
            robin "Huh? Oh! Y-yea! I'm fine!"
            pro "You sure?"
            robin "Uh-huh! I-I'm just... uh..."
            robin "My fan stopped working!"
            show robin tank
            robin "Yea, my stupid old fan stopped working in my room and I was just grabbing a drink to cool off."
            pro "Oh... okay."
            pro "Do you want me to fix it for you? I could bring my toolbox over and see if I can get it working again."
            show robin tank open at jumper
            robin "U-um, no!"
            robin "No thank you, that's very kind of you though."
            hide robin with easeoutleft
            "He grabs his drink and speed walks back to his room."
            "His face looked incredibly red, and he looked really nervous..."
            pro "I wonder what he was really doing in there..."
            play sound positive_event_01
            system "{color=#bb0028}Desire increased by 5{/color}"
            $ desire += 5
            scene black with dissolve
            pause 0.5
            show prologue9 with dissolve
            pause 1.0
            jump day
        
        "Stare at Robin's ass (2)" if robin_progression_level >= 2:
            scene kitchen_night1 with dissolve
            "Look's like Robin is grabbing a snack or something..."
            "Fuck, his ass looks perfect."
            "The way those shorts hug his body is amazing."
            "I feel a little weird staring at him like this, but I can't help myself."
            play sound positive_event_01
            system "{color=#bb0028}Desire increased by 15{/color}"
            $ desire += 15
            scene black with dissolve
            pause 0.5
            show prologue9 with dissolve
            pause 1.0
            jump day
        
        "Surprise Robin (3)" if robin_progression_level >= 3:
            scene kitchen_night with dissolve
            pro "Look's like Robin is grabbing a snack or something..."
            pro "It would be really funny if I surprised him and spooked him a little, haha."
            scene kitchen_night2 with dissolve
            "I slowly approach Robin from behind."
            robin "..."
            "He has no idea I'm right behind him!"
            "Should I wait for him to turn around..."
            "Or maybe I should just grab his shoulders and yell boo!"
            robin "..."
            pro "Boo!"
            scene black with hpunch:
                zoom 1.1
            robin "AAH!"
            "He screams and whips around, running straight into me and taking me to the ground."
            pro "OW!"
            scene kitchen_night3 at slight_wobble with dissolve:
                zoom 2.5 xalign 0.5 yalign 0.5
                ease 3.0 zoom 1.02
            "Robin is laying on top of me."
            robin "Why'd you scare me like that!!"
            pro "I thought you'd just get a bit scared, not topple me to the ground!"
            robin "I-I'm sorry! I didn't mean to!"
            robin "I just got really scared and my body reacted!"
            robin "I'm so sorry!"
            "He looks really flustered and embarrassed."
            pro "It's okay, it was my fault for scaring you like that."
            robin "I-I'm sorry!"
            "I notice his bulge pressing against me."
            "I feel my face flush red."
            pro "Uhh... Robin?"
            pro "You're still on top of me..."
            robin "Oh! I'm so sorry!"
            scene black with dissolve
            "He quickly gets up and helps me to my feet, running back to his room right after."
            pro "Note to self: never surprise Robin again."
            play sound positive_event_01
            system "{color=#bb0028}Desire increased by 20{/color}"
            $ desire += 20
            scene black with dissolve
            pause 0.5
            show prologue9 with dissolve
            pause 1.0
            jump day
        
        "Fuck Robin (4)" if robin_progression_level >= 4:
            scene kitchen_night with dissolve
            pro "Look's like Robin is grabbing a snack or something in the kitchen."
            pro "Fuck, he looks so sexy right now..."
            scene kitchen_night2 with dissolve
            "I take off my pants and slowly approach Robin."
            play sound kitchen_night2 fadein 0.5 loop
            show penis with dissolve:
                zoom 1.0 xpos 797 ypos 793
                ease 1.0 yoffset -15
                ease 1.0 yoffset 15
                repeat
            "I start rubbing my cock on his ass."
            robin "O-oh!"
            pro "Sorry, did I startle you?"
            robin "Your rubbing your dick against me..."
            pro "I know..."
            pro "You just looked so good right now, I couldn't help but... tease you a little."
            robin "Hehe..."
            robin "Do you want me to help you take care of that?"
            pro "I mean... I thought I was laying on that pretty thick, but if you insist."
            stop sound fadeout 0.5
            scene black with dissolve
            "Robin pushes me onto the kitchen floor."
            robin "You ready?"
            pro "Oh, you're getting right into it huh..."
            play sound suck_2 fadein 0.5 loop
            scene kitchen_night4 with dissolve:
                xalign 0.5 yalign 0.5
                zoom 1.0
                ease 0.25 yalign 1.0 zoom 1.07
                ease 0.2 yalign 0.5 zoom 1.0
                repeat
            "He gets on his knees and takes my dick into his mouth, sucking and licking the head and shaft."
            pro "Oh god, Robin..."
            pro "Your mouth... it's so warm."
            robin "Mphm..."
            robin "You're so hard..."
            "His technique has gotten much better since our first time and he seems to be more confident, bobbing his head back and forth and teasing me with his tongue."
            pro "F-fuck..."
            pro "Keep going... don't stop...!"
            "He moans softly as he continues to suck and lick my cock."
            pro "Good boy..."
            robin "Mm..."
            pro "So good..."
            menu:
                "Continue":
                    stop sound fadeout 0.5
                    scene kitchen_night5 with dissolve
                    play sound slight_exertion_slow fadein 0.5 loop
                    "He pulls his mouth off of my dick."
            robin "Hehe, it's so big..."
            robin "I want you to fuck me with it..."
            pro "Oh, right here in the kitchen?"
            robin "Mhm..."
            robin "Lay me on the kitchen table and fill my femboy bussy..."
            pro "Wow, you're one horny boy..."
            robin "Hehe..."
            stop sound fadeout 1.0
            scene black with dissolve
            "Robin lays down on the kitchen table with his legs spread."
            play sound storybeat6_23 fadein 0.5 loop
            scene kitchen_night6 with dissolve:
                xalign 0.5 yalign 0.5
                zoom 1.0
                ease 0.2 yalign 1.0 zoom 1.07
                ease 0.15 yalign 0.5 zoom 1.0
                repeat
            "I slam my cock inside of him, the familiar feeling of his tightness and warmth enveloping my dick."
            robin "Ahn! Yess...!"
            "I begin to thrust back and forth, rocking the table as I pound into him."
            robin "Yes...! Yes...!"
            robin "Your dick feels so fucking good!"
            "Robin's ass bounces with every thrust, his body in rhythm with mine."
            robin "Don't stop... don't fucking stop!"
            pro "Fuck, your ass is so fucking tight!"
            robin "Ahn~!"
            robin "I'm so addicted to your dick!"
            pro "Do you like it when I fuck you like this Robin?"
            robin "YES!"
            robin "F-FUCK...!"
            robin "You're... you're... AHN!!"
            "I can feel Robin's hole tightening around my cock."
            pro "Are you reaching your limit?"
            robin "Mhm, but I'm trying to hold on for a bit longer!"
            pro "It's okay Robin, be a good boy and cum for me..."
            "I speed up my thrusts, slamming my dick into his prostate again and again."
            robin "AAAAAAAHN! FUCK! FUCK!"
            robin "I-I'm... I'm going to cum!"
            robin "Please, please, please, PLEASE!"
            pro "Fuck... I'm going to burst!"
            menu:
                "Cum":
                    pro "FUCK! I'M CUMMING!"
            show whiteflash zorder 50
            pause 1.0
            show whiteflash zorder 50
            pause 1.0
            show whiteflash zorder 50
            pause 1.0
            stop sound fadeout 1.0
            scene white with dissolve
            pause 1.0
            play sound storybeat5_15_climax fadein 0.5
            scene kitchen_night7 at slight_wobble with dissolve:
                zoom 1.01 xalign 0.5 yalign 0.5
            "We cum together, Robin shooting his load onto his stomach as I fill his hole with my cum."
            robin "I can feel you... so warm, so filling..."
            robin "You're filling me up on our kitchen table...!"
            "Robin's ass doesn't let go and clenches even tighter, almost as if he wants to milk every single drop out of me."
            pro "Fuck... that was so fucking hot."
            robin "Hehe... for sure..."
            scene black with dissolve
            "After a few moments, I pull out."
            play sound pleasured_exertion_slow fadein 0.5
            scene kitchen_night8 at slight_wobble with dissolve:
                zoom 1.01 xalign 0.5 yalign 0.5
            robin "Look at all of your seed dripping out of my ass..."
            robin "I'm always surprised at how much you cum, hehe."
            pro "It's not my fault!"
            pro "You're just too fucking sexy, you know that right?"
            robin "Hehe..."
            scene black with dissolve
            "I help Robin clean up. He gives me a kiss before heading back to his room for the night."
            play sound positive_event_01
            system "{color=#bb0028}Desire increased by 30{/color}"
            $ desire += 30
            scene black with dissolve
            pause 0.5
            show prologue9 with dissolve
            pause 1.0
            jump day

        "Leave Robin alone":
            call screen kitchen_night with dissolve
            

label robin_kitchen_interact:

    if robin_progression_level == 0 and key_task == 0:
        scene kitchen
        play sound error_001
        system "You should probably complete your tasks before using the kitchen."
        call screen kitchen_afternoon

    if robin_progression_level == 0 and key_task == 1:
        scene kitchen
        call screen interact_afternoon

    if robin_progression_level >= 1 and key_task >= 2:
        scene kitchen
        call screen interact_afternoon
# KITCHEN INTERACTION -------------------------------------------------------------------------------------------------------------------------------------------

screen kitchen_cook_menu_day:
    modal True

    add "images/overlay/kitchen/interact_bg.png"

    imagebutton:
        idle "images/overlay/kitchen/cook_idle.png"
        hover "images/overlay/kitchen/cook_hover.png"
        action [Hide("kitchen_cook_menu_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_cook_options")]
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("kitchen_cook_menu_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_day")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7

screen kitchen_cook_menu_afternoon:
    modal True

    add "images/overlay/kitchen/interact_bg.png"

    imagebutton:
        idle "images/overlay/kitchen/cook_idle.png"
        hover "images/overlay/kitchen/cook_hover.png"
        action [Hide("kitchen_cook_menu_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_cook_options")]
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("kitchen_cook_menu_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_afternoon")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7

screen kitchen_cook_menu_evening:
    modal True

    add "images/overlay/kitchen/interact_bg.png"

    imagebutton:
        idle "images/overlay/kitchen/cook_idle.png"
        hover "images/overlay/kitchen/cook_hover.png"
        action [Hide("kitchen_cook_menu_evening"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_cook_options")]
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("kitchen_cook_menu_evening"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_evening")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7

screen kitchen_cook_options:
    modal True

    add "images/overlay/kitchen/interact_bg.png"

    text "{color=#ffffff}Money:{/color}{color=#37B700} $[money]{/color}" xalign 0.25 yalign 0.25:
        font 'fonts/FredokaOne-Regular.ttf'
        size 50

    vbox:
        align (0.05, 0.4)
        imagebutton:
            focus_mask True
            idle "images/overlay/kitchen/pizza_idle.png"
            hover "images/overlay/kitchen/pizza_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at food_hover
            action [Hide("kitchen_cook_options"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("pizza_kitchen")] # TODO JUMP TO SCREEN
            xalign 0.05
            yalign 0.4

        text "{color=#ffffff}Pizza ($10){/color}" xalign 0.5 yalign 0.99:
            font 'fonts/FredokaOne-Regular.ttf'
            at hover

        text "{color=#ff87ff}Affection ++{/color}" xalign 0.5 yalign 0.99:
            font 'fonts/FredokaOne-Regular.ttf'
            at hover

    vbox:
        align (0.4, 0.4)
        imagebutton:
            focus_mask True
            idle "images/overlay/kitchen/popcorn_idle.png"
            hover "images/overlay/kitchen/popcorn_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at food_hover
            action [Hide("kitchen_cook_options"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("popcorn_kitchen")] # TODO JUMP TO SCREEN
            xalign 0.05
            yalign 0.4

        text "{color=#ffffff}Popcorn ($10){/color}" xalign 0.5 yalign 0.99:
            font 'fonts/FredokaOne-Regular.ttf'
            at hover

        text "{color=#918fff}Trust ++{/color}" xalign 0.5 yalign 0.99:
            font 'fonts/FredokaOne-Regular.ttf'
            at hover

    if robin_progression_level >= 1:
        vbox:
            align (0.085, 0.75)
            imagebutton:
                focus_mask True
                idle "images/overlay/kitchen/sandwich_idle.png"
                hover "images/overlay/kitchen/sandwich_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("kitchen_cook_options"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("sandwich_kitchen")] # TODO JUMP TO SCREEN
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Sandwich ($35){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#918fff}Trust ++{/color}\n{color=#ff87ff}Affection ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover


    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("kitchen_cook_options"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("show_correct_kitchen_screen")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.95

label show_correct_kitchen_screen:
    
        if time_of_day == "day":
            call screen kitchen_cook_menu_day
        
        if time_of_day == "afternoon":
            call screen kitchen_cook_menu_afternoon

        if time_of_day == "evening":
            call screen kitchen_cook_menu_evening

label pizza_kitchen:
    
        if money < 10:
            scene kitchen
            play sound error_001
            system "You don't have enough money to buy the ingredients to this dish."
            call screen kitchen_cook_options
    
        if money >= 10:
            $ money -= 10
            scene kitchen
            "You make a pizza for Robin."
            "You use high-quality ingredients and make sure to add all of the best toppings."
            show robin neutral with easeinbottom
            robin "Hey, something smells yummy..."
            pro "Oh, I was making a pizza. I thought you might be hungry."
            show robin smile at jumper
            robin "I am! I am! I love pizza!"
            robin "You're the best, [protagonist_name]!"
            scene pizza_kitchen with dissolve
            "Robin scarfs down the whole pizza."
            robin "Mphm... this is really good!"
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 5{/color}"
            $ affection += 5
            jump jump_to_tomorrow

label popcorn_kitchen:
    
        if money < 10:
            scene kitchen
            play sound error_001
            system "You don't have enough money to buy the ingredients to this dish."
            call screen kitchen_cook_options
    
        if money >= 10:
            $ money -= 10
            scene kitchen
            "You make a bag of home-made popcorn for Robin."
            "You season it with a special blend of spices and butter."
            show robin neutral with easeinbottom
            robin "Ooh, are you making popcorn?"
            pro "Yeah, I thought you might like some."
            show robin smile at jumper
            robin "Ooh, popcorn!"
            robin "What brand?"
            pro "It's homemade, actually."
            robin "Wow, that's so cool!"
            robin "Let's see if it's any good!"
            scene popcorn_kitchen with dissolve
            "Robin munches on the popcorn."
            "I think he's enjoying it."
            robin "Mmm, this is really good!"
            robin "Thanks, [protagonist_name]!"
            play sound positive_event_01
            system "{color=#918fff}Trust increased by 5{/color}"
            $ trust += 5
            jump jump_to_tomorrow

label sandwich_kitchen:

        if money < 35:
            scene kitchen
            play sound error_001
            system "You don't have enough money to buy the ingredients to this dish."
            call screen kitchen_cook_options
    
        if money >= 35:
            $ money -= 35
            scene kitchen
            "You make a sandwich for Robin."
            "You freshly slice the cheese, cook the meat, and add some fresh veggies."
            "You even add a little bit of your mom's special sauce."
            show robin neutral with easeinbottom
            robin "Hey [protagonist_name], what's that smell?"
            pro "Oh, I was making a sandwich. I thought you might be hungry."
            show robin smile at jumper
            robin "That looks really good!"
            robin "You made that for me?"
            pro "Yeah, I thought you might like it."
            robin "Aw, thank you!"
            robin "I can't wait to try it!"
            scene sandwich_kitchen with dissolve
            "Robin takes a bite of the sandwich."
            robin "Oh wow, this is really good!"
            robin "The meat is perfect, and I love this sauce!"
            robin "Thank you [protagonist_name], you're the best!"
            play sound positive_event_01
            system "{color=#918fff}Trust increased by 13{/color}"
            $ trust += 13
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 13{/color}"
            $ affection += 13
            jump jump_to_tomorrow
