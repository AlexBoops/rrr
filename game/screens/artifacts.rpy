default artifacts_page = 0

screen artifacts:
    modal True

    add "images/overlay/ui/artifact_menu.png"

    if artifact1 and artifact2 and artifact3 and artifact4 and artifact5 and artifact6 and artifact7 and artifact8 and artifact9 and artifact10 and artifact11 and artifact12:
        $ achievement.grant("artifacts_complete")

    frame:
        xalign 0.5
        yalign 0.5
        background None

        viewport:
            mousewheel True
            draggable True
            area (0, 0, 1785, 704)


        if artifacts_page == 0:
            hbox:
                xalign 0.07
                yalign 0.8
                spacing 10

                if artifact1:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact1_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact1_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a1_locked.png"
                        hover "images/overlay/ui/artifacts/a1_locked.png"

                
                if artifact2:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact2_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact2_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a2_locked.png"
                        hover "images/overlay/ui/artifacts/a2_locked.png"


                if artifact3:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact3_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact3_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a3_locked.png"
                        hover "images/overlay/ui/artifacts/a3_locked"

            if artifact1 and artifact2 and artifact3:
                imagebutton:
                    xpos 114
                    ypos 224
                    idle "images/overlay/ui/artifacts/collectible_1.png"
                    hover "images/overlay/ui/artifacts/collectible_1.png"
            else:
                imagebutton:
                    xpos 114
                    ypos 224
                    idle "images/overlay/ui/artifacts/collectible_1_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_1_locked.png"

            hbox:
                xalign 0.34
                yalign 0.8
                spacing 10

                if artifact4:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact4_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact4_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a4_locked.png"
                        hover "images/overlay/ui/artifacts/a4_locked.png"


            if artifact4:
                imagebutton:
                    xpos 487
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_3.png"
                    hover "images/overlay/ui/artifacts/collectible_3.png"
            else:
                imagebutton:
                    xpos 487
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_3_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_3_locked.png"


            hbox:
                xalign 0.56
                yalign 0.8
                spacing 10

                if artifact5:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact5_unlocked.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact5_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a5_locked.png"
                        hover "images/overlay/ui/artifacts/a5_locked.png"

                if artifact6:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact6_unlocked.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/a6_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a6_locked.png"
                        hover "images/overlay/ui/artifacts/a6_locked.png"

            if artifact5 and artifact6:
                imagebutton:
                    xpos 890
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_4.png"
                    hover "images/overlay/ui/artifacts/collectible_3.png"
            else:
                imagebutton:
                    xpos 890
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_4_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_4_locked.png"

            hbox:
                xalign 0.89
                yalign 0.8
                spacing 10

                if artifact3:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact3_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact3_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a3_locked.png"
                        hover "images/overlay/ui/artifacts/a3_locked"

                if artifact4:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact4_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact4_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a4_locked.png"
                        hover "images/overlay/ui/artifacts/a4_locked.png"

                if artifact5:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact5_unlocked.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact5_hover.png"

                if artifact6:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact6_unlocked.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/a6_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a6_locked.png"
                        hover "images/overlay/ui/artifacts/a6_locked.png"

            if artifact1 and artifact2 and artifact3 and artifact4 and artifact5 and artifact6:
                imagebutton:
                    xpos 1300
                    ypos 333
                    idle "images/overlay/ui/artifacts/collectible_2.png"
                    hover "images/overlay/ui/artifacts/collectible_2.png"
            else:
                imagebutton:
                    xpos 1300
                    ypos 333
                    idle "images/overlay/ui/artifacts/collectible_2_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_2_locked.png"

            imagebutton:
                xalign 1.0
                yalign 0.9
                idle "images/overlay/ui/artifacts/next_button.png"
                hover "images/overlay/ui/artifacts/next_button_hover.png"
                action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), SetVariable("artifacts_page", artifacts_page + 1)]

        if artifacts_page == 1:
            hbox:
                xalign 0.115
                yalign 0.8
                spacing 10

                if artifact7:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact7_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact7_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a7_locked.png"
                        hover "images/overlay/ui/artifacts/a7_locked.png"

            if artifact7:
                imagebutton:
                    xpos 100
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_5.png"
                    hover "images/overlay/ui/artifacts/collectible_5.png"
            else:
                imagebutton:
                    xpos 100
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_6_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_6_locked.png"                   

            hbox:
                xalign 0.33
                yalign 0.8
                spacing 10

                if artifact8:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact8_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact8_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a8_locked.png"
                        hover "images/overlay/ui/artifacts/a8_locked.png"

            if artifact8:
                imagebutton:
                    xpos 490
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_6.png"
                    hover "images/overlay/ui/artifacts/collectible_6.png"
            else:
                imagebutton:
                    xpos 490
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_6_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_6_locked.png"  

            hbox:
                xalign 0.565
                yalign 0.8
                spacing 10

                if artifact9:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact9_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact9_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a9_locked.png"
                        hover "images/overlay/ui/artifacts/a9_locked.png"

            if artifact9:
                imagebutton:
                    xpos 887
                    ypos 301
                    idle "images/overlay/ui/artifacts/collectible_7.png"
                    hover "images/overlay/ui/artifacts/collectible_7.png"
            else:
                imagebutton:
                    xpos 887
                    ypos 301
                    idle "images/overlay/ui/artifacts/collectible_7_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_7_locked.png"

            hbox:
                xalign 0.863
                yalign 0.8
                spacing 10

                if artifact7:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact7_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact7_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a7_locked.png"
                        hover "images/overlay/ui/artifacts/a7_locked.png"

                if artifact8:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact8_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact8_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a8_locked.png"
                        hover "images/overlay/ui/artifacts/a8_locked.png"

                if artifact9:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact9_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact9_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a9_locked.png"
                        hover "images/overlay/ui/artifacts/a9_locked.png"

            if artifact9:
                imagebutton:
                    xpos 1340
                    ypos 301
                    idle "images/overlay/ui/artifacts/collectible_8.png"
                    hover "images/overlay/ui/artifacts/collectible_8.png"
            else:
                imagebutton:
                    xpos 1340
                    ypos 301
                    idle "images/overlay/ui/artifacts/collectible_7_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_7_locked.png"

            imagebutton:
                xalign 0
                yalign 0.9
                idle "images/overlay/ui/artifacts/back_button.png"
                hover "images/overlay/ui/artifacts/back_button_hover.png"
                action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), SetVariable("artifacts_page", artifacts_page - 1)]

            imagebutton:
                xalign 1.0
                yalign 0.9
                idle "images/overlay/ui/artifacts/next_button.png"
                hover "images/overlay/ui/artifacts/next_button_hover.png"
                action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), SetVariable("artifacts_page", artifacts_page + 1)]                

        if artifacts_page == 2:
            hbox:
                xalign 0.5
                yalign 0.8
                spacing 10

                if artifact10:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact10_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact10_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a10_locked.png"
                        hover "images/overlay/ui/artifacts/a10_locked.png"

                if artifact11:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact11_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact11_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a11_locked.png"
                        hover "images/overlay/ui/artifacts/a11_locked.png"

                if artifact12:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/artifact12_idle.png"
                        action [Play("sound", "audio/music/collect_item.mp3")]
                        hover "images/overlay/ui/artifacts/artifact12_hover.png"
                else:
                    imagebutton:
                        idle "images/overlay/ui/artifacts/a12_locked.png"
                        hover "images/overlay/ui/artifacts/a12_locked.png"

            if artifact10 and artifact11 and artifact12:
                imagebutton:
                    xalign 0.5
                    ypos 227
                    idle "collectible_9"
                    hover "collectible_9"
            else:
                imagebutton:
                    xalign 0.5
                    ypos 227
                    idle "images/overlay/ui/artifacts/collectible_9_locked.png"
                    hover "images/overlay/ui/artifacts/collectible_9_locked.png"

            imagebutton:
                xalign 0
                yalign 0.9
                idle "images/overlay/ui/artifacts/back_button.png"
                hover "images/overlay/ui/artifacts/back_button_hover.png"
                action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), SetVariable("artifacts_page", artifacts_page - 1)]

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("artifacts")]
        tooltip "Go back"
        xalign 1.0
        yalign 0.05

image collectible_9:
    Movie(play="images/overlay/ui/artifacts/collectible_vid.webm")
    zoom 0.5