screen tasks:
    modal True

    add "images/overlay/ui/tasks_menu.png"

    frame:
        xalign 0.5
        yalign 0.5
        background None  # This makes the frame background transparent

        # Scrollable area for hints
        viewport:
            mousewheel True
            draggable True
            area (0, 0, 1785, 704)

            vbox:
                spacing 10  # Spacing between hints

                if robin_progression_level == 0 and key_task == 0:
                    hbox:
                        add "images/overlay/ui/heart.png"
                        text _("{color=#ffffff}Interact with your computer and work on your game in{/color}{color=#FF9D26} the morning.{/color}"):
                            size 50

                if robin_progression_level == 0 and key_task == 1:

                    if trust < 20:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#918fff}trust{/color} with Robin ([trust]/20){/color}"):
                                size 50

                    if affection < 20:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#ff87ff}affection{/color} with Robin ([affection]/20){/color}"):
                                size 50

                    if desire < 20:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#bb0028}desire{/color} with Robin ([desire]/20){/color}"):
                                size 50

                if robin_progression_level == 0 and key_task == 1 and trust >= 20 and affection >= 20 and desire >= 20:
                    hbox:
                        add "images/overlay/ui/heart.png"
                        text _("{color=#ffffff}Interact with your computer and work on your game in{/color}{color=#FF9D26} the morning.{/color}"):
                            size 50

                if robin_progression_level == 1 and key_task == 2:

                    if trust < 75:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#918fff}trust{/color} with Robin ([trust]/75){/color}"):
                                size 50

                    if affection < 75:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#ff87ff}affection{/color} with Robin ([affection]/75){/color}"):
                                size 50

                    if desire < 75:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#bb0028}desire{/color} with Robin ([desire]/75){/color}"):
                                size 50

                if robin_progression_level == 1 and key_task == 2 and trust >= 75 and affection >= 75 and desire >= 75:
                    hbox:
                        add "images/overlay/ui/heart.png"
                        text _("{color=#ffffff}Interact with your computer and work on your game in{/color}{color=#FF9D26} the morning.{/color}"):
                            size 50

                if robin_progression_level == 2 and key_task == 3:

                    if trust < 175:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#918fff}trust{/color} with Robin ([trust]/175){/color}"):
                                size 50

                    if affection < 175:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#ff87ff}affection{/color} with Robin ([affection]/175){/color}"):
                                size 50

                    if desire < 175:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#bb0028}desire{/color} with Robin ([desire]/175){/color}"):
                                size 50

                if robin_progression_level == 2 and key_task == 3 and trust >= 175 and affection >= 175 and desire >= 175:
                    hbox:
                        add "images/overlay/ui/heart.png"
                        text _("{color=#ffffff}Interact with your computer and work on your game in{/color}{color=#FF9D26} the morning.{/color}"):
                            size 50

                if robin_progression_level == 3 and key_task == 4:

                    if trust < 275:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#918fff}trust{/color} with Robin ([trust]/275){/color}"):
                                size 50

                    if affection < 275:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#ff87ff}affection{/color} with Robin ([affection]/275){/color}"):
                                size 50

                    if desire < 275:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#bb0028}desire{/color} with Robin ([desire]/275){/color}"):
                                size 50

                if robin_progression_level == 3 and key_task == 4 and trust >= 275 and affection >= 275 and desire >= 275:
                    hbox:
                        add "images/overlay/ui/heart.png"
                        text _("{color=#ffffff}Interact with your computer and work on your game in{/color}{color=#FF9D26} the morning.{/color}"):
                            size 50

                if robin_progression_level == 4 and key_task == 5:

                    if trust < 450:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#918fff}trust{/color} with Robin ([trust]/450){/color}"):
                                size 50

                    if affection < 450:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#ff87ff}affection{/color} with Robin ([affection]/450){/color}"):
                                size 50

                    if desire < 450:
                        hbox:
                            add "images/overlay/ui/heart.png"
                            text _("{color=#ffffff}Raise your {color=#bb0028}desire{/color} with Robin ([desire]/450){/color}"):
                                size 50

                if robin_progression_level == 4 and key_task == 5 and trust >= 450 and affection >= 450 and desire >= 450:
                    hbox:
                        add "images/overlay/ui/heart.png"
                        text _("{color=#ffffff}Interact with your computer in{/color}{color=#FF9D26} the morning{/color}{color=#ffffff} to initiate the ending.{/color}"):
                            size 50

    imagebutton:
        idle "images/overlay/ui/exit_idle.png"
        hover "images/overlay/ui/exit_hover.png"
        action [Hide("tasks")]
        tooltip _("Go back")
        xalign 1.0
        yalign 0.05
