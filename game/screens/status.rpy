default selected_outfit = "default"
default tank_unlocked = False
# default robin_perception = ""

# label update_perception:
#     if robin_progression_level == 0:
#         $ robin_perception = "stranger"
#     elif robin_progression_level == 1:
#         $ robin_perception = "friend"

screen status:
    modal True

    add "images/overlay/stats_menu/stats_menu.png"

    if selected_outfit == "default":
        add "images/overlay/stats_menu/default_outfit.png"
    elif selected_outfit == "tank":
        add "images/overlay/stats_menu/tank_outfit.png"
    elif selected_outfit == "bussyball":
        add "images/overlay/stats_menu/bussyball_outfit.png"
    elif selected_outfit == "swimsuit":
        add "images/overlay/stats_menu/swimsuit_outfit.png"
    elif selected_outfit == "cat":
        add "images/overlay/stats_menu/cat_outfit.png"
    elif selected_outfit == "booters":
        add "images/overlay/stats_menu/booters_outfit.png"
    elif selected_outfit == "lingerie":
        add "images/overlay/stats_menu/lingerie_outfit.png"

    text "{color=#ffffff}Select Outfit{/color}" xalign 0.87 yalign 0.18:
        outlines [(3, "#000000", 0, 1.5)]
        size 40
        font 'fonts/FredokaOne-Regular.ttf'

    text "{color=#ffffff}Progression Level: {color=#FF00E8}[robin_progression_level]{/color}" xalign 0.5 yalign 0.35:
        outlines [(3, "#000000", 0, 1.5)]
        size 40
        font 'fonts/FredokaOne-Regular.ttf'
    
    # text "{color=#ffffff}He considers you a:{/color}  {color=#FF00E8}[robin_perception]{/color}" xalign 0.5 yalign 0.45:
    #     outlines [(3, "#000000", 0, 1.5)]
    #     size 40
    #     font 'fonts/FredokaOne-Regular.ttf'

    text "{color=#ff87ff}Affection:{/color} {color=#FF00E8}[affection]{/color}" xalign 0.5 yalign 0.55:
        outlines [(3, "#000000", 0, 1.5)]
        size 50
        font 'fonts/FredokaOne-Regular.ttf'

    text "{color=#918fff}Trust:{/color} {color=#FF00E8}[trust]{/color}" xalign 0.5 yalign 0.65:
        outlines [(3, "#000000", 0, 1.5)]
        size 50
        font 'fonts/FredokaOne-Regular.ttf'

    text "{color=#bb0028}Desire:{/color} {color=#FF00E8}[desire]{/color}" xalign 0.5 yalign 0.75:
        outlines [(3, "#000000", 0, 1.5)]
        size 50
        font 'fonts/FredokaOne-Regular.ttf'

    hbox:
        xalign 0.95
        yalign 0.3
        spacing 5 

        vbox:
            imagebutton:
                idle "images/overlay/stats_menu/default_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                hover "images/overlay/stats_menu/default_idle.png"
                action [SetVariable("selected_outfit", "default"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

        # if tank_unlocked:
        #     vbox:
        #         imagebutton:
        #             idle "images/overlay/stats_menu/tank_idle.png"
        #             hover "images/overlay/stats_menu/tank_hover.png"
        #             action [SetVariable("selected_outfit", "tank")]
        
        if robin_progression_level >= 1 and key_task >= 2:
            vbox:
                imagebutton:
                    hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                    idle "images/overlay/stats_menu/bussyball_hover.png"
                    hover "images/overlay/stats_menu/bussyball_idle.png"
                    action [SetVariable("selected_outfit", "bussyball"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

        else:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/locked_hover.png"
                    hover "images/overlay/stats_menu/locked_hover.png"

    hbox:
        xalign 0.95
        yalign 0.55
        spacing 5 

        if robin_progression_level >= 2:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/swimsuit_idle.png"
                    hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                    hover "images/overlay/stats_menu/swimsuit_hover.png"
                    action [SetVariable("selected_outfit", "swimsuit"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]
        else:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/locked_hover.png"
                    hover "images/overlay/stats_menu/locked_hover.png"

        # if tank_unlocked:
        #     vbox:
        #         imagebutton:
        #             idle "images/overlay/stats_menu/tank_idle.png"
        #             hover "images/overlay/stats_menu/tank_hover.png"
        #             action [SetVariable("selected_outfit", "tank")]
        
        if lingerie == True:
            vbox:
                imagebutton:
                    hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                    idle "images/overlay/stats_menu/lingerie_idle.png"
                    hover "images/overlay/stats_menu/lingerie_hover.png"
                    action [SetVariable("selected_outfit", "lingerie"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

        else:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/locked_hover.png"
                    hover "images/overlay/stats_menu/locked_hover.png"

    hbox:
        xalign 0.95
        yalign 0.80
        spacing 5 

        if cat == True:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/cat_idle.png"
                    hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                    hover "images/overlay/stats_menu/cat_hover.png"
                    action [SetVariable("selected_outfit", "cat"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]
        else:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/locked_hover.png"
                    hover "images/overlay/stats_menu/locked_hover.png"

        # if tank_unlocked:
        #     vbox:
        #         imagebutton:
        #             idle "images/overlay/stats_menu/tank_idle.png"
        #             hover "images/overlay/stats_menu/tank_hover.png"
        #             action [SetVariable("selected_outfit", "tank")]
        
        if restuarant_outfit == True:
            vbox:
                imagebutton:
                    hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                    idle "images/overlay/stats_menu/booters_idle.png"
                    hover "images/overlay/stats_menu/booters_hover.png"
                    action [SetVariable("selected_outfit", "booters"), Play("sound", "audio/sound/interface_sounds/click_003.ogg")]

        else:
            vbox:
                imagebutton:
                    idle "images/overlay/stats_menu/locked_hover.png"
                    hover "images/overlay/stats_menu/locked_hover.png"


    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("status")]
        tooltip "Go back"
        xalign 0.01 
        yalign 0.99