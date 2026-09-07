screen date_menu:
    modal True

    add "images/overlay/date_menu/date_bg.png"

    if robin_progression_level >= 3:
        vbox:
            align (0, 0.5)
            imagebutton:
                idle "images/overlay/date_menu/location1_idle.png"
                hover "images/overlay/date_menu/location1_hover.png"
                action [Hide("date_menu")]
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Stuffed Bear ($20){/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'
    else:
        vbox:
            align (0, 0.5)
            imagebutton:
                idle "images/overlay/date_menu/location_locked.png"
                hover "images/overlay/date_menu/location_locked.png"
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Locked{/color} {color=#FF5454}(Progression Level 4){/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'

    if robin_progression_level >= 4:
        vbox:
            align (0.5, 0.5)
            imagebutton:
                idle "images/overlay/date_menu/location1_idle.png"
                hover "images/overlay/date_menu/location1_hover.png"
                action [Hide("date_menu")]
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Stuffed Bear ($20){/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'
    else:
        vbox:
            align (0.5, 0.5)
            imagebutton:
                idle "images/overlay/date_menu/location_locked.png"
                hover "images/overlay/date_menu/location_locked.png"
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Locked{/color} {color=#FF5454}(Progression Level 4){/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'            

    if robin_progression_level >= 4:
        vbox:
            align (0.9, 0.5)
            imagebutton:
                idle "images/overlay/date_menu/location1_idle.png"
                hover "images/overlay/date_menu/location1_hover.png"
                action [Hide("date_menu")]
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Stuffed Bear ($20){/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'
    else:
        vbox:
            align (1.0, 0.5)
            imagebutton:
                idle "images/overlay/date_menu/location_locked.png"
                hover "images/overlay/date_menu/location_locked.png"
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Locked{/color} {color=#FF5454}(Progression Level 4){/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Hide("date_menu")]
        xalign 0.5
        yalign 0.9