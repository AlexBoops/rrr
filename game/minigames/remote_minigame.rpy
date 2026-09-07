default meter_value = 0
default meter_max = 100

default intensity = 0
default intensity_max = 1
default intensity_step = 1

default thresholds = [33, 66]
default intensity_levels = [1, 2, 3]

# Add prev_intensity to track previous intensity level
default prev_intensity = 0

init python:
    def crank_up():
        if store.intensity < store.intensity_max:
            store.intensity += store.intensity_step
            check_intensity_change()
            renpy.restart_interaction()

    def crank_down():
        if store.intensity > 0:
            store.intensity -= store.intensity_step
            check_intensity_change()
            renpy.restart_interaction()

    def update_meter():
        if store.intensity == store.intensity_max and store.intensity > 0:
            store.meter_value += store.intensity * 0.2  # Adjust as needed

            store.meter_value = min(store.meter_value, store.meter_max)

            update_intensity_max()

        renpy.restart_interaction()

    def update_intensity_max():
        if store.meter_value >= store.thresholds[1]:
            store.intensity_max = store.intensity_levels[2]
        elif store.meter_value >= store.thresholds[0]:
            store.intensity_max = store.intensity_levels[1]
        else:
            store.intensity_max = store.intensity_levels[0]

        if store.intensity > store.intensity_max:
            store.intensity = store.intensity_max
            check_intensity_change()

    def get_sprite_image(st, at):
        renpy.redraw(get_sprite_image, 0.1)

        if store.intensity >= 3:
            return "sprite_shake3", 0
        elif store.intensity >= 2:
            return "sprite_shake2", 0
        elif store.intensity >= 1:
            return "sprite_shake1", 0
        else:
            return "sprite_normal", 0

    # Function to handle sound playback based on intensity
    def check_intensity_change():
        if store.intensity != store.prev_intensity:
            # Stop any previous sound
            renpy.music.stop(channel='sound')

            # Play new sound if intensity > 0
            if store.intensity == 1:
                renpy.music.play("audio/sound/nsfw_sounds/plug_1.wav", loop=True, channel='sound')
            elif store.intensity == 2:
                renpy.music.play("audio/sound/nsfw_sounds/plug_2.wav", loop=True, channel='sound')
            elif store.intensity == 3:
                renpy.music.play("audio/sound/nsfw_sounds/plug_3.wav", loop=True, channel='sound')

            # Update prev_intensity
            store.prev_intensity = store.intensity

style vertical_meter:
    bar_vertical True
    bar_invert True
    xmaximum 120
    ymaximum 500
    left_bar Null()
    right_bar Solid("#FD00E6")
    left_gutter 0
    right_gutter 0
    bar_resizing False

screen mini_game():
    timer 0.1 action Function(update_meter) repeat True

    add DynamicDisplayable(get_sprite_image) at center

    imagebutton:
        idle "minigames/remote_minigame/meter.png"
        hover "minigames/remote_minigame/meter.png"
        xalign 0.965
        yalign 0.5

    fixed:
        bar value meter_value range meter_max style "vertical_meter" xalign 0.95 yalign 0.5

    vbox:
        xalign 0.1 yalign 0.5
        spacing 10

        text "Intensity: [intensity]" size 70

        imagebutton:
            idle "minigames/remote_minigame/increase.png"
            hover "minigames/remote_minigame/increase_hover.png"
            insensitive "minigames/remote_minigame/increase_disabled.png"
            action Function(crank_up)
            sensitive (intensity < intensity_max)

        imagebutton:
            idle "minigames/remote_minigame/decrease.png"
            hover "minigames/remote_minigame/decrease_hover.png"
            insensitive "minigames/remote_minigame/decrease_disabled.png"
            action Function(crank_down)
            sensitive (intensity > 0)

    if meter_value >= meter_max:
        imagebutton:
            idle "minigames/remote_minigame/finish_idle.png"
            hover "minigames/remote_minigame/finish_hover.png"
            action Return()
            xalign 0.5 yalign 0.9

image sprite_normal = "minigames/remote_minigame/sprite_normal.png"

image sprite_shake1:
    "minigames/remote_minigame/sprite_shake1.png"
    linear 0.1 xoffset -5
    linear 0.1 xoffset 5
    repeat

image sprite_shake2:
    "minigames/remote_minigame/sprite_shake2.png"
    linear 0.1 xoffset -10
    linear 0.1 xoffset 10
    repeat

image sprite_shake3:
    "minigames/remote_minigame/sprite_shake3.png"
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    repeat

label remote_minigame:
    $ meter_value = 0
    $ intensity = 0
    $ intensity_max = 1
    $ prev_intensity = 0  # Reset prev_intensity at the start
    show screen mini_game
    $ renpy.pause(hard=True)
    hide screen mini_game
    $ renpy.music.stop(channel='sound')  # Stop any playing sound

    "Mini-game finished!"
