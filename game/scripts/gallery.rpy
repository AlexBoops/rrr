screen gallery():

    tag menu

    add "images/backgrounds/replay_bg.png"

    $start = gallery_page * maxperpage
    $end = min(start + maxperpage - 1, len(gallery_items) - 1)

    # Grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_items[i].thumb:
                    style "gallery_button"
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    at gallery_button_zoom
                    xalign 0.5
                    yalign 0.5
                    padding (4, 5)  # Center the thumbnail within the imagebutton

        # Required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    # Grid for info
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbx - 20
                xalign 0.5
                yalign 0.1
                # text gallery_items[i].name:
                #     color "#ff0000"
                #     outlines [ (3, "#ffffff", 0, 0) ]
                #     font "fonts/FredokaOne-Regular.ttf"
        # Required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null


    # Previous/Next buttons
    if gallery_page > 0:
        imagebutton:
            idle "gui/qm_buttons/galback_idle.png"
            hover "gui/qm_buttons/galback_hover.png"
            focus_mask True
            action [SetVariable("gallery_page", gallery_page - 1), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
            xalign 0.1
            yalign 0.98
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        imagebutton:
            idle "gui/qm_buttons/galfront_idle.png"
            hover "gui/qm_buttons/galfront_hover.png"
            focus_mask True
            action [SetVariable("gallery_page", gallery_page + 1), Play("sound", "audio/sound/interface_sounds/drop_003.ogg")]
            xalign 0.9
            yalign 0.98
    # Return button
    imagebutton:
        idle "gui/qm_buttons/back.png"
        hover "gui/qm_buttons/back_hover.png"
        action Return()
        xalign 0.5
        yalign 0.98

screen gallery_closeup(images):  # Shows full-sized image as a button on top of everything!
    zorder 1
    imagebutton idle images[closeup_page]:
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 0.98
        background "#fff8"

transform gallery_button_zoom:
    zoom 1.0 xalign 0.5 yalign 0.5
    on idle:
        ease 0.2 zoom 1.0 xalign 0.5 yalign 0.5
    on hover:
        ease 0.2 zoom 1.05 xalign 0.5 yalign 0.5

style gallery_button:
    hover_background "images/replay/hover.png"
    
