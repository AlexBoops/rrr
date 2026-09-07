screen wishlist:
    modal True
    add "images/overlay/wishlist_prompt.png"

    imagebutton:
        focus_mask True
        idle "images/overlay/wishlist_button.png"
        hover "images/overlay/wishlist_button_hover.png"
        action [OpenURL("https://store.steampowered.com/app/2972800/My_Femboy_Roommate/")]
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("wishlist")]
        tooltip "Go back"
        xalign 0.01 
        yalign 0.99

screen wishlist_work_day:
    modal True
    add "images/overlay/wishlist_prompt.png"

    imagebutton:
        focus_mask True
        idle "images/overlay/wishlist_button.png"
        hover "images/overlay/wishlist_button_hover.png"
        action [OpenURL("https://store.steampowered.com/app/2972800/My_Femboy_Roommate/")]
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("wishlist"), Show("mc_bedroom_day")]
        tooltip "Go back"
        xalign 0.01 
        yalign 0.99

screen wishlist_work_afternoon:
    modal True
    add "images/overlay/wishlist_prompt.png"

    imagebutton:
        focus_mask True
        idle "images/overlay/wishlist_button.png"
        hover "images/overlay/wishlist_button_hover.png"
        action [OpenURL("https://store.steampowered.com/app/2972800/My_Femboy_Roommate/")]
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("wishlist"), Show("mc_bedroom_afternoon")]
        tooltip "Go back"
        xalign 0.01 
        yalign 0.99
    
screen wishlist_work_evening:
    modal True
    add "images/overlay/wishlist_prompt.png"

    imagebutton:
        focus_mask True
        idle "images/overlay/wishlist_button.png"
        hover "images/overlay/wishlist_button_hover.png"
        action [OpenURL("https://store.steampowered.com/app/2972800/My_Femboy_Roommate/")]
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("wishlist"), Show("mc_bedroom_evening")]
        tooltip "Go back"
        xalign 0.01 
        yalign 0.99

screen wishlist_work_generic:
    modal True
    add "images/overlay/wishlist_prompt.png"

    imagebutton:
        focus_mask True
        idle "images/overlay/wishlist_button.png"
        hover "images/overlay/wishlist_button_hover.png"
        action [OpenURL("https://store.steampowered.com/app/2972800/My_Femboy_Roommate/")]
        xalign 0.5
        yalign 0.5

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("wishlist"), Rollback()]
        tooltip "Go back"
        xalign 0.01 
        yalign 0.99