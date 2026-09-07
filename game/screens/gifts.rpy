default bear = False
default lingerie = False
default dildo = False
default console = False
default panties = False
default wine = False
default restuarant_outfit = False
default cat = False
default buttplug = False

screen gift_menu:
    modal True

    if bear and lingerie and dildo and console and panties and wine and restuarant_outfit and cat and buttplug:
        $ achievement.grant("buy_everything")

    add "images/overlay/gift/interact_bg.png"

    text "{color=#ffffff}Money:{/color}{color=#37B700} $[money]{/color}" xalign 0.5 yalign 0.25:
        font 'fonts/FredokaOne-Regular.ttf'
        size 50

    if bear == False:
        vbox:
            align (0.05, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/bear_idle.png"
                hover "images/overlay/gift/bear_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("bear_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Stuffed Bear ($20){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#ff87ff}Affection ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    else:
        vbox:
            align (0.05, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/bear_purchased.png"
                hover "images/overlay/gift/bear_purchased.png"
                at food_hover

    if robin_progression_level >= 4 and lingerie == False:
        vbox:
            align (0.23, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/lingerie_idle.png"
                hover "images/overlay/gift/lingerie_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("lingerie_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Cat Lingerie ($100){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}\n{color=#ff87ff}Affection ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif lingerie == True:
        vbox:
            align (0.23, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/lingerie_purchased.png"
                hover "images/overlay/gift/lingerie_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.23, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/lingerie_locked.png"
                hover "images/overlay/gift/lingerie_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 4{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    if robin_progression_level >= 4 and dildo == False:
        vbox:
            align (0.38, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/dildo_idle.png"
                hover "images/overlay/gift/dildo_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("dildo_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Dildo ($100){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif dildo == True:
        vbox:
            align (0.38, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/dildo_purchased.png"
                hover "images/overlay/gift/dildo_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.38, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/dildo_locked.png"
                hover "images/overlay/gift/dildo_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 4{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    if console == False:
        vbox:
            align (0.55, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/console_idle.png"
                hover "images/overlay/gift/console_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("console_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Gaming Console ($50){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#ff87ff}Affection ++{/color}\n{color=#918fff}Trust ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    else:
        vbox:
            align (0.55, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/console_purchased.png"
                hover "images/overlay/gift/console_purchased.png"
                at food_hover

    if robin_progression_level >= 4 and panties == False:
        vbox:
            align (0.77, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/panties_idle.png"
                hover "images/overlay/gift/panties_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("panties_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Panties ($75){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif panties == True:
        vbox:
            align (0.77, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/panties_purchased.png"
                hover "images/overlay/gift/panties_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.77, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/panties_locked.png"
                hover "images/overlay/gift/panties_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 4{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    if robin_progression_level >= 4 and wine == False:
        vbox:
            align (0.92, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/wine_idle.png"
                hover "images/overlay/gift/wine_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("wine_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Wine ($80){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif wine == True:
        vbox:
            align (0.92, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/wine_purchased.png"
                hover "images/overlay/gift/wine_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.92, 0.45)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/wine_locked.png"
                hover "images/overlay/gift/wine_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 4{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    if robin_progression_level >= 3 and cat == False:
        vbox:
            align (0.05, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/cat_idle.png"
                hover "images/overlay/gift/cat_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("cat_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Cat Ears ($60){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif cat == True:
        vbox:
            align (0.05, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/cat_purchased.png"
                hover "images/overlay/gift/cat_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.05, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/cat_locked.png"
                hover "images/overlay/gift/cat_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 3{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    if robin_progression_level >= 4 and buttplug == False:
        vbox:
            align (0.23, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/buttplug_idle.png"
                hover "images/overlay/gift/buttplug_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("buttplug_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Butt Plug ($70){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}\n{color=#ff87ff}Affection ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif buttplug == True:
        vbox:
            align (0.23, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/buttplug_purchased.png"
                hover "images/overlay/gift/buttplug_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.23, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/buttplug_locked.png"
                hover "images/overlay/gift/buttplug_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 4{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    if robin_progression_level >= 4 and restuarant_outfit == False:
        vbox:
            align (0.38, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/restaurant_outfit_idle.png"
                hover "images/overlay/gift/restaurant_outfit_hover.png"
                hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                at food_hover
                action [Hide("gift_menu"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("restaurant_purchase")]
                xalign 0.05
                yalign 0.4

            text "{color=#ffffff}Outfit ($100){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover
    elif restuarant_outfit == True:
        vbox:
            align (0.38, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/restaurant_outfit_purchased.png"
                hover "images/overlay/gift/restaurant_outfit_purchased.png"
                at food_hover
    else:
        vbox:
            align (0.38, 0.88)
            imagebutton:
                focus_mask True
                idle "images/overlay/gift/restaurant_outfit_locked.png"
                hover "images/overlay/gift/restaurant_outfit_locked.png"
                at food_hover

            text "{color=#ffffff}(Locked){/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

            text "{color=#FF5454}Progression Level 4{/color}" xalign 0.5 yalign 0.99:
                font 'fonts/FredokaOne-Regular.ttf'
                at hover

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at five_percent
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Hide("gift_menu"), Jump("show_correct_gift_screen")]
        xalign 0.5
        yalign 0.95


label show_correct_gift_screen:
    
        if time_of_day == "day":
            jump work_day
        
        if time_of_day == "afternoon":
            jump work_afternoon

        if time_of_day == "evening":
            jump work_evening

# PURCHASE LABELS

label bear_purchase:
    scene purchase_scene
    image giftbear_purchase = "images/overlay/gift/bear_purchased.png"

    menu:
        system "Are you sure you want to purchase the bear?"
        "Yes":
            if money >= 20:
                $ bear = True
                $ money -= 20
                show giftbear_purchase with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Bear successfully purchased!"
                hide giftbear_purchase
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[20 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label wine_purchase:
    scene purchase_scene
    image wine_purchased = "images/overlay/gift/wine_purchased.png"

    menu:
        system "Are you sure you want to purchase the wine?"
        "Yes":
            if money >= 80:
                $ wine = True
                $ money -= 80
                show wine_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Wine successfully purchased!"
                hide wine_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[80 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label console_purchase:
    scene purchase_scene
    image console_purchased = "images/overlay/gift/console_purchased.png"

    menu:
        system "Are you sure you want to purchase the gaming console?"
        "Yes":
            if money >= 50:
                $ console = True
                $ money -= 50
                show console_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Gaming Console successfully purchased!"
                hide console_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[50 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label lingerie_purchase:
    scene purchase_scene
    image lingerie_purchased = "images/overlay/gift/lingerie_purchased.png"

    menu:
        system "Are you sure you want to purchase the cat lingerie?"
        "Yes":
            if money >= 100:
                $ lingerie = True
                $ money -= 100
                show lingerie_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Cat Lingerie successfully purchased!"
                hide lingerie_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[100 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label restaurant_purchase:
    scene purchase_scene
    image restaurant_purchased = "images/overlay/gift/restaurant_outfit_purchased.png"

    menu:
        system "Are you sure you want to purchase the restaurant waiter outfit?"
        "Yes":
            if money >= 100:
                $ restuarant_outfit = True
                $ money -= 100
                show restaurant_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Restaurant Waiter Outfit successfully purchased!"
                hide restaurant_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[100 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label cat_purchase:
    scene purchase_scene
    image cat_purchased = "images/overlay/gift/cat_purchased.png"

    menu:
        system "Are you sure you want to purchase the cat ears?"
        "Yes":
            if money >= 60:
                $ cat = True
                $ money -= 60
                show cat_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Cat Ears successfully purchased!"
                hide cat_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[60 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label buttplug_purchase:
    scene purchase_scene
    image buttplug_purchased = "images/overlay/gift/buttplug_purchased.png"

    menu:
        system "Are you sure you want to purchase the buttplug?"
        "Yes":
            if money >= 70:
                $ buttplug = True
                $ money -= 70
                show buttplug_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Butt Plug successfully purchased!"
                hide buttplug_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[70 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label dildo_purchase:
    scene purchase_scene
    image dildo_purchased = "images/overlay/gift/dildo_purchased.png"

    menu:
        system "Are you sure you want to purchase the dildo?"
        "Yes":
            if money >= 100:
                $ dildo = True
                $ money -= 100
                show dildo_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Dildo successfully purchased!"
                hide dildo_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[100 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu

label panties_purchase:
    scene purchase_scene
    image panties_purchased = "images/overlay/gift/panties_purchased.png"

    menu:
        system "Are you sure you want to purchase the panties?"
        "Yes":
            if money >= 75:
                $ panties = True
                $ money -= 75
                show panties_purchased with easeinbottom:
                    xalign 0.5
                    yalign 0.5
                play sound confirmation_001
                system "Panties successfully purchased!"
                hide panties_purchased
                call screen gift_menu
            else:
                play sound error_001
                system "You don't have enough money for this item. You are short {color=#37B700}[75 - money] dollars.{/color}"
                call screen gift_menu
        "No":
            call screen gift_menu   

# GIFT SCENES ----------------------------------------------------------------------------------------------------------------

label lingerie_gift:
    show robin neutral
    pro "Hey, Robin, I got you something."
    show lingerie_idle with easeinbottom:
        xalign 0.5 yalign 0.4
    "I hand him the cat lingerie I bought for him."
    hide lingerie_idle with easeouttop
    show robin smile
    robin "Oh my god, you got this for me?"
    robin "This must've been so expensive..."
    pro "Nah, it was nothing."
    pro "Just wanted to surprise you."
    robin "Thank you so much, I love it!"
    robin "I'll quickly go change and come back with it on, okay?"
    pro "Can't wait."
    scene black with dissolve
    "He emerges from his room a few minutes later."
    scene catlingerie_1 with dissolve:
        subpixel True
        zoom 2.0 xalign 0.3 yalign 0.5
        ease 3.5 zoom 1.0 xalign 0.5 yalign 0.5
    robin "Well... what do you think?"
    "He looks so fucking cute..."
    pro "Holy... fuck..."
    pro "You look absolutely stunning."
    robin "Hehe... you really think so?"
    robin "I don't usually feel comfortable wearing stuff like this in front of others..."
    robin "But I trust you, so I don't mind if you see me like this..."
    pro "Your body, it's... it's perfect."
    pro "God... you have no idea what you do to me."
    show catlingerie_2
    robin "Maybe I do, hehe."
    pro "Well then..."
    pro "How about I show you what exactly you do to me?"
    stop music fadeout 0.5
    hide catlingerie2
    scene catlingerie_1:
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 0.5 zoom 1.7 xalign 0.45 yalign 0.35
        ease 0.3 zoom 1.65
    robin "Hm?"
    scene catlingerie_3 with vpunch:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.0
        repeat
    play sound storybeat5_18 loop 
    "I lay down on the couch and begin fucking Robin mercilessly."
    robin "Ahn.. ahn.. mmm..."
    robin "Fuck... you're so... rough...!"
    "I pound into him harder, my balls slapping against his ass."
    "I'm in a full nelson position with Robin, thrusting into his ass as he squeals in pleasure."
    pro "Your ass is so fucking good, Robin."
    pro "So fucking tight, so warm..."
    "He's completely under my control, my cock sliding in and out of his ass without any resistance."
    pro "Do you like that, Robin? Do you like my cock stretching out your bussy?"
    robin "Y-Yes..!"
    pro "What a good kitty..."
    "I continue to slam into him, each thrust sending shivers of pleasure through his body."
    menu:
        "Continue":
            scene catlingerie_4 with hpunch:
                subpixel True
                xalign 0.5 yalign 1.0
                zoom 1.0
                ease 0.25 xalign 1.0 zoom 1.07
                ease 0.15 xalign 0.5 zoom 1.0
                repeat
            play sound storybeat5_17 loop 
            "I get Robin on his knees and begin fucking him from behind."
    "I bury myself deep into his asshole."
    robin "A-Ahn... fuck...!"
    robin "More, more, more! Don't stop!"
    "The bell on his choker jingles as his ass bounces with every thrust."
    robin "Ahn.. Ahn.. mmm...!"
    robin "P-Please, more..."
    robin "I want you to cum and feel good, I want to be a good kitty for you..."
    "Robin is completely submissive."
    "He clearly loves the feeling of my cock inside him and would do anything to please me."
    pro "Fuck, that's hot..."
    menu:
        "Cum":
            pro "Fuck... I'm reaching my limit!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound pleasured_exertion_slow
    scene catlingerie_5 at slight_wobble with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.2
        ease 4.0 zoom 1.3 yalign 0.6
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.4
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.2
        repeat
    "I quickly pull out and Robin gets on his knees, taking my cum as it shoots onto his face and lips."
    robin "Ahn~!"
    robin "Mmm... your cum..."
    robin "It's so warm... and it tastes so sweet."
    "He leaves his tongue out to catch my cum, not wasting a single drop."
    robin "Hehe, you really like this outfit, huh?"
    pro "Yeah... maybe a little too much."
    "He waggles his butt, the bell on his choker still ringing."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 35{/color}"
    $ desire += 35
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 35{/color}"
    $ trust += 35
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 35{/color}"
    $ affection += 35
    $ achievement.grant("lingerie")
    jump jump_to_tomorrow

label restaurant_gift:
    show robin neutral
    pro "Hey, Robin, I got you something."
    show restaurant_outfit_idle with easeinbottom:
        xalign 0.5 yalign 0.4
    "I give Robin a Femboy Booters waiter outfit."
    hide restaurant_outfit_idle with easeouttop
    robin "Oh my god, is this..."
    pro "Yup, a Femboy Booters uniform haha."
    pro "I think that you'd look really good in it..."
    show robin smile at jumper
    robin "This is so cute!"
    robin "Give me a second to change."
    scene black with dissolve
    "After a few moments, Robin returns wearing the outfit."
    scene booters_1 with dissolve:
        subpixel True
        zoom 2.0 xalign 0.3 yalign 0.5
        ease 2.5 zoom 1.0 xalign 0.5 yalign 0.5
    robin "Hehe, this is really cute."
    robin "I can see why so many people love going to Femboy Booters."
    robin "If all waiters wear this, they probably bring in quite a lot of revenue, hehe."
    pro "I hope I'm not asking for too much, but..."
    pro "Could you pretend you're working there right now and serve me something to drink?"
    show booters_2
    robin "Ooh, like some roleplay?"
    pro "Yeah, some roleplay."
    pro "I can be a loyal customer and you can be the cute waiter serving me my food."
    hide booters_2
    robin "Hehe, got it!"
    robin "Ahem, here I go."
    "Robin takes a moment to get into character."
    robin "Welcome to Femboy Booters, how may I take your order!"
    pro "Hey, I'd like two beers please!"
    pro "Oh, and give me a side of your cute femboy bussy."
    robin "Coming right up!"
    scene booters_3 with dissolve
    "He walks over to the kitchen and begins preparing my beers."
    "I stare at his ass as he bends over to pick up the beer mugs."
    "His shorts hug his butt perfectly, showing off his plump cheeks and cute physique."
    scene booters_4 with dissolve
    "Robin returns with the beers on a tray along with another tray for food."
    robin "There you go sir, two beers!"
    robin "Would you like to drink them right now..."
    robin "Or would you like your side of femboy bussy first?"
    "My cock immediately hardens in my pants, aching to be touched."
    pro "Well..."
    pro "How about a taste test of my Femboy Bussy?"
    scene white with dissolve
    robin "Of course, please tell me what you think!"
    scene booters_45 with dissolve
    "Robin takes off his pants and spreads his cheeks."
    robin "Please taste my bussy until you're satisfied!"
    play sound storybeat6_21 loop
    show tongue with dissolve:
        xpos 1055 ypos 613
        anchor (0.5, 1.0)
        ease 1.0 rotate 15
        ease 1.0 rotate -15
        repeat
    "I immediately begin licking and sucking on his asshole, moving my tongue between his thong."
    robin "Ahn... mhmm..."
    robin "Yes, please keep going..."
    robin "I always want to make sure that... ahn..."
    robin "That my customers are fully satisfied with their meal..."
    "I continue to tease him, rubbing my tongue against his prostate and stretching his hole out."
    robin "AAHN! Yes, just like that...!"
    robin "You're a good customer sir, hehe."
    robin "Would you like to have your main course now?"
    pro "Mm, yes..."
    pro "But I don't want to move too quickly, I want to savor your bussy a little longer."
    robin "Ahn... I love hearing you say that..."
    robin "I'll serve you the main course whenever you're ready, okay?"
    menu:
        "Continue":
            hide tongue with dissolve
            stop sound fadeout 1.0
            "I stop eating Robin's ass and pull away my tongue."
    pro "Mmm... I think I'm ready for my main meal now."
    robin "Hehe, okay..."
    scene white with dissolve
    "Robin doesn't waste a second and immediately jumps on my lap."
    robin "You ready, sir?"
    pro "Mhm."
    play sound storybeat6_23 fadein 0.5 loop
    scene booters_5 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.0
        repeat
    "Robin shoves my cock into his ass and begins riding me."
    robin "Ahn... ahn... mmmm..."
    robin "Gosh sir, your dick is really big..."
    "He continues to bounce on my cock, moaning softly as he feels me filling him up."
    pro "Wow Robin, you really are the best femboy waiter for Femboy Booters."
    robin "Hehe, it's my job to make sure that the customer is completely satisfied!"
    robin "And I always put my heart and soul into my work!"
    "Robin increases his pace and slams my dick into his hole again and again."
    robin "Fuck... ahn..."
    robin "Your cock is so fucking big..."
    robin "I'm going crazy..."
    robin "I need to be filled by you..."
    menu:
        "Continue":
            play sound storybeat5_14 fadein 0.5 loop
            scene booters_6 with dissolve:
                subpixel True
                xalign 0.5 yalign 0.5
                zoom 1.0
                ease 0.25 yalign 1.0 zoom 1.07
                ease 0.2 yalign 0.5 zoom 1.0
                repeat
            "I turn Robin around. He immediately continues riding me."
    "I watch as his ass bounces with every thrust."
    pro "I'll be sure to give you a huge tip after I finish my meal... fuck..."
    robin "Ahn... t-thank you... sir... mmm...!"
    robin "I'm glad you... ahn..."
    robin "Enjoyed the food... fuck..."
    "Robin struggles to get his words out as he moans in pleasure."
    robin "I love the feeling of you inside of me...!"
    robin "Fuck, I love it so much..."
    robin "I can feel you deep, deep inside!"
    robin "So fucking deep!"
    play sound storybeat5_14_2 fadein 0.5 loop
    scene booters_6:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.0
        repeat
    "He bounces even faster on my cock and I know that he's getting close to climax."
    robin "Oh god, oh god..."
    robin "I'm going to... cum soon!"
    robin "I'm reaching my limit sir!"
    pro "Yeah, me too Robin."
    pro "I'm gonna blow my load deep inside you."
    robin "P-PLEASE!"
    robin "I want it! I want it all!"
    robin "Please fill me up...!!"
    menu:
        "Cum":
            pro "Fuck... I'm reaching my limit!"     
            "I thrust one final time before reaching my limit."
    pro "Fuck... I'm cumming!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound storybeat5_15_climax fadein 0.5
    scene booters_7 at slight_wobble with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.2
        ease 4.0 zoom 1.3 yalign 0.6
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.4
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.2
        repeat 
    robin "A-AAAAHHN!"
    robin "YOU'RE FILLING ME UP...!"
    pro "Take it Robin... all of it...!"
    robin "I LOVE IT..."
    robin "Keep pumping... keep filling me..."
    robin "Ahn...!"
    pro "Fuck... that was amazing..."
    pro "You did such a great job serving me, Robin."
    robin "Thanks... hehe."
    robin "I'm glad to be the best femboy waiter there is..."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 45{/color}"
    $ desire += 45
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 45{/color}"
    $ trust += 45
    $ achievement.grant("restaurant_outfit")
    jump jump_to_tomorrow

label bear_gift:
    show robin neutral
    pro "Hey, Robin, I got you something."
    show bear_idle with easeinbottom:
        xalign 0.5 yalign 0.4
    "I give Robin the pink stuffed bear that I bought for him."
    hide bear_idle with easeouttop
    pro "I saw it online and it made me think of you!"
    show robin smile at jumper
    robin "Oh. My. God."
    scene bear_gift with dissolve
    "He takes it into his hands, hugging it close to his chest."
    robin "Aww... this is adorable."
    "He squeezes the bear tightly and giggles."
    robin "I had a ton of stuffed animals when I was a kid, but I had to give them away."
    pro "Really, why?"
    robin "When I was growing up, my parents didn't want me to have any stuffed animals."
    robin "They thought that stuffed animals would make me more girly, so they threw them away."
    robin "Clearly, the stuffed animals weren't the issue."
    robin "Thank you so much, I'll cherish it forever!"
    pro "No problem."
    pro "I'm glad that it makes you so happy!"
    robin "Hehe... you're too sweet!"
    robin "I'm going to name him... Robin the second!"
    pro "Oh god..."
    pro "Why..."
    robin "Because Robin the first needs a loyal companion, that's why!"
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 20{/color}"
    $ affection += 20
    jump jump_to_tomorrow

label console_gift:
    show robin neutral
    pro "Hey, Robin, I got you something."
    show console_idle with easeinbottom:
        xalign 0.5 yalign 0.4
    "I give Robin the handheld game console that I bought for him."
    hide console_idle with easeouttop
    pro "I saw it online and figured you'd like it!"
    pro "Maybe you could stream some new games on it too."
    show robin smile at jumper
    robin "This is so awesome!"
    robin "I'll be able to play games on the go with this!"
    pro "Yeah, I thought you'd like it."
    scene console_gift with dissolve
    "He takes the handheld game console into his hands."
    robin "This is so cool..."
    robin "It even has the new Femboy Kart game on it!"
    robin "I'm definitely streaming with this tonight!"
    robin "Thank you so much, [protagonist_name]!"
    robin "I'll cherish this forever!"
    pro "No problem!"
    "I'm glad Robin likes the gift so much!"
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 25{/color}"
    system "{color=#918fff}Trust increased by 25{/color}"
    $ affection += 25
    $ trust += 25
    jump jump_to_tomorrow

label cat_gift:
    show robin neutral
    pro "Hey, Robin, I got you something."
    show cat_idle with easeinbottom:
        xalign 0.5 yalign 0.4
    "I give Robin the cat ears that I bought for him."
    hide cat_idle with easeouttop
    pro "I saw it online. Apparently it has some weird powers or something."
    pro "Either way, here you go!"
    show robin smile at jumper
    robin "Ahh, this is cute! I'll try it on right now."
    "He takes a moment to put the cat ears on his head."
    pro "Oooh... you look so cute!"
    robin "Hehe really?"
    robin "Thank you-"
    scene white with dissolve
    "Suddenly, a burst of white light blinds me."
    pro "What happened!"
    robin "Wh...whaaaaat!!!"
    pro "Robin?"
    scene furry_1 with dissolve:
        zoom 2.5 xalign 0.5 yalign 0.5
        ease 3.0 zoom 1.0
    "As I regain my vision, I see that Robin's entire body has been transformed."
    "He has fluffy white ears, a tail, cat paws, and his tongue is even shaped like a cats."
    robin "[protagonist_name]!"
    robin "What... what happened to me!"
    pro "I guess I see what the 'special powers' were..."
    "I reach for Robin's cat ears, attempting to take them off of his head."
    pro "Let's see if we can remove these."
    "I try pulling on them but they won't budge."
    robin "Ow! Stop, you're hurting me."
    pro "Sorry..."
    robin "What's going on?"
    pro "It seems like you've been turned into a... cat?"
    robin "What!"
    robin "What do you mean!"
    pro "It was probably the cat ears."
    pro "I'm so sorry Robin, I had no idea that these had any magical properties or anything like that!"
    pro "I'll try to find a way to reverse this, okay? I promise!"
    robin "Mmm okay..."
    scene black with dissolve
    "I head back to my room and boot up my computer."
    scene mc_bedroom with dissolve
    pro "Ah, here's the listing I bought the ears from."
    "I read through the description and find that the cat ears have some... unique properties."
    pro "The cat ears will transform any human that puts it on into a cat person. The effect only lasts an hour."
    pro "That's a relief. At least we know it's not permanent."
    scene black with dissolve
    pro "I should go check up on Robin."
    scene furry_2 with dissolve
    "Returning to the living room, I see that Robin's on all fours."
    pro "Robin, what are you doing!"
    robin "Meow?"
    pro "Wait..."
    pro "Don't tell me that the cat ears took away your ability to talk."
    "Robin turns and looks at me, his eyes wide."
    robin "Meeoow."
    pro "This isn't good."
    robin "Mreeeooww..."
    scene furry_3 with dissolve
    "He crawls over to me, his tail swaying."
    robin "Meow, meow, purrrr..."
    pro "Robin..."
    pro "You need to stop acting like this."
    pro "You're a human being."
    "His tail swishes as he approaches, his eyes locked on me."
    robin "Mreow..."
    pro "Robin, snap out of it!"
    pro "You're not a cat!"
    "His ears twitch, and his head tilts slightly."
    robin "Meeeooww..."
    "Even his tail is wiggling back and forth."
    "His little paws are so cute..."
    "I decide to let him continue being a cat until the effect wears off."
    robin "Meow!!"
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 40{/color}"
    $ desire += 40
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 40{/color}"
    $ trust += 40
    $ achievement.grant("cat_ears")
    jump jump_to_tomorrow

label wine_gift:
    show robin neutral
    pro "Hey Robin, I got you something!"
    show wine_idle with easeinbottom:
        xalign 0.5 yalign 0.4
    "I hand Robin a glass of the fancy wine that I bought online."
    hide wine_idle with easeouttop
    pro "Here you go! I don't know if you drink or anything, but I thought that it might be a fun thing to try out!"
    show robin smile at jumper
    robin "Oh, thanks!"
    robin "I don't drink often, but I'm willing to try it."
    pro "I mean... if you aren't busy we can have some right now?"
    show robin open
    robin "But it's so early in the [time_of_day]!"
    pro "It's 5PM somewhere!"
    show robin neutral
    robin "Mmm..."
    show robin smile
    robin "I guess I'm free the rest of the day, let's do it!"
    scene black with dissolve
    "We grab two wine glasses and head to Robin's room."
    scene robin_room1 with dissolve
    show robin smile with easeinbottom
    robin "This is the perfect place to relax and have some wine."
    "I pour us each a glass and we clink our glasses together before taking a sip."
    pro "Wow, this actually tastes great!"
    robin "Yeah... I've never had fancy wine before."
    robin "To be honest, I stay away from alcohol in general."
    robin "I can't handle my booze well, so I'll try to stay in moderation!"
    pro "Don't worry, I got you."
    pro "The whole point is to relax anyways."
    robin "Hehe, this wine does help me a bit though."
    robin "Maybe a few more sips wouldn't hurt."
    scene black with dissolve
    "A few hours pass and 'a few sips' turned into a few more glasses, until the entire bottle was almost finished and it's pitch black outside."
    scene wine_1 at slight_wobble with dissolve:
        subpixel True
        zoom 1.03 xalign 0.5 yalign 0.5
    "By this point, Robin's words were slurred and he looked to be having the time of his life."
    robin "Hehehe, and that's when I realized that my skirt was tucked into my panties!"
    pro "Oh god... hahahaha!"
    "Robin's giggly voice and cute demeanor make me laugh as he shares stories of his past."
    robin "I can't believe that, *hiccup*, nobody told me...!"
    robin "It was so embarrassing!"
    "His face is completely flushed, but he seems to be enjoying himself. I've rarely seen him this talkative..."
    robin "My face feels hot... *hiccup*, it's kinda funny actually."
    robin "My entire body is tingly!"
    pro "That's because you're tipsy."
    pro "We should probably stop drinking now."
    robin "N-no! C'mon, just one more!!"
    robin "I'm not drunk!"
    pro "Nope, the bottle is almost empty Robin!"
    robin "You're a, *hiccup*, meanie!"
    pro "Haha, but a meanie who loves you and is just looking out for you."
    scene black with dissolve
    "I grab the wine and put the cork back in before turning around to hide the bottle somewhere safe in Robin's closet."
    stop music fadeout 1.0
    pro "There, now you won't be able to find it-"
    play music sensual fadein 1.0
    scene wine_2 at slight_wobble with dissolve:
        zoom 1.05 xalign 0.5 yalign 0.5
    "As I turn around, I see Robin completely naked in his bed."
    robin "C'mere you..."
    "I'm frozen, staring at his gorgeous figure and his plump butt."
    pro "R-robin... what are you-"
    robin "Stop being, *hiccup*, stupid and come fuck me!"
    pro "Are you sure you're okay with this?"
    robin "Yes, I'm fine, you're not taking advantage of me... I want this!"
    robin "That wine made me really... really... really... really... really-"
    pro "Really what, Robin?"
    robin "Horny!"
    robin "Now fuck me or, *hiccup*, face the consequences!"
    "He's so fucking adorable, but I don't know if I should do it."
    "He seems pretty determined to do it though."
    robin "If you keep staring at me without doing something, I'm gonna, *hiccup*, start thinking that you're not attracted to me!"
    pro "That could never be the case, Robin."
    robin "Prove it then..."
    play sound storybeat6_21 loop
    show tongue with dissolve:
        xpos 640 ypos 1050
        anchor (0.5, 1.0)
        ease 1.0 rotate 15
        ease 1.0 rotate -15
        repeat
    "I crawl over to him on the bed and begin licking his asshole."
    "He lets out a soft whimper, but I'm not going to give in easily."
    robin "Mmm..."
    "I shove my tongue into him, feeling the tightness and warmth around my mouth as I move my tongue around inside his hole."
    robin "A-ahh..."
    "I continue to lick and tease his prostate with my tongue, enjoying the sounds that escape his mouth."
    pro "You're really sensitive when you're drunk..."
    "I continue to push my tongue into his ass, feeling the walls tighten around me as I move."
    robin "Mhm... m-more... *hiccup*..."
    robin "P-Please...!"
    robin "D-don't... *hiccup*, don't tease me..."
    stop sound fadeout 0.5
    hide tongue with dissolve
    "I move my mouth away from his ass."
    pro "Sorry Robin, you're just so cute when I tease you..."
    robin "M-Meanie...!"
    scene white with dissolve
    pro "Don't worry, I'll make you feel really good."
    play sound storybeat5_14 fadein 0.5 loop
    scene wine_3 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.0
        repeat
    "I grab onto Robin's ass cheeks and thrust my cock into him."
    robin "Ah!"
    "I slowly begin moving back and forth, enjoying the feeling of Robin's warm, soft ass as he continues to moan in pleasure."
    pro "Do you like that Robin?"
    pro "Do you like it when I fill you up like that?"
    robin "Yes! Yes! More, more, more!"
    "I continue to thrust in and out, watching as his butt bounces against me and listening to him whimpering."
    pro "Your ass is so nice Robin... so fucking soft and plump..."
    pro "I can feel my entire dick being wrapped by your warm, tight bussy..."
    robin "God I love your big fat fucking cock!"
    robin "I want you, *hiccup*, fuck my brains out!"
    pro "You're such a dirty boy Robin."
    pro "I can't believe how slutty you become after having some alcohol, haha!"
    play sound storybeat5_14_2 loop
    scene wine_3:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.0
        repeat
    "I speed up, pushing my dick deeper inside him as he cries out in ecstasy."
    robin "Ooh~!"
    "I can feel the tip of my dick hitting his prostate again and again as I move my hips back and forth, slamming into his hole as he whimpers loudly."
    robin "You're filling me up!!"
    robin "Fuck, fuck, fuck!"
    pro "Good boy... keep moaning like that."
    pro "I want to hear your voice as I make you feel good."
    robin "You're gonna make me... gonna make me-"
    "I can feel his hole tightening around me as he reaches his limit."
    robin "I'm so fucking close!"
    pro "Just a little longer... hold on for a little longer."
    robin "But-"
    pro "You're my good boy, aren't you?"
    robin "Y-yes..."
    "I can feel him struggling to hold on, trying his best not to cum."
    pro "Fuck, you're so good, Robin..."
    pro "Such a good femboy for me..."
    "I can feel myself getting closer and closer to release, the warmth and tightness of his ass making it hard to control myself."
    pro "Robin, I'm gonna cum soon."
    robin "Please... I want it inside...!"
    "I can feel him struggling, trying to hold back his orgasm as I continue to pound into him."
    menu:
        "Cum":
            pro "Fuck, I'm about to burst..."
            pro "Cum for me Robin, show me how much of a slut you are...!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound storybeat5_15_climax
    scene wine_4 at slight_wobble with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.2
        ease 4.0 zoom 1.3 yalign 0.6
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.4
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.2
        repeat 
    "I can feel his walls tightening around my cock and the sensation sends me over the edge as I shoot my entire load inside him."
    robin "A-aaaaaahn~!~~!"
    robin "It feels so fucking warm and wet~"
    robin "I love feeling full and bloated of your cum...!"
    pro "Good boy, Robin..."
    pro "Good boy..."
    robin "Hehe, you were right..."
    robin "I am, *hiccup*, a good boy!"
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 55{/color}"
    $ desire += 55
    play sound positive_event_01
    system "{color=#918fff}Trust increased by 55{/color}"
    $ trust += 55
    $ achievement.grant("wine")
    jump jump_to_tomorrow

default what_room = ""

label buttplug_gift:
    show robin neutral
    pro "Hey Robin, I got you something."
    show buttplug_idle with easeinbottom:
        xalign 0.5 yalign 0.4    
    "I hand Robin the butt plug I purchased for him online."
    hide buttplug_idle with easeouttop
    show robin open
    robin "Is this..."
    robin "A b-buttplug?"
    pro "I thought you would like to wear it during the day when we're not... y'know."
    show robin smile
    robin "Hehe, I didn't know you were into this stuff."
    pro "I don't know if I am or not... I just thought it would be fun."
    pro "It even vibrates!"
    show robin open blush at jumper
    robin "Huh?"
    robin "There's a remote control for it..."
    pro "Yeah! You can use it to pleasure yourself whenever I'm not around."
    pro "Or... we could use it while we're together too, that's up to you."
    robin "O-Oh..."
    pro "I mean, I'm not gonna force you to wear it or anything. I just figured you would be into that kinda thing."
    show robin smile blush
    robin "No, no, no! I think its hot..."
    if time_of_day == "afternoon":
        $ what_room = "kitchen"
    if time_of_day == "day":
        $ what_room = "living room"
    robin "But like... we're in the [what_room] right now."
    pro "So?"
    show robin open blush
    robin "S-so I'm gonna be putting this in my ass here and now?"
    robin "Where you could see it?"
    pro "Well, I wasn't planning on watching you put it in, unless you want me to."
    pro "But I can leave if you want."
    show robin smile blush
    "He looks at me with a nervous, but excited expression."
    robin "No, it's okay. You can watch."
    scene white with dissolve
    "I nod as Robin takes his pants off."
    scene plug_1 with dissolve:
        zoom 2.0 xalign 0.5 yalign 0.5
        ease 3.0 zoom 1.0
    "He carefully inserts the butt plug into his asshole."
    robin "Ah..."
    pro "How does it feel?"
    robin "Good...!"
    robin "It's a perfect fit..."
    robin "How does it look?"
    pro "Really fucking hot..."
    pro "If you want, I can play with the vibrations a little?"
    robin "Mmmm..."
    robin "Are you sure they aren't too intense?"
    pro "You don't think you can handle it?"
    robin "Of course I can take it!"
    robin "I'm just... a little inexperienced with vibrating toys."
    pro "Do you want me to turn it on for a little bit?"
    robin "Um, s-sure..."
    $ _skipping = False
    scene plug_2 with dissolve
    $ meter_value = 0
    $ intensity = 0
    $ intensity_max = 1
    show screen mini_game with dissolve
    $ renpy.pause(hard=True)
    hide screen mini_game
    show sprite_shake3
    $ _skipping = True
    "I slowly increase the intensity more and more until he reaches his limit."
    robin "I'm... reaching my limit...!"
    robin "F-fuck...!"
    pro "Already?"
    robin "I'm... I'm gonna cum-!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound climax_regular fadein 0.5
    scene plug_3 at slight_wobble with dissolve:
        zoom 1.05 xalign 0.5 yalign 0.5    
    "Robin bursts, cumming everywhere while hes still standing."
    robin "FUCKKK~!"
    robin "AHN...!"
    "His legs wobble and he looks like hes about to fall to the floor."
    robin "T-that thing is... s-strong..."
    pro "Hehe, too much for you to handle?"
    robin "Shut up..."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 25{/color}"
    $ desire += 25
    play sound positive_event_01
    system "{color=#ff87ff}Affection increased by 25{/color}"
    $ affection += 25
    $ achievement.grant("butt_plug")
    jump jump_to_tomorrow

label dildo_gift:
    show robin neutral
    pro "Hey Robin, I got you something."
    show dildo_idle with easeinbottom:
        xalign 0.5 yalign 0.4        
    "I hand Robin the red dildo I purchased for him online."
    hide dildo_idle with easeouttop
    pro "I know it's a bit weird to give someone a sex toy, but I figured you'd like it."
    robin "Whoah, it's so big...!"
    robin "It's the perfect size too... I've been needing a new toy!"
    pro "You want to try it out?"
    show robin neutral blush
    robin "R-right now?"
    robin "Like... in front of you?"
    pro "I mean... you don't have to do it in front of me."
    pro "But... y'know..."
    pro "I wouldn't mind if you did."
    robin "O-Oh..."
    show robin smile blush
    "He looks at me with a nervous, but excited expression."
    robin "Okay... I trust you..."
    robin "Um... how about you sit on the couch."
    robin "I'll get on the coffee table in front of you."
    pro "Damn... sure."
    scene dildo_1 with dissolve
    "I do as Robin asks and take a seat, waiting in anticipation for what comes next."
    show dildo_2 with dissolve
    "Robin plops the dildo onto the table."
    "He takes off his pants and positions himself above the dildo."
    stop music fadeout 1.0
    scene white with dissolve
    robin "Here goes nothing..."
    play sound storybeat5_14 fadein 0.5 loop
    scene dildo_3 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.0
        repeat       
    "Robin slowly lowers himself down, his ass stretching as he takes the dildo inside of him."
    robin "A-ah..."
    pro "Does it feel good, Robin?"
    robin "Mhm..."
    robin "It feels great..."
    "He moves his hips up and down, the dildo sliding in and out of his asshole."
    robin "Ahn..."
    pro "You look so fucking sexy, Robin."
    robin "Y-yeah?"
    pro "Yeah, you do."
    pro "You look so fucking hot with that big dildo in your ass."
    "He blushes and continues to move up and down."
    robin "I can feel every inch of it..."
    robin "I can't believe this thing actually fits in my ass, hehe!"
    "He continues to bounce up and down on the dildo, his moans growing louder and louder with each thrust."
    robin "Mmphm, mmphm, mmmphm..."
    robin "I can feel my hole stretching out to take it all in...!"
    pro "Fuck... I'm so hard right now."
    "I unzip my pants and begin jerking off."
    robin "Hehe... you like the view?"
    pro "Fuck yes... you look amazing right now Robin."
    "He speeds up and I match his pace, jerking off to the sight of him riding that massive dildo."
    pro "Does my cute femboy like his new toy?"
    robin "Y-yes..."
    robin "I love it!"
    robin "I want more!"
    robin "I want your cock too!"
    pro "Oh yeah?"
    scene white with dissolve
    "Without hesitation, I move to the other side of the coffee table."
    pro "Get ready, Robin."
    play sound dildo_3 fadein 0.5 loop
    scene dildo_4 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.01
        repeat        
    "I shove my dick inside his mouth while he is still riding the dildo."
    robin "Mhm~!"
    robin "Fmhm~!"
    "It takes him a moment to adjust, but he quickly begins bobbing his head back and forth."
    robin "Hmhm..."
    robin "Mmmphm..."
    "He sucks on my dick eagerly, his eyes locked on mine while his mouth works on my cock."
    robin "Hmphm~"
    robin "Ahm... hmphm..."
    "Robin's eyes begin to roll into the back of his head as he continues to suck on my dick while riding the dildo."
    robin "Fmmhm... hmphm..."
    "I can feel him taking me deep, his lips pressing up against the base of my cock."
    robin "Mhm!"  
    robin "Mmphm!"
    "Robin's eyes are completely rolled back and his body begins to convulse."
    "I can tell that he's close."
    robin "Hmphm... mphm..."
    "He begins to gag on my dick, but continues to suck me off."
    pro "Fuck... I'm reaching my limit Robin."
    pro "I'm going to cum soon..."
    robin "Hmphm..."
    menu:
        "Cum": 
            pro "Cum with me, Robin!"
    robin "Mphm, mmm, MPHM!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound dildo_5 fadein 0.5
    scene dildo_5 at slight_wobble with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.2
        ease 4.0 zoom 1.3 yalign 0.6
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.4
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.2
        repeat    
    robin "MPHMM!!"
    "Robin lets out a muffled moan, cumming everywhere while hes still sitting on the coffee table."
    "He bursts and I unload into his mouth at the exact same time."
    pro "Fuck!!"
    robin "Ghmhmhm~!"
    "Robin's eyes are still rolled back and he's struggling to keep his composure, his entire body shaking as he cums."
    robin "Agh... ahn..."
    show white with dissolve
    "I pull my cock out of his mouth and he immediately flops down."
    play sound dildo_6 fadein 0.5
    scene dildo_6 at slight_wobble with dissolve:
        zoom 2.0 xalign 0.5 yalign 0.5
        ease 3.0 zoom 1.01
    robin "Hah..."
    pro "Robin, a-are you okay?"
    robin "I've never..."
    robin "I've never came that hard before..."
    robin "That was..."
    robin "So amazing..."
    "He lays there panting, my cum spilling out of his mouth."
    robin "You came so much..."
    pro "Yeah, well... what do you expect when I have such a sexy femboy in front of me?"
    robin "Hehe... hehe..."
    "Looks like I broke him..."
    pro "Well... I'll get you cleaned up."
    pro "And maybe we should only save this kind of thing for special occasions, huh?"
    scene black with dissolve
    "I carefully help Robin get to his bedroom, the two of us cuddling for a bit until Robin is back to normal."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 45{/color}"
    $ desire += 45
    $ achievement.grant("dildo")
    jump jump_to_tomorrow

label panties_gift:
    show robin neutral
    pro "Hey Robin, I got you something."
    show panties_idle with easeinbottom:
        xalign 0.5 yalign 0.4    
    "I hand Robin the blue panties I bought for him."
    hide panties_idle with easeouttop
    show robin smile at jumper
    robin "Whoa... these are so cute!"
    pro "I figured you would like them, the colour compliments your eyes really well!"
    "He looks at me with a happy smile."
    robin "Thank you, I really appreciate it."
    robin "Should I put them on right now?"
    pro "If you want!"
    scene black with dissolve
    stop music fadeout 1.0
    "Robin leaves the room for a moment and comes back with his new panties on."
    play music sensual fadein 2.0
    scene panties_1 with dissolve:
        subpixel True
        zoom 2.0 xalign 0.3 yalign 0.5
        ease 2.5 zoom 1.0 xalign 0.5 yalign 0.5
    "He's also wearing a blue choker and blue top to match."
    "Cute."
    pro "Wow... you look fucking sexy..."
    "He giggles at my compliment."
    robin "Hehe... thank you..."
    show panties_2 with dissolve
    "He smiles shyly and bites his bottom lip."
    robin "So... was there any particular reason you got me this gift?"
    robin "I know your horny ass was just thinking about fucking me while I wear this."
    pro "Maybe..."
    robin "You can never seem to get enough of me..."
    pro "Wow, you're really bold and confident today huh?"
    robin "Hehe, maybe it's because I know I have power over you, you dirty dog!"
    "I roll my eyes playfully at his comment."
    pro "You know you're the biggest horndog between the both of us."
    robin "Whatever..."
    robin "So are you just going to stand there and ogle me or are you gonna come here and fuck me?"
    "Wow, he is really fucking bold today."
    "I don't need to be asked twice."
    scene white with dissolve
    "I quickly move over to Robin and pick him up bridal style, walking over to his bedroom."
    "Once we reach the bed, I lay him down and immediately begin reaching underneath his panties."
    robin "Hehe..."
    play sound storybeat5_17 fadein 0.5 loop
    scene panties_3 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.01
        repeat
    "I push them to the side and slam my cock inside of his ass, not pausing for a even a moment."
    robin "Ooh~!"
    robin "You're so rough~!"
    "I pound his asshole as he writhes underneath me, moaning loudly."
    robin "Fuck, yes! Harder!"
    "My balls slap against his soft butt with each thrust."
    robin "Please, more..."
    robin "Give me all you've got!"
    pro "Fuck... Robin, you look so fucking sexy right now."
    robin "Tell me... tell me how much you love fucking me."
    robin "Tell me... how I'm your good femboy cum-dump!"
    "Damn, he's really bold today..."
    pro "You're a sexy fucking femboy who deserves to get his ass pounded by me every single day."
    "I start to thrust harder into him, my cock slamming into his prostate."
    robin "AH!"
    robin "R-right there! Keep hitting me riiiight there!"
    robin "I'm... c-close...!"
    pro "Then beg for it..."
    pro "Beg to cum."
    robin "P-please...!"
    robin "Let me cum all over myself!"
    robin "I need to stain my pretty blue panties with my cum!"
    robin "PLEASE, JUST LET ME FINISH MYSELF OFF WITH YOUR MASSIVE DICK!"
    play sound storybeat5_18 fadein 0.5 loop 
    scene panties_4 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.01
        repeat
    "I pick him up and turn him around, fucking him full nelson."
    pro "You don't get to finish until I say so, understood?"
    robin "F-fuck! Yes sir!"
    pro "Good boy..."
    robin "God, your cock is so deep inside of me right now...!"
    robin "It feels... so good~!"
    pro "Beg louder! I know you love being a submissive fuck slut!"
    robin "Please, don't make me hold it back any more~!"
    robin "I wanna cum all over these pretty blue panties! I need it so bad~!"
    robin "Please~!"
    "I speed up, the sound of my balls slapping against his cheeks becoming louder and louder."
    robin "PLEASE~ I CAN'T HOLD IT ANYMORE~!"
    robin "I NEED TO CUM~!"
    "I finally give in and listen to his pleas."
    pro "Go ahead then! Cum for me, slut!"
    pro "Cum for me like the pathetic femboy bitch you are!"
    pro "Now!"
    robin "A-AH! FUCK-!"
    menu:
        "Cum":
            show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    play sound storybeat5_15_climax
    scene panties_5 at slight_wobble with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.2
        ease 4.0 zoom 1.3 yalign 0.6
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.4
        pause 1.0
        ease 4.0 zoom 1.0 yalign 0.2
        repeat 
    "I slam my cock into him one last time as we both simultaneously reach our climax."
    robin "FUCKKKK~!"
    robin "S-SO MUCCCCHHH~!"
    robin "YOU'RE FILLING ME UP SO FUCKING MUCH~!"
    "His asshole stays tight, squeezing every last drop of cum out of me."
    scene white with dissolve
    "After a few moments, I gently lay him down on his bed while he catches his breath."
    play sound slight_exertion_slow fadein 0.5
    scene panties_6 at slight_wobble with dissolve:
        zoom 1.03 xalign 0.5 yalign 0.5
    robin "Hah... hah... that was..."
    robin "So... fucking hot..."
    robin "I'm not used to you being so rough with me..."
    robin "I liked it..."
    "I laugh."
    pro "Maybe next time you should be the one calling all the shots then, huh?"
    pro "I wouldn't mind that either..."
    robin "Good... because next time we're fucking, I'm going to ride you until your balls dry."
    "Damn, I really brought out his kinkier side..."
    pro "I look forward to it, Robin..."
    play sound positive_event_01
    system "{color=#bb0028}Desire increased by 55{/color}"
    $ desire += 55
    $ achievement.grant("panties")
    jump jump_to_tomorrow