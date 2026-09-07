# Declarations used in game
image ctc_blink:
    "gui/ctc_arrow.png"
    ease 1 alpha 1.0 yoffset -2
    ease 1 alpha 0.6 yoffset 2
    repeat 

image ghost_scene:
    "images/cutin/bathroom/ghost_1.png" with Dissolve(0.2)
    pause 0.2
    "images/cutin/bathroom/ghost_2.png" with Dissolve(0.2)
    pause 0.2
    "images/cutin/bathroom/ghost_3.png" with Dissolve(0.2)
    pause 0.2
    "images/cutin/bathroom/ghost_4.png" with Dissolve(0.2)
    pause 0.2
    repeat

image trust_movie_bg:
    "images/cutin/trust_movie_1/trust_movie_3_3.png" with Dissolve(0.2)
    pause 0.2
    "images/cutin/trust_movie_1/trust_movie_3_4.png" with Dissolve(0.2)
    pause 0.2
    "images/cutin/trust_movie_1/trust_movie_3_5.png" with Dissolve(0.2)
    pause 0.2
    "images/cutin/trust_movie_1/trust_movie_3_6.png" with Dissolve(0.2)
    pause 0.2
    repeat

image ghost_trust_jitter:
    "images/cutin/trust_movie_1/ghost_trust1.png" with Dissolve(0.1)
    pause 1.0
    "images/cutin/trust_movie_1/ghost_trust2.png" with Dissolve(0.1)
    pause 0.2
    repeat

image ghost_trust_jitter2:
    "images/cutin/trust_movie_1/ghost_trust3.png" with Dissolve(0.1)
    pause 1.0
    "images/cutin/trust_movie_1/ghost_trust4.png" with Dissolve(0.1)
    pause 0.2
    "images/cutin/trust_movie_1/ghost_trust5.png" with Dissolve(0.2)
    pause 0.4
    repeat

image ghost_trust_jitter3:
    "images/cutin/trust_movie_1/trust_movie_3_8.png" with Dissolve(0.1)
    pause 1.0
    "images/cutin/trust_movie_1/trust_movie_3_9.png" with Dissolve(0.1)
    pause 0.2
    "images/cutin/trust_movie_1/trust_movie_3_10.png" with Dissolve(0.2)
    pause 0.4
    repeat

image ghost_trust_jitter4:
    "images/cutin/trust_movie_1/trust_movie_3_11.png" with Dissolve(0.1)
    pause 1.0
    "images/cutin/trust_movie_1/trust_movie_3_12.png" with Dissolve(0.1)
    pause 0.2
    "images/cutin/trust_movie_1/trust_movie_3_13.png" with Dissolve(0.2)
    pause 0.4
    repeat

# Characters
define robin = Character("Robin", who_color = "#1c7fff", callback = name_callback, cb_name = "robin", ctc="ctc_blink", ctc_position="nestled")
define pro = Character('[protagonist_name]', who_color = "#FF9EF6", callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled")
define chat = Character("Stream Chat", who_color = "#46179c", callbackR = name_callback, cb_name = None)
define stalker = Character("Stalker", who_color = "#aaaaaa", callback = name_callback, cb_name = "stalker")
define system = Character("System", who_color = "#ff0000", callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled")
define unknown = Character("Unknown", who_color = "#ffffff", callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled")
define man = Character("Perverted Man", who_color = "#c42727", callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled")
define cop = Character("Cop", who_color = "#2344ff", callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled")
define ghost = Character("Ghost", who_color = "#53FFAD", callback = name_callback, cb_name = None, ctc="ctc_blink", ctc_position="nestled")

# Robin Images
image robin neutral = At('robin_neutral', sprite_highlight('robin'))
image robin open = At('robin_openmouth', sprite_highlight('robin'))
image robin smile = At('robin_smile', sprite_highlight('robin'))
image robin star = At('robin_stareyes', sprite_highlight('robin'))
image robin tank = At('robin_tank', sprite_highlight('robin'))
image robin towel = At('robin_shower', sprite_highlight('robin'))
image robin swimsuit = At('robin_swimsuit', sprite_highlight('robin'))

image robin neutral blush = At('robin_neutral_blush', sprite_highlight('robin'))
image robin smile blush= At('robin_smile_blush', sprite_highlight('robin'))
image robin open blush= At('robin_openmouth_blush', sprite_highlight('robin'))
image robin tank smile= At('robin_tank_smile', sprite_highlight('robin'))
image robin tank open = At('robin_tank_open', sprite_highlight('robin'))

image robin sport neutral = At('robin_sport_neutral', sprite_highlight('robin'))
image robin sport open = At('robin_sport_openmouth', sprite_highlight('robin'))
image robin sport smile = At('robin_sport_smile', sprite_highlight('robin'))
image robin sport neutral blush = At('robin_sport_neutral_blush', sprite_highlight('robin'))
image robin sport smile blush= At('robin_sport_smile_blush', sprite_highlight('robin'))
image robin sport open blush= At('robin_sport_open_blush', sprite_highlight('robin'))
image robin sport train = At('robin_sport_training', sprite_highlight('robin'))

image robin cosplay neutral = At('robin_cosplay_neutral', sprite_highlight('robin'))
image robin cosplay smile = At('robin_cosplay_smile', sprite_highlight('robin'))

image stalker smile = At("stalker", sprite_highlight('stalker'))
image stalker angry = At("stalker_angry", sprite_highlight('stalker'))

# Flags
default walked_in = False
default bathroom_jerk = False
default tell_truth = False

# Cut-Ins
image robin_walk_blur:
    "robin_sunny_walk" with dissolve
    pause 3.0 
    "robin_sunny_walk_blur" with dissolve
    pause 1.0
    repeat

# Tranforms
image white = "#ffffff"
image whiteflash:
    Solid("#fff")
    alpha 0.0
    linear 0.25 alpha 0.8
    linear 0.75 alpha 0.0
    linear 1.0 alpha 0.8
    linear 0.25 alpha 0.0

default flash = None
$ flash = Fade(.25, 0, .75, color="#fff")

init:
    transform slight_wobble:
        zoom 1.0
        linear 0.1 xoffset 1.5
        linear 0.1 yoffset 1.5
        linear 0.1 xoffset -1
        linear 0.1 yoffset -1
        linear 0.1 xoffset 0
        linear 0.1 yoffset 0
        repeat

    transform jumper:
        ease .06 yoffset 15
        ease .06 yoffset -15
        ease .06 yoffset 3
        ease .06 yoffset -3
        ease .06 yoffset 0

    transform card_percent:
        zoom 0.8

    transform six_percent:
        zoom 0.7

    transform five_percent:
        zoom 0.5

    transform anim_choice_button: 
        on hover: 
            ease 0.25 zoom 1.1
        on idle: 
            ease 0.25 zoom 1.0

    transform hover:
        zoom 0.65
        ease 1.0 yoffset 20
        ease 1.5 yoffset -20
        repeat

    transform food_hover:
        zoom 0.3
        ease 1.0 yoffset 15
        ease 1.5 yoffset -15
        repeat

    transform gift_hover:
        zoom 0.2
        ease 1.0 yoffset 15
        ease 1.5 yoffset -15
        repeat     

    transform tv_card_icon:
        zoom 0.23
        on hover:
            ease 0.5 yoffset -25
        on idle:
            ease 1.0 yoffset 0

    transform decision_hover:
        on hover:
            ease 0.5 yoffset -25
        on idle:
            ease 1.0 yoffset 0        

    transform choice_hover:
        xalign 0.5
        on hover:
            ease 0.3 zoom 1.15
        on idle:
            ease 0.5 zoom 1.0

    transform menu_button:
        zoom 0.75
        on hover:
            ease 0.3 yoffset -25
        on idle:
            ease 0.6 yoffset 0

    transform demo_button:
        zoom 1.5
        on hover:
            ease 0.3 yoffset -25
        on idle:
            ease 0.6 yoffset 0

    transform slide_out:
        alpha 1.0 xalign 0.52 ypos 670
        pause 1.0
        parallel:
            easeout 1.5 xpos -300
        parallel:
            easeout 1.5 alpha 0.0

    transform slide_in:
        alpha 0.0 xpos 2220 ypos 670
        pause 1.0
        parallel:
            easein 1.5 xalign 0.52
        parallel:
            linear 1.5 alpha 1.0