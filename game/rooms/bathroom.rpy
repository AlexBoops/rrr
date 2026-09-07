# DAY -------------------------------------------------------------------------------------------------------------------------------------------

screen bathroom_day:
    modal True

    add "images/backgrounds/bathroom.png"
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

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/robin_room_idle.png"
                hover "images/overlay/house_icons/day/robin_room_hover.png"
                action [Hide("bathroom_day"), Show("robin_room_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/mc_room_idle.png"
                hover "images/overlay/house_icons/day/mc_room_hover.png"
                action [Hide("bathroom_day"), Show("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/kitchen_idle.png"
                hover "images/overlay/house_icons/day/kitchen_hover.png"
                action [Hide("bathroom_day"), Show("kitchen_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/lr_idle.png"
                hover "images/overlay/house_icons/day/lr_hover.png"
                action [Hide("bathroom_day"), Show("livingroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 872
        ypos 619
        idle "images/overlay/ui/bathroom/shower_idle.png"
        hover "images/overlay/ui/bathroom/shower_hover.png"
        at hover
        action [Hide("bathroom_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("shower_day")]

label shower_day:

    if robin_progression_level == 0 and key_task == 0:
        scene bathroom
        play sound error_001
        system "You should probably complete your tasks before using the shower."
        call screen bathroom_day
  
    scene bathroom
    system  "Taking a shower passes time, {color=#FF5151}but something may happen{/color}. Would you like to take a shower?"
    $ robin_walks_in = renpy.random.randint(1, 100)

    menu:
        "Yes":
            $ achievement.grant("shower_walkin")
            if robin_progression_level == 0:
                scene black with dissolve

                if robin_walks_in > 50:
                    label bathroomevent_1: 
                        "I hop into the shower and turn on the water."
                        play music shower_running loop
                        scene walkin1_1 with dissolve
                        pro "Ah, that feels nice..."
                        "The warm water feels amazing running down my skin."
                        menu:
                            "Finish your shower":
                                scene black with dissolve
                                stop sound fadeout 1.0
                                "I finish my shower and dry myself off."
                                jump afternoon
                            "Jerk off":
                                "I'm starting to feel a bit horny..." 
                                "Maybe I should jerk off and relieve myself."
                                "I grab my dick and start rubbing it a bit."
                                scene walkin1_2 with dissolve
                                $ achievement.grant("robin_walkin_shower")
                                show robin open blush with easeinbottom
                                "As I'm rubbing my cock, I hear the bathroom door open and Robin steps in."
                                pro "Shit, I forgot to lock the door!"
                                robin "Oh shit, sorry [protagonist_name]!"
                                robin "I didn't mean to walk in on you."
                                "He's embarrassed and is looking away from me."
                                pro "It's fine, sorry I forgot to lock the door!"
                                robin "..."
                                pro "..."
                                robin "Umm... well, I'm gonna leave now."
                                robin "Sorry for disturbing you!"
                                "He quickly exits the bathroom."
                                stop sound fadeout 1.0
                                scene black with dissolve
                                pro "Fuck, that was embarrassing."
                                play sound positive_event_01
                                system "{color=#bb0028}Desire increased by 5{/color}"
                                $ desire += 5
                                jump afternoon
                else:
                    "I take a quick shower. I feel refreshed and energized."
                    jump afternoon

            if robin_progression_level == 1 or robin_progression_level == 2 or robin_progression_level == 3:
                scene black with dissolve

                if robin_walks_in > 50:
                    label bathroomevent_2: 
                        "I hop into the shower and turn on the water."
                        play music shower_running loop
                        scene walkin1_1 with dissolve
                        pro "Ah, that feels nice..."
                        "The warm water feels amazing running down my skin."
                        menu:
                            "Finish your shower":
                                scene black with dissolve
                                stop sound fadeout 1.0
                                "I finish my shower and dry myself off."
                                jump afternoon
                            "Jerk off":
                                "I'm starting to feel a bit horny..." 
                                "Maybe I should jerk off and relieve myself."
                                "I grab my dick and start rubbing it a bit."
                                scene walkin1_2 with dissolve
                                $ achievement.grant("robin_walkin_shower")                                
                                show robin open blush with easeinbottom
                                "As I'm rubbing my cock, I hear the bathroom door open and Robin steps in."
                                pro "Shit, I forgot to lock the door!"
                                robin "Oh shit, sorry [protagonist_name]!"
                                robin "I didn't mean to walk in on you."
                                "He's embarrassed and is looking away from me."
                                pro "It's fine, sorry I forgot to lock the door!"
                                robin "..."
                                pro "..."
                                robin "Umm... well, I'm gonna leave now."
                                robin "Sorry for disturbing you!"
                                "He quickly exits the bathroom."
                                stop sound fadeout 1.0
                                scene black with dissolve
                                pro "Fuck, that was embarrassing."
                                play sound positive_event_01
                                system "{color=#bb0028}Desire increased by 5{/color}"
                                $ desire += 5
                                jump afternoon

                else:
                    "I take a quick shower. I feel refreshed and energized."
                    jump afternoon

            if robin_progression_level == 4:
                scene black with dissolve

                if robin_walks_in > 50:
                    label bathroomevent_3: 
                        "I hop into the shower and turn on the water."
                        play music shower_running loop
                        scene walkin1_1 with dissolve
                        pro "Ah, that feels nice..."
                        "The warm water feels amazing running down my skin."
                        menu:
                            "Finish your shower":
                                scene black with dissolve
                                stop sound fadeout 1.0
                                "I finish my shower and dry myself off."
                                jump afternoon
                            "Jerk off":
                                "I'm starting to feel a bit horny..." 
                                "Maybe I should jerk off and relieve myself."
                                "I grab my dick and start rubbing it a bit."
                                scene walkin1_2 with dissolve
                                $ achievement.grant("robin_walkin_shower")                                
                                show robin open blush with easeinbottom
                                "As I'm rubbing my cock, I hear the bathroom door open and Robin steps in."
                                pro "Shit, I forgot to lock the door!"
                                robin "Oh..."
                                "He blushes at the sight of me masturbating in front of him."
                                show robin smile blush
                                robin "Hehe, you know you don't have to jerk off right?"
                                robin "I'm always here to help."
                                pro "Oh... really?"
                                robin "Hehe... give me a second dummy!"
                                scene white with dissolve
                                "He takes off his clothes and jumps in the shower with me."
                                pro "Whoa, Robin!"
                                play sound hand_job fadein 0.5 loop
                                scene walkin1_3 with dissolve:
                                    xalign 0.5 yalign 0.5
                                    zoom 1.0
                                    ease 0.35 yalign 1.0 zoom 1.07
                                    ease 0.3 yalign 0.5 zoom 1.0
                                    repeat
                                "He starts to stroke my cock, his hand gripping firmly."
                                robin "Hehe, look at this big guy..."
                                robin "Do you want me to help you take care of it?"
                                robin "I like the way it feels in my hands... so big and hard."
                                robin "What were you thinking about before I walked in?"
                                robin "Tell me..."
                                pro "I... I was thinking about you..."
                                robin "Hehe, you were?"
                                robin "What part of me were you thinking about?"
                                robin "My ass? My lips? My cute cock?"
                                robin "Come on, tell me..."
                                robin "Tell me what you want to do to me..."
                                pro "I was thinking of fucking you..."
                                robin "Hehe, what else?"
                                pro "And... filling up your pretty mouth with my cum..."
                                pro "And making you swallow every drop."
                                robin "That's so hot..."
                                menu:
                                    "Continue":
                                        play sound suck_2 fadein 0.5 loop
                                        scene walkin1_4 with dissolve:
                                            xalign 0.5 yalign 0.5
                                            zoom 1.0
                                            ease 0.35 yalign 1.0 zoom 1.07
                                            ease 0.3 yalign 0.5 zoom 1.0
                                            repeat                                            
                                        "Without warning, Robin begins sucking on my cock."
                                pro "F-fuck...!"
                                pro "Robin..."
                                robin "Mhmm..."
                                "His tongue swirls around my dick while his head bobs up and down."
                                pro "That feels so fucking good..."
                                robin "Do you like the way my mouth feels?"
                                "I moan in agreement as he continues to suck me off."
                                pro "Fuck, your lips are perfect... such a good femboy."
                                pro "You look so hot when you have my dick in your mouth."
                                robin "Mmm~"
                                menu:
                                    "Continue":
                                        pro "Fuck... I can't wait any longer."
                                        pro "I need to be inside of you!"
                                        pro "Turn around and spread your legs."
                                stop sound fadeout 0.5
                                scene white with dissolve
                                "He releases my dick from his mouth and turns around, spreading his legs."
                                play sound storybeat5_18 fadein 0.5 loop
                                scene walkin1_5 with dissolve:
                                    xalign 0.5 yalign 0.5
                                    zoom 1.0
                                    ease 0.2 yalign 1.0 zoom 1.07
                                    ease 0.15 yalign 0.5 zoom 1.0
                                    repeat  
                                "I slam my cock inside of him, not giving him even a moment to brace himself."
                                robin "Fuck~!"
                                pro "You feels so fucking good, holy shit..."
                                robin "Ahn! Y-Yes!"
                                robin "It's yours to use whenever you want...!"
                                robin "It's your hole to fuck...!"
                                robin "You feel so fucking good!"
                                robin "God... I love feeling your cock inside of me...!"
                                pro "You're such a fucking tease... you know that right?"
                                pro "You drive me fucking crazy..."
                                "I slam my dick into his prostate over and over."
                                robin "AH!"
                                pro "You love this, don't you?"
                                robin "Y-Yes!"
                                robin "It's so good! Keep pounding into me! Harder! I need it so bad! Please!"
                                "I can feel myself reaching my limit as Robin's ass tightens around my dick."
                                pro "Fuck, I'm going to cum."
                                pro "Be a good femboy and take my load."
                                robin "Y-Yes...!"
                                robin "I want your cum inside me!"
                                menu:
                                    "Cum":
                                        robin "I'm... cumming!"
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
                                scene walkin1_6 at slight_wobble with dissolve
                                pro "F-fuck!"
                                "I cum inside of Robin's ass, shooting out more cum than I thought I even had."
                                pro "FUCK!"
                                robin "YESSSSSS~!"
                                robin "FILL ME ALL THE WAY UP~!"
                                "My dick keeps pumping out more and more cum."
                                "I fill his hole with so much cum that it starts leaking out of his ass."
                                robin "Fuck, that was amazing...!"
                                robin "Next time you think of jerking off in the shower, just call me over..."
                                robin "I'll treat you to this every time..."
                                play sound positive_event_01
                                system "{color=#bb0028}Desire increased by 25{/color}"
                                $ desire += 25
                                jump afternoon

                else:
                    "I take a quick shower. I feel refreshed and energized."
                    jump afternoon

        "No":
            "I decide not to take a shower."
            call screen bathroom_day with dissolve

# AFTERNOON -------------------------------------------------------------------------------------------------------------------------------------------

screen bathroom_afternoon:
    modal True

    add "images/backgrounds/bathroom.png"
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

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/robin_room_idle.png"
                hover "images/overlay/house_icons/afternoon/robin_room_hover.png"
                action [Hide("bathroom_afternoon"), Show("robin_room_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/mc_room_idle.png"
                hover "images/overlay/house_icons/afternoon/mc_room_hover.png"
                action [Hide("bathroom_afternoon"), Show("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                action [Hide("bathroom_afternoon"), Show("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/lr_idle.png"
                hover "images/overlay/house_icons/afternoon/lr_hover.png"
                action [Hide("bathroom_afternoon"), Show("livingroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 872
        ypos 619
        idle "images/overlay/ui/bathroom/shower_idle.png"
        hover "images/overlay/ui/bathroom/shower_hover.png"
        at hover
        action [Hide("bathroom_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("shower_afternoon")]

label shower_afternoon:

    if robin_progression_level == 0 and key_task == 0:
        scene bathroom
        play sound error_001
        system "You should probably complete your tasks before using the shower."
        call screen bathroom_afternoon

    scene bathroom
    system "Taking a shower passes time, {color=#FF5151}but something may happen{/color}. Would you like to take a shower?"
    $ robin_walks_in = renpy.random.randint(1, 100)

    menu:
        "Yes":
            $ achievement.grant("shower_walkin")
            if robin_progression_level == 0:

                scene black with dissolve

                if robin_walks_in > 50:
                    "I hop into the shower and turn on the water."
                    play music shower_running loop
                    scene walkin1_1 with dissolve
                    pro "Ah, that feels nice..."
                    "The warm water feels amazing running down my skin."
                    menu:
                        "Finish your shower":
                            scene black with dissolve
                            stop sound fadeout 1.0
                            "I finish my shower and dry myself off."
                            jump evening
                        "Jerk off":
                            "I'm starting to feel a bit horny..." 
                            "Maybe I should jerk off and relieve myself."
                            "I grab my dick and start rubbing it a bit."
                            scene walkin1_2 with dissolve
                            $ achievement.grant("robin_walkin_shower")                            
                            show robin open blush with easeinbottom
                            "As I'm rubbing my cock, I hear the bathroom door open and Robin steps in."
                            pro "Shit, I forgot to lock the door!"
                            robin "Oh shit, sorry [protagonist_name]!"
                            robin "I didn't mean to walk in on you."
                            "He's embarrassed and is looking away from me."
                            pro "It's fine, sorry I forgot to lock the door!"
                            robin "..."
                            pro "..."
                            robin "Umm... well, I'm gonna leave now."
                            robin "Sorry for disturbing you!"
                            "He quickly exits the bathroom."
                            stop sound fadeout 1.0
                            scene black with dissolve
                            pro "Fuck, that was embarrassing."
                            play sound positive_event_01
                            system "{color=#bb0028}Desire increased by 5{/color}"
                            $ desire += 5
                            jump evening
                else:
                    "I take a quick shower. I feel refreshed and energized."
                    jump evening

            if robin_progression_level == 1 or robin_progression_level == 2 or robin_progression_level == 3:
                scene black with dissolve

                if robin_walks_in > 50:
                        "I hop into the shower and turn on the water."
                        play music shower_running loop
                        scene walkin1_1 with dissolve
                        pro "Ah, that feels nice..."
                        "The warm water feels amazing running down my skin."
                        menu:
                            "Finish your shower":
                                scene black with dissolve
                                stop sound fadeout 1.0
                                "I finish my shower and dry myself off."
                                jump evening
                            "Jerk off":
                                "I'm starting to feel a bit horny..." 
                                "Maybe I should jerk off and relieve myself."
                                "I grab my dick and start rubbing it a bit."
                                scene walkin1_2 with dissolve
                                $ achievement.grant("robin_walkin_shower")                                
                                show robin open blush with easeinbottom
                                "As I'm rubbing my cock, I hear the bathroom door open and Robin steps in."
                                pro "Shit, I forgot to lock the door!"
                                robin "Oh shit, sorry [protagonist_name]!"
                                robin "I didn't mean to walk in on you."
                                "He's embarrassed and is looking away from me."
                                pro "It's fine, sorry I forgot to lock the door!"
                                robin "..."
                                pro "..."
                                robin "Umm... well, I'm gonna leave now."
                                robin "Sorry for disturbing you!"
                                "He quickly exits the bathroom."
                                stop sound fadeout 1.0
                                scene black with dissolve
                                pro "Fuck, that was embarrassing."
                                play sound positive_event_01
                                system "{color=#bb0028}Desire increased by 5{/color}"
                                $ desire += 5
                                jump evening

                else:
                    "I take a quick shower. I feel refreshed and energized."
                    jump evening                    

            if robin_progression_level == 4:
                scene black with dissolve

                if robin_walks_in > 50:
                        "I hop into the shower and turn on the water."
                        play music shower_running loop
                        scene walkin1_1 with dissolve
                        pro "Ah, that feels nice..."
                        "The warm water feels amazing running down my skin."
                        menu:
                            "Finish your shower":
                                scene black with dissolve
                                stop sound fadeout 1.0
                                "I finish my shower and dry myself off."
                                jump evening
                            "Jerk off":
                                "I'm starting to feel a bit horny..." 
                                "Maybe I should jerk off and relieve myself."
                                "I grab my dick and start rubbing it a bit."
                                scene walkin1_2 with dissolve
                                $ achievement.grant("robin_walkin_shower")                                
                                show robin open blush with easeinbottom
                                "As I'm rubbing my cock, I hear the bathroom door open and Robin steps in."
                                pro "Shit, I forgot to lock the door!"
                                robin "Oh..."
                                "He blushes at the sight of me masturbating in front of him."
                                show robin smile blush
                                robin "Hehe, you know you don't have to jerk off right?"
                                robin "I'm always here to help."
                                pro "Oh... really?"
                                robin "Hehe... give me a second dummy!"
                                scene white with dissolve
                                "He takes off his clothes and jumps in the shower with me."
                                pro "Whoa, Robin!"
                                play sound hand_job fadein 0.5 loop
                                scene walkin1_3 with dissolve:
                                    xalign 0.5 yalign 0.5
                                    zoom 1.0
                                    ease 0.35 yalign 1.0 zoom 1.07
                                    ease 0.3 yalign 0.5 zoom 1.0
                                    repeat
                                "He starts to stroke my cock, his hand gripping firmly."
                                robin "Hehe, look at this big guy..."
                                robin "Do you want me to help you take care of it?"
                                robin "I like the way it feels in my hands... so big and hard."
                                robin "What were you thinking about before I walked in?"
                                robin "Tell me..."
                                pro "I... I was thinking about you..."
                                robin "Hehe, you were?"
                                robin "What part of me were you thinking about?"
                                robin "My ass? My lips? My cute cock?"
                                robin "Come on, tell me..."
                                robin "Tell me what you want to do to me..."
                                pro "I was thinking of fucking you..."
                                robin "Hehe, what else?"
                                pro "And... filling up your pretty mouth with my cum..."
                                pro "And making you swallow every drop."
                                robin "That's so hot..."
                                menu:
                                    "Continue":
                                        play sound suck_2 fadein 0.5 loop
                                        scene walkin1_4 with dissolve:
                                            xalign 0.5 yalign 0.5
                                            zoom 1.0
                                            ease 0.35 yalign 1.0 zoom 1.07
                                            ease 0.3 yalign 0.5 zoom 1.0
                                            repeat                                            
                                        "Without warning, Robin begins sucking on my cock."
                                pro "F-fuck...!"
                                pro "Robin..."
                                robin "Mhmm..."
                                "His tongue swirls around my dick while his head bobs up and down."
                                pro "That feels so fucking good..."
                                robin "Do you like the way my mouth feels?"
                                "I moan in agreement as he continues to suck me off."
                                pro "Fuck, your lips are perfect... such a good femboy."
                                pro "You look so hot when you have my dick in your mouth."
                                robin "Mmm~"
                                menu:
                                    "Continue":
                                        pro "Fuck... I can't wait any longer."
                                        pro "I need to be inside of you!"
                                        pro "Turn around and spread your legs."
                                stop sound fadeout 0.5
                                scene white with dissolve
                                "He releases my dick from his mouth and turns around, spreading his legs."
                                play sound storybeat5_18 fadein 0.5 loop
                                scene walkin1_5 with dissolve:
                                    xalign 0.5 yalign 0.5
                                    zoom 1.0
                                    ease 0.2 yalign 1.0 zoom 1.07
                                    ease 0.15 yalign 0.5 zoom 1.0
                                    repeat  
                                "I slam my cock inside of him, not giving him even a moment to brace himself."
                                robin "Fuck~!"
                                pro "You feel so fucking good, holy shit..."
                                robin "Ahn! Y-Yes!"
                                robin "It's yours to use whenever you want...!"
                                robin "It's your hole to fuck...!"
                                robin "You feel so fucking good!"
                                robin "God... I love feeling your cock inside of me...!"
                                pro "You're such a fucking tease... you know that right?"
                                pro "You drive me fucking crazy..."
                                "I slam my dick into his prostate over and over."
                                robin "AH!"
                                pro "You love this, don't you?"
                                robin "Y-Yes!"
                                robin "It's so good! Keep pounding into me! Harder! I need it so bad! Please!"
                                "I can feel myself reaching my limit as Robin's ass tightens around my dick."
                                pro "Fuck, I'm going to cum."
                                pro "Be a good femboy and take my load."
                                robin "Y-Yes...!"
                                robin "I want your cum inside me!"
                                menu:
                                    "Cum":
                                        robin "I'm... cumming!"
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
                                scene walkin1_6 at slight_wobble with dissolve
                                pro "F-fuck!"
                                "I cum inside of Robin's ass, shooting out more cum than I thought I even had."
                                pro "FUCK!"
                                robin "YESSSSSS~!"
                                robin "FILL ME ALL THE WAY UP~!"
                                "My dick keeps pumping out more and more cum."
                                "I fill his hole with so much cum that it starts leaking out of his ass."
                                robin "Fuck, that was amazing...!"
                                robin "Next time you think of jerking off in the shower, just call me over..."
                                robin "I'll treat you to this every time..."
                                play sound positive_event_01
                                system "{color=#bb0028}Desire increased by 25{/color}"
                                $ desire += 25
                                jump evening
                else:
                    "I take a quick shower. I feel refreshed and energized."
                    jump evening

        "No":
            "I decide not to take a shower."
            call screen bathroom_afternoon with dissolve

# EVENING -------------------------------------------------------------------------------------------------------------------------------------------

screen bathroom_evening:
    modal True

    add "images/backgrounds/bathroom_occupied.png"
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

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/robin_room_idle.png"
                hover "images/overlay/house_icons/evening/robin_room_hover.png"
                action [Hide("bathroom_evening"), Show("robin_room_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/mc_room_idle.png"
                hover "images/overlay/house_icons/evening/mc_room_hover.png"
                action [Hide("bathroom_evening"), Show("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/kitchen_idle.png"
                hover "images/overlay/house_icons/evening/kitchen_hover.png"
                action [Hide("bathroom_evening"), Show("kitchen_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/lr_idle.png"
                hover "images/overlay/house_icons/evening/lr_hover.png"
                action [Hide("bathroom_evening"), Show("livingroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 872
        ypos 619
        idle "images/overlay/ui/bathroom/spy_idle.png"
        hover "images/overlay/ui/bathroom/spy_hover.png"
        at hover
        action [Hide("bathroom_evening"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("shower_evening")]

    # ARTIFACT 6
    if not artifact6:
        imagebutton:
            xpos 140
            ypos 726
            at artifact6_zoom
            idle "images/overlay/artifacts/artifact6_idle.png"
            hover "images/overlay/artifacts/artifact6_hover.png"
            action [SetScreenVariable("artifact6_moving", True), SetVariable("artifact6", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact6_moving:
        default artifact_image = "images/overlay/artifacts/artifact6_idle.png"
        image artifact_image at unlock_artifact6
        timer 0.9 action [Hide("artifact6_moving")]

label shower_evening:

    if robin_progression_level == 0 and key_task == 0:
        scene bathroom_occupied
        play sound error_001
        system "You should probably complete your tasks before using the shower."
        call screen bathroom_evening

    scene bathroom_occupied
    system "Looks like Robin is using the shower."
    system "The door is slightly open, would you like to peek? {color=#bb0028}(Desire ++){/color}"
    menu:
            "Yes":
                $ achievement.grant("shower_walkin")
                if robin_progression_level == 0:
                    stop music fadeout 1.0
                    scene white with dissolve
                    "I decide to peek through the door."
                    play music shower_running fadein 1.0 loop
                    scene robin_bathroom with dissolve:
                        zoom 2.0 xalign 0.5 yalign 0.2
                        ease 4.0 zoom 1.3 yalign 0.6
                        pause 1.0
                        ease 4.0 zoom 1.0 yalign 0.4
                        pause 1.0
                        ease 4.0 zoom 2.0 yalign 0.2
                        repeat
                    "Robin is standing in the shower, facing towards me."
                    "I watch as he lets the water drip down his smooth body."
                    "His cute dick flops around slightly as he moves."
                    "I stare in awe, watching as he runs his hands through his curly hair."
                    "Fuck, this is so creepy..."
                    "I should stop..."
                    stop sound fadeout 1.0
                    scene black with dissolve
                    "I close the door."
                    "Maybe increasing my {color=#FF00E8}progression level{/color} would give me the confidence to keep watching."
                    play sound positive_event_01
                    system "{color=#bb0028}Desire increased by 10{/color}"
                    $ desire += 10
                    jump jump_to_tomorrow

                if robin_progression_level == 1:
                    stop music fadeout 1.0
                    scene white with dissolve
                    "I decide to peek through the door."
                    play music shower_running fadein 1.0 loop
                    scene robin_bathroom with dissolve:
                        zoom 2.0 xalign 0.5 yalign 0.2
                        ease 4.0 zoom 1.3 yalign 0.6
                        pause 1.0
                        ease 4.0 zoom 1.0 yalign 0.4
                        pause 1.0
                        ease 4.0 zoom 2.0 yalign 0.2
                        repeat
                    "Robin is standing in the shower, facing towards me."
                    "I watch as he lets the water drip down his smooth body."
                    "His cute dick flops around slightly as he moves."
                    "I stare in awe, watching as he runs his hands through his curly hair."
                    "Fuck, this is so creepy..."
                    menu:
                        "Continue watching":
                            scene robin_bathroom_2 with dissolve
                            "He turns around and lets the water rush down his back."
                            "His smooth, perfectly shaped ass is exposed to me."
                            "My god, he looks so perfect."
                            "If I keep staring, I'll go insane..."
                        "Stop watching":
                            "This is too far."
                    stop sound fadeout 1.0
                    scene black with dissolve
                    "I close the door."
                    "Maybe increasing my {color=#FF00E8}progression level{/color} would give me the confidence to keep watching."
                    play sound positive_event_01
                    system "{color=#bb0028}Desire increased by 20{/color}"
                    $ desire += 20
                    jump jump_to_tomorrow

                if robin_progression_level == 2 or robin_progression_level == 3:
                    stop music fadeout 1.0
                    scene white with dissolve
                    "I decide to peek through the door."
                    play music shower_running fadein 1.0 loop
                    scene robin_bathroom with dissolve:
                        zoom 2.0 xalign 0.5 yalign 0.2
                        ease 4.0 zoom 1.3 yalign 0.6
                        pause 1.0
                        ease 4.0 zoom 1.0 yalign 0.4
                        pause 1.0
                        ease 4.0 zoom 2.0 yalign 0.2
                        repeat
                    "Robin is standing in the shower, facing towards me."
                    "I watch as he lets the water drip down his smooth body."
                    "His cute dick flops around slightly as he moves."
                    "I stare in awe, watching as he runs his hands through his curly hair."
                    "Fuck, this is so creepy..."
                    menu:
                        "Continue watching":
                            scene robin_bathroom_2 with dissolve
                            "He turns around and lets the water rush down his back."
                            "His smooth, perfectly shaped ass is exposed to me."
                            "My god, he looks so perfect."
                            "If I keep staring, I'll go insane..."
                            menu:
                                "Keep watching":
                                    play sound robin_bathroom_3 fadein 0.5 loop
                                    scene robin_bathroom_3 with dissolve:
                                        zoom 1.0 xalign 0.5 yalign 0.2
                                        ease 4.0 zoom 1.3 yalign 0.6
                                        pause 1.0
                                        ease 4.0 zoom 1.0 yalign 0.4
                                        pause 1.0
                                        ease 4.0 zoom 1.0 yalign 0.2
                                        repeat
                                    "Holy shit... is he?"
                                    "He's masturbating in the shower... what the fuck."
                                    "He's rubbing his hand up and down his dick..."
                                    "This can't be real..."
                                    "He's moaning so softly..."
                                    "I can't believe I'm watching my femboy roommate jerk off in the shower..."
                                    "This is so wrong but... I can't look away."
                                    "Fuck, I need to stop."
                                    

                                "Stop watching":
                                    "This is too far."

                        "Stop watching":
                            "This is too far."
                    stop sound fadeout 1.0
                    scene black with dissolve
                    "I close the door."
                    "Maybe increasing my {color=#FF00E8}progression level{/color} would give me the confidence to keep watching."
                    play sound positive_event_01
                    system "{color=#bb0028}Desire increased by 20{/color}"
                    $ desire += 20
                    jump jump_to_tomorrow

                if robin_progression_level == 4:
                    stop music fadeout 1.0
                    scene white with dissolve
                    "I decide to peek through the door."
                    play music shower_running fadein 1.0 loop
                    scene robin_bathroom with dissolve:
                        zoom 2.0 xalign 0.5 yalign 0.2
                        ease 4.0 zoom 1.3 yalign 0.6
                        pause 1.0
                        ease 4.0 zoom 1.0 yalign 0.4
                        pause 1.0
                        ease 4.0 zoom 2.0 yalign 0.2
                        repeat
                    "Robin is standing in the shower, facing towards me."
                    "I watch as he lets the water drip down his smooth body."
                    "His cute dick flops around slightly as he moves."
                    "I stare in awe, watching as he runs his hands through his curly hair."
                    menu:
                        "Continue watching":
                            scene robin_bathroom_2 with dissolve
                            "He turns around and lets the water rush down his back."
                            "His smooth, perfectly shaped ass is exposed to me."
                            "My god, he looks so perfect."
                            "If I keep staring, I'll go insane..."
                            menu:
                                "Keep watching":
                                    play sound robin_bathroom_3 fadein 0.5 loop
                                    scene robin_bathroom_3 with dissolve:
                                        zoom 1.0 xalign 0.5 yalign 0.2
                                        ease 4.0 zoom 1.3 yalign 0.6
                                        pause 1.0
                                        ease 4.0 zoom 1.0 yalign 0.4
                                        pause 1.0
                                        ease 4.0 zoom 1.0 yalign 0.2
                                        repeat
                                    "Holy shit... is he?"
                                    "He's masturbating in the shower... what the fuck."
                                    "He's rubbing his hand up and down his dick..."
                                    "This can't be real..."
                                    "He's moaning so softly..."
                                    "I can't believe I'm watching my femboy roommate jerk off in the shower..."
                                    "I can't look away."
                                    menu:
                                        "Enter the bathroom":
                                            "I enter the bathroom"
                                            pro "Robin..."
                                            robin "Oh... was the door open?"
                                            robin "You were watching, weren't you?"
                                            pro "Well I-"
                                            robin "Hehe, you like what you see?"
                                            "He continues to rub his dick, his body completely exposed."
                                            robin "Well, don't keep me waiting..."
                                            robin "Come fuck me dummy!"
                                            stop sound fadeout 0.5
                                            scene white with dissolve
                                            "I waste no time and strip off my clothes, jumping in the shower with him."
                                            robin "Hehe..."
                                            robin "Come eat my ass [protagonist_name]..."
                                            scene robin_bathroom_4 with dissolve
                                            "He turns around and leans against the shower wall."
                                            play sound storybeat6_21 loop 
                                            show tongue with dissolve:
                                                xpos 913 ypos 713
                                                anchor (0.5, 1.0)
                                                ease 1.0 rotate 15
                                                ease 1.0 rotate -15
                                                repeat
                                            "I kneel down and spread his cheeks, revealing his perfectly smooth, tight hole."
                                            "I begin to lick and suck at his asshole, feeling the warmth of the water and the tightness of his rim."
                                            robin "O-Oh god..."
                                            robin "That feels so fucking good..."
                                            robin "Deeper, please..."
                                            "I push my tongue into his asshole, stretching him out as I continue to suck on his hole."
                                            robin "Mhmm..."
                                            robin "Your tongue..."
                                            robin "It's... it's so warm..."
                                            "I push my tongue further into him, swirling it around and teasing his prostate."
                                            robin "Ahn, ahn, ahn!"
                                            robin "Y-You're gonna make me cum already!"
                                            menu:
                                                "Continue":
                                                    hide tongue with dissolve
                                                    stop sound fadeout 0.5
                                            "I pull my tongue out."
                                            robin "Hehe, you ready to fuck me already?"
                                            pro "Watching you in the shower, touching yourself, was the hottest thing I've ever seen."
                                            robin "Come on, [protagonist_name]."
                                            scene white with dissolve
                                            robin "Breed your cute femboy."
                                            play sound storybeat5_18 fadein 0.5 loop 
                                            scene robin_bathroom_5 with dissolve:
                                                xalign 0.5 yalign 0.5
                                                zoom 1.0
                                                ease 0.2 yalign 1.0 zoom 1.07
                                                ease 0.15 yalign 0.5 zoom 1.0
                                                repeat  
                                            "Without hesitation, I grab his ass and shove my cock into his ass as he whimpers loudly."
                                            robin "Ah!"
                                            robin "Yes...! That's it...!"
                                            "I thrust my dick back and forth, pounding into Robin's ass as he moans loudly."
                                            pro "So fucking tight..."
                                            pro "You feel so good, Robin."
                                            pro "Such a perfect ass for me to fill up."
                                            robin "Mmm...!!"
                                            robin "Ahn... your cock...!"
                                            robin "So fucking big...!"
                                            robin "B-Breed me, breed me, breed me, breed me!"
                                            "Warm water runs down our bodies as I slam into his ass over and over again."
                                            pro "Is that good Robin? Do you like how I fuck your bussy?"
                                            robin "Yessss~"
                                            robin "O-oh fuck...!"
                                            "I can feel myself reaching my limit, my cock throbbing inside of him."
                                            robin "I'm close...! Don't stop, don't stop, don't stop!"
                                            robin "Give me your fucking cum!"
                                            menu:
                                                "Cum":
                                                    robin "I'm... cumming!"
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
                                            scene robin_bathroom_6 at slight_wobble with dissolve
                                            "Robin's tightens around my dick and we cum together, his load shooting onto the shower wall."
                                            robin "Fuck...!!"
                                            robin "Your filling me up!!"
                                            robin "I can feel every single drop of cum!"
                                            pro "Robin..."
                                            pro "Don't move..."
                                            pro "Don't let a single drop out."
                                            robin "N-no..."
                                            robin "I need it all..."
                                            stop sound fadeout 0.5
                                            scene white with dissolve
                                            "We stay locked together for a few moments before I pull out."
                                            play sound slight_exertion_slow fadein 0.5
                                            scene robin_bathroom_7 at slight_wobble with dissolve
                                            "I watch as my load slowly trickles out of his asshole."
                                            robin "Hehe, you were really pent up, huh?"
                                            pro "That's your fault, Robin."
                                            robin "What do you mean?"
                                            pro "You just... you just have that effect on me."
                                            pro "And I love it."
                                            robin "Hehe."
                                            stop sound fadeout 1.0
                                            scene black with dissolve
                                            "We finish our shower together, washing each other's bodies with care and affection."
                                            play sound positive_event_01
                                            system "{color=#bb0028}Desire increased by 30{/color}"
                                            $ desire += 30
                                            jump jump_to_tomorrow

                                        "Stop watching":
                                            "This is too far."

                                "Stop watching":
                                    "This is too far."

                        "Stop watching":
                            "This is too far."
                    stop sound fadeout 1.0
                    scene black with dissolve
                    "I close the door."
                    "Maybe next time I should keep watching."
                    play sound positive_event_01
                    system "{color=#bb0028}Desire increased by 20{/color}"
                    $ desire += 20
                    jump jump_to_tomorrow

            "No":
                "I decide not to peek into the shower."
                call screen bathroom_evening with dissolve

# NIGHT -------------------------------------------------------------------------------------------------------------------------------------------

screen bathroom_night:
    modal True

    add "images/backgrounds/bathroom_night.png"
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

    if robin_progression_level >= 2:
        imagebutton:
            xpos 872
            ypos 619
            idle "images/overlay/ui/bathroom/ghost_idle.png"
            hover "images/overlay/ui/bathroom/ghost_hover.png"
            at hover
            action [Hide("bathroom_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("ghost_scene")]

    imagebutton:
        xalign 0.9
        yalign 0.2
        focus_mask True
        at six_percent
        idle "images/overlay/ui/artifact_idle.png"
        hover "images/overlay/ui/artifact_hover.png"
        action [Show("artifacts"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")] # TODO: Add artifact screen

    # ARTIFACT 7
    if not artifact7 and robin_progression_level >= 2:
        imagebutton:
            xpos 1541
            ypos 984
            at artifact7_zoom
            idle "images/overlay/artifacts/artifact7_idle.png"
            hover "images/overlay/artifacts/artifact7_hover.png"
            action [SetScreenVariable("artifact7_moving", True), SetVariable("artifact7", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact7_moving:
        default artifact_image = "images/overlay/artifacts/artifact7_idle.png"
        image artifact_image at unlock_artifact7
        timer 0.9 action [Hide("artifact7_moving")] 

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
                    action [Hide("bathroom_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/robin_room_idle.png"
                    hover "images/overlay/house_icons/night/robin_room_hover.png"
                    action [Hide("bathroom_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/mc_room_idle.png"
                hover "images/overlay/house_icons/night/mc_room_hover.png"
                action [Hide("bathroom_night"), Show("mc_bedroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                    hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                    action [Hide("bathroom_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/kitchen_idle.png"
                    hover "images/overlay/house_icons/night/kitchen_hover.png"
                    action [Hide("bathroom_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/lr_idle.png"
                hover "images/overlay/house_icons/night/lr_hover.png"
                action [Hide("bathroom_night"), Show("livingroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

# GHOST SCENE 

label ghost_scene:
    scene bathroom_night
    "I enter the bathroom late at night."
    "I heard that if I repeat this incantation, a ghost may appear."
    pro "Hm... should I try it?"
    menu:
        "Try summoning a ghost":
            pro "Okay, here goes nothing."
            stop music fadeout 1.0
            "I stand in front of the mirror."
            "All I need to do is say 'Bloody Bussy' three times."
            pro "Bloody Bussy."
            pro "Bloody Bussy.."
            pro "Bloody Bussy..."
            pro "..."
            "I wait for a few moments, but nothing seems to change."
            "Did it not work...?"
            "Or was it all just a-"
            play music intrigue fadein 2.0
            pro "Huh?"
            scene ghost_glow_scene at slight_wobble with dissolve:
                subpixel True
                zoom 1.01 xalign 0.5 yalign 0.5
            "A faint glow appears in the mirror."
            pro "Oh... oh fuck!"
            show ghost_4
            hide ghost_4
            show ghost_scene at slight_wobble with dissolve:
                zoom 1.0 xalign 0.5 yalign 0.5
                ease 1.0 zoom 1.03
            "A figure begins to materialize in front of me."
            pro "Holy fuck, it actually worked!"
            "Before I know it, a ghost in standing in front of me."
            "They have long white hair, glowing green eyes, and their body is slightly translucent."
            ghost "Hehe, you summoned me?"
            ghost "It's been so long since someone has called upon me."
            "I notice the ghost's bulge."
            pro "Are you... a femboy ghost?"
            pro "What the fuck..."
            ghost "Hehe..."
            ghost "So... why did you summon me human?"
            pro "I... uh..."
            pro "To be honest, it was mostly just out of curiosity..."
            ghost "I see."
            ghost "Well, is there any way I can make your summon more... interesting?"
            "I think for a moment."
            pro "Well..."
            pro "I'm sort of interested in my roommate, sorry."
            ghost "Hm, I guess we can't have fun then."
            ghost "But it's cute that you are remaining loyal to him..."
            ghost "Would you like me to show you one of your possible futures with him?"
            pro "A possible future...?"
            pro "Uh... I mean..."
            ghost "You're curious, aren't you?"
            pro "Maybe a little..."
            stop music fadeout 2.0
            scene white with dissolve
            "The ghost gently touches my head."
            "My vision goes completely white."
            play music wedding fadein 2.0
            "..."
            "Are those... wedding bells?"
            scene ghost_5 with dissolve
            "When I regain my vision, I see Robin standing in front of me in a beautiful white wedding dress."
            pro "Wait... is this...?"
            "Is this... a possible future?"
            robin "I can't wait for our honeymoon."
            robin "I have so many things planned for you, hehe."
            robin "I'm going to take such good care of my husband, I promise."
            "H-husband?!"
            "So we... get married in the future?"
            pro "Robin..."
            stop music fadeout 1.0
            scene white with dissolve
            "My vision goes white again."
            pro "W-what's happening!"
            play music love fadein 1.0
            scene ghost_6 with dissolve
            "When I regain my vision, I'm in a beautiful bedroom."
            robin "Hehe... c'mon silly..."
            robin "Don't leave me waiting, you're my husband now!"
            "He's covered in rose petals."
            robin "You can do whatever you want to me..."
            robin "Fuck me like a dirty femboy."
            stop music fadeout 1.0
            scene white with dissolve
            "My vision goes white once more."
            pro "Ah!"
            play music intrigue fadein 2.0
            show ghost_scene at slight_wobble with dissolve:
                zoom 1.0 xalign 0.5 yalign 0.5
                ease 1.0 zoom 1.03            
            "I'm back in the present, the ghost still in front of me."
            ghost "Hehe... did you enjoy what you saw?"
            pro "Robin and I were married..."
            pro "We were in love."
            pro "And we had a happy future together..."
            ghost "I can't say for sure if that is your definite future."
            ghost "But, I can say that it is certainly a possibility."
            pro "Wow... that's..."
            pro "I... I can't believe it..."
            pro "..."
            ghost "Hehe."
            pro "Oh, you're leaving so soon?"
            ghost "Don't worry, we'll see each other again someday."
            stop music fadeout 1.0
            scene bathroom_night with dissolve
            "In an instant, he disappears."
            pro "Wow... that was something..."
            pro "I have a chance at a happy future with Robin..."
            play sound positive_event_01
            system "{color=#bb0028}Desire increased by 25{/color}"
            $ desire += 25
            jump jump_to_tomorrow  

        "Go back":
            call screen bathroom_night with dissolve