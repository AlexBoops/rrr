screen robin_room_enter_day:
    modal True

    add "images/backgrounds/robin_room1.png"
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
        focus_mask True
        xpos 1371
        ypos 654
        idle "images/overlay/robin_room_enter/dildo_idle.png"
        hover "images/overlay/robin_room_enter/dildo_hover.png"
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if bear == True:
        imagebutton:
            focus_mask True
            xpos 588
            ypos 772
            idle "images/overlay/robin_room_enter/bear_idle.png"
            hover "images/overlay/robin_room_enter/bear_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if console == True:
        imagebutton:
            focus_mask True
            xpos 959
            ypos 644
            idle "images/overlay/robin_room_enter/console_idle.png"
            hover "images/overlay/robin_room_enter/console_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if restuarant_outfit == True:
        imagebutton:
            focus_mask True
            xpos 1243
            ypos 922
            idle "images/overlay/robin_room_enter/restaurant_outfit_idle.png"
            hover "images/overlay/robin_room_enter/restaurant_outfit_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if lingerie == True:
        imagebutton:
            focus_mask True
            xpos 1455
            ypos 969
            idle "images/overlay/robin_room_enter/lingerie_idle.png"
            hover "images/overlay/robin_room_enter/lingerie_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if cat == True:
        imagebutton:
            focus_mask True
            xpos 949
            ypos 952
            idle "images/overlay/robin_room_enter/cat_idle.png"
            hover "images/overlay/robin_room_enter/cat_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if panties == True:
        imagebutton:
            focus_mask True
            xpos 285
            ypos 973
            idle "images/overlay/robin_room_enter/panties_idle.png"
            hover "images/overlay/robin_room_enter/panties_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if dildo == True:
        imagebutton:
            focus_mask True
            xpos 76
            ypos 857
            idle "images/overlay/robin_room_enter/dildo2_idle.png"
            hover "images/overlay/robin_room_enter/dildo2_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/mc_room_idle.png"
                hover "images/overlay/house_icons/day/mc_room_hover.png"
                action [Hide("robin_room_enter_day"), Show("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/bathroom_idle.png"
                hover "images/overlay/house_icons/day/bathroom_hover.png"
                action [Hide("robin_room_enter_day"), Show("bathroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/kitchen_idle.png"
                hover "images/overlay/house_icons/day/kitchen_hover.png"
                action [Hide("robin_room_enter_day"), Show("kitchen_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/lr_idle.png"
                hover "images/overlay/house_icons/day/lr_hover.png"
                action [Hide("robin_room_enter_day"), Show("livingroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

# AFTERNOON ---------------------------------------------------------

screen robin_room_enter_afternoon:
    modal True

    add "images/backgrounds/robin_room1.png"
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
        focus_mask True
        xpos 1371
        ypos 654
        idle "images/overlay/robin_room_enter/dildo_idle.png"
        hover "images/overlay/robin_room_enter/dildo_hover.png"
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if bear == True:
        imagebutton:
            focus_mask True
            xpos 588
            ypos 772
            idle "images/overlay/robin_room_enter/bear_idle.png"
            hover "images/overlay/robin_room_enter/bear_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if console == True:
        imagebutton:
            focus_mask True
            xpos 959
            ypos 644
            idle "images/overlay/robin_room_enter/console_idle.png"
            hover "images/overlay/robin_room_enter/console_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if restuarant_outfit == True:
        imagebutton:
            focus_mask True
            xpos 1243
            ypos 922
            idle "images/overlay/robin_room_enter/restaurant_outfit_idle.png"
            hover "images/overlay/robin_room_enter/restaurant_outfit_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if lingerie == True:
        imagebutton:
            focus_mask True
            xpos 1455
            ypos 969
            idle "images/overlay/robin_room_enter/lingerie_idle.png"
            hover "images/overlay/robin_room_enter/lingerie_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if cat == True:
        imagebutton:
            focus_mask True
            xpos 949
            ypos 952
            idle "images/overlay/robin_room_enter/cat_idle.png"
            hover "images/overlay/robin_room_enter/cat_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if panties == True:
        imagebutton:
            focus_mask True
            xpos 285
            ypos 973
            idle "images/overlay/robin_room_enter/panties_idle.png"
            hover "images/overlay/robin_room_enter/panties_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if dildo == True:
        imagebutton:
            focus_mask True
            xpos 76
            ypos 857
            idle "images/overlay/robin_room_enter/dildo2_idle.png"
            hover "images/overlay/robin_room_enter/dildo2_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/mc_room_idle.png"
                hover "images/overlay/house_icons/afternoon/mc_room_hover.png"
                action [Hide("robin_room_enter_afternoon"), Show("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/bathroom_idle.png"
                hover "images/overlay/house_icons/afternoon/bathroom_hover.png"
                action [Hide("robin_room_enter_afternoon"), Show("bathroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                action [Hide("robin_room_enter_afternoon"), Show("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/lr_idle.png"
                hover "images/overlay/house_icons/afternoon/lr_hover.png"
                action [Hide("robin_room_enter_afternoon"), Show("livingroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

# EVENING ---------------------------------------------------------

screen robin_room_enter_evening:
    modal True

    add "images/backgrounds/robin_room1.png"
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
        focus_mask True
        xpos 1371
        ypos 654
        idle "images/overlay/robin_room_enter/dildo_idle.png"
        hover "images/overlay/robin_room_enter/dildo_hover.png"
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if bear == True:
        imagebutton:
            focus_mask True
            xpos 588
            ypos 772
            idle "images/overlay/robin_room_enter/bear_idle.png"
            hover "images/overlay/robin_room_enter/bear_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if console == True:
        imagebutton:
            focus_mask True
            xpos 959
            ypos 644
            idle "images/overlay/robin_room_enter/console_idle.png"
            hover "images/overlay/robin_room_enter/console_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if restuarant_outfit == True:
        imagebutton:
            focus_mask True
            xpos 1243
            ypos 922
            idle "images/overlay/robin_room_enter/restaurant_outfit_idle.png"
            hover "images/overlay/robin_room_enter/restaurant_outfit_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if lingerie == True:
        imagebutton:
            focus_mask True
            xpos 1455
            ypos 969
            idle "images/overlay/robin_room_enter/lingerie_idle.png"
            hover "images/overlay/robin_room_enter/lingerie_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if cat == True:
        imagebutton:
            focus_mask True
            xpos 949
            ypos 952
            idle "images/overlay/robin_room_enter/cat_idle.png"
            hover "images/overlay/robin_room_enter/cat_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if panties == True:
        imagebutton:
            focus_mask True
            xpos 285
            ypos 973
            idle "images/overlay/robin_room_enter/panties_idle.png"
            hover "images/overlay/robin_room_enter/panties_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if dildo == True:
        imagebutton:
            focus_mask True
            xpos 76
            ypos 857
            idle "images/overlay/robin_room_enter/dildo2_idle.png"
            hover "images/overlay/robin_room_enter/dildo2_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/mc_room_idle.png"
                hover "images/overlay/house_icons/evening/mc_room_hover.png"
                action [Hide("robin_room_enter_evening"), Show("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/bathroom_idle.png"
                hover "images/overlay/house_icons/evening/bathroom_hover.png"
                action [Hide("robin_room_enter_evening"), Show("bathroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/kitchen_idle.png"
                hover "images/overlay/house_icons/evening/kitchen_hover.png"
                action [Hide("robin_room_enter_evening"), Show("kitchen_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/lr_idle.png"
                hover "images/overlay/house_icons/evening/lr_hover.png"
                action [Hide("robin_room_enter_evening"), Show("livingroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

# NIGHT ---------------------------------------------------------

screen robin_room_enter_night:
    modal True

    add "images/backgrounds/robin_room2.png"
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

    # ARTIFACT 12
    if not artifact12 and robin_progression_level >= 4:
        imagebutton:
            xpos 209
            ypos 722
            at artifact12_zoom
            idle "images/overlay/artifacts/artifact12_idle.png"
            hover "images/overlay/artifacts/artifact12_hover.png"
            action [SetScreenVariable("artifact12_moving", True), SetVariable("artifact12", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact12_moving:
        default artifact_image = "images/overlay/artifacts/artifact12_idle.png"
        image artifact_image at unlock_artifact12
        timer 0.9 action [Hide("artifact12_moving")]

    imagebutton:
        focus_mask True
        xpos 1371
        ypos 654
        idle "images/overlay/robin_room_enter/dildo_idle.png"
        hover "images/overlay/robin_room_enter/dildo_hover.png"
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if bear == True:
        imagebutton:
            focus_mask True
            xpos 588
            ypos 772
            idle "images/overlay/robin_room_enter/bear_idle.png"
            hover "images/overlay/robin_room_enter/bear_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if console == True:
        imagebutton:
            focus_mask True
            xpos 959
            ypos 644
            idle "images/overlay/robin_room_enter/console_idle.png"
            hover "images/overlay/robin_room_enter/console_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if restuarant_outfit == True:
        imagebutton:
            focus_mask True
            xpos 1243
            ypos 922
            idle "images/overlay/robin_room_enter/restaurant_outfit_idle.png"
            hover "images/overlay/robin_room_enter/restaurant_outfit_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if lingerie == True:
        imagebutton:
            focus_mask True
            xpos 1455
            ypos 969
            idle "images/overlay/robin_room_enter/lingerie_idle.png"
            hover "images/overlay/robin_room_enter/lingerie_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if cat == True:
        imagebutton:
            focus_mask True
            xpos 949
            ypos 952
            idle "images/overlay/robin_room_enter/cat_idle.png"
            hover "images/overlay/robin_room_enter/cat_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if panties == True:
        imagebutton:
            focus_mask True
            xpos 285
            ypos 973
            idle "images/overlay/robin_room_enter/panties_idle.png"
            hover "images/overlay/robin_room_enter/panties_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    if dildo == True:
        imagebutton:
            focus_mask True
            xpos 76
            ypos 857
            idle "images/overlay/robin_room_enter/dildo2_idle.png"
            hover "images/overlay/robin_room_enter/dildo2_hover.png"
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/mc_room_idle.png"
                hover "images/overlay/house_icons/night/mc_room_hover.png"
                action [Hide("robin_room_enter_night"), Show("mc_bedroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/bathroom_idle.png"
                hover "images/overlay/house_icons/night/bathroom_hover.png"
                action [Hide("robin_room_enter_night"), Show("bathroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                    hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                    action [Hide("robin_room_enter_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/kitchen_idle.png"
                    hover "images/overlay/house_icons/night/kitchen_hover.png"
                    action [Hide("robin_room_enter_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/lr_idle.png"
                hover "images/overlay/house_icons/night/lr_hover.png"
                action [Hide("robin_room_enter_night"), Show("livingroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'