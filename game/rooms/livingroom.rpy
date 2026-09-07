# DAY -------------------------------------------------------------------------------------------------------------------------------------------

screen livingroom_day:
    modal True

    add "images/backgrounds/livingroom_day.png"
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

    # imagebutton:
    #     xpos 809
    #     ypos 821
    #     idle "images/overlay/ui/living_room/tv_idle.png"
    #     hover "images/overlay/ui/living_room/tv_hover.png"
    #     at hover
    #     action [Hide("livingroom_day"), Jump("tv_interact_morning")] # TV

    # imagebutton:
    #     xpos 400
    #     ypos 439
    #     idle "images/overlay/ui/living_room/date_idle.png"
    #     hover "images/overlay/ui/living_room/date_hover.png"
    #     at hover
    #     action [Show("date_menu")]

    # Robin
    imagebutton:
        xpos 653
        ypos 365
        focus_mask True
        idle "images/overlay/house_icons/day/robin_idle.png"
        hover "images/overlay/house_icons/day/robin_hover.png"
        action [Hide("livingroom_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("robin_livingroom_interact")]

    # ARTIFACT 1
    if not artifact1:
        imagebutton:
            xpos 1455
            ypos 489
            at artifact1_zoom
            idle "images/overlay/artifacts/artifact1_idle.png"
            hover "images/overlay/artifacts/artifact1_hover.png"
            action [SetScreenVariable("artifact1_moving", True), SetVariable("artifact1", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact1_moving:
        default artifact_image = "images/overlay/artifacts/artifact1_idle.png"
        image artifact_image at unlock_artifact1
        timer 0.9 action [Hide("artifact1_moving")] 

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/robin_room_idle.png"
                hover "images/overlay/house_icons/day/robin_room_hover.png"
                action [Hide("livingroom_day"), Show("robin_room_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/bathroom_idle.png"
                hover "images/overlay/house_icons/day/bathroom_hover.png"
                action [Hide("livingroom_day"), Show("bathroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/kitchen_idle.png"
                hover "images/overlay/house_icons/day/kitchen_hover.png"
                action [Hide("livingroom_day"), Show("kitchen_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/day/mc_room_idle.png"
                hover "images/overlay/house_icons/day/mc_room_hover.png"
                action [Hide("livingroom_day"), Show("mc_bedroom_day"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

label tv_interact_morning:

    if robin_progression_level == 0 and key_task == 0:
        scene livingroom_day
        play sound error_001
        system "You should probably complete your tasks before using the TV."
        call screen livingroom_day
    
    if robin_progression_level == 0 and key_task == 1:
        scene livingroom_day
        # call screen tv_interact_menu_day with dissolve
        play sound error_001
        system "You can only use the TV at {color=#4800FF}night{/color} in the demo version of the game."
        system "Please wishlist the game on Steam to support the development of the full game."
        call screen livingroom_day

    if robin_progression_level == 1 and key_task == 2:
        scene livingroom_day
        # call screen tv_interact_menu_day with dissolve
        play sound error_001
        system "You can only use the TV at {color=#4800FF}night{/color} in the demo version of the game."
        system "Please wishlist the game on Steam to support the development of the full game."
        call screen livingroom_day

# AFTERNOON -------------------------------------------------------------------------------------------------------------------------------------------

screen livingroom_afternoon:
    modal True

    add "images/backgrounds/livingroom_day.png"
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

    # imagebutton:
    #     xpos 809
    #     ypos 821
    #     idle "images/overlay/ui/living_room/tv_idle.png"
    #     hover "images/overlay/ui/living_room/tv_hover.png"
    #     at hover
    #     action [Hide("livingroom_afternoon"), Jump("tv_interact_afternoon")] # TV

    # imagebutton:
    #     xpos 400
    #     ypos 439
    #     idle "images/overlay/ui/living_room/date_idle.png"
    #     hover "images/overlay/ui/living_room/date_hover.png"
    #     at hover
    #     action [Show("date_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/robin_room_idle.png"
                hover "images/overlay/house_icons/afternoon/robin_room_hover.png"
                action [Hide("livingroom_afternoon"), Show("robin_room_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/bathroom_idle.png"
                hover "images/overlay/house_icons/afternoon/bathroom_hover.png"
                action [Hide("livingroom_afternoon"), Show("bathroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                action [Hide("livingroom_afternoon"), Show("kitchen_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/afternoon/mc_room_idle.png"
                hover "images/overlay/house_icons/afternoon/mc_room_hover.png"
                action [Hide("livingroom_afternoon"), Show("mc_bedroom_afternoon"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

    # ARTIFACT 8
    if not artifact8 and robin_progression_level >= 2:
        imagebutton:
            xpos 1602
            ypos 1022
            at artifact8_zoom
            idle "images/overlay/artifacts/artifact8_idle.png"
            hover "images/overlay/artifacts/artifact8_hover.png"
            action [SetScreenVariable("artifact8_moving", True), SetVariable("artifact8", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact8_moving:
        default artifact_image = "images/overlay/artifacts/artifact8_idle.png"
        image artifact_image at unlock_artifact8
        timer 0.9 action [Hide("artifact8_moving")]

label tv_interact_afternoon:

    if robin_progression_level == 0 and key_task == 0:
        scene livingroom_day
        play sound error_001
        system "You should probably complete your tasks before using the TV."
        call screen livingroom_afternoon
    
    if robin_progression_level == 0 and key_task == 1:
        scene livingroom_day
        # call screen tv_interact_menu_afternoon with dissolve
        play sound error_001
        system "You can only use the TV at {color=#4800FF}night{/color} in the demo version of the game."
        system "Please wishlist the game on Steam to support the development of the full game."
        call screen livingroom_afternoon

    if robin_progression_level == 1 and key_task == 2:
        scene livingroom_day
        # call screen tv_interact_menu_day with dissolve
        play sound error_001
        system "You can only use the TV at {color=#4800FF}night{/color} in the demo version of the game."
        system "Please wishlist the game on Steam to support the development of the full game."
        call screen livingroom_afternoon

# EVENING -------------------------------------------------------------------------------------------------------------------------------------------

screen livingroom_evening:
    modal True

    add "images/backgrounds/livingroom_evening.png"
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

    # imagebutton:
    #     xpos 809
    #     ypos 821
    #     idle "images/overlay/ui/living_room/tv_idle.png"
    #     hover "images/overlay/ui/living_room/tv_hover.png"
    #     at hover
    #     action [Hide("livingroom_evening"), Jump("tv_interact_evening")] # TV

    # imagebutton:
    #     xpos 400
    #     ypos 439
    #     idle "images/overlay/ui/living_room/date_idle.png"
    #     hover "images/overlay/ui/living_room/date_hover.png"
    #     at hover
    #     action [Show("date_menu")]

    hbox:
        xalign 0.35
        yalign -0.01
        spacing 5 

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/robin_room_idle.png"
                hover "images/overlay/house_icons/evening/robin_room_hover.png"
                action [Hide("livingroom_evening"), Show("robin_room_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent
                
            text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/bathroom_idle.png"
                hover "images/overlay/house_icons/evening/bathroom_hover.png"
                action [Hide("livingroom_evening"), Show("bathroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/kitchen_idle.png"
                hover "images/overlay/house_icons/evening/kitchen_hover.png"
                action [Hide("livingroom_evening"), Show("kitchen_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/evening/mc_room_idle.png"
                hover "images/overlay/house_icons/evening/mc_room_hover.png"
                action [Hide("livingroom_evening"), Show("mc_bedroom_evening"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

label tv_interact_evening:

    if robin_progression_level == 0 and key_task == 0:
        scene livingroom_evening
        play sound error_001
        system "You should probably complete your tasks before using the TV."
        call screen livingroom_evening
    
    if robin_progression_level == 0 and key_task == 1:
        scene livingroom_evening
        # call screen tv_interact_menu_evening with dissolve
        play sound error_001
        system "You can only use the TV at {color=#4800FF}night{/color} in the demo version of the game."
        system "Please wishlist the game on Steam to support the development of the full game."
        call screen livingroom_evening

    if robin_progression_level == 1 and key_task == 2:
        scene livingroom_evening
        # call screen tv_interact_menu_day with dissolve
        play sound error_001
        system "You can only use the TV at {color=#4800FF}night{/color} in the demo version of the game."
        system "Please wishlist the game on Steam to support the development of the full game."
        call screen livingroom_evening

# NIGHT -------------------------------------------------------------------------------------------------------------------------------------------

screen livingroom_night:
    modal True

    add "images/backgrounds/livingroom_night.png"
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

    imagebutton:
        xpos 809
        ypos 821
        idle "images/overlay/ui/living_room/tv_idle.png"
        hover "images/overlay/ui/living_room/tv_hover.png"
        at hover
        action [Hide("livingroom_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("tv_interact_night")] # TV

    # ARTIFACT 11
    if not artifact11 and robin_progression_level >= 4:
        imagebutton:
            xpos 1602
            ypos 1022
            at artifact11_zoom
            idle "images/overlay/artifacts/artifact11_idle.png"
            hover "images/overlay/artifacts/artifact11_hover.png"
            action [SetScreenVariable("artifact11_moving", True), SetVariable("artifact11", True), Play("sound", "audio/music/collect_item.mp3")]

    if artifact11_moving:
        default artifact_image = "images/overlay/artifacts/artifact11_idle.png"
        image artifact_image at unlock_artifact11
        timer 0.9 action [Hide("artifact11_moving")]

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
                    action [Hide("livingroom_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/robin_room_idle.png"
                    hover "images/overlay/house_icons/night/robin_room_hover.png"
                    action [Hide("livingroom_night"), Show("robin_room_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent
                    
                text "{color=#ffffff}Robin's Room{/color}" xalign 0.5 yalign 0.99:
                    font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/bathroom_idle.png"
                hover "images/overlay/house_icons/night/bathroom_hover.png"
                action [Hide("livingroom_night"), Show("bathroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#ffffff}Bathroom{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/afternoon/kitchen_idle.png"
                    hover "images/overlay/house_icons/afternoon/kitchen_hover.png"
                    action [Hide("livingroom_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99
        else:
            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/night/kitchen_idle.png"
                    hover "images/overlay/house_icons/night/kitchen_hover.png"
                    action [Hide("livingroom_night"), Show("kitchen_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                    at card_percent

                text "{color=#ffffff}Kitchen{/color}" xalign 0.5 yalign 0.99

        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/house_icons/night/mc_room_idle.png"
                hover "images/overlay/house_icons/night/mc_room_hover.png"
                action [Hide("livingroom_night"), Show("mc_bedroom_night"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
                at card_percent

            text "{color=#FF9EF6}[protagonist_name]'s{/color} {color=#ffffff}Room{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'

label tv_interact_night:

    if robin_progression_level == 0 and key_task == 0:
        scene livingroom_night
        play sound error_001
        system "You should probably complete your tasks before using the TV."
        call screen livingroom_night
    
    if robin_progression_level == 0 and key_task == 1:
        scene livingroom_night
        call screen tv_interact_menu_night

    if robin_progression_level == 1 and key_task == 2:
        scene livingroom_night
        call screen tv_interact_menu_night

    if robin_progression_level >= 2:
        scene livingroom_night
        call screen tv_interact_menu_night

# ROBIN INTERACTION -------------------------------------------------------------------------------------------------------------------------------------------

label robin_livingroom_interact:

    if robin_progression_level == 0 and key_task == 0:
        scene livingroom_day
        play sound error_001
        system "You should probably complete your tasks before interacting with Robin."
        call screen livingroom_day

    if robin_progression_level == 0 and key_task == 1:
        scene livingroom_day
        call screen interact_day

    if robin_progression_level >= 1 and key_task >= 2:
        scene livingroom_day
        call screen interact_day

# TV INTERACTION -------------------------------------------------------------------------------------------------------------------------------------------

screen tv_interact_menu_day:
    modal True

    add "images/overlay/tv/interact_bg.png"

    imagebutton:
        idle "images/overlay/tv/tv_idle.png"
        hover "images/overlay/tv/tv_hover.png"
        action [Hide("tv_interact_menu_day")] # TODO JUMP TO SCREEN
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("tv_interact_menu_day"), Show("livingroom_day")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7

screen tv_interact_menu_afternoon:
    modal True

    add "images/overlay/tv/interact_bg.png"

    imagebutton:
        idle "images/overlay/tv/tv_idle.png"
        hover "images/overlay/tv/tv_hover.png"
        action [Hide("tv_interact_menu_afternoon")] # TODO JUMP TO SCREEN
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("tv_interact_menu_afternoon"), Show("livingroom_afternoon")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7 

screen tv_interact_menu_evening:
    modal True

    add "images/overlay/tv/interact_bg.png"

    imagebutton:
        idle "images/overlay/tv/tv_idle.png"
        hover "images/overlay/tv/tv_hover.png"
        action [Hide("tv_interact_menu_evening")] # TODO JUMP TO SCREEN
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("tv_interact_menu_evening"), Show("livingroom_evening")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7 

screen tv_interact_menu_evening:
    modal True

    add "images/overlay/tv/interact_bg.png"

    imagebutton:
        idle "images/overlay/tv/tv_idle.png"
        hover "images/overlay/tv/tv_hover.png"
        action [Hide("tv_interact_menu_evening")] # TODO JUMP TO SCREEN
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("tv_interact_menu_evening"), Show("livingroom_evening")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7 

screen tv_interact_menu_night:
    modal True

    add "images/overlay/tv/interact_bg.png"

    imagebutton:
        idle "images/overlay/tv/tv_idle.png"
        hover "images/overlay/tv/tv_hover.png"
        action [Hide("tv_interact_menu_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("tv_options_night")] # TODO JUMP TO SCREEN
        xalign 0.15
        yalign 0.4

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("tv_interact_menu_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("livingroom_night")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.7 

screen tv_options_night:
    modal True

    add "images/overlay/tv/interact_bg.png"


    imagebutton:
        idle "images/overlay/tv/horror_idle.png"
        hover "images/overlay/tv/horror_hover.png"
        hover_sound "audio/sound/interface_sounds/drop_003.ogg"
        at tv_card_icon
        action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("trust_movie_1")] # TODO JUMP TO SCREEN
        xalign 0.0
        yalign 0.35

    imagebutton:
        idle "images/overlay/tv/desire_idle.png"
        hover "images/overlay/tv/desire_hover.png"
        hover_sound "audio/sound/interface_sounds/drop_003.ogg"
        at tv_card_icon
        action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("desire_movie_1")] # TODO JUMP TO SCREEN
        xalign 0.1
        yalign 0.35

    imagebutton:
        idle "images/overlay/tv/romance_idle.png"
        hover "images/overlay/tv/romance_hover.png"
        hover_sound "audio/sound/interface_sounds/drop_003.ogg"
        at tv_card_icon
        action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_movie_1")] # TODO JUMP TO SCREEN
        xalign 0.2
        yalign 0.35

    if robin_progression_level >= 2:
        imagebutton:
            idle "images/overlay/tv/desire2_idle.png"
            hover "images/overlay/tv/desire2_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("desire_movie_2")] # TODO JUMP TO SCREEN
            xalign 0.3
            yalign 0.35
    else:
        imagebutton:
            idle "images/overlay/tv/locked.png"
            hover "images/overlay/tv/locked.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            xalign 0.3
            yalign 0.35

    if robin_progression_level >= 2:
        imagebutton:
            idle "images/overlay/tv/horror2_idle.png"
            hover "images/overlay/tv/horror2_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("trust_movie_2")] # TODO JUMP TO SCREEN
            xalign 0.4
            yalign 0.35
    else:
        imagebutton:
            idle "images/overlay/tv/locked.png"
            hover "images/overlay/tv/locked.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            xalign 0.4
            yalign 0.35

    if robin_progression_level >= 2:
        imagebutton:
            idle "images/overlay/tv/romance2_idle.png"
            hover "images/overlay/tv/romance2_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_movie_2")] # TODO JUMP TO SCREEN
            xalign 0.5
            yalign 0.35
    else:
        imagebutton:
            idle "images/overlay/tv/locked.png"
            hover "images/overlay/tv/locked.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            xalign 0.5
            yalign 0.35

    if robin_progression_level >= 3:
        imagebutton:
            idle "images/overlay/tv/romance3_idle.png"
            hover "images/overlay/tv/romance3_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_movie_3")] # TODO JUMP TO SCREEN
            xalign 0.15
            yalign 0.7
    else:
        imagebutton:
            idle "images/overlay/tv/locked.png"
            hover "images/overlay/tv/locked.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            xalign 0.15
            yalign 0.7    

    if robin_progression_level >= 3:
        imagebutton:
            idle "images/overlay/tv/horror3_idle.png"
            hover "images/overlay/tv/horror3_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("trust_movie_3")] # TODO JUMP TO SCREEN
            xalign 0.25
            yalign 0.7
    else:
        imagebutton:
            idle "images/overlay/tv/locked.png"
            hover "images/overlay/tv/locked.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            xalign 0.25
            yalign 0.7

    if robin_progression_level >= 3:
        imagebutton:
            idle "images/overlay/tv/desire3_idle.png"
            hover "images/overlay/tv/desire3_hover.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("desire_movie_3")] # TODO JUMP TO SCREEN
            xalign 0.35
            yalign 0.7
    else:
        imagebutton:
            idle "images/overlay/tv/locked.png"
            hover "images/overlay/tv/locked.png"
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at tv_card_icon
            xalign 0.35
            yalign 0.7

    # if robin_progression_level >= 4:
    #     imagebutton:
    #         idle "images/overlay/tv/desire4_idle.png"
    #         hover "images/overlay/tv/desire4_hover.png"
    #         hover_sound "audio/sound/interface_sounds/drop_003.ogg"
    #         at tv_card_icon
    #         action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_movie_1")] # TODO JUMP TO SCREEN
    #         xalign 0.3
    #         yalign 0.7
    # else:
    #     imagebutton:
    #         idle "images/overlay/tv/locked.png"
    #         hover "images/overlay/tv/locked.png"
    #         hover_sound "audio/sound/interface_sounds/drop_003.ogg"
    #         at tv_card_icon
    #         xalign 0.3
    #         yalign 0.7

    # if robin_progression_level >= 4:
    #     imagebutton:
    #         idle "images/overlay/tv/affection4_idle.png"
    #         hover "images/overlay/tv/affection4_hover.png"
    #         hover_sound "audio/sound/interface_sounds/drop_003.ogg"
    #         at tv_card_icon
    #         action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_movie_1")] # TODO JUMP TO SCREEN
    #         xalign 0.4
    #         yalign 0.7
    # else:
    #     imagebutton:
    #         idle "images/overlay/tv/locked.png"
    #         hover "images/overlay/tv/locked.png"
    #         hover_sound "audio/sound/interface_sounds/drop_003.ogg"
    #         at tv_card_icon
    #         xalign 0.4
    #         yalign 0.7

    # if robin_progression_level >= 4:
    #     imagebutton:
    #         idle "images/overlay/tv/trust4_idle.png"
    #         hover "images/overlay/tv/trust4_hover.png"
    #         hover_sound "audio/sound/interface_sounds/drop_003.ogg"
    #         at tv_card_icon
    #         action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_movie_1")] # TODO JUMP TO SCREEN
    #         xalign 0.5
    #         yalign 0.7
    # else:
    #     imagebutton:
    #         idle "images/overlay/tv/locked.png"
    #         hover "images/overlay/tv/locked.png"
    #         hover_sound "audio/sound/interface_sounds/drop_003.ogg"
    #         at tv_card_icon
    #         xalign 0.5
    #         yalign 0.7            

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("tv_options_night"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("tv_interact_menu_night")] # TODO JUMP TO SCREEN
        xalign 0.25
        yalign 0.95

# MOVIES -------------------------------------------------------------------------------------------------------------------------------------------

label trust_movie_1:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch a horror movie called 'The Bloody Nurse' on FemFlix."
    scene livingroom_night with dissolve
    pro "Oh man, this looks good..."
    pro "It's rated R and the reviews are good."
    "Just before I hit play and start watching the movie, Robin walks into the living room."
    show robin tank with easeinleft
    robin "Hey there [protagonist_name]."
    robin "Uh... what are you watching?"
    pro "Just a horror movie that I found on FemFlix."
    pro "It's called 'The Bloody Nurse'."
    robin "A horror movie?"
    robin "Won't you be scared this late at night..."
    pro "Nah, I'll be fine. I've watched plenty of horror movies before."
    pro "You wanna join me?"
    robin "Oh no, I'm okay..."
    pro "Come on, it'll be fun!"
    pro "It's not scary, it's just a slasher flick."
    robin "I-I don't know..."
    pro "Here, come sit next to me."
    pro "I pat the spot next to me and make room for Robin."
    robin "Um... Okay, I guess I can join you for a bit..."
    scene black with dissolve 
    "He sits next to me and we begin watching the movie."
    scene trust_movie_1_1 with dissolve:
        zoom 1.1 xalign 0.99 yalign 0.5
        ease 5.0 xalign 0.5
    robin "Oh man... I really hope they don't go into that building..."
    "He's shaking and trembling a little."
    movie "I'm... coming... for... you..."
    movie "AAAAAAAAH!"
    scene trust_movie_1_1:
        zoom 1.1 xalign 0.5 yalign 0.5
        ease 0.2 zoom 1.3 xalign 0.35
        ease 0.05 zoom 1.25
    robin "AAAH! NO!"
    robin "Oh my god, they're gonna die!"
    scene trust_movie_1_1:
        zoom 1.25 xalign 0.35 yalign 0.5
        ease 2.0 zoom 1.0 xalign 0.5
    "Don't worry, Robin. It's just a movie."
    robin "I know, but it's scary!"
    pro "Come on, it's not that bad."
    scene trust_movie_1_1:
        zoom 1.0 xalign 0.5 yalign 0.5
    show trust_movie1_2 with dissolve:
        xpos 860 ypos 427
        ease 1.0 yoffset -8
        ease 1.0 yoffset 8
        repeat
    "I pat and rub his shoulder reassuringly and he seems to calms down a bit."
    pro "See, it's okay."
    robin "Um, okay..."
    pro "You can hold onto me if you need to."
    robin "..."
    scene black with dissolve
    "The movie plays for a while and Robin eventually gets more comfortable."
    "After the movie finishes, we get up off the couch and stretch a bit."
    scene livingroom_night with dissolve
    show robin tank smile with easeinbottom
    robin "Ah, that was actually really fun!"
    robin "I've never watched a horror movie with someone before."
    pro "Yeah, it's always better with a friend."
    show robin tank open at jumper
    robin "F-friend!"
    pro "Yea, friend!"
    robin "Right... friends..."
    show robin tank smile
    robin "Hehe..."
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 10{/color}"
    $ trust += 10
    scene black with dissolve
    "We both head off to bed for the night."
    jump day

label desire_movie_1:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch an erotic romance movie called 'Corrupting my Twink' on FemFlix."
    scene livingroom_night with dissolve
    pro "This looks really good..."
    pro "It's got a lot of steamy scenes and the reviews are very positive."
    "Just before I hit play and start watching the movie, Robin walks into the living room."
    show robin tank with easeinleft
    robin "Hey there, whatcha watchin'?"
    pro "Just a movie."
    show robin tank smile
    robin "Ooh, that sounds fun."
    robin "What kind of movie?"
    pro "..."
    pro "Well..."
    "Robin looks at the screen and reads the title of the movie."
    show robin tank open at jumper
    robin "CORRUPTING MY TWINK?!"
    pro "Hehe, yeah..."
    robin "What kind of movie is this?"
    pro "It's a romance with lots of... spicy scenes."
    robin "Oh my gosh, you're going to watch this?"
    pro "Hey, I'm an adult and these type of movies are my guilty pleasure."
    show robin tank
    robin "..."
    "I pat the spot next to me on the couch."
    pro "Come on, sit down."
    show robin tank open
    robin "N-no way! I can't watch this!"
    pro "Why not?"
    robin "It's too... lewd! I can't just watch this!"
    pro "So? Come on, it's not that bad."
    pro "There's some sweet moments too. It's a great story."
    show robin tank
    robin "..."
    robin "Fine... maybe I'll stay for a little."
    scene black with dissolve
    "Robin finally gives in and sits down next to me on the couch."
    scene desire_movie_1_1 with dissolve:
        zoom 1.2 xalign 0.3 yalign 0.5
        ease 5.0 zoom 1.0 xalign 0.5
    movie "O-oh, please, Sir! I don't think I can take any more of your cock!"
    movie "Haha! You'll be begging for more after this!"
    robin "This is... a lot."
    pro "It's a normal part of the storyline, don't worry."
    pro "It's erotic fiction, after all."
    robin "Mhm... right..."
    movie "Ahh! Fuck me, fuck me, fuck me! My body is yours!"
    pro "Uh oh, this is the scene."
    show desire_movie_1_2 with dissolve
    robin "Wait, what's going on?!"
    show desire_movie_1_3 with dissolve
    robin "Wait... he's grabbing his..."
    pro "Robin, are you okay?"
    robin "Uh... y-yeah! I'm okay! Just..."
    robin "Wow..."
    "Robin's face is bright red."
    pro "Are you getting into the 'plot' now?"
    robin "Ah... maybe a little."
    scene desire_movie_1_4 with dissolve
    "I notice Robin's dick getting erect through his boxers."
    "He was also breathing a lot heavier as the movie went on."
    robin "..."
    scene black with dissolve
    "We watch the rest of the movie together."
    scene livingroom_night with dissolve
    show robin tank smile with dissolve
    pro "So, did you enjoy the movie?"
    robin "Yea, I can see why you're into these types of films..."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 10{/color}"
    robin "Anyways, I should head to bed for the night."
    pro "Yeah, same here."
    scene black with dissolve
    "He heads to his room and I turn off the TV."
    $ desire += 10
    jump day

label affection_movie_1:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch a romance movie called 'Everlasting Love' on FemFlix."
    scene livingroom_night with dissolve
    pro "I've heard this one’s supposed to be really heartwarming..."
    pro "Maybe a bit sappy, but I could use some feel-good romance."
    show robin tank with easeinleft
    "Just as I’m about to start the movie, Robin walks into the living room."
    robin "Hey [protagonist_name], whatcha watching?"
    pro "Just a romance movie called 'Everlasting Love'."
    robin "A romance movie? I didn’t know you were into those."
    pro "Sometimes, yeah."
    pro "They can be nice when you're in that mood, you know?"
    robin "I guess... I usually avoid stuff like that."
    pro "Why don’t you join me? It might be fun."
    show robin tank open
    robin "Hmm... I don’t know, romance isn’t really my thing."
    pro "Come on, it’s always better to watch with someone. Besides, it might surprise you."
    robin "Well... okay, I guess I’ll give it a try."
    scene black with dissolve
    "Robin sits down next to me, looking a bit hesitant."
    scene affection_movie_1_1 with dissolve:
        zoom 1.2 xalign 0.3 yalign 0.5
        ease 5.0 zoom 1.0 xalign 0.5
    robin "I just hope it’s not too cheesy..."
    "We start watching the movie, and it’s clear that Robin is getting drawn into the story."
    movie "I promise to love you... forever and always."
    robin "That’s so corny..."
    pro "But it’s sweet, right?"
    scene affection_movie_1_2
    robin "Mmm... just a little."
    movie "Even if the world changes... my love for you never will."
    robin "Okay, I have to admit, that was kinda cute."
    pro "See? You’re enjoying it!"
    robin "Maybe just a little..."
    "Robin seems to relax a bit, leaning slightly closer as the movie goes on."
    pro "I knew you’d like it."
    robin "It’s not bad... I just didn’t expect it to make me feel this way."
    pro "Movies like this can be pretty touching."
    robin "Yeah... I guess it’s nice to imagine love like that."
    scene black with dissolve
    "We keep watching, and by the end of the movie, Robin’s got a soft smile on his face."
    scene livingroom_night with dissolve
    show robin tank smile with dissolve
    robin "Okay, I’ll admit it. That was actually really nice."
    robin "I didn’t think I’d enjoy a romance movie this much."
    pro "Told you! Sometimes you just need to let yourself enjoy the warm fuzzies."
    robin "Hehe, I guess so."
    robin "Thanks for inviting me to watch it with you."
    pro "Anytime! It was fun having you here."
    robin "Hehe, yeah... it was."
    robin "Maybe we can watch something together again sometime?"
    pro "I’d like that."
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 10{/color}"
    scene black with dissolve
    "He heads to his room and I turn off the TV."
    $ affection += 10
    jump day

label desire_movie_2:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch an erotic movie called 'Fifty Shades of Femboy' on FemFlix."
    scene livingroom_night with dissolve
    pro "This looks really good..."
    pro "A little erotic but..."
    pro "Fuck it."
    show robin tank with easeinleft
    "Right before I start the movie, Robin walks in the living room."
    robin "Oh, you about to watch something?"
    pro "Uh... yeah..."
    pro "It's uh..."
    pro "An erotic movie."
    show robin tank open
    robin "An erotic movie..."
    robin "Um..."
    pro "Yeah, not porn or anything like that."
    pro "Just very... spicy."
    pro "It's called 'Fifty Shades of Femboy'."
    robin "Oh...!"
    robin "I've actually heard of it online."
    pro "Yeah, I haven't seen it myself but there is a ton of buzz around it."
    show robin tank
    robin "..."
    robin "You mind if I watch a little with you?"
    pro "Oh... yeah! That's fine, I don't mind."
    show robin tank smile
    robin "Thanks..."
    scene black with dissolve
    "Robin sits next to me on the couch and I press play."
    pro "Alright, lets see how this goes..."
    scene desire_movie_2_1 with dissolve
    "We start watching the movie and it doesn't take me long to realize that this movie is way spicier than I expected."
    "It's definitely a lot more hardcore than what I'm used to."
    pro "Wow... that is a huge dildo."
    robin "Yeah... it's so big..."
    "Robin squirms a bit in his seat."
    movie "I can't take it anymore!"
    movie "I need to be inside of you right now!"
    movie "Turn over."
    robin "Oh my gosh..."
    pro "Are you doing okay?"
    robin "Y-yeah, I'm fine!"
    robin "I just wasn't expecting it to be so intense so early on."
    pro "Yeah, me either..."
    robin "Mm..."
    "We continue to watch the movie and soon we reach a particularly intense scene."
    robin "He's... he's really getting railed by that other guy..."
    pro "Y-yeah, that's..."
    pro "Wow..."
    "I can tell Robin is getting really into the movie."
    pro "Are you sure you're doing okay?"
    robin "Y-yeah, I'm fine..."
    robin "I... I'm just..."
    robin "I'm fine, I swear."
    robin "Let's keep watching."
    pro "Okay then..."
    scene desire_movie_2_2 with dissolve
    "Robin's breathing is getting heavier and heavier as he watches the movie."
    movie "You like it when I fuck you like this, don't you?"
    movie "Yeah... you're my femboy cumslut."
    movie "Take it, slut!"
    "I can see the outline of Robin's erection from the corner of my eyes."
    "He's even leaking a little precum..."
    "He's squirming a lot now, but he's so engrossed in the film he doesn't seem to notice."
    movie "I bet you want to feel my cum filling you up, don't you?"
    movie "You want it all over your face too..."
    robin "..."
    "Even my dick is throbbing, this movie is borderline pornography..."
    scene black with dissolve
    "I power through the rest of the movie with him. The ending is surprisingly heartwarming."
    scene livingroom_night with dissolve
    show robin tank smile with dissolve
    robin "Wow, that was a lot..."
    robin "I can see why this movie is so popular though, it just engrosses you within the story..."
    pro "Right... the 'story'."
    show robin tank open at jumper
    robin "S-shut up!"
    show robin tank
    robin "I wasn't paying attention to all that lewd stuff!"
    show robin tank smile
    robin "I was here for the plot."
    pro "Right..."
    robin "Hehe, well I'm glad I took a chance with it."
    robin "Thanks for letting me watch with you!"
    pro "Of course."
    pro "I'm glad I wasn't alone to watch that."
    "I notice that Robin is still erect, but he seems to be trying to cover it."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 20{/color}"
    show robin tank
    robin "Well uh... goodnight!"
    pro "Yeah, goodnight Robin!"
    scene black with dissolve
    "He heads to his room and I turn off the TV."
    $ desire += 20
    jump day

label trust_movie_2:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch a horror movie called 'My Vampire Roommate' on FemFlix."
    scene livingroom_night with dissolve
    pro "Huh, a horror movie about living with a roommate."
    pro "Could be a fun watch, the plot seems interesting..."
    show robin tank with easeinleft
    "Right before I turn it on, Robin walks into the living room."
    robin "Oh, hey."
    robin "Are you about to watch a movie?"
    pro "Yep! It's a new horror movie I found on FemFlix."
    robin "Oh..."
    robin "I was planning on joining you, but if its a horror movie then maybe I'll pass..."
    robin "It'll be scary this late at night..."
    pro "C'mon, don't be scared!"
    pro "The point of a horror movie is to be thrilling, not necessarily scary!"
    robin "I don't know..."
    robin "It's just... it's gonna give me nightmares, I'm not a big horror fan."
    pro "Well I won't force you but..."
    pro "I guess you're a chicken then."
    show robin tank open at jumper
    robin "W-what!"
    robin "I am NOT a chicken!"
    "Look's like his competitive side is coming out."
    pro "Then you should have no problem watching this movie."
    robin "F-fine... I'll watch it."
    robin "What's it called?"
    pro "My Vampire Roommate."
    show robin tank
    robin "My Vampire Roommate..."
    robin "Are you sure I won't be afraid of you by the end of this?"
    pro "I'm positive that you'll be safe, I have no intention of sucking your blood tonight."
    show robin tank smile
    robin "Hehe... alright, lets start the movie."
    scene black with dissolve
    "We begin watching the movie together and I can already see that Robin is getting scared."
    scene trust_movie_2_1 with dissolve:
        zoom 1.4 xalign 0.5 yalign 0.5
        ease 5.0 zoom 1.0
    "He keeps jumping at the slightest noises or any hint of a jump scare."
    pro "You okay there Robin?"
    robin "Y-yeah, I'm fine!"
    robin "I can handle a little scary movie."
    movie "Hey, I'm your new roommate!"
    movie "Nice to meet you man!"
    robin "Oh, the two main characters are meeting each other."
    pro "Yeah, it seems like they are hitting it off pretty well."
    robin "I wonder which one is the vampire..."
    "Robin watches intensely, despite clearly being scared."
    movie "I'm gonna go to bed now, thanks for showing me around!"
    movie "No worries man, it's nice to have the company!"
    pro "Wow... they seem really nice."
    pro "It sucks that one of them is a vampire... but who is it?"
    robin "M-maybe it's a different character..."
    robin "Maybe both of the guys are just regular humans."
    pro "Maybe..."
    "We continue to watch and soon the horror elements of the movie start to show themselves."
    movie "I... I need to feed..."
    movie "Need... blood!"
    "Robin starts to get more and more scared."
    movie "Ah... fresh blood..."
    movie "I can sense it nearby..."
    "The suspense is killing us."
    robin "Is he... is he gonna suck his blood?"
    "The suspense builds and builds."
    movie "You're mine...!"
    "There's a sudden jumpscare!"
    scene black with dissolve
    robin "AHH!"
    "Robin squeals and jumps onto me."
    scene trust_movie_2_2 at slight_wobble with dissolve:
        zoom 1.5 xalign 0.5 yalign 0.5
        ease 3.0 zoom 1.05 xalign 0.5
    pro "Uh... Robin..."
    robin "[protagonist_name]! HES SUCKING HIS BLOOD!"
    robin "ITS HIS OWN ROOMMATE!"
    "He doesn't seem to realize what's happening..."
    robin "This is so fucked up..."
    "Do I move... do I say something?"
    pro "Uh..."
    robin "Huh?"
    pro "Robin..."
    pro "You're on my lap right now."
    robin "I... I'm on..."
    "His face goes bright red."
    robin "S-sorry... I'm just really scared!"
    pro "I-it's okay!"
    pro "You got startled!"
    scene trust_movie_2_1 with dissolve
    "He slowly gets off of me."
    robin "S-sorry about that..."
    pro "It's no worries, Robin."
    scene black with dissolve
    "We watch the rest of the movie mostly in silence, with Robin squealing and screaming at the scary parts."
    scene livingroom_night with dissolve
    show robin tank smile with dissolve
    robin "That... that was a really intense movie..."
    robin "Who knew vampires could still be so scary..."
    pro "Honestly it was a lot more bloody than I expected."
    pro "I enjoyed it though, I always get a good thrill out of these types of movies!"
    robin "Yeah it was fun!"
    show robin tank open
    robin "And uh... sorry again."
    robin "I didn't mean to jump on you..."
    pro "It's okay, I know how scary those movies can get."
    pro "You don't have to feel embarrassed or anything."
    show robin tank smile
    "He smiles and nods."
    robin "Thanks, I'm glad you're understanding."
    show robin tank
    "He looks away, his face turning red again."
    pro "You should uh... go get some rest."
    robin "O-oh yeah, good idea."
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 20{/color}"
    $ trust += 20
    scene black with dissolve
    "He quickly leaves the living room, heading to his bedroom for the night."
    "I shut off the TV and head to bed as well."
    jump day

label affection_movie_2:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch a romantic movie called 'Ocean Blue Eyes' on FemFlix."
    scene livingroom_night with dissolve
    pro "Hm, this looks cute."
    pro "Seems like the story follows two people discovering their love for each other while stranded on a beach."
    pro "Could be a fun watch!"
    show robin tank with easeinleft
    "Before I can start the movie, Robin walks into the living room."
    robin "Oh, hey."
    robin "What are you watching?"
    pro "I was just about to start a new movie called 'Ocean Blue Eyes'."
    robin "Oh, what is it about?"
    pro "Based on the description, it looks like two people get stranded on a beach. Maybe on some deserted island?"
    pro "Anyways, it's a romance movie, so it should be a wholesome watch."
    pro "You want to watch it with me?"
    show robin tank smile
    robin "S-sure! It sounds like a cute premise."
    pro "Alright then, let's start it up!"
    scene black with dissolve
    "We begin watching the movie and it starts off pretty slow."
    "It's just the two main characters on a boat together."
    "They seem to have some chemistry, but not much else has happened so far."
    scene affection_movie_2_1 with dissolve
    pro "I don't think I've seen this actor before."
    robin "Me either."
    robin "I wonder if they're new to acting or something."
    pro "Could be, but they're doing a good job."
    robin "Yeah, I agree. They both have great chemistry."
    pro "It's almost like they've known each other for years."
    pro "Like they're just meant to be or something."
    scene affection_movie_2_3
    robin "Heh... yeah..."
    "We continue to watch the movie. The chemistry between the two main characters is undeniable."
    "It's clear that they are falling in love with each other."
    "They eventually get to a romantic scene together on the beach."
    robin "Are they gonna kiss..."
    robin "God, I just want them to confess to each other already!"
    scene affection_movie_2_2
    robin "It's clear they both like each other, but both of them are too scared to say something..."
    pro "I know, it's pretty frustrating to watch."
    pro "But that's part of what makes it so good."
    robin "Yeah... I guess..."
    robin "But still!"
    robin "I want to see them kiss!"
    robin "I want them to live happily ever after!"
    scene affection_movie_2_3
    robin "Gosh, they're perfect for each other..."
    "I can tell that Robin is really into this movie."
    pro "You're really invested in the romance, huh?"
    robin "Hehe... y-yeah..."
    robin "Is there something wrong with that?"
    pro "No, no! It's cute to see how passionate you are."
    "Robin blushes and gets a little flustered."
    "It's adorable..."
    scene affection_movie_2_2
    robin "H-hey, the movies not over yet."
    robin "I still haven't seen the two of them kiss yet!"
    pro "Oh yeah, right!"
    pro "Lets finish this."
    pro "I wanna see how it ends too."
    scene black with dissolve
    "Robin continues watching the movie with intensity."
    "Eventually, the two characters kiss and are rescued from the beach."
    "They end up getting married and living a happy life by the end of the movie."
    scene livingroom_night with dissolve
    show robin tank smile with dissolve
    robin "That was... so wholesome..."
    robin "I'm so happy for them!"
    pro "Yeah, me too."
    pro "They were a great couple."
    robin "Yeah, they deserved that happiness."
    robin "Well, thanks for letting me watch this with you, it was really cute!"
    pro "Of course, I'm glad you liked it!"
    pro "I'm a sucker for cheesy romance films, so it's always nice when someone can share my enjoyment of them!"
    robin "For sure, hehe."
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 20{/color}"
    $ affection += 20
    robin "Anyways, I'm going to go to bed now."
    robin "Goodnight [protagonist_name]!"
    pro "Goodnight Robin, sweet dreams!"
    scene black with dissolve
    "Once he leaves, I shut the TV off and head to bed."
    jump day

label trust_movie_3:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch a horror movie called 'The Mysterious Woman' on FemFlix."
    scene livingroom_night with dissolve
    pro "This looks really creepy..."
    pro "I like horror movies though, so..."
    show robin tank with easeinleft
    "Right before I turn it on, Robin walks into the living room."
    robin "Oh, you're watching a movie?"
    pro "Yeah, I found this horror movie called 'The Mysterious Woman'."
    pro "It's about a creepy woman who crawls out of a television and murders people."
    pro "Apparently, it's based on a real urban legend..."
    show robin tank open
    robin "W-what!"
    robin "Um... that sounds... scary!"
    robin "Maybe you shouldn't watch it..."
    pro "It'll be fine!"
    pro "Besides, this is just a movie, right?"
    show robin tank
    robin "I guess..."
    pro "Come on, it'll be fun!"
    pro "Don't you want to watch it with me? It'll be a good bonding experience."
    robin "I... I don't know..."
    robin "I think I'll pass on this one, even just hearing about it is giving me the creeps..."
    pro "Are you sure?"
    pro "I'll be here to protect you!"
    show robin tank smile
    robin "Hehe, thank you but..."
    robin "I just don't want to watch it."
    robin "You have fun though, okay?"
    robin "Just make sure to leave the TV off when you're done, okay?"
    pro "Oh yeah, no problem!"
    pro "Have a good night!"
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 30{/color}"
    $ trust += 30
    hide robin with easeoutleft
    "Robin leaves the living room."
    pro "I guess I'm watching it alone tonight."
    scene trust_movie_3_1 with dissolve
    "I turn on the movie."
    "I watch for about half an hour, but I can feel myself starting to fall asleep."
    "The movie isn't even remotely scary, it's just bad."
    stop music fadeout 1.0
    scene black with dissolve
    "After a little bit, I end falling asleep on the couch."
    "..."
    "..."
    play music horror fadein 1.0
    scene trust_movie_3_2 with dissolve
    "I wake up in the middle of the night."
    pro "Damn, I fell asleep on the couch..."
    "It's pitch black."
    pro "I should probably go to bed."
    pro "I wonder if I left the movie playing or not..."
    "I check the TV and its on, but the screen is completely black."
    pro "That's a bit weird... I wonder if I accidentally turned off the sound or something?"
    scene trust_movie_bg with dissolve
    "Suddenly, white static noise appears on the TV."
    pro "What the fuck..."
    "I try turning off the TV with the remote, but the button doesn't work."
    pro "Uh..."
    pro "What the hell is happening..."
    show ghost_trust_jitter with dissolve
    "Out of nowhere, a scary white figure appears in front of the TV."
    "Their skin is grey and pale, their eyes glowing blue."
    "They are wearing a long white shirt..."
    pro "Wh-what...."
    pro "What... who are you..."
    hide ghost_trust_jitter with dissolve
    show ghost_trust_jitter2 with dissolve
    "In an instant, they appear bent over on the coffee table in front of me."
    "They look kind of like... Robin?"
    pro "Robin...?"
    pro "If you're playing some sort of prank on me, it's not funny..."
    scene trust_movie_3_7 with dissolve
    "In another instant, the creature appears on top of me."
    "They are sitting on my lap..."
    pro "What the fuck..."
    pro "What do you want..."
    "I want to push them off and run, but my body is completely frozen in fear."
    "I can't even scream."
    scene black with dissolve
    "In a last ditch effort, I try closing my eyes."
    "Maybe this is all just a dream..."
    pro "Please be a dream..."
    pro "Please be a dream...."
    pro "Please-"
    "..."
    pro "Huh?"
    play sound hand_job fadein 0.5 loop
    show trust_movie_3_8
    hide trust_movie_3_8
    scene ghost_trust_jitter3 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.35 yalign 1.0 zoom 1.07
        ease 0.3 yalign 0.5 zoom 1.0
        repeat       
    "I open my eyes and the creature is giving me a handjob."
    pro "What are you doing..."
    "The creature doesn't respond."
    "Their hair is exactly like Robin's though, and their eyes are blue just like his."
    "This must be some sort of fucked up dream..."
    pro "F-fuck..."
    pro "Your hands feel so good..."
    "The figure continues stroking my cock, their hands moving quickly and skillfully."
    "I can't control my body, and I can't resist the pleasure..."
    pro "Ah...!"
    pro "Fuck...!"
    "I can't believe I'm getting a hand-job from a ghost..."
    pro "At this rate... I'm going to..."
    menu:
        "Cum":
            pro "Ah...! I'm going to cum!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    show trust_movie_3_11
    hide trust_movie_3_11
    scene ghost_trust_jitter4 with dissolve:
        zoom 1.5 xalign 0.7 yalign 0.5
        ease 4.0 zoom 1.0 xalign 0.5
    "I cum all over the creature's face."
    pro "Holy fuck..."
    pro "That's a lot..."
    pro "Uh..."
    pro "Can you tell me who, or what, you are now?"
    "The creature doesn't respond."
    stop music fadeout 1.0
    scene trust_movie_3_14 with dissolve
    "In an instant, it disappears again."
    pro "That was... really fucking weird."
    scene black with dissolve
    "I get up and head to bed after cleaning myself up."
    jump day

label affection_movie_3:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch a romantic movie called 'Office Love' on FemFlix."
    scene livingroom_night with dissolve
    pro "This looks cute."
    pro "It seems like it's about a guy who falls in love with a coworker of his..."
    show robin tank with easeinleft
    "Before I can start the movie, Robin walks into the living room."
    robin "Hey, what are you watching?"
    pro "I'm about to watch this new movie I found on FemFlix called 'Office Love'."
    pro "It's about someone who falls in love with their coworker."
    show robin tank smile
    robin "Oh, that's a pretty cute premise."
    pro "Yeah, I like the idea of it."
    pro "So uh, you want to watch it with me?"
    show robin tank open
    robin "Oh, well I don't really have time for that tonight..."
    robin "I have to be up early tomorrow, I was just coming outside to grab a glass of water."
    show robin tank
    robin "Maybe we can watch a movie together another night, okay?"
    pro "Oh, okay."
    pro "Goodnight, Robin!"
    hide robin with easeoutleft
    "Robin heads back to his bedroom."
    "I guess it'll just be me tonight..."
    scene trust_movie_3_1 with dissolve
    "I turn on the movie and begin watching."
    "It starts off pretty slow, and it's just a typical romance movie at first."
    pro "The main character seems to have a nice friendship with the person he's in love with..."
    "As the movie goes on, I start getting really bored."
    stop music fadeout 1.0
    scene black with dissolve
    "Before I know it, I've started dozing off and fall asleep."
    "..."
    "..."
    robin "[protagonist_name]..."
    "Hm..."
    "Huh...?"
    "Did someone just say my name..."
    scene white with dissolve
    "I open my eyes and see that I'm no longer in the living room."
    pro "What the fuck..."
    pro "Where the hell am I?"
    "I'm in some sort of office building..."
    pro "Uh... what the fuck..."
    robin "Hey, there you are!"
    robin "I've been looking for you, why'd you wander off?"
    play music sensual fadein 3.0
    scene affection_movie_3_1 with dissolve:
        zoom 1.3 xalign 0.3 yalign 0.5
        ease 5.0 zoom 1.0 xalign 0.5
    "I turn around to see Robin."
    "He's wearing an white, professional buttoned shirt."
    robin "C'mon, you agreed to work overtime with me!"
    robin "There's a little bit of work left."
    pro "Uh... I'm sorry but I'm really confused."
    pro "I'm not sure what's happening right now..."
    robin "You don't remember?"
    robin "Geez, did you drink too much coffee or something? Hehe!"
    pro "What?"
    robin "We have that huge company deadline coming up, so you agreed to work overtime with me so we could finish it!"
    robin "Everyone else has gone home already, so it's just you and me."
    robin "Don't you remember?"
    pro "Uh, I guess..."
    robin "You guess? Hehe..."
    robin "Well, sit down. Let's work through some of these papers!"
    "Is this some kind of dream?"
    "It feels too real to be a dream..."
    scene white with dissolve
    pro "Yeah, lets get this done so we can go home."
    scene affection_movie_3_2 with dissolve:
        zoom 1.3 xalign 0.3 yalign 0.5
        ease 5.0 zoom 1.0 xalign 0.5   
    robin "I know it's not the most fun, but I appreciate you staying with me, hehe."
    "Robin and I start working through a bunch of paperwork."
    "It feels like real paperwork, this is so fucking strange..."
    robin "Hey... I'm sorry about making you stay late with me."
    robin "I've just been having a hard time keeping up with all the work we have to do lately..."
    pro "No, it's no problem Robin!"
    pro "I like working overtime with you."
    pro "Even if it's not very fun, I still enjoy spending time with you."
    robin "Hehe, shut up!"
    pro "It's true though!"
    "He smiles at me softly."
    robin "Hey, um..."
    robin "You know, we're the only ones here right now."
    robin "And uh... no one will be coming in or anything."
    robin "We could always take a little break..."
    robin "If you want to, I mean..."
    robin "We can take a break from our work."
    pro "Oh, uh... yeah!"
    pro "I think it would be good to take a break right now."
    scene white with dissolve
    "Robin smiles and gets up."
    robin "Good, because I've had something in mind for a while."
    pro "What are you talking about?"
    "Robin crawls underneath my desk."
    robin "I'm talking about this~"
    pro "W-wait, Robin!"
    scene affection_movie_3_3 with dissolve
    "He begins pulling my pants down, revealing my erect cock."
    robin "Wow, you're already so hard!"
    robin "I can't believe it..."
    pro "Robin, wait!"
    robin "Why are you so nervous?"
    robin "I'm going to give you a blowjob, isn't that what you want?"
    pro "I mean... yes, but..."
    pro "This is really sudden!"
    robin "Don't worry about that."
    robin "Just sit back and let me take care of you."
    "I'm in some kind of crazy alternate universe and my roommate is giving me a blowjob..."
    "Is this what being horny and tired does to you?"
    scene white with dissolve
    robin "Now then, let's get started~"
    play sound suck_2 fadein 0.5 loop 
    scene affection_movie_3_4 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.35 yalign 1.0 zoom 1.07
        ease 0.3 yalign 0.5 zoom 1.0
        repeat
    "Without hesitation, Robin begins sucking and licking the tip of my cock."
    robin "Mmm~"
    pro "Oh fuck..."
    robin "You taste so good already~"
    robin "I can't wait until we go further~"
    pro "Oh my god..."
    "Robin takes my dick into his mouth and slowly begins bobbing his head up and down on it."
    pro "Fuck... that's good..."
    pro "Your mouth is so soft and warm..."
    robin "You're so big, it's hard to fit all of you in my mouth."
    robin "But I'll make it work."
    pro "Oh god..."
    pro "Are you sure we won't get caught..."
    robin "Mmm, positive."
    robin "We're all alone right now, hehe."
    "Robin continues sucking me off, his tongue swirling around my dick."
    robin "Mmmm~"
    pro "Fuck..."
    robin "Does that feel good?"
    pro "Y-yes, keep going!"
    robin "Hehe, anything to make my favourite coworker happy~"
    "Robin continues sucking me off faster and faster."
    pro "Oh fuck, I'm going to cum soon!"
    pro "Keep going!"
    robin "Mmm..."
    robin "I'm not stopping until I've milked you dry..."
    pro "F-fuck..."
    robin "Mmmm~"
    "His lips continue tightly sucking on my dick, bringing me closer and closer to climax."
    menu:
        "Cum":
            pro "Oh god...!"
            pro "F-fuck! I'm cumming!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound slight_exertion_slow fadein 0.5
    scene affection_movie_3_5 with dissolve:
        zoom 1.5 xalign 0.7 yalign 0.5
        ease 4.0 zoom 1.0 xalign 0.5
    "I shoot a large load of cum into Robin's mouth."
    pro "H-holy fuck!"
    robin "Mmmm..."
    robin "So much..."
    "Robin takes my entire load into his mouth, showing off all of my cum as it drips from his tongue."
    robin "You came a lot, hehe."
    pro "Y-yeah..."
    pro "That was... incredible..."
    robin "I'm glad, you deserve it!"
    robin "You work so hard, I figured it's the least I could do."
    pro "Thanks, Robin..."
    pro "I appreciate it a lot."
    robin "You're welcome!"
    robin "But now it's time for you to return the favour."
    pro "R-return the favour...?"
    scene white with dissolve
    "Before I can react, Robin stands up and turns around, his ass facing me."
    stop sound fadeout 1.0
    scene affection_movie_3_6 with dissolve
    "He bends over and pulls down his pants, revealing his cute pink ass."
    robin "Fuck me~"
    pro "W-what!"
    pro "We're going to get caught!"
    robin "No, I promise."
    robin "Just be quick about it!"
    scene white with dissolve
    stop music fadeout 1.0
    "Right as I reach out to grab Robin, he disappears."
    pro "Wait... no..."
    scene black with dissolve
    pro "Robin..."
    "..."
    scene trust_movie_3_1 with dissolve
    "I wake up and I'm back in the living room."
    pro "Fuck..."
    pro "Why did I have to wake up at the best part..."
    pro "I wanted him to ride my dick..."
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 30{/color}"
    $ affection += 30
    "That was the most vivid dream I've ever had..."
    scene black with dissolve
    "I shut off the TV and head to bed."
    jump day

label desire_movie_3:
    define movie = Character("Movie", who_color = "#ff5555", callback = name_callback, cb_name = None)
    scene black with dissolve
    "I decide to watch an erotic movie called 'My Femboy Secretary' on FemFlix."
    scene livingroom_night with dissolve
    pro "Hmm..."
    pro "Well, this is a more hardcore film..."
    show robin tank with easeinleft
    "Before I turn it on, Robin walks into the living room."
    robin "Hey, you about to watch a movie?"
    pro "Oh yeah, just about to start it."
    pro "It's an erotic movie called 'My Femboy Secretary', it's about this businessman and his femboy secretary..."
    show robin tank open
    robin "F-femboy secretary!"
    robin "Um... that sounds..."
    pro "Yeah it's a bit more hardcore compared to what I usually watch, but I've been a little curious to see how it is."
    show robin tank
    robin "I see..."
    pro "Would you like to watch it with me?"
    robin "I... I would love to but..."
    robin "I really only came out of my room to grab some water before heading to bed..."
    robin "But uh... have a good rest of your night, okay?"
    pro "Okay, I will!"
    hide robin with easeoutleft
    "Robin heads to the kitchen to get water, then goes back to his bedroom."
    pro "I wonder what got him so flustered..."
    pro "Was it really that awkward of a movie title?"
    "I guess I'll watch it alone..."
    scene trust_movie_3_1 with dissolve
    "I turn on the movie."
    "I quickly realize that this is a very intense erotic film..."
    pro "Holy fuck, that's a lot of rope."
    pro "This secretary is being tied up in the office."
    pro "And... he's sucking his boss off now, wow!"
    "I continue watching the movie, it's definitely a lot more hardcore than what I'm used to, but it's also a little arousing."
    "Despite this, the story itself is very boring."
    stop music fadeout 1.0
    scene black with dissolve
    "I slowly start to fall asleep."
    "..."
    "..."
    "..."
    pro "...?"
    scene white with dissolve
    "I open my eyes and I'm in a bedroom."
    play music sensual fadein 3.0
    scene desire_movie_3_1 with dissolve
    pro "R-robin?!"
    "Robin is standing in front of me, dressed up in a sexy office outfit."
    pro "Wh-what's happening...?"
    robin "You know exactly whats happening."
    robin "Everytime we're in the office, you're always eyeing me down..."
    robin "I know you want me, and I'm ready to give myself to you."
    pro "Wait, what!"
    pro "Robin, what's gotten into you!"
    robin "Oh, nothing yet~"
    robin "But that's about to change."
    show white with dissolve
    scene desire_movie_3_2 with dissolve
    "Robin lays down on the bed and spreads his legs."
    pro "H-hold on!"
    pro "Let me process this!"
    robin "C'mon, don't you want to fuck me? You've fantasized about it for so long, haven't you?"
    "Fuck, I do want to fuck him..."
    "Maybe I should just go along with it..."
    robin "Don't keep me waiting, you've had plenty of time to admire me already."
    robin "How about you eat me out a little first, just to warm me up~"
    pro "Uh... o-okay."
    show tongue with dissolve:
        xpos 285 ypos 833
        anchor (0.5, 1.0)
        ease 1.0 rotate 15
        ease 1.0 rotate -15
        repeat
    "I crawl between his legs and begin to lick his asshole."
    robin "A-ahh!"
    robin "Fuck, that's it..."
    robin "Lick my ass...!"
    pro "Fuck..."
    robin "God, that's good..."
    robin "Your tongue feels so nice...!"
    "I can tell he's loving every second of this."
    "I keep licking his ass, making sure to tease his hole with my tongue."
    robin "A-ahh!"
    robin "I want your cock in me, I need you inside me so badly!"
    "I slowly pull out my tongue."
    hide tongue with dissolve
    pro "Maybe you should convince me..."
    robin "Hm?"
    scene white with dissolve
    pro "Let me see how good that mouth of yours feels..."
    "I lay down and Robin crawls towards me."
    robin "Hehe, do you want me to-"
    play sound suck_2 fadein 1.0 loop
    scene desire_movie_3_3 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.35 yalign 1.0 zoom 1.07
        ease 0.3 yalign 0.5 zoom 1.0
        repeat
    "I shove my cock into his mouth and begin face fucking him, not giving him even a moment to prepare himself."
    pro "Fuck yes..."
    "His moans are muffled by my dick, but I can tell he's loving every second of this."
    robin "Mmmf!"
    pro "That's it, such a good boy..."
    "I continue fucking his face."
    "God, this feels fucking amazing..."
    robin "Mmmphh! G-glkh!"
    pro "Yes, that's it, take it all you whore."
    robin "G-glkh!"
    robin "Mmmhmmm~!"
    pro "Do you like that?"
    pro "Tell me how much you like it."
    robin "Mmmm!~"
    stop sound fadeout 0.5
    scene desire_movie_3_4 with dissolve    
    play sound pleasured_exertion_slow fadein 0.5
    "I pull my dick out of his mouth."
    robin "P-please~!"
    robin "I need you to fuck me!"
    pro "I've teased you enough..."
    pro "Get on your hands and knees, I want to take you from behind."
    robin "O-of course sir!"
    scene white with dissolve
    "Robin flips over and eagerly gets on all fours."
    robin "I can handle it, please! Give it all to me!"
    stop sound fadeout 0.5
    "Right before I insert my dick into him, he disappears."
    stop music fadeout 1.0
    pro "Wait... no..."
    pro "No...!"
    show black with dissolve
    scene trust_movie_3_1 with dissolve
    "I wake up in the living room."
    pro "Fuck, right as the dream was getting good..."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 30{/color}"
    $ desire += 30
    jump day