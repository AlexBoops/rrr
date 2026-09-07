# DAY -------------------------------------------------------------------------------------------------------------------------------------------

screen robin_room_day:
    modal True

    add "images/backgrounds/robin_room_outside_day.png"
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
                idle "images/overlay/house_icons/day/mc_room_idle.png"
                hover "images/overlay/house_icons/day/mc_room_hover.png"
                action [Hide("robin_room_day"), Show("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/bathroom_idle.png"
                hover "images/overlay/house_icons/day/bathroom_hover.png"
                action [Hide("robin_room_day"), Show("bathroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/kitchen_idle.png"
                hover "images/overlay/house_icons/day/kitchen_hover.png"
                action [Hide("robin_room_day"), Show("kitchen_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/lr_idle.png"
                hover "images/overlay/house_icons/day/lr_hover.png"
                action [Hide("robin_room_day"), Show("livingroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 865
        ypos 474
        idle "images/overlay/ui/robin_room/knock_idle.png"
        hover "images/overlay/ui/robin_room/knock_hover.png"
        at hover
        action [Hide("robin_room_day"),Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_room_knock")]

# AFTERNOON -------------------------------------------------------------------------------------------------------------------------------------------

screen robin_room_afternoon:
    modal True

    add "images/backgrounds/robin_room_outside_afternoon.png"
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
                idle "images/overlay/house_icons/afternoon/mc_room_idle.png"
                hover "images/overlay/house_icons/afternoon/mc_room_hover.png"
                action [Hide("robin_room_afternoon"), Show("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/bathroom_idle.png"
                hover "images/overlay/house_icons/afternoon/bathroom_hover.png"
                action [Hide("robin_room_afternoon"), Show("bathroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                action [Hide("robin_room_afternoon"), Show("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/lr_idle.png"
                hover "images/overlay/house_icons/afternoon/lr_hover.png"
                action [Hide("robin_room_afternoon"), Show("livingroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 865
        ypos 474
        idle "images/overlay/ui/robin_room/knock_idle.png"
        hover "images/overlay/ui/robin_room/knock_hover.png"
        at hover
        action [Hide("robin_room_afternoon"),Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_room_knock")]

# EVENING -------------------------------------------------------------------------------------------------------------------------------------------

screen robin_room_evening:
    modal True

    add "images/backgrounds/robin_room_outside_evening.png"
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
                idle "images/overlay/house_icons/evening/mc_room_idle.png"
                hover "images/overlay/house_icons/evening/mc_room_hover.png"
                action [Hide("robin_room_evening"), Show("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/bathroom_idle.png"
                hover "images/overlay/house_icons/evening/bathroom_hover.png"
                action [Hide("robin_room_evening"), Show("bathroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/kitchen_idle.png"
                hover "images/overlay/house_icons/evening/kitchen_hover.png"
                action [Hide("robin_room_evening"), Show("kitchen_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/lr_idle.png"
                hover "images/overlay/house_icons/evening/lr_hover.png"
                action [Hide("robin_room_evening"), Show("livingroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 865
        ypos 474
        idle "images/overlay/ui/robin_room/knock_idle.png"
        hover "images/overlay/ui/robin_room/knock_hover.png"
        at hover
        action [Hide("robin_room_evening"),Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_room_knock")]

# NIGHT -------------------------------------------------------------------------------------------------------------------------------------------

screen robin_room_night:
    modal True

    add "images/backgrounds/robin_room_outside_night.png"
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

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/mc_room_idle.png"
                hover "images/overlay/house_icons/night/mc_room_hover.png"
                action [Hide("robin_room_night"), Show("mc_bedroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/bathroom_idle.png"
                hover "images/overlay/house_icons/night/bathroom_hover.png"
                action [Hide("robin_room_night"), Show("bathroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                    hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                    action [Hide("robin_room_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/kitchen_idle.png"
                    hover "images/overlay/house_icons/night/kitchen_hover.png"
                    action [Hide("robin_room_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/lr_idle.png"
                hover "images/overlay/house_icons/night/lr_hover.png"
                action [Hide("robin_room_night"), Show("livingroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 865
        ypos 474
        idle "images/overlay/ui/robin_room/knock_idle.png"
        hover "images/overlay/ui/robin_room/knock_hover.png"
        at hover
        action [Hide("robin_room_night"),Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_room_knock")]

# KNOCK -------------------------------------------------------------------------------------------------------------------------------------------

label robin_room_knock:
    
    if time_of_day == "day":
        scene robin_room_outside_day
        "You knock on Robin's door."
        "There's no answer, he's probably not in his room."
        menu:
            system "What would you like to do?"
            "Enter his room anyway":
                call screen robin_room_enter_day
            "Go back":
                call screen robin_room_day

    if time_of_day == "afternoon":
        scene robin_room_outside_afternoon
        "You knock on Robin's door."
        "There's no answer, he's probably not in his room."
        menu:
            system "What would you like to do?"
            "Enter his room anyway":
                call screen robin_room_enter_afternoon
            "Go back":
                call screen robin_room_afternoon

    if time_of_day == "evening":
        scene robin_room_outside_evening
        "You knock on Robin's door."
        "There's no answer, he's probably not in his room."
        menu:
            system "What would you like to do?"
            "Enter his room anyway":
                call screen robin_room_enter_evening
            "Go back":
                call screen robin_room_evening                
    
    if time_of_day == "night":
        scene robin_room_outside_night
        "You knock on Robin's door."
        if robin_progression_level >= 1 and key_task >= 2:
            "There's no answer, he's probably not in his room."
            menu:
                system "What would you like to do?"
                "Enter his room anyway":
                    call screen robin_room_enter_night
                "Go back":
                    call screen robin_room_night
        else:
            scene robin_door_open_1 with dissolve
            robin "Yes?"
            pro "Hey, can I come in?"
            robin "Oh..."
            robin "Um..."
            "Robin sounds a little hesitant."
            "Seems like he's not ready to let you in."
            pro "Sorry for bothering you."
            robin "No, it's okay."
            robin "I'm just tired."
            call screen robin_room_night with dissolve
