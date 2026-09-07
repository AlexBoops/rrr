# DAY -------------------------------------------------------------------------------------------------------------------------------------------

screen mc_bedroom_day:
    modal True

    add "images/backgrounds/mc_bedroom.png"
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
                action [Hide("mc_bedroom_day"), Show("robin_room_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/bathroom_idle.png"
                hover "images/overlay/house_icons/day/bathroom_hover.png"
                action [Hide("mc_bedroom_day"), Show("bathroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/kitchen_idle.png"
                hover "images/overlay/house_icons/day/kitchen_hover.png"
                action [Hide("mc_bedroom_day"), Show("kitchen_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/lr_idle.png"
                hover "images/overlay/house_icons/day/lr_hover.png"
                action [Hide("mc_bedroom_day"), Show("livingroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 429
        ypos 672
        idle "images/overlay/ui/mc_room/sleep_idle.png"
        hover "images/overlay/ui/mc_room/sleep_hover.png"
        at hover
        action [Hide("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("nap_day")]

    imagebutton:
        xpos 997
        ypos 493
        idle "images/overlay/ui/mc_room/work_idle.png"
        hover "images/overlay/ui/mc_room/work_hover.png"
        at hover
        action [Hide("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("work_day")]

    # ARTIFACT 3
    if not artifact3:
        imagebutton:
            xpos 86
            ypos 563
            at artifact3_zoom
            idle "images/overlay/artifacts/artifact3_idle.png"
            hover "images/overlay/artifacts/artifact3_hover.png"
            action [SetScreenVariable("artifact3_moving", True), SetVariable("artifact3", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact3_moving:
        default artifact_image = "images/overlay/artifacts/artifact3_idle.png"
        image artifact_image at unlock_artifact3
        timer 0.9 action [Hide("artifact3_moving")] 

label nap_day:
    scene mc_bedroom
    system "Taking a nap passes time, would you like to take a nap?"
    menu:
        "Yes":
            scene black with dissolve
            jump afternoon
        "No":
            call screen mc_bedroom_day with dissolve

label work_day:

    scene prologue2
    menu:

        "Initiate ending of game." if robin_progression_level == 4 and key_task == 5 and trust >= 450 and affection >= 450 and desire >= 450:
            menu:
                system "You {color=#FF2323}cannot go back after this decision{/color} so I recommend {color=#FF2323}saving your game{/color} before proceeding. Are you sure you want to proceed?"
                "Yes":
                    scene black with dissolve
                    jump story_beat6
                "No":
                    call screen mc_bedroom_day with dissolve

        "Work on your game":

            if robin_progression_level == 0 and key_task == 0:
                scene black with dissolve
                jump story_beat1

            if robin_progression_level == 0 and key_task == 1 and trust >= 20 and affection >= 20 and desire >= 20:
                scene black with dissolve
                jump story_beat2

            if robin_progression_level == 1 and key_task == 2 and trust >= 75 and affection >= 75 and desire >= 75:
                scene black with dissolve
                jump story_beat3
    
            if robin_progression_level == 2 and key_task == 3 and trust >= 175 and affection >= 175 and desire >= 175:
                scene black with dissolve
                jump story_beat4

            if robin_progression_level == 3 and key_task == 4 and trust >= 275 and affection >= 275 and desire >= 275:
                scene black with dissolve
                jump story_beat5

            scene black with dissolve
            system "You spend the morning working and {color=#FFD800}earn $25.{/color}"
            $ money += 25
            jump afternoon
        "Purchase a gift for Robin":
            play sound click_003
            call screen gift_menu
        "Go back":
            call screen mc_bedroom_day with dissolve

# AFTERNOON -------------------------------------------------------------------------------------------------------------------------------------------

screen mc_bedroom_afternoon:
    modal True

    add "images/backgrounds/mc_bedroom.png"
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
                action [Hide("mc_bedroom_afternoon"), Show("robin_room_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/bathroom_idle.png"
                hover "images/overlay/house_icons/afternoon/bathroom_hover.png"
                action [Hide("mc_bedroom_afternoon"), Show("bathroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                action [Hide("mc_bedroom_afternoon"), Show("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/lr_idle.png"
                hover "images/overlay/house_icons/afternoon/lr_hover.png"
                action [Hide("mc_bedroom_afternoon"), Show("livingroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 429
        ypos 672
        idle "images/overlay/ui/mc_room/sleep_idle.png"
        hover "images/overlay/ui/mc_room/sleep_hover.png"
        at hover
        action [Hide("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("nap_afternoon")]

    imagebutton:
        xpos 997
        ypos 493
        idle "images/overlay/ui/mc_room/work_idle.png"
        hover "images/overlay/ui/mc_room/work_hover.png"
        at hover
        action [Hide("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("work_afternoon")]

    # ARTIFACT 5
    if not artifact5:
        imagebutton:
            xpos 1465
            ypos 763
            at artifact5_zoom
            idle "images/overlay/artifacts/artifact5_idle.png"
            hover "images/overlay/artifacts/artifact5_hover.png"
            action [SetScreenVariable("artifact5_moving", True), SetVariable("artifact5", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact5_moving:
        default artifact_image = "images/overlay/artifacts/artifact5_idle.png"
        image artifact_image at unlock_artifact5
        timer 0.9 action [Hide("artifact5_moving")] 

label nap_afternoon:
    scene mc_bedroom
    system "Taking a nap passes time, would you like to take a nap?"
    menu:
        "Yes":
            scene black with dissolve
            jump evening
        "No":
            call screen mc_bedroom_afternoon with dissolve

label work_afternoon:
    scene prologue2
    menu:
        "Work on your game":
            scene black with dissolve
            system "You spend the afternoon working and {color=#FFD800}earn $25.{/color}"
            $ money += 25
            jump evening
        "Purchase a gift for Robin":
            play sound click_003
            call screen gift_menu
        "Go back":
            call screen mc_bedroom_afternoon with dissolve

# EVENING -------------------------------------------------------------------------------------------------------------------------------------------

screen mc_bedroom_evening:
    modal True

    add "images/backgrounds/mc_bedroom_evening.png"
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
                action [Hide("mc_bedroom_evening"), Show("robin_room_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/bathroom_idle.png"
                hover "images/overlay/house_icons/evening/bathroom_hover.png"
                action [Hide("mc_bedroom_evening"), Show("bathroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/kitchen_idle.png"
                hover "images/overlay/house_icons/evening/kitchen_hover.png"
                action [Hide("mc_bedroom_evening"), Show("kitchen_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/lr_idle.png"
                hover "images/overlay/house_icons/evening/lr_hover.png"
                action [Hide("mc_bedroom_evening"), Show("livingroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        xpos 429
        ypos 672
        idle "images/overlay/ui/mc_room/sleep_idle.png"
        hover "images/overlay/ui/mc_room/sleep_hover.png"
        at hover
        action [Hide("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("nap_evening")]

    imagebutton:
        xpos 997
        ypos 493
        idle "images/overlay/ui/mc_room/work_idle.png"
        hover "images/overlay/ui/mc_room/work_hover.png"
        at hover
        action [Hide("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("work_evening")]

label nap_evening:
    scene mc_bedroom_evening
    system "Taking a nap passes time, would you like to take a nap?"
    menu:
        "Yes":
            scene black with dissolve
            jump night
        "No":
            call screen mc_bedroom_evening with dissolve

label work_evening:
    scene prologue2
    menu:
        "Work on your game":
            scene black with dissolve
            system "You spend the evening working and {color=#FFD800}earn $25.{/color}"
            $ money += 25
            jump night
        "Purchase a gift for Robin":
            play sound click_003
            call screen gift_menu
        "Go back":
            call screen mc_bedroom_evening with dissolve

# NIGHT -------------------------------------------------------------------------------------------------------------------------------------------

screen mc_bedroom_night:
    modal True

    add "images/backgrounds/mc_bedroom_night.png"
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

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/robin_room_idle.png"
                    hover "images/overlay/house_icons/afternoon/robin_room_hover.png"
                    action [Hide("mc_bedroom_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/robin_room_idle.png"
                    hover "images/overlay/house_icons/night/robin_room_hover.png"
                    action [Hide("mc_bedroom_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/bathroom_idle.png"
                hover "images/overlay/house_icons/night/bathroom_hover.png"
                action [Hide("mc_bedroom_night"), Show("bathroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                    hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                    action [Hide("mc_bedroom_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/kitchen_idle.png"
                    hover "images/overlay/house_icons/night/kitchen_hover.png"
                    action [Hide("mc_bedroom_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/lr_idle.png"
                hover "images/overlay/house_icons/night/lr_hover.png"
                action [Hide("mc_bedroom_night"), Show("livingroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Living Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    # ARTIFACT 9
    if not artifact9 and robin_progression_level >= 2:
        imagebutton:
            xpos 395
            ypos 1039
            at artifact9_zoom
            idle "images/overlay/artifacts/artifact9_idle.png"
            hover "images/overlay/artifacts/artifact9_hover.png"
            action [SetScreenVariable("artifact9_moving", True), SetVariable("artifact9", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact9_moving:
        default artifact_image = "images/overlay/artifacts/artifact9_idle.png"
        image artifact_image at unlock_artifact9
        timer 0.9 action [Hide("artifact9_moving")]

    imagebutton:
        xpos 429
        ypos 672
        idle "images/overlay/ui/mc_room/sleep_idle.png"
        hover "images/overlay/ui/mc_room/sleep_hover.png"
        at hover
        action [Hide("mc_bedroom_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("nap_night")]


label nap_night:
    scene mc_bedroom_night
    system "Taking a nap passes time, would you like to take a nap?"
    menu:
        "Yes":
            scene black with dissolve
            show prologue9 with dissolve
            # play sound
            pause 1.0
            jump day
        "No":
            call screen mc_bedroom_night with dissolve
