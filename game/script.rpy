
label start:
    stop music fadeout 1.0
    show black with dissolve
    system "This game contains mature, adult content that is intended for an 18+ audience only."
    system "By playing this game, you agree that you are 18 years of age or older."
    system "If you are not 18 years of age or older, please exit the game now."
    menu:
        system "By clicking 'I agree', you confirm that you are 18 years of age or older."
        "I agree.":
            system "Okay then, let's get started!"
    $ protagonist_name = "Sparrow"
    $ temp_name = renpy.input("Enter your name (Sparrow by Default):")
    if temp_name.strip() != "": 
        $ protagonist_name = temp_name
    

    play music summerlove_full_loop fadein 2.0
    scene mc_bedroom with dissolve
    "I just moved to a new city to start my career as an indie game developer."
    "Until recently, I was living with my parents and working a corporate job that I hated."
    "I decided to take a leap of faith and move to a new city to pursue my dream of making games."
    "Money is tight though, so I decided to take advantage of the extra room in my apartment and find a roommate."
    scene prologue1 with dissolve
    "I put up an ad online and got a decent amount of responses, but none of them really panned out."
    "There was this one guy who I thought was perfect. He didn't try to haggle over rent and said he wouldn't even be home often."
    "But turns out he just wanted to use the apartment as a drug den where he could stash his weed and have his friends over all the time."
    "Another couple asked if I would be willing to join their polyamorous relationship as a third partner."
    "Of course, I declined."
    "I just wanted a normal roommate that I would get along with and wouldn't cause any trouble."
    "After a few hours and a headache, I finally found a person that looked decent."
    scene prologue2 with dissolve
    "His name was Robin."
    "Based on our conversation, I could sort of tell he was an introvert, which would be perfect since I don't want a loud roommate."
    "He was also willing to move in right away."
    "Just to be safe though, I asked him to send me a picture of himself along with ID before taking a deposit."
    scene prologue3 with dissolve
    "He sent a photo of himself and, to my surprise, he looked more like a girl than a guy."
    scene prologue4 with dissolve
    "He had curly black hair, a small, pointed face, and a soft, feminine looking body. His eyes were light blue and his lips were full and pouty."
    "After looking at the photo, I wasn't quite sure what to think."
    "He definitely didn't look like any of the other guys I interviewed, and his appearance was very ambiguous."
    "However, it's not like I'm looking for a roommate based on their looks, and he seemed like a perfectly nice guy over our messages."
    scene black with dissolve
    "Today is his move-in day."
    stop music fadeout 2.0
    scene prologue5 with dissolve
    "I'm waiting outside of the apartment building for Robin to arrive."
    pro "He should be here any minute now."
    "I figured it would make a good first impression to greet him at the door and help him move his stuff in."
    scene black with dissolve
    "After a few minutes, a car pulls up."
    pro "This must be him."
    play music happiness_full_loop fadein 2.0
    scene prologue6 with dissolve
    show robin neutral with easeinleft
    $ achievement.grant("meet_robin")
    "Robin steps out of the car wearing a black cropped hoodie and shorts."
    "His clothes hugged his thin figure tightly and I could see the shape of his hips and chest."
    "I felt a little nervous as he walked towards me, I've never met someone who looked like him before."
    pro "Hey! Are you Robin?"
    voice voiceline1
    robin "Yeah, h-hi."
    pro "It's nice to meet you. I'm [protagonist_name]."
    voice voiceline2
    robin "It's nice to meet you too!"
    pro "Is this all the stuff you're bringing? I can help you take it inside."
    show robin open
    voice voiceline3
    robin "Oh don't worry about it, I can handle it myself."
    pro "I insist."
    show robin smile
    voice voiceline4
    robin "Oh... okay."
    scene prologue7 with dissolve
    "He softly smiles for a moment before turning around to grab his bag."
    "As he grabbed his bags, his shorts slightly slipped down."
    voice voiceline5
    robin "I only have two boxes to bring to my room, so we can each take one if you'd like..."
    pro "Uh... for sure."
    "Even his voice is super feminine, it's almost surprising that he's actually a guy."
    scene black with dissolve
    "I pick up one of the boxes and take it inside."
    scene apartment_stairway with dissolve
    show robin neutral with easeinbottom
    pro "So Robin, where did you live before this?"
    voice voiceline6
    robin "I lived in New York City, in an apartment."
    pro "New York!? Why would you ever want to leave that place!?"
    voice voiceline7
    robin "Oh, uh..."
    show robin open
    voice voiceline8
    robin "I guess a change of pace would be the best way to describe it."
    pro "A change of pace?"
    show robin neutral
    voice voiceline9
    robin "Yeah..."
    voice voiceline10
    robin "I, um, just needed a quiet place for my career."
    voice voiceline11
    robin "Somewhere where I don't have to worry about the problems that come with a big city."
    pro "Oh that makes sense."
    pro "I've never really lived in a big city before, so I guess I wouldn't know what it's like."
    voice voiceline12
    robin "It's not all bad, but it's definitely not for everyone."
    pro "I can imagine."
    scene apartment_livingroom with dissolve
    "We set down the boxes in his room while continuing our conversation."
    show robin neutral with easeinbottom
    pro "So what do you do for work?"
    voice voiceline13
    robin "I uh..."
    voice voiceline14
    robin "W-work from home."
    pro "Oh that's convenient, I'm in the same sort of situation myself."
    pro "I'm an indie game dev, so I basically can work from wherever I want provided I have my computer and an internet connection."
    show robin smile at jumper
    voice voiceline15
    robin "Wow, that's so cool!"
    voice voiceline16
    robin "A game developer seems like a dream job to be honest."
    pro "Eh, it's alright. Not the most stable career I could be in, but I've always wanted to make games and I finally got my opportunity to do so."
    voice voiceline17
    robin "What were you doing before this?"
    pro "I was working as a software engineer for a big tech company."
    pro "I didn't like the corporate environment, so I decided to go indie and make my own games."
    voice voiceline18
    robin "That's really brave of you."
    pro "Thanks, I guess."
    scene black with dissolve
    "We finished unpacking Robin's belongings."
    scene apartment_livingroom with dissolve
    show robin smile with easeinbottom
    voice voiceline19
    robin "Thank you for your help [protagonist_name]."
    voice voiceline20
    robin "I really appreciate it, I've never really moved to a new place all on my own before so I was a little nervous."
    pro "No problem! Is there anything else you need help with?"
    show robin open
    voice voiceline21
    robin "Um, no I think that was everything..."
    show robin neutral
    pro "Well if you need anything, I'll be in my room."
    voice voiceline22
    robin "O-okay. I'll let you know if I do."
    pro "Nice meeting you Robin!"
    pro "I think we'll get along just fine."
    show robin smile
    voice voiceline23
    robin "Nice meeting you too!"
    scene black with dissolve
    "Robin smiled at me before I turned and walked back to my room."
    scene mc_bedroom with dissolve
    "I'm glad he seems like a nice person, but his appearance and demeanor really caught me off guard."
    "He also seemed weirdly vague about why he moved and his career, am I sure he's not some serial killer looking for his next victim?"
    "But then again, he seemed pretty nervous to move here so maybe he was just being awkward or shy."
    "And he is going to be living with me for who knows how long, so it would be best for the both of us to just get along well."
    "It's strange though. He acts like a girl and he's very pretty like one too. The way he acts is... cute. Almost like a fembo-"
    pro "Nope! No. That's inappropriate and weird to think about."
    stop music fadeout 2.0
    scene black with dissolve
    "I decide to get some work done for the day."
    scene black with dissolve
    pause 1.0
    play sound positive_stinger
    show prologue95 with dissolve
    pause 1.5
    hide prologue95 with dissolve
    scene mc_bedroom_evening with dissolve
    pro "Ah shit, my back..."
    "I've been working on my project for a few hours and it's starting to get late."
    "Maybe I should take a break to grab some dinner."
    pro "I wonder if Robin wants to join me, it could give us a chance to get more comfortable with each other as roommates."
    "Also wouldn't hurt to split the bill..."
    pro "Maybe I should invite him anyway. Just in case."
    screen robin_room_prologue:
        modal True
        add "images/backgrounds/mc_bedroom_evening.png"

        hbox:
            xalign 0.5
            yalign 0.1
            spacing 5 

            vbox:
                align (0.9, 0.5)
                imagebutton:
                    idle "images/overlay/house_icons/robin_room_idle.png"
                    hover "images/overlay/house_icons/robin_room_hover.png"
                    action [Hide("robin_room_prologue"), Play("sound", "audio/sound/interface_sounds/drop_003.ogg"), Jump("icon_clicked")]

    show screen robin_room_prologue with dissolve
    system "Click on the icon to visit Robin's room."

label icon_clicked:
    scene black with dissolve
    "I stand up from my chair and walk over to Robin's room."
    "Knock knock"
    voice voiceline24
    robin "C-come in!"
    play music summerlove_full_loop fadein 2.0
    scene robin_room1 with dissolve
    show robin neutral with dissolve
    voice voiceline25
    robin "Hey [protagonist_name]."
    pro "Hey Robin, how's everything going?"
    voice voiceline26
    robin "It's good so far. Just getting settled in."
    pro "That's great! Um, I was about to go get something to eat. Do you wanna join me?"
    show robin open
    voice voiceline27
    robin "Oh, uh..."
    pro "Oh sorry I don't mean to be pushy! You're not obligated to come with me or anything it's just an offer. I just thought I would-"
    show robin neutral at jumper
    voice voiceline28
    robin "I-it's okay! I'm just going to be a little busy soon..."
    voice voiceline29
    robin "Is it okay if I give you a rain check?"
    pro "Yeah totally! No worries!"
    pro "Hey listen, I totally understand that you're just settling in, so if you need anything or have any questions then feel free to come to me!"
    voice voiceline30
    robin "Okay, thank you..."
    pro "See you later, Robin!"
    voice voiceline31
    robin "Yeah... see you later."
    "As I'm leaving, I spot something from one of his boxes out of the corner of my eye."
    show prologue8 with easeinleft
    "Is that a..."
    "A dildo?"
    scene black with dissolve
    "I quickly look away and leave his room."
    pro "Nope! Shut up and stop being creepy. Not your business."
    "I head back to my room and close the door."
    scene mc_bedroom_evening with dissolve
    pro "I should probably let him settle in for the rest of the day."
    pro "I can start getting to know him more tomorrow."
    stop music fadeout 2.0
    show black with dissolve
    "I decide to spend the rest of my evening working on my game."
    "I ended up ordering some takeout for dinner."
    window hide
    pause 1.0
    play sound positive_stinger
    show prologue9 with dissolve
    pause 1.5
    scene black with dissolve
    "..."
    scene mc_bedroom with dissolve
    "Knock Knock"
    "The next day, I wake up to a knock on my room door."
    pro "Hm...?"
    play music afternoontea_full_loop fadein 2.0
    scene prologue10 with dissolve
    voice voiceline32
    robin "Uh... [protagonist_name]?"
    voice voiceline33
    robin "It's Robin. Sorry to bother you."
    pro "Just a second."
    "I drag myself out of bed and over to the door."
    show prologue12 with dissolve
    pro "Shit, sorry I slept in."
    pro "Did you need something?"
    voice voiceline34
    robin "It's okay, it must've been a late night huh..."
    voice voiceline35
    robin "I was just wondering whether you were okay with me doing your laundry, I was gonna do mine anyway so..."
    pro "Oh! That's nice of you, but you really don't have to."
    voice voiceline36
    robin "I-it's no problem at all, really. I want to do something nice for you since you were so kind yesterday."
    voice voiceline37
    robin "You know, as a thank you for helping me move in and not being a total creep..."
    scene prologue11 with dissolve
    show robin neutral with dissolve
    "Well I sure feel like one after seeing his dildo last night..."
    pro "Uh, well then sure, if you really want to then I can take you up on that offer."
    show robin smile
    voice voiceline38
    robin "Awesome, I'll do what ever you have in your laundry bin right now."
    pro "Hey uh, Robin."
    pro "If you wanted to grab lunch, we could get to know each other a bit and talk about dividing house chores?"
    show robin neutral
    voice voiceline39
    robin "Oh uh..."
    "He looks nervous again, like he did yesterday."
    voice voiceline40
    robin "What do you want to do for lunch? I don't exactly have much money..."
    pro "Oh I can cover both of us, it's no problem."
    pro "Consider it like a housewarming gift."
    voice voiceline41
    robin "I appreciate the offer."
    show robin smile
    voice voiceline42
    robin "Maybe a bit later, once I get settled in y'know..."
    hide robin with easeoutbottom
    "Robin smiles at me before he turns and walks away."
    pro "Weird, he keeps stuttering around me when I try getting closer..."
    "It's probably just because he's a little awkward, at least I hope that's the case..."
    scene black with dissolve
    "I decide to get dressed and start my day."
    jump tutorial

label tutorial:
    scene tut1 with dissolve
    system "Welcome to the UI tutorial."
    system "This tutorial will guide you through the user interface of the game."
    scene tut2 with dissolve
    system "This is the time of day indicator."
    system "Different events are available at different times of the day."
    scene tut3 with dissolve
    system "This is the menu to select which room you are in."
    system "You can click on the icons to visit different rooms."
    system "This icon with Robin indicates that he is currently in this room."
    scene tut4 with dissolve
    system "This is the status menu."
    system "You can view your progress with Robin here and see your relationship status."
    scene tut5 with dissolve
    system "This is the tasks menu."
    system "You can view your current tasks here and get hints on what to do next."
    scene tut6 with dissolve
    system "This is the artifacts menu."
    system "You can view all of the artifacts, which are the collectible stickers seen around the house, here."
    system "As you collect more artifacts, additional unlockable images will appear."
    scene tut1 with dissolve
    system "Now that you are familiar with the UI, you can start playing the game."
    system "Be sure to check the status and tasks menu often to keep track of your progress."
    scene black with dissolve
    system "Good luck and have fun!"
    
label day:
    if robin_progression_level == 1 and key_task == 2 and desire >= 60 and not desireevent_1:
        stop music fadeout 1.0
        $ desireevent_1 = True
        jump desireevent_1

    play music afternoontea_full_loop fadein 1.0
    $ time_of_day = "day"
    call screen mc_bedroom_day with dissolve
    
label afternoon:
    play music summerlove_full_loop fadein 1.0
    $ time_of_day = "afternoon"
    call screen mc_bedroom_afternoon with dissolve

label evening:
    play music happiness_full_loop fadein 1.0
    $ time_of_day = "evening"
    call screen mc_bedroom_evening with dissolve

label night:
    play music starry_night_nopercussion fadein 1.0
    $ time_of_day = "night"
    call screen mc_bedroom_night with dissolve

label jump_to_tomorrow:
    if time_of_day == "day":
        jump afternoon
    elif time_of_day == "afternoon":
        jump evening
    elif time_of_day == "evening":
        jump night
    elif time_of_day == "night":
        jump day

label back_to_prev_time:
    if time_of_day == "day":
        jump day
    elif time_of_day == "afternoon":
        jump afternoon
    elif time_of_day == "evening":
        jump evening
    elif time_of_day == "night":
        jump night

label desireevent_1:
    play sound pleasured_exertion_slow fadein 0.5 volume 0.2 loop
    scene mc_bedroom_night with dissolve
    "I wake up in the middle of the night to the sound of whimpering."
    pro "These are the same as that night before..."
    scene storybeat1_2 with dissolve
    menu:
        "Should I investigate?"

        "Yes":
            scene black with dissolve
            "I go to check it out."
            stop sound fadeout 0.5
            scene desireevent1_1 with dissolve
            play sound pleasured_exertion_slow fadein 0.5 volume 0.6 loop
            "I end up outside of Robin's room, the sounds are coming from his room."
            "His door is slightly open, but I can hear him inside whimpering."
            pro "Robin...?"
            scene black with dissolve
            "I gently push the door open and peek inside."
            scene desireevent1_2 at slight_wobble with dissolve:
                zoom 1.1 xalign 0.5 yalign 0.5
                ease 5.0 zoom 1.2 
            robin "Hah... hah..."
            "Holy shit, he's riding a dildo on his bed..."
            robin "Ngh..."
            robin "Ah..."
            robin "Mphm..."
            scene desireevent1_3 at slight_wobble with dissolve:
                zoom 1.1 xalign 0.5 yalign 0.5
                ease 5.0 zoom 1.2
            "His ass is bouncing up and down, the dildo sliding in and out smoothly."
            robin "Ha... ha..."
            robin "Mmphm..."
            "Will he notice me staring?"
            "I should stop watching but..."
            "I can't look away..."
            robin "Fuck..."
            "I need to stop, this is wrong."
            stop sound fadeout 1.0
            scene black with dissolve
            "Without making a sound, I slowly back away and go back to my room."
            jump day

        "No":
            stop sound fadeout 0.5
            "I should go back to sleep."
            scene black with dissolve
            pause 1.0
            jump day


screen game_end:

    imagebutton:
        xalign 0.2
        yalign 0.5
        at demo_button
        hover_sound "audio/sound/interface_sounds/drop_003.ogg"
        idle "gui/overlay/wishlist_button.png"
        hover "gui/overlay/wishlist_button_hover.png"
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), OpenURL("https://store.steampowered.com/app/3257270/Haunted_by_Femboy/")]

    imagebutton:
        xalign 0.8
        yalign 0.5
        at demo_button
        hover_sound "audio/sound/interface_sounds/drop_003.ogg"
        idle "gui/overlay/discord_button.png"
        hover "gui/overlay/discord_button_hover.png"
        action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), OpenURL("https://discord.gg/u9GwfyjJNs")]

    text _("{color=#ffffff}Thank you for playing{/color}") xalign 0.5 yalign 0.2:
        size 95
        font 'fonts/FredokaOne-Regular.ttf'

    hbox:
        spacing 40
        xalign 0.5
        yalign 0.9
        
        textbutton _("{color=#0094FF}Main Menu{/color}"):
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at anim_choice_button
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), MainMenu()]
        
        textbutton _("{color=#0094FF}Load Save File{/color}"):
            hover_sound "audio/sound/interface_sounds/drop_003.ogg"
            at anim_choice_button
            action [Play("sound", "audio/sound/interface_sounds/click_003.ogg"), ShowMenu('load')]
