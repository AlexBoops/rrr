# GIFT MENU -------------------------------------------------------------------------------------------------------------------------------------------

screen gift_give_screen:
    modal True

    add "images/overlay/ui/interact/gift_give_screen.png"

    $ available_gifts = []

    if bear == True:
        $ available_gifts.append({
            'name': 'Stuffed Bear',
            'affection': 'Affection ++',
            'idle_image': 'images/overlay/gift/bear_idle.png',
            'hover_image': 'images/overlay/gift/bear_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("bear_gift")],
        })
    if console == True:
        $ available_gifts.append({
            'name': 'Game Console',
            'affection': 'Affection ++',
            'idle_image': 'images/overlay/gift/console_idle.png',
            'hover_image': 'images/overlay/gift/console_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("console_gift")],
        })
    if lingerie == True:
        $ available_gifts.append({
            'name': 'Cat Lingerie',
            'affection': '{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}\n{color=#ff87ff}Affection ++{/color}',
            'idle_image': 'images/overlay/gift/lingerie_idle.png',
            'hover_image': 'images/overlay/gift/lingerie_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("lingerie_gift")],
        })
    if restuarant_outfit == True:
        $ available_gifts.append({
            'name': 'Restaurant Waiter Outfit',
            'affection': '{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}',
            'idle_image': 'images/overlay/gift/restaurant_outfit_idle.png',
            'hover_image': 'images/overlay/gift/restaurant_outfit_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("restaurant_gift")],
        })
    if cat == True:
        $ available_gifts.append({
            'name': 'Cat Ears',
            'affection': '{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}',
            'idle_image': 'images/overlay/gift/cat_idle.png',
            'hover_image': 'images/overlay/gift/cat_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("cat_gift")],
        })
    if wine == True:
        $ available_gifts.append({
            'name': 'Wine',
            'affection': '{color=#bb0028}Desire ++{/color}\n{color=#918fff}Trust ++{/color}',
            'idle_image': 'images/overlay/gift/wine_idle.png',
            'hover_image': 'images/overlay/gift/wine_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("wine_gift")],
        })
    if buttplug == True:
        $ available_gifts.append({
            'name': 'Buttplug',
            'affection': '{color=#bb0028}Desire ++{/color}\n{color=#ff87ff}Affection ++{/color}',
            'idle_image': 'images/overlay/gift/buttplug_idle.png',
            'hover_image': 'images/overlay/gift/buttplug_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("buttplug_gift")],
        })
    if dildo == True:
        $ available_gifts.append({
            'name': 'Dildo',
            'affection': '{color=#bb0028}Desire ++{/color}',
            'idle_image': 'images/overlay/gift/dildo_idle.png',
            'hover_image': 'images/overlay/gift/dildo_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("dildo_gift")],
        })
    if panties == True:
        $ available_gifts.append({
            'name': 'Panties',
            'affection': '{color=#bb0028}Desire ++{/color}',
            'idle_image': 'images/overlay/gift/panties_idle.png',
            'hover_image': 'images/overlay/gift/panties_hover.png',
            'action': [Hide("gift_give_screen"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("panties_gift")],
        })

    hbox:
        spacing 30
        xpos 0.5
        xanchor 0.5
        ypos 0.5
        yanchor 0.5

        for gift in available_gifts:
            vbox:
                spacing 10
                align (0.5, 0.5)

                imagebutton:
                    idle gift['idle_image']
                    hover gift['hover_image']
                    action gift['action']
                    focus_mask True
                    hover_sound "audio/sound/interface_sounds/drop_003.ogg"
                    at gift_hover  # Include any transitions or animations
                    xalign 0.5

                text "{color=#ffffff}%s{/color}" % gift['name']:
                    font 'fonts/FredokaOne-Regular.ttf'
                    size 25
                    xalign 0.5
                    at hover  # Include any text animations

                text "{color=#ff87ff}%s{/color}" % gift['affection']:
                    font 'fonts/FredokaOne-Regular.ttf'
                    size 25
                    xalign 0.5
                    at hover  # Include any text animations

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at six_percent
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Hide("gift_give_screen"), Jump("show_correct_interact_screen")]
        xalign 0.5
        yalign 0.95

label show_correct_interact_screen:
    
        if time_of_day == "day":
            call screen interact_day
        
        if time_of_day == "afternoon":
            call screen interact_afternoon

# DAY -------------------------------------------------------------------------------------------------------------------------------------------

screen interact_day:
    modal True

    add "images/overlay/ui/interact/day/interact_bg.png"
    
    image "images/robin/robin_neutral.png"

    imagebutton:
        idle "images/overlay/ui/interact/chat_idle.png"
        hover "images/overlay/ui/interact/chat_hover.png"
        at anim_choice_button
        action [Hide("interact_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("chat_day")]
        xalign 0.2
        yalign 0.2

    imagebutton:
        idle "images/overlay/ui/interact/gift_idle.png"
        hover "images/overlay/ui/interact/gift_hover.png"
        at anim_choice_button
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("gift_give_screen")]
        xalign 0.8
        yalign 0.2

    imagebutton:
        idle "images/overlay/ui/interact/affection_idle.png"
        hover "images/overlay/ui/interact/affection_hover.png"
        at anim_choice_button
        action [Hide("interact_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_day")]
        xalign 0.2
        yalign 0.7

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at anim_choice_button
        action [Hide("interact_day"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("livingroom_day")]
        xalign 0.8
        yalign 0.7

label chat_day:
    scene livingroom_day
    show robin neutral
    "What would you like to do with Robin?"
    menu:
        "Say hi to Robin (Progression Level 0)" if robin_progression_level == 0 and key_task == 1:
            "You approach Robin and say hello."
            pro "Hey, Robin."
            pro "What are you up to?"
            robin "Oh nothing, I was just going to watch some TV."
            show robin smile
            robin "Did you need something?"
            pro "Just wanted to say hi."
            robin "Oh, okay."
            call screen interact_day with dissolve

        "Talk about 'Bussy Ball' (Progression Level 1)"  if robin_progression_level >= 1 and key_task >= 2:
            "You approach Robin, who seems to be watching Bussy Ball on TV."
            pro "Hey, Robin!"
            show robin smile
            robin "Hey, [protagonist_name]!"
            show robin open
            robin "Have you seen the latest news about Bussy Ball on Twinkr?"
            pro "Nah, I stopped using Twinkr when that billionaire bought it and renamed it to 'T.com'"
            show robin smile at jumper
            robin "Oh, you're missing out!"
            robin "They're going to have a special event for the series 30th anniversary next month."
            robin "I can't wait to see what they have in store."
            pro "That sounds exciting!"
            robin "Right? I'm so hyped for it!"
            robin "I hope they bring back some of the old characters."
            "He talks about the show for a while while and I listen intently."
            "I feel like I learned a little more about Robin from this conversation"
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 5{/color}"
            $ affection += 5
            jump afternoon
        
        "Ask about Robin's cosplay (Progression Level 2)" if robin_progression_level >= 2:
            "You approach Robin, who seems to be watching Bussy Ball on TV."
            pro "Hey, Robin!"
            show robin smile
            robin "Hey, [protagonist_name]!"
            show robin neutral
            robin "Did you need something?"
            pro "I was just wondering about your cosplay."
            robin "Oh! Was there something you wanted to know?"
            pro "I was just curious what other characters from Bussy Ball you've cosplayed as."
            show robin smile
            robin "Oh, I've cosplayed as a few characters from the show."
            robin "My most recent cosplay was 'Femgeta', the main rival in the show."
            robin "I thought it was a fun character to cosplay as."
            pro "That's really cool!"
            robin "Thanks! I'm glad you think so."
            robin "Um... actually."
            robin "Would you like to see some pictures I took in the outfit?"
            pro "Oh sweet, I'd love to see them!"
            robin "Hehe, okay."
            scene lr_talk1 with dissolve
            "He opens his phone and scrolls through the pictures."
            robin "It took me awhile to find the perfect wig."
            robin "Turns out, there's not a lot of wigs in his hair style out there."
            robin "But I managed to find one that worked!"
            "He talks passionately about his cosplay and I listen intently."
            "I feel like I learned a little more about Robin from this conversation."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 10{/color}"
            $ affection += 10
            jump afternoon
        
        "Ask about his favourite movie (Progression Level 3)" if robin_progression_level >= 3:
            "You approach Robin, who seems to be watching something on TV."
            pro "Hey, Robin!"
            show robin smile
            robin "Hey, [protagonist_name]!"
            show robin neutral
            robin "Did you need something?"
            pro "I was just wondering what your favourite movie is."
            show robin neutral blush
            robin "Oh... well..."
            robin "Um..."
            pro "What?"
            robin "It's... a dirty movie..."
            pro "Oh, really?"
            robin "Yeah... it's called 'The Nutty Professor'."
            pro "The Nutty Professor?!"
            show robin open blush at jumper
            robin "Shut up! I know it's embarrassing!"
            robin "But it's a classic, okay?!"
            pro "I'm not judging you!"
            robin "You better not!"
            robin "It's a good movie, okay?!"
            robin "It's funny and heartwarming!"
            show robin neutral blush
            robin "..."
            show robin smile blush
            robin "Also the right amount of sexy..."
            show black with dissolve
            "He talks passionately about the movie and I listen intently."
            hide black with dissolve
            pro "It sounds weirdly good..."
            robin "Right?!"
            robin "I'm glad you understand!"
            robin "Here, let me put on my favourite scene for you!"
            scene lr_talk2 with dissolve
            "He puts on a clip from the movie."
            "Immediately, the lewd elements of the movie become apparent."
            robin "Oh, uh... I forgot about this part..."
            movie "Oh Professor, you're so big!"
            movie "Yes, take it my dear!"
            movie "Be injected with knowledge by my seed!"
            robin "Oh god, I'm so sorry!"
            robin "I forgot about this part!"
            pro "It's okay, it's okay!"
            robin "I swear it's not all like this!"
            pro "I trust you..."
            "We watch the movie for a while and have a great time."
            "I feel like we've gotten closer from this experience."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 15{/color}"
            $ affection += 20
            jump afternoon
    
            
    
        "Go back":
            call screen interact_day with dissolve

label affection_day:
    scene livingroom_day
    show robin neutral
    "What would you like to do with Robin?"
    menu:
        "Watch a show with Robin (Progression Level 0)"  if robin_progression_level == 0 and key_task == 1:
            show robin neutral
            pro "Hey Robin, did you want to watch a show together?"
            robin "Oh, uh..."
            robin "I was just about to go to my room actually, but maybe later?"
            pro "Oh, okay."
            "I don't think I have enough {color=#ff87ff}affection{/color} with Robin to do this."
            call screen interact_day with dissolve
      

        "Watch a show with Robin (Progression Level 1)"  if robin_progression_level >= 1 and key_task >= 2:
            show robin neutral
            pro "Hey Robin, did you want to watch a show together?"
            show robin smile
            robin "Yea, sure!"
            robin "What do you want to watch?"
            pro "Well I was thinking of watching this new comedy series on FemFlix."
            robin "Oh, that sounds fun!"
            pro "It sounds really good, but I guess we'll have to see."
            robin "Alright, put it on!"
            scene black with dissolve
            "We turn on the TV and start watching the show."
            scene lr_affection1 with dissolve
            robin "Dude, this is hilarious!"
            robin "I can't believe I haven't seen this before."
            pro "I know, right? It's so good!"
            "We watch the show for a while and have a great time."
            "I feel like we've gotten closer from this experience."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 7{/color}"
            $ affection += 7
            jump afternoon

        "Compliment Robin's outfit (Progression Level 2)"  if robin_progression_level >= 2:
            show robin neutral
            pro "Your outfit looks really cute today, Robin."
            show robin smile blush
            robin "Oh, but I wear the same thing every day."
            pro "I know, but it looks good on you."
            pro "It's hitting different today."
            scene lr_affection2 with dissolve           
            robin "O-oh!"
            "His face turns red."
            robin "Th-thanks, [protagonist_name]."
            robin "I'm glad you like it..."
            robin "Good to know I'm doing something right, hehe."
            pro "Of course! You gotta help me redo my wardrobe sometime."
            robin "I'd love to!"
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 15{/color}"
            $ affection += 15
            jump afternoon
        
        "Give Robin a foot massage (Progression Level 3)"  if robin_progression_level >= 3:
            show robin neutral
            pro "Hey Robin!"
            robin "Oh, hey [protagonist_name]..."
            "He looks a little tired."
            pro "Is everything okay?"
            pro "You seem a little stressed out."
            robin "Oh, it's nothing..."
            robin "I've just been having this aching pain in my feet lately."
            pro "Really? That sucks..."
            pro "Do you want me to give you a foot massage?"
            show robin open blush
            robin "W-what...!"
            "His face turns red."
            robin "You don't have to do that..."
            pro "It's no big deal!"
            pro "I give really good foot massages, trust me."
            robin "O-okay, if you say so..."
            scene white with dissolve
            "He takes off his shoes and socks."
            scene lr_affection3 with dissolve
            "I start massaging his feet."
            robin "Oh...!"
            "He lets out a small moan."
            robin "That feels so good..."
            robin "I didn't know you were this nice at massages..."
            pro "I told you I was good!"
            robin "Hehe, you're right."
            robin "Fuck... that's good..."
            robin "I can already feel the pain going away."
            "I continue massaging his feet for a while."
            "I feel like we've gotten closer from this experience."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 20{/color}"
            $ affection += 20
            jump afternoon

        "Go back":
            call screen interact_day with dissolve

# AFTERNOON -------------------------------------------------------------------------------------------------------------------------------------------

screen interact_afternoon:
    modal True

    add "images/overlay/ui/interact/afternoon/interact_bg.png"
    
    image "images/robin/robin_neutral.png"

    imagebutton:
        idle "images/overlay/ui/interact/chat_idle.png"
        hover "images/overlay/ui/interact/chat_hover.png"
        at anim_choice_button
        action [Hide("interact_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("chat_afternoon")]
        xalign 0.2
        yalign 0.2

    imagebutton:
        idle "images/overlay/ui/interact/gift_idle.png"
        hover "images/overlay/ui/interact/gift_hover.png"
        at anim_choice_button
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("gift_give_screen")]
        xalign 0.8
        yalign 0.2

    imagebutton:
        idle "images/overlay/ui/interact/affection_idle.png"
        hover "images/overlay/ui/interact/affection_hover.png"
        at anim_choice_button
        action [Hide("interact_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Jump("affection_afternoon")]
        xalign 0.2
        yalign 0.7

    imagebutton:
        idle "images/overlay/ui/interact/back_idle.png"
        hover "images/overlay/ui/interact/back_hover.png"
        at anim_choice_button
        action [Hide("interact_afternoon"), Play("sound", "audio/sound/interface_sounds/click_003.ogg"), Show("kitchen_afternoon")]
        xalign 0.8
        yalign 0.7

label chat_afternoon:
    scene kitchen
    show robin neutral
    "What would you like to do with Robin?"
    menu:
        "Say hi to Robin (0)"  if robin_progression_level >= 0 and key_task >= 1:
            "You approach Robin and say hello."
            pro "Hey, Robin."
            pro "What are you up to?"
            robin "Just thinking about what to eat for lunch."
            show robin smile
            robin "Maybe I'll make a peanut butter and jelly sandwich, hehe."
            robin "Want one?"
            pro "Nah I'm good, thanks."
            robin "No worries, talk to you later!"
            call screen interact_afternoon with dissolve
        
        "Ask Robin about his favourite snacks (1)"  if robin_progression_level >= 1 and key_task >= 2:
            pro "Hey Robin, what's your favourite snack?"
            show robin smile
            robin "Oh, that's easy!"
            robin "I love anything with chocolate in it."
            robin "Chocolate chip cookies, chocolate cake, chocolate ice cream..."
            robin "Chocolate coins, chocolate bars, chocolate..."
            robin "You get the idea, hehe."
            pro "Wow... you really like chocolate."
            robin "Duh, it's the best."
            robin "Other than that, I usually stick with chips and soda."
            robin "You know, the usual snacks."
            pro "I see, I see."
            pro "I'll keep that in mind whenever I want to get you something."
            robin "Oh, you don't have to do that!"
            robin "But if you do, I won't say no, hehe."
            "I feel like I learned a little more about Robin from this conversation."
            call screen interact_afternoon with dissolve

        "Ask Robin for some cooking tips (2)"  if robin_progression_level >= 2:
            pro "Hey Robin, do you have any cooking tips?"
            show robin smile
            robin "Oh, is there something specific you want to know?"
            pro "I was just wondering if you had any general tips."
            pro "Specifically for something like pasta."
            robin "Oh, pasta is easy!"
            robin "The trick is to not overcook it."
            robin "You want it to be al dente, which means it's firm to the bite."
            robin "You also want to salt the water before you put the pasta in."
            robin "It helps season the pasta from the inside out."
            pro "Oh, I see."
            pro "I'll keep that in mind next time I make pasta."
            robin "Good luck!"
            call screen interact_afternoon with dissolve

        "Make Robin a special 'milkshake' (3)"  if robin_progression_level >= 3:
            pro "Hey Robin, I was thinking of making a special milkshake."
            show robin smile
            robin "Oh, that sounds fun!"
            robin "What kind of milkshake are you making?"
            pro "It's a secret recipe."
            pro "But I promise you'll love it."
            robin "Oh, I can't wait!"
            pro "For this milkshake, I'll need you to go to your room."
            robin "Oh, okay."
            robin "Let me know when it's ready."
            scene white with dissolve
            "He goes to his room."
            scene kitchentalk_1 with dissolve
            show kitchentalk_2 with dissolve:
                subpixel True
                xalign 0.6 yalign 1.25
                ease 0.08 zoom 1.0 yoffset 25
                ease 0.15 yoffset -25
                repeat
            "I start masturbating in the kitchen."
            pro "Fuck... Robin..."
            "I imagine Robin in all sorts of dirty poses."
            show kitchentalk_3 at slight_wobble with dissolve:
                subpixel True
                xalign 0 yalign 0.5
                xoffset -30
                ease 5.0 xalign 0.05
            robin "Hey... come put it in my ass."
            robin "Don't be shy..."
            show kitchentalk_4 at slight_wobble with dissolve:
                subpixel True
                xalign 1.0 yalign 0.5
                xoffset 30
                ease 5.0 xalign 0.95
            robin "Oh fuck, that feels so fucking good..."
            robin "Keep pounding my bussy..."
            "I get closer to orgasm as I fantasise about Robin."
            pro "Fuck... Robin..."
            menu:
                "Continue":
                    "I continue to masturbate furiously."
            "I can't hold out any longer, I'm going to cum."
            scene white with dissolve
            "I quickly grab a cup and cum inside of it."
            pro "Fuck~!"
            "I fill the cup all the way to the top."
            pro "That should be good..."
            scene kitchen with dissolve
            pro "Robin, the special milkshake is done."
            robin "Okay, I'm coming."
            show robin smile with easeinleft
            "Robin arrives in the kitchen, excited for his 'milkshake.'"
            pro "Here's your milkshake."
            robin "Thanks! It looks delicious."
            scene kitchentalk_5 with dissolve
            "He starts to drink the milkshake, a little bit spilling onto his face in his excitement."
            robin "Oops!"
            robin "Mmm, it's really sweet!"
            robin "A little salty too."
            robin "The consistency is really thick... but I like it!"
            pro "I'm glad you like it."
            robin "It's so good I think I'm gonna finish it all!"
            play sound positive_event_01
            system "{color=#bb0028}Desire increased by 20{/color}"
            $ desire += 20
            jump evening            

        "Go back":
            call screen interact_afternoon with dissolve

label affection_afternoon:
    scene kitchen
    show robin neutral
    "What would you like to do with Robin?"
    menu:
        "Give Robin a pat on the head (Progression Level 0)"  if robin_progression_level == 0 and key_task == 1:
            "You approach Robin."
            show robin smile
            robin "Hey, [protagonist_name]."
            robin "Did you need something?"
            pro "Just was wondering if you..."
            robin "Wondering if I what?"
            "I don't think I have enough {color=#ff87ff}affection{/color} with Robin to do this."
            pro "Nevermind, I'll talk to you later."
            robin "Oh, okay..."
            call screen interact_afternoon with dissolve
      
        "Give Robin a pat on the head (Progression Level 1)"  if robin_progression_level >= 1:
            "You approach Robin."
            show robin smile
            robin "Hey, [protagonist_name]."
            scene kitchenaffection_1 with dissolve
            "I reach out and pat Robin on the head."
            robin "Wh-what!"
            "His entire face turns red."
            robin "What was that for?"
            pro "Just felt like it."
            robin "[protagonist_name]..."
            robin "You're so weird, hehe."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 7{/color}"
            $ affection += 7
            jump evening

        "Grab Robin's cheeks (Progression Level 2)"  if robin_progression_level >= 2:
            "You approach Robin."
            show robin smile
            robin "Hey, [protagonist_name]."
            scene kitchenaffection_2 with dissolve
            "I reach out and smush Robin's cheeks."
            robin "W-wha!"
            "He pouts."
            robin "Why are you smushing my cheeks?"
            pro "Just felt like it."
            robin "You're so mean, hehe."
            robin "But I guess I'll let it slide this time."
            robin "Just don't do it again, okay?"
            pro "No promises!"
            robin "Grr..."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 15{/color}"
            $ affection += 15
            jump evening

        "Fantasise about Robin (Progression Level 3)"  if robin_progression_level >= 3:
            "You approach Robin."
            show robin smile
            robin "Hey, [protagonist_name]."
            stop music fadeout 1.0
            scene white with dissolve
            "I close my eyes and imagine what it would be like if Robin were wearing a kitchen apron."
            play music sensual fadein 1.0
            scene kitchenaffection_3 with dissolve:
                subpixel True
                zoom 2.0 xalign 0.3 yalign 0.5
                ease 4.5 zoom 1.0 xalign 0.5 yalign 0.5
            robin "Hey [protagonist_name]..."
            robin "You worked so hard today!"
            robin "Let your cute femboy make you dinner tonight."
            pro "Oh, Robin..."
            robin "I'll make you something special, just for you."
            robin "I'll make sure it's delicious and nutritious!"
            robin "My special milkshake has lots, and lots, and lots of protein!"
            pro "What kind of protein?"
            robin "The best kind!"
            robin "The kind that comes from my body!"
            pro "Oh... you mean..."
            robin "Hehe, you got it!"
            robin "I'll make sure you get all the protein you need tonight!"
            robin "Then we can have fun all night long!"
            robin "Just you and me, [protagonist_name]..."
            pro "Hehe..."
            robin "Hey... [protagonist_name]..."
            robin "What are you doing?"
            pro "Huh?"
            scene white with dissolve
            stop music fadeout 1.0
            "I snap out of my daydream."
            scene kitchen with dissolve
            show robin open with dissolve
            robin "You were just staring off into space."
            robin "Is everything okay?"
            pro "Oh, uh..."
            pro "I was just thinking about something."
            robin "Oh, okay."
            "You feel more affectionate towards Robin after that daydream."
            "Robin thinks you're a little weird now."
            play sound positive_event_01
            system "{color=#ff87ff}Affection increased by 20{/color}"
            $ affection += 20
            jump evening

        "Go back":
            call screen interact_afternoon with dissolve