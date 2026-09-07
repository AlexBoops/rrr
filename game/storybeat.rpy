label story_beat1:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    stop music fadeout 1.0
    scene black with dissolve
    pause 1.0
    play sound positive_stinger
    show storybeat1_1 with dissolve
    pause 1.5
    hide storybeat1_1 with dissolve
    pro "All done for the day."
    scene mc_bedroom_night with dissolve
    pro "Damn, I forgot to prepare dinner."
    pro "I guess I'll just order takeout tonight, no way am I cooking something for myself this late."
    scene storybeat1_2 with dissolve
    play sound pleasured_exertion_slow fadein 0.5 volume 0.2 loop
    "As I get up from my desk, I hear a strange noise coming from outside my room."
    pro "Huh?"
    "It sounded like whimpering..."
    pro "Wait a second."
    "Is that..."
    "Robin?"
    pro "Is he crying...?"
    pro "Or hurt...?"
    "I'm not sure whether I should be concerned or just leave him alone."
    "He did seem like an introverted guy so maybe he's just overwhelmed by moving and having a roommate all at once."
    "But I'd still feel like crap if I didn't check on him..."
    pro "Maybe I should see what's wrong."
    stop sound fadeout 0.5
    scene storybeat1_3 with dissolve
    play sound pleasured_exertion_slow fadein 0.5 volume 0.6 loop
    "I step out of my room and walk over to Robin's room."
    "Before I go inside, I knock on the door softly."
    pro "Robin?"
    stop sound
    voice voiceline43
    robin "Ah!"
    scene storybeat1_3:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.1 zoom 1.1 xalign 0.5 yalign 0.5
        ease 0.1 zoom 1.08 xalign 0.5 yalign 0.5
        pause 1.5
        ease 2 zoom 1.0
    "I hear a sudden thud followed by scrambling from the other side of the door."
    pro "What was that...?"
    voice voiceline44
    robin "U-uhh, come in!"
    pro "Okay..."
    show white with dissolve
    "I slowly open the door and look inside."
    pro "Hey, sorry to disturb you..."
    pro "Are you okay?"
    scene storybeat1_4 with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.7
        ease 5.0 zoom 1.0 yalign 0.5
    voice voiceline45
    robin "Oh, uh... yea, I'm fine."
    "He's laying on his bed breathing heavily, his hair in a mess and he seems sweaty."
    voice voiceline46
    robin "Did you need something?"
    pro "Nothing, I just heard what sounded like whimpering or something coming from your room?"
    pro "Just wanted to make sure you were alright."
    voice voiceline47
    robin "That was um..."
    voice voiceline48
    robin "Uhh..."
    "Oh no..."
    "Did I walk in on him when he was..."
    pro "Must've just been the wind I guess... haha..."
    pro "I'll let you sleep then, sorry for bothering you Robin."
    voice voiceline49
    robin "No no it's okay, thank you for checking on me..."
    pro "It's no problem, have a good night!"
    voice voiceline50
    robin "Y-you too."
    scene black with dissolve
    "As I close the door, I can hear Robin let out a sigh of relief."
    pro "Sorry Robin..."
    "I quickly head back to my room in shame."
    scene mc_bedroom_night with dissolve
    "This is so embarrassing."
    "I really have to get used to roommate life."
    "I should give him space, I don't want him to feel uncomfortable living here."
    "I'll just go to bed and forget about it."
    scene black with dissolve
    pause 1.0
    play sound positive_stinger
    show prologue9 with dissolve
    pause 1.5
    show black with dissolve
    scene livingroom_day with dissolve
    show robin neutral with dissolve
    play music afternoontea_full_loop fadein 1.0
    "The next day, I decide to talk with Robin in the living room."
    voice voiceline51
    robin "Oh, hey [protagonist_name]..."
    pro "Hey Robin, is it okay if we talk?"
    voice voiceline52
    robin "Uh yea, for sure."
    voice voiceline53
    robin "Is something wrong?"
    pro "Not really, I just wanted to discuss how our roommate situation will work."
    pro "Since you moved in, we haven't really gotten a chance to address any details such as paying for groceries and utilities."
    voice voiceline54
    robin "Oh. Okay."
    "Robin seems to look a little anxious at this topic. Hopefully he'll be able to handle it."
    pro "I was just wondering if you wanted to make a roommate contract or something."
    pro "It's my first time doing something like this, so I'm sorry if I'm not good at communicating."
    pro "Just know that I'm willing to work with you to make living here comfortable for the both of us."
    show robin open
    voice voiceline55
    robin "I trust you, no need for a contract or anything."
    show robin neutral
    voice voiceline56
    robin "Sorry if that isn't apparent, I'm just not used to having a roommate and didn't want to mess anything up right as I moved in..."
    pro "Hey Robin, I promise I'm not going to bite.."
    pro "We'll have plenty of time to get used to each other and establish boundaries and all that."
    show robin smile
    voice voiceline57
    robin "Yeah, you're right."
    show robin open
    voice voiceline58
    robin "So then... what exactly do you have in mind?"
    scene black with dissolve
    "We spend the next hour discussing groceries, utilities, and other miscellaneous house chores."
    "Robin seems to be more relaxed now that we've discussed everything."
    "I slowly feel that Robin is opening up to me more."
    scene storybeat1_5 with dissolve
    pro "I feel like that should be everything we need to talk about..."
    show storybeat1_6
    voice voiceline59
    robin "Y-yea. For sure."
    hide storybeat1_6
    pro "Is there anything else you want to discuss?"
    show storybeat1_6
    voice voiceline60
    robin "Oh! Well..."
    hide storybeat1_6
    pro "Hm?"
    show storybeat1_6
    voice voiceline61
    robin "I was just wondering how safe this area was?"
    voice voiceline62
    robin "A big reason I left my old place was due to safety concerns..."
    hide storybeat1_6
    pro "Safety concerns?"
    menu:
        "Is there anything in specific you're worried about?":
            show storybeat1_6
            voice voiceline63
            robin "Just... the area in general. I don't know much about it."
            hide storybeat1_6
            pro "Oh it's very safe here, don't worry about it."
            pro "I did a lot of research before moving, so I can assure you that this area is very safe."
            pro "It's mostly just a quiet neighborhood with a lot of families and elderly people."
            show storybeat1_7
            voice voiceline64
            robin "Oh, okay. That's really reassuring to hear."
            play sound positive_event_01
            system "Robin {color=#918fff}trusts{/color} you a {color=#8AFF59}little bit{/color} more now."
            $ trust += 3

        "Oh it's very safe here, don't worry about it.":
            show storybeat1_6
            voice voiceline65
            robin "Oh, that's good to hear..."
            hide storybeat1_6
            pro "It's mostly just a quiet neighborhood with a lot of families and elderly people."
            pro "Don't worry, you're safe here."
            show storybeat1_6
            voice voiceline66
            robin "I'm just a little paranoid about safety."
            hide storybeat1_6
            show storybeat1_7
            voice voiceline67
            robin "But thank you for the reassurance."
            pro "Of course, I understand. If you ever feel unsafe, you can always come to me for help."
            pro "I'll beat them up for ya!"
            voice voiceline68
            robin "Hehe, thank you."
            play sound positive_event_01
            system "Robin {color=#918fff}trusts{/color} you a {color=#8AFF59}considerably{/color} more now."
            $ trust += 5
        
        "Why are you scared about safety?":       
            show storybeat1_6
            voice voiceline69
            robin "Just uh..."
            hide storybeat1_6
            voice voiceline70
            robin "Nevermind, forget it."
            show storybeat1_6
            voice voiceline71
            robin "I'm sure it'll be fine."

    hide storybeat1_7
    show storybeat1_6
    voice voiceline72
    robin "Sorry that I even brought it up..."
    hide storybeat1_6
    pro "No no, it's okay to ask about this stuff. You just moved in, after all."
    pro "Was there anything else you wanted to talk about?"
    show storybeat1_6
    voice voiceline73
    robin "O-okay. So uh... have you seen any weird guys around?"
    hide storybeat1_6
    pro "Weird guys?"
    show storybeat1_6
    voice voiceline74
    robin "Yea, y'know... sketchy people that seem suspicious..."
    voice voiceline75
    robin "Any men who approach you late at night or stare at you too long..."
    hide storybeat1_6
    pro "Robin..."
    show storybeat1_6
    voice voiceline76
    robin "B-because those are usually the ones to watch out for..."
    hide storybeat1_6
    "Robin begins to fidget nervously."
    pro "You can always come to me for help, alright?"
    show storybeat1_6
    voice voiceline77
    robin "Alright..."
    hide storybeat1_6
    pro "Have you had past issues with people following you...?"
    scene livingroom_day with dissolve
    show robin neutral with dissolve
    voice voiceline78
    robin "Uh... well..."
    "It feels like I don't have enough {color=#918fff}trust{/color} with Robin for him to confide in me."
    voice voiceline79
    robin "...I would rather not talk about it."
    pro "Ah, sorry Robin. Didn't mean to pry."
    voice voiceline80
    robin "No, it's okay..."
    show robin smile
    voice voiceline81
    robin "Anyways, thank you for talking with me about all of this. It makes me feel better."
    voice voiceline82
    robin "I feel like I'll be able to enjoy living here now."
    scene black with dissolve
    "I smile at Robin and head back to my room."
    scene mc_bedroom with dissolve
    pro "He seems nice, I'm glad he's feeling more comfortable."
    "I still want to get to know him more."
    "Maybe doing things with him throughout the day will help me gain his {color=#918fff}trust{/color}, {color=#ff87ff}affection{/color}, and {color=#bb0028}desire{/color} to talk to me."
    pro "But I need to be careful. I don't want to make him uncomfortable."
    "I'll just see what happens, maybe I'll find more reasons to bond with him."
    $ achievement.grant("storybeat1")
    $ renpy.end_replay()
    scene black with dissolve
    system "You are now able to do tasks around the house."
    system "Certain tasks will raise certain stats."
    system "You can check your stats in the status menu."
    system "You can also see how many points you need left in the task menu."
    system "Goodluck."
    $ key_task += 1
    jump afternoon

label story_beat2:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    stop music fadeout 1.0
    scene black with dissolve
    pause 1.0
    play sound positive_stinger
    show storybeat1_1 with dissolve
    pause 1.5
    hide storybeat1_1 with dissolve
    play music starry_night_nopercussion fadein 1.0
    "I wrap up my work for the night."
    scene mc_bedroom_night with dissolve
    pro "Phew, I'm so tired..."
    "I feel like I've been slacking off lately, I've barely gotten any work done these past few days."
    "Though I really grinded today, I worked non-stop for hours."
    pro "Maybe I should take a break tomorrow."
    "I sigh and push myself out of my chair."
    pro "I guess I could just relax the rest of the night, maybe watch a movie or show in the living room."
    scene black with dissolve
    "I head to the living room and plop myself onto the couch."
    scene storybeat2_2 with dissolve
    pro "Alright, let's see here..."
    "I peruse through the various movies on FemFlix, nothing really catches my interest."
    pro "Eh, I'll just binge some shows instead."
    scene storybeat2_3 with dissolve
    "As I'm about to turn on an anime, I see Robin walk into the living room."
    scene storybeat2_4 with dissolve
    voice voiceline83
    robin "Oh, hey [protagonist_name]. I didn't expect you to be out here so late."
    pro "Ah, hey Robin."
    pro "I decided to take a break from work, I've been in my room all day."
    voice voiceline84
    robin "Oh, that's nice."
    pro "Yeah. Hey, you wanna watch something?"
    voice voiceline85
    robin "What were you going to watch?"
    pro "I was thinking about watching a show or something."
    pro "You know, clear my head up a bit."
    voice voiceline86
    robin "Oh, okay."
    "I scoot over to make room for Robin and pat the empty spot next to me."
    pro "Here, sit down."
    scene black with dissolve
    "Robin sits down next to me."
    scene storybeat2_5 with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.6
        ease 5.0 zoom 1.0 yalign 0.5
    pro "What do you like to watch?"
    voice voiceline87
    robin "Um..."
    voice voiceline88
    robin "Well, I'm not that picky..."
    voice voiceline89
    robin "I do like watching anime."
    pro "Really? Me too!"
    voice voiceline90
    robin "Yea, I watched a lot of it growing up."
    voice voiceline91
    robin "I used to read a ton of manga and watch anime every day actually."
    pro "Sweet, a fellow nerd huh."
    pro "I was planning on rewatching 'Bussy Ball Z' if you wanna join me!"
    scene storybeat2_6
    voice voiceline92
    robin "Ooh, I love 'Bussy Ball'!"
    "Robin's face lights up and he smiles brightly."
    voice voiceline93
    robin "I'd love to watch it with you!"
    pro "Hell yeah, I'll start it up."
    scene black with dissolve
    "I hit play and lean back on the couch."
    "We watch the first episode together. I look over to Robin, who looks invested in the show."
    scene storybeat2_7 with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.6
        ease 5.0 zoom 1.0 yalign 0.5
    pro "Man, I used to love this show..."
    voice voiceline94
    robin "Same, I've always been a huge fan."
    voice voiceline95
    robin "I just wish they made more episodes..."
    voice voiceline96
    robin "I was obsessed with it as a kid."
    pro "Me too, I used to collect the figures and everything."
    pro "Typical nerd things, haha."
    voice voiceline97
    robin "Collecting figurines isn't that bad!"
    voice voiceline98
    robin "I actually cosplayed as one of the characters..."
    pro "Holy shit, really?"
    voice voiceline99
    robin "Yeah..."
    scene storybeat2_8
    voice voiceline100
    robin "It was a while ago, though..."
    pro "I didn't know you were into that."
    pro "That's so cool though!"
    scene storybeat2_7
    voice voiceline101
    robin "Uhh... Yeah..."
    voice voiceline102
    robin "It's nothing special, it was just a shitty cosplay..."
    voice voiceline103
    robin "It was mostly just something that I did for work."
    pro "Wait, I thought you worked from home?"
    scene storybeat2_8
    voice voiceline104
    robin "Oh, uh..."
    voice voiceline105
    robin "I guess I never really told you but..."
    voice voiceline106
    robin "I'm a live-streamer."
    pro "A live-streamer?"
    voice voiceline107
    robin "Yeah."
    pro "That's so cool!"
    voice voiceline108
    robin "It's not that interesting."
    voice voiceline109
    robin "I just play video games and talk to my viewers..."
    pro "Still, it's cool that you can make a career out of that."
    pro "I've always wondered how I could get into that kind of thing."
    scene storybeat2_7
    voice voiceline110
    robin "It's definitely fun, I'm glad I found something I'm good at."
    scene storybeat2_8
    voice voiceline111
    robin "I'm just not very good at marketing myself, so playing while I'm in a cosplay does bring in views."
    voice voiceline112
    robin "I just don't feel like I'm good enough to do it without it."
    pro "Maybe you should show me sometime."
    voice voiceline113
    robin "Ah, I don't know..."
    voice voiceline114
    robin "I guess I could get my cosplay out from one of my boxes..."
    pro "That would be awesome!"
    voice voiceline115
    robin "It's just not something I'm proud of, that's all."
    menu:
        "You shouldn't put yourself down like that.":
            voice voiceline116
            robin "I guess you're right..."
            pro "You should be proud of your work, Robin."
            pro "It's clear that you're passionate about it."
            pro "Plus, I'm very easy to impress."
            scene storybeat2_7
            voice voiceline117
            robin "Hehe, that's sweet."
            play sound positive_event_01
            system "Robin's {color=#ff87ff}affection{/color} for you has increased a {color=#8AFF59}a lot{/color} more now."
            $ affection += 6

        "Come on, I'm sure it's great.":
            voice voiceline118
            robin "I don't know..."
            pro "Dude, I'm a massive nerd."
            pro "Cosplaying is awesome, I'd love to see it."
            scene storybeat2_7
            voice voiceline119
            robin "I guess I could show you..."
            play sound positive_event_01
            system "Robin's {color=#ff87ff}affection{/color} for you has increased a {color=#8AFF59}little bit{/color} more now."
            $ affection += 3

        "If it makes you happy, that's all that matters.":
            voice voiceline120
            robin "Yeah, you're right."
            voice voiceline121
            robin "I just haven't really showed this side of my personality to anyone before."
            pro "Well, I'm glad you're showing it to me."
            pro "Now c'mon, show me your cosplay!"
            scene storybeat2_7
            voice voiceline122
            robin "Okay!"

    scene black with dissolve
    "Robin gets up from the couch."
    voice voiceline123
    robin "I'm gonna go get it, I'll be right back."
    pro "Okay, I'll wait here."
    stop music fadeout 1.0
    scene livingroom_night with dissolve
    "Robin heads to his room."
    pro "He seems nervous about showing me his cosplay..."
    pro "I hope it's not because he's embarrassed or something."
    pro "Maybe it's just something he doesn't like to talk about."
    pro "Also live-streaming was not what I had in mind when he told me he 'worked from home'."
    scene black with dissolve
    "After a few minutes and some rustling from Robin's room, he returns."
    voice voiceline124
    robin "Okay... I got it..."
    play music starry_night_nopercussion fadein 1.5
    scene storybeat2_9 with dissolve
    "He steps out of his room and into the living room."
    show robin cosplay neutral with easeinright
    $ achievement.grant("storybeat2_1")
    "He's wearing a top made of bandages, just like in the show, with baggy orange pants."
    show robin cosplay neutral:
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 1.5 zoom 1.3 yalign 0.2
    "He even has a wig on for the protagonists signature spikey, blonde hair."
    show robin cosplay neutral:
        ease 1.5 zoom 1.3 yalign 0.05
    "He looks absolutely adorable."
    show robin cosplay neutral:
        ease 1.5 zoom 1.0 xalign 0.5 yalign 0.5
    pro "Wow! This is awesome!"
    voice voiceline125
    robin "You think so...?"
    pro "Hell yeah! You look great!"
    voice voiceline126
    robin "Really...?"
    show robin cosplay smile
    voice voiceline127
    robin "Thanks..."
    "Robin's face goes bright red and he looks away from me."
    pro "Come on, you should be proud of this!"
    voice voiceline128
    robin "I.. I guess I am proud of it."
    voice voiceline129
    robin "It's just... it's been a long time since I last wore it so... it's embarrassing."
    voice voiceline130
    robin "I didn't think I'd end up showing you it, but it seemed like you really wanted to see it so... here it is..."
    pro "You look awesome, like fucking amazing!"
    pro "Seriously, you look really good."
    voice voiceline131
    robin "Hehe... thank you..."
    pro "Don't get all embarrassed!"
    voice voiceline132
    robin "I don't think I can help it..."
    voice voiceline133
    robin "Anyways, I'll go get changed..."
    hide robin cosplay neutral with easeoutbottom
    "He heads back into his room."
    show robin tank with easeinbottom
    "Robin comes back into the room wearing his pajamas."
    voice voiceline134
    robin "Thank you for watching the show with me. It was nice..."
    pro "Yeah, for sure. Anytime you wanna watch it with me again, let me know."
    show robin tank smile
    voice voiceline135
    robin "Definitely. I really enjoyed it."
    voice voiceline136
    robin "Seeing something nostalgic with you was really nice."
    voice voiceline137
    robin "It also took my mind off things and relaxed me."
    pro "Yea moving is really stressful..."
    pro "You know, you can always talk to me about this kind of stuff."
    voice voiceline138
    robin "Really?"
    pro "Of course. I'm your friend after all."
    pro "If you have any worries, just let me know and I'll help you out."
    pro "I hope we can be closer soon so you feel comfortable talking to me about everything."
    voice voiceline139
    robin "Yea, for sure!"
    voice voiceline140
    robin "I had a really nice time hanging out with you tonight, [protagonist_name]."
    pro "For sure. We'll have to hang out more often."
    pro "Hopefully, that'll give us both something to look forward to."
    pro "But anyways, I'm gonna go ahead and head to bed."
    pro "I'll see you tomorrow morning."
    voice voiceline141
    robin "Yea, for sure. Goodnight!"
    pro "Goodnight Robin!"
    scene black with dissolve
    "I get up from the couch and head into my room."
    scene mc_bedroom_night with dissolve
    pro "Whew, it feels good to finally get off my ass."
    pro "I guess I should get to bed. I'm pretty exhausted."
    stop music fadeout 2.0
    scene storybeat2_10 with dissolve
    "I change into my pajamas and plop down onto my bed."
    pro "Hopefully he can trust me more and talk to me about the real reason he left his old apartment."
    scene black with dissolve
    "I drift off to sleep..."
    "..."
    "..."
    play sound suck_low fadein 1.0 loop
    unknown "Mphm... Mphm..."
    "I feel a pleasant sensation on my dick..."
    "It's warm and wet..."
    scene storybeat2_11 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        linear 0.35 yalign 1.0 zoom 1.06
        ease 0.35 yalign 0.5 zoom 1.0
        repeat
    "I slowly open my eyes to find Robin giving me a blowjob."
    pro "Rob- Robin?! What are you-"
    pro "A-ah... Robin... Wait..."
    "His eyes sparkle and he stares at me seductively."
    pro "Robin..."
    pro "What are you doing?"
    voice voiceline142
    robin "Hm? What do you mean?"
    "His voice sounds beautiful and elegant, almost hypnotizing..."
    pro "No... I don't understand..."
    voice voiceline143
    robin "Don't you want this?"
    "He bats his eyelashes and stares at me lovingly."
    pro "Want what...?"
    voice voiceline144
    robin "I want you, silly~"
    "My heart begins to race..."
    pro "What are you talking about...?"
    voice voiceline145
    robin "Shh, just enjoy it..."
    voice voiceline146
    robin "I'll make you feel good~"
    pro "Wait..."
    pro "Robin..."
    "He stares at me with half-lidded eyes and continues bobbing his head up and down..."
    pro "Ah... Robin... Stop..."
    "His mouth is so warm, his lips wrap around my shaft perfectly."
    pro "Robin... Ah... Ngh..."
    pro "Fuck... This feels amazing..."
    pro "Fuck..."
    pro "Don't stop... Don't stop..."
    "His tongue runs up and down my shaft, sending chills down my spine."
    pro "I'm gonna cum... I'm gonna cum..."
    pro "Don't stop... Keep going..."
    menu:
        "Cum":
            pro "I'm cumming...!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    scene storybeat2_12 at slight_wobble with dissolve
    "I finally release inside of Robin's mouth."
    pro "Ah... Robin..."
    scene storybeat2_13 at slight_wobble with dissolve
    "He stares up at me, opening his mouth to show all of my cum on his tongue."
    voice voiceline147
    robin "Hehe..."
    voice voiceline148
    robin "Bet you'd love it if this really happened, huh?"
    pro "W-what?"
    scene black with dissolve
    "Everything starts fading to black once more."
    scene storybeat2_10 with dissolve
    "I blink and Robin is gone."
    "I'm left there laying in my room."
    pro "Did I just have a wet-dream... about my roommate?"
    pro "Fuck, that's weird..."
    scene black with dissolve
    "I slowly drift back into unconsciousness..."
    "..."
    $ achievement.grant("storybeat2_2")
    $ renpy.end_replay()
    $ key_task += 1
    $ robin_progression_level += 1
    play sound positive_event_01
    system "{color=#FF5454}Progression Level{/color} has increased"
    show prologue9 with dissolve
    pause 1.0
    hide prologue9 with dissolve
    jump day

label story_beat3:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    stop music fadeout 1.0
    pause 1.0
    scene mc_bedroom with dissolve
    play music afternoontea_full_loop fadein 1.0
    pro "God, the weather is gorgeous outside."
    pro "Summer's almost over and I feel like all I've done is work."
    pro "Maybe I should take a break today and enjoy the sun before the season ends."
    pro "What would be fun and relaxing?"
    pro "Maybe a day at the beach could be fun?"
    pro "Though, I dunno what I would do all by myself..."
    scene livingroom_day with dissolve
    "I go to the living room and catch Robin leaving his room."
    show robin neutral with easeinbottom
    robin "Good morning!"
    pro "Oh, hey Robin."
    pro "The weather is really nice today."
    show robin open
    robin "Oh wow! It's really sunny today."
    pro "Yeah, but it's almost the end of summer."
    pro "I was thinking about going to the beach."
    pro "It just wouldn't be much fun to go by myself."
    pro "If you're free today and are up for it, maybe we could go on a little roommate-trip to the beach?"
    show robin smile at jumper
    robin "R-really? You wanna hang out with me at the beach?"
    pro "Of course! I think it'd be fun to hang out with you outside of the apartment."
    show robin open
    robin "Oh, uh..."
    show robin smile
    robin "If you really wanna go with me, I'd love to join you!"
    pro "Great! I'll start packing some towels and sunscreen!"
    pro "You've got a swimsuit, right?"
    show robin neutral
    robin "Oh shoot, I don't really have anything suitable for the weather."
    show robin open
    robin "The weather in New York is always so cold and rainy, so I've never really gone out and bought myself proper 'beach' clothes."
    pro "I may have an extra pair of swimming trunks if you want?"
    robin "No, it's okay!"
    show robin neutral
    robin "There should be shops in the area that sell that kind of stuff, right?"
    pro "Yeah, I think so."
    pro "I guess we can hit up the shops before the beach."
    show robin smile
    robin "Sounds like a plan!"
    robin "I'm so excited, this is going to be so much fun!"
    "It almost feels like we're going on a date or something."
    pro "I'll order us a ride to take us to the beach, you go freshen up and pack whatever you need to."
    pro "And remember, apply some sunscreen!"
    robin "Yeah, definitely!"
    scene black with dissolve
    "I head to my room to pack my stuff."
    scene mc_bedroom with dissolve
    pro "I'm so glad Robin agreed to go to the beach with me."
    pro "He's always so shy and reserved, so I didn't think he'd want to come with me."
    pro "Though, I have felt us getting a lot closer lately. It really feels like he's opening up to me."
    pro "He's just so sweet and caring, it's hard not to connect with him."
    pro "It's nice having a roommate that you get along with."
    pro "I wonder if he likes me in that way..."
    pro "No, no. I shouldn't think like that."
    pro "We're just friends, I can't read into things too much."
    pro "He probably just wants to hang out with me as a friend."
    pro "Yeah, that's probably it..."
    scene black with dissolve
    "I pack my bag with some towels, sunscreen, and snacks."
    "I throw on my swimming trunks and a white tanktop before heading out to the living room again."
    "Robin is already stood waiting for me."
    scene storybeat3_1 with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.6
        ease 5.0 zoom 1.0 yalign 0.5
    "He's wearing a sexy black bikini."
    "He also has a white shawl draped over his shoulders, slightly covering his body."
    pro "R-Robin..."
    pro "I thought you didn't have any beach attire?"
    robin "Well... that might've been a little lie."
    robin "I wear this for some of my, ahem, live-streams."
    pro "Why would you need to... oh."
    pro "I see."
    robin "Yeah, I was embarrassed by it, but I'd rather not spend any more money on a new one."
    robin "So, I'll just wear it for today."
    pro "It's really, really cute. I think it suits you!"
    robin "Hehe... thanks I guess."
    pro "Anyways, you all set Robin?"
    robin "Yeah, I think so. I packed sunscreen, some snacks, and a towel."
    pro "Alright, let's head out!"
    scene black with dissolve
    stop music fadeout 1.0
    "We take our bags and get into our ride, which is waiting outside."
    "After a short drive, we arrive at the beach."
    $ achievement.grant("storybeat3_1")
    play music 'audio/music/CR_Upbeat_Jingle_Loop.mp3'
    scene storybeat3_beach1 with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.8
        ease 3.0 zoom 1.0 yalign 0.5
    "The sun is bright, the air is warm, and the ocean breeze is refreshing."
    robin "Wow, it's beautiful here."
    pro "Isn't it? I haven't been to a beach in ages!"
    robin "Then we'd better make the most of it!"
    robin "Let's set up our stuff over there!"
    pro "Good idea, it's a perfect spot."
    scene black with dissolve
    "We find a nice spot on the beach and set up our towels."
    "The beach is packed today, with families and couples scattered about."
    scene storybeat3_2 with dissolve:
        subpixel True
        zoom 1.2 xalign 0.2 yalign 0.5
        ease 5.0 zoom 1.0 xalign 0.5
    robin "There's a lot of people here..."
    pro "Yeah, looks like we weren't the only ones with the idea to go to the beach today."
    pro "Anyways, what do you want to do first Robin?"
    robin "I don't know, what do people usually do at the beach?"
    robin "We could play in the water? Build a sandcastle? Take a walk?"
    pro "Any of those sound fun to me!"
    pro "Though, I wouldn't mind just laying out and sunbathing for a bit."
    robin "That sounds relaxing!"
    robin "Let's do it!"
    scene white with dissolve
    "We put our towels out on the sand and lie down to sunbathe."
    scene storybeat3_3 with dissolve:
        subpixel True
        zoom 1.3 xalign 0.1 yalign 0.5
        ease 10.0 zoom 1.1 xalign 0.5
        pause 1.0
        ease 3.0 zoom 1.0
    robin "The sun feels so nice..."
    pro "Yeah, I love this kind of weather."
    robin "It was always rainy in New York, so this is a nice change."
    robin "It's good to just get away from everything sometimes and relax."
    "Robin's skin is beginning to glow in the sun, making him look even more radiant than usual."
    "His black swimsuit makes him look so fucking sexy..."
    pro "Y-yeah, it's nice."
    pro "Anyways, what are you thinking about for the rest of the day?"
    robin "Well, I don't really want to go for a swim or anything..."
    robin "Maybe we could go for a walk or something."
    robin "Y'know, just chat and enjoy the weather."
    pro "Sounds like a plan!"
    pro "Let's go check it out right now."
    robin "Oh, before we leave could you help me reapply my sunscreen?"
    pro "O-oh."
    pro "Uh... sure."
    robin "I wasn't able to reach my back properly at home, and I don't want to get sun burnt..."
    scene storybeat3_4 with dissolve
    "He rolls over and lays down on his stomach, taking off the straps of his swimsuit so I can get better coverage of his back."
    "His asshole is slightly visible because of how tight and short his swimsuit is."
    pro "Did you want me to apply it everywhere..."
    robin "If that's not too much trouble, please."
    pro "Ok, I'll try my best."
    show beach_hand1 with dissolve:
        xpos 1265 ypos 264
        ease 1.0 xoffset -15
        ease 1.0 xoffset 13
        repeat
    show beach_hand2 with dissolve:
        xpos 523 ypos 252
        ease 1.0 xoffset -15
        ease 1.0 xoffset 13
        repeat
    "I apply Robin's back with sunscreen and begin rubbing it on him."
    "I feel my dick getting hard just rubbing his body and hearing his quiet moans."
    robin "Your hands are so gentle..."
    pro "Oh, I'm sorry... Do you need me to rub harder?"
    robin "No, it's good just like that..."
    robin "It feels nice, hehe."
    "Oh fuck, why is this turning me on so much?"
    "I continue rubbing it all over his back, stopping just before I reach his ass."
    robin "Why'd you stop?"
    pro "Oh, uh..."
    pro "I finished your back and didn't want to rub any further."
    pro "You know, because it might make you uncomfortable or something..."
    robin "I'd rather you be thorough, to be honest."
    robin "It's only awkward if you make it awkward."
    pro "Sure..."
    pro "Just let me know when to stop."
    hide beach_hand1 with dissolve
    hide beach_hand2 with dissolve
    show beach_hand3 with dissolve:
        xpos 1135 ypos 315
        ease 1.0 xoffset -15
        ease 1.0 xoffset 13
        repeat
    show beach_hand4 with dissolve:
        xpos 397 ypos 327
        ease 1.0 yoffset -15
        ease 1.0 yoffset 13
        repeat
    play sound slight_exertion_slow loop fadein 0.5
    "Internally, I'm about to pass out. This doesn't feel real."
    "My cute, femboy roommate is letting me rub his ass with sunscreen."
    "His ass is so perky and smooth, it's almost unreal."
    "I rub the sunscreen all over his ass and in between his cheeks."
    robin "Mm..."
    "I can hear him softly moaning..."
    "Is this... turning him on?"
    "I continue rubbing his ass, making sure to be thorough."
    robin "I think that's good enough."
    stop sound fadeout 1.0
    $ achievement.grant("storybeat3_2")
    hide beach_hand3 with dissolve
    hide beach_hand4 with dissolve
    "Fuck, I was really getting into it."
    robin "Thank you [protagonist_name]!"
    scene white with dissolve
    "He gets up and stretches."
    "I quickly try tucking my boner into the waistband of my swim trunks."
    pro "Y-yeah, no problem."
    pro "You ready for that walk?"
    stop music fadeout 1.0
    robin "Yeah, let's go!"
    scene storybeat3_5 with dissolve:
        subpixel True
        zoom 1.3 xalign 0.1 yalign 0.5
        ease 5.0 zoom 1.1 xalign 0.5
        pause 1.0
        ease 3.0 zoom 1.0        
    play music 'audio/music/CR_Happiness_Piano_Low_Loop.mp3'

    "We walk along the beach, admiring the scenery and chatting."
    "Robin seems to be enjoying himself a lot."
    "He's been smiling and laughing a lot, which is a nice change from his usual quiet demeanor."
    robin "No way, you really fought some dude over some french fries!"
    pro "Yea, college was wild..."
    robin "Wow, I've never really experienced anything like that."
    robin "I've always just kept to myself, even back in New York."
    pro "Well, now you're stuck with me and I'm gonna make sure you have the time of your life."
    robin "Hehe, thanks."
    robin "I sure lucked out when I found you as a roommate, huh."
    pro "What do you mean?"
    robin "Well, you're a really nice guy."
    robin "You aren't pushy or creepy, and you actually want to hang out with me."
    robin "It's rare to find someone like that."
    pro "I'm glad you feel good about being my roommate. We both really lucked out, huh."
    robin "Yeah, I guess we did!"
    "Robin and I continue walking, the conversation flowing easily."
    robin "So, you don't have a girlfriend or anything?"
    pro "Nope, haven't had the time to really meet anyone."
    pro "Just been busy with work, I honestly barely leave the house..."
    pro "You?"
    show storybeat3_6
    robin "Oh, I uh... no."
    robin "I'm not..."
    pro "Right... not into girls?"
    robin "Yea... though I guess you probably already realized that."
    pro "How about a boyfriend?"
    robin "I um, no."
    pro "Hmm, no experience either?"
    robin "Nope, I'm a complete virgin."
    robin "Not that I'm proud of it or anything."
    show storybeat3_7
    robin "I've just never had the chance, or really been interested in anyone."
    pro "Well, I'm sure you'll find someone eventually."
    robin "I dunno..."
    robin "Some people aren't meant to find people, and I'm fine being one of those people."
    pro "What?"
    pro "Now what makes you think you aren't meant to find someone."
    robin "Well, look at me."
    robin "I'm shy, quiet, and have a body like a girl's."
    show storybeat3_6
    robin "I'm not exactly a prime cut of beef, y'know?"
    menu:
        "Hey, I think you're great!":
            robin "Yeah, it's easy to say that when you're not me."
            pro "I'm serious, Robin."
            pro "You're a really great person, and I'm sure you'll find someone who sees that."
            hide storybeat3_6
            hide storybeat3_7
            show storybeat3_5
            robin "Thanks, [protagonist_name]."
            play sound positive_event_01
            system "Robin {color=#918fff}trusts{/color} you {color=#8AFF59}much{/color} more now."
            $ trust += 13

        "You're super sweet and kind.":
            show storybeat3_8 with dissolve
            robin "I-I am?"
            pro "Yeah, you are."
            robin "Thanks..."
            robin "I'm, uh, not used to people saying that to me."
            robin "It's nice to hear..."
            play sound positive_event_01
            system "Robin's {color=#ff87ff}affection{/color} for you has increased {color=#8AFF59}much{/color} more now."
            $ affection += 13

        "Not in a weird way but you're very, very cute.":
            show storybeat3_8 with dissolve
            robin "R-really?"
            pro "Yeah, really."
            robin "I-I don't know what to say..."
            robin "That's really sweet of you to say..."
            "His face goes red."
            play sound positive_event_01
            system "Robin's {color=#bb0028}desire{/color} for you has increased {color=#8AFF59}much{/color} more now."
            $ desire += 13            

    robin "I-I just assumed I wasn't good enough for anyone."
    robin "But maybe I'm wrong..."
    pro "You are wrong, I'm certain of that haha."
    scene black with dissolve
    "Robin and I finish our walk and head back to where we set up our towels and chairs."
    scene storybeat3_9 with dissolve
    robin "Honestly I'm so happy that we went to the beach today, I really needed this."
    pro "Right? Catching this gorgeous weather one last time before autumn was totally worth it."
    robin "Yeah, totally!"
    show storybeat3_2
    robin "Anyways, what time is it?"
    robin "I don't want to stay out too late or anything."
    "I reach into my pockets to grab my phone, but it isn't there."
    pro "What the fuck, where's my phone?"
    robin "It isn't in your trunks?"
    pro "No, it's not..."
    pro "I must've dropped it earlier on our walk, shit."
    pro "I'm going to quickly run and retrace our steps, you stay here okay?"
    robin "Oh, okay..."
    robin "Do you want me to come help you look?"
    pro "No it's cool."
    scene black with dissolve
    "I leave Robin and retrace our steps, searching the sand and the rocks near the water."
    "I'm freaking out, what if I can't find it and have to buy a new phone?"
    "After a few minutes of searching, I finally find it wedged between two rocks."
    pro "Fuck, that was a close call."
    "I head back with my phone in hand."
    stop music fadeout 1.0
    pro "Hey Robin, I found my ph-"
    scene storybeat3_10 with dissolve:
        subpixel True
        zoom 1.2 xalign 0.5 yalign 0.5
        ease 5.0 zoom 1.0
    play music 'audio/music/INTRIGUE.mp3'

    pro "What the fuck?"
    robin "Uh... can you please leave me alone..."
    man "C'mon beautiful, just go for a quick swim with me."
    man "I can show you a good time."
    robin "I'm fine, just leave me alone."
    robin "I'm with someone."
    man "He's not here, c'mon. We won't tell."
    "He's getting harassed by some random fucking dude."
    man "I'm a lot of fun, trust me."
    "He tries grabbing Robin's ass."
    robin "H-hey!"
    robin "Keep your hands off of me, you fucking creep!"
    man "Should a pretty little thing like you be speaking to me like that?"
    "I can feel the rage building up inside of me."
    "I'm about to kick his fucking ass."
    pro "Hey asshole!"
    scene storybeat3_11:
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 0.5 zoom 1.7 xalign 0.45 yalign 0.2
    man "Huh?"
    scene white with dissolve
    "Before he gets a chance to process that I'm approaching him, I sucker punch him in the face."
    scene storybeat3_12 at slight_wobble with dissolve:
        subpixel True
        zoom 1.4 xalign 0.45 yalign 0.5
        ease 5.0 zoom 1.01 xalign 0.5
    robin "O-oh!"
    pro "Get the fuck away from him, or you're gonna end up with a broken fucking jaw."
    man "Fuck you dude!"
    man "He's not even that cute anyways, I could tell he's a total bottom."
    "He spits on the ground and walks away."
    stop music fadeout 1.0
    pro "You okay, Robin?"
    robin "Y-yeah, I'm fine."
    robin "T-that was... are you okay?"
    pro "Yeah, I'm good."
    pro "What a fucking asshole."
    robin "Yeah, definitely..."
    robin "I can't believe you protected me..."
    "He's still shaking, but I can tell he's relieved."
    robin "I thought I was going to have to just stand there and take it."
    pro "Robin..."
    pro "C'mon, let's go."
    robin "N-no it's okay..."
    robin "I'm fine I'm just... a little shaken."
    robin "I still want to hang out."
    pro "Are you sure?"
    robin "Yeah, I'm sure."
    pro "At the very least we should get out of this area."
    pro "Let's go find a quieter spot to hang out."
    robin "Okay..."
    $ achievement.grant("storybeat3_3")
    scene black with dissolve
    "We grab our stuff and find a secluded area away from the other people."
    "We lay down on the sand."
    play music 'audio/music/CR_Happiness_Piano_Low_Loop.mp3' 
    scene storybeat3_13 with dissolve:
        subpixel True
        zoom 1.3 xalign 0.1 yalign 0.5
        ease 3.0 zoom 1.0 xalign 0.5
    robin "You know, I'm not used to people sticking up for me like that."
    show storybeat3_14
    robin "It was nice..."
    pro "Well, you shouldn't have to deal with shit like that."
    pro "Nobody should."
    show storybeat3_13
    robin "Yeah, I know."
    robin "I just don't like causing trouble."
    robin "I try to ignore it, but some people just won't leave me alone."
    pro "It's not your fault that they're assholes."
    pro "You shouldn't have to deal with it, and I'll be happy to step in if anything like that happens again."
    show storybeat3_14
    robin "Thanks, that means a lot."
    robin "You're really..."
    robin "Really just..."
    show storybeat3_15
    robin "..."
    robin "Nevermind..."
    pro "What is it?"
    robin "Forget it, don't worry..."
    "What was he going to say?"
    pro "Um, okay."
    pro "Well, I'm glad you're feeling better."
    scene storybeat3_16 with dissolve:
        subpixel True
        zoom 1.6 xalign 0.1 yalign 0.5
        ease 15.0 zoom 1.1 xalign 0.5 
    "We stare up at the sky and watch the clouds slowly move by."
    pro "Hey Robin, can I ask you a personal question?"
    robin "Uh, sure."
    pro "What was the real reason you left your old place and moved way out here?"
    robin "Oh..."
    robin "Um... well..."
    pro "It's okay if you don't want to talk about it."
    robin "No, it's okay..."
    robin "I've never told anyone about this, but I guess I should talk about it."
    robin "As you know, I'm a live-streamer."
    robin "And I love it, really."
    robin "But theres a ton of creeps online."
    robin "At first they were easy to ignore, just block them from my livestream chat and move on."
    robin "But then they harassed me on Twinkr... and FemstaGram..."
    robin "Pretty much just saying creepy things that sexualized me on all my social media platforms."
    pro "Whoa, that sounds horrible."
    robin "Yea... it was."
    robin "It was manageable though, it's just the internet right?"
    stop music fadeout 1.5
    scene black with dissolve
    robin "Well, at least thats what I thought..."
    play music 'audio/music/Intruder.mp3' fadein 1.0
    scene storybeat3_17 at slight_wobble with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.5
    robin "About a month ago, I heard a knock on my door really late at night."
    robin "I lived by myself in an apartment, so I thought it was weird."
    show black with dissolve
    robin "But I opened it anyways, and..."
    scene storybeat3_18 at slight_wobble with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.5
        ease 3.0 zoom 1.01
    robin "He was there..."
    robin "Somehow, one of the creeps online found out where I lived..."
    pro "What the fuck..."
    robin "I... I was so scared."
    robin "I froze and he..."
    show black with dissolve
    robin "He almost..."
    pro "Jesus fucking Christ."
    pro "Did you call the cops?"
    robin "No, I couldn't."
    robin "He threatened to tell everyone where I lived and..."
    robin "I didn't want to risk it."
    stop music fadeout 1.0
    scene storybeat3_15 with dissolve
    pro "Oh my god, Robin..."
    pro "That's horrible, I'm so sorry."
    show storybeat3_13
    play music highschool_dream_piano fadein 1.0
    robin "It's okay, I just..."
    robin "I had to get out of there."
    robin "That's why I came here."
    hide storybeat3_13
    show storybeat3_15
    robin "I figured it would be a smaller town, and nobody would bother me."
    pro "I'm so sorry you had to go through that, Robin."
    pro "No one should ever have to go through that."
    robin "It's fine, really."
    robin "It's kind of nice getting it off my chest..."
    robin "I just hate being..."
    robin "So weak."
    menu:
        "Hey, you aren't weak.":
            show storybeat3_13
            robin "I don't know..."
            robin "I'm just worried that the stalker will eventually find me again..."
            robin "And that if he does, I won't be able to get away."
            hide storybeat3_13
        "I'll protect you.":
            pro "Robin, I'll protect you."
            pro "If the stalker or anyone else comes after you, I'll be there."
            robin "I..."
            show storybeat3_14
            robin "That means a lot to me, thank you."
            play sound positive_event_01
            system "Robin {color=#918fff}trusts{/color} you a {color=#8AFF59}little bit{/color} more now."
            $ trust += 7
            hide storybeat3_14


    "I want to hug him."
    "I want to hold him and tell him that everything will be okay."
    robin "Um..."
    robin "I'm kind of tired, so if you want to go back that's fine."
    pro "Oh, right."
    pro "Yeah, we should definitely go back."
    robin "Okay, let's pack up and go."
    show storybeat3_14
    robin "Thanks for listening and letting me talk about this."
    scene black with dissolve
    "We pack up and head back to the car."
    robin "This was a good day, wasn't it?"
    pro "Definitely, one of the best days we've had."
    robin "Yeah, I'm glad I decided to come here."
    "I'm glad he came here."
    "We drive back, the radio playing softly in the background."
    "I'm still processing what Robin told me."
    "God, what a fucking asshole."
    "I can't believe someone would do that to him."
    "Robin is so sweet and innocent, it makes me sick to think that people would prey on him like that."
    "I need to protect him."
    scene livingroom_night with dissolve
    "After a short drive, we arrive home and head inside our apartment."
    show robin swimsuit with easeinbottom
    robin "Well, I'm going to take a shower and then head to bed."
    robin "Today was a lot of fun, thanks again for everything."
    pro "Of course, I'm glad we got to spend the day together."
    robin "Me too, goodnight."
    pro "Goodnight."
    hide robin with easeoutleft
    "I watch him walk into the bathroom and hear the shower turn on."
    scene black with dissolve
    "I enter my room and pass out immediately after I lay down on my bed."
    "Today was fun but exhausting."
    $ renpy.end_replay()
    $ key_task += 1
    $ robin_progression_level += 1
    play sound positive_event_01
    system "{color=#FF5454}Progression Level{/color} has increased"
    show prologue9 with dissolve
    pause 1.0
    hide prologue9 with dissolve
    jump day

label story_beat4:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name
    
    stop music fadeout 1.0
    pause 1.0
    scene mc_bedroom_night with dissolve
    play music thunderstorm fadein 1.0
    "Fuck, there's a really bad thunderstorm outside..."
    "I'm sitting at my desk, trying to focus on my work, but the lights keep flickering."
    pro "What if the power goes out...?"
    pro "Honestly I'm not even going to risk this..."
    "I turn off my computer and unplug it from the outlets to prevent a sudden power surge."
    pro "I guess if I can't do work, I could try chilling in the living room..."
    scene livingroom_night with dissolve
    "I leave my room and see Robin already sitting on the couch."
    show robin tank with easeinbottom
    robin "Hey, this storm is really starting to ramp up huh..."
    pro "Yeah, it's definitely pretty bad out there."
    pro "How are you holding up?"
    robin "I'm fine, just didn't want to be locked up in my room in case the power went out..."
    pro "Ah, I had the same idea."
    pro "It's not like we can get anything done anyway, right?"
    show robin tank smile
    robin "Well, at least it gives us a chance to hang out together."
    pro "Mind if I sit with you then?"
    robin "Not at all, go ahead."
    scene storybeat4_1 with dissolve
    "I plop down on the couch next to Robin and get comfortable."
    show storybeat4_2
    robin "So, do you think the power is going to go out?"
    hide storybeat4_2
    pro "Considering the way this storm is going, it's likely."
    show storybeat4_2
    robin "Hopefully not for long, though..."
    robin "Do you have any candles or flashlights?"
    hide storybeat4_2
    pro "Nope..."
    pro "But the apartment does have one or two backup lights that are hooked up to a generator."
    pro "Even if the power goes out, we should have some light until it comes back on."
    show storybeat4_2
    robin "That's good..."
    robin "You know, I've been thinking about something lately."
    hide storybeat4_2
    pro "Oh? What's that?"
    show storybeat4_2
    robin "Well, um... maybe this is a good time to ask you this since we're already talking."
    hide storybeat4_2
    pro "Uh huh, what are you referring to exactly?"
    show storybeat4_2
    robin "Remember how I told you about that stalker at my old place..."
    robin "You know, at the beach trip."
    hide storybeat4_2
    pro "Of course I remember. Have you seen him around here or something?"
    show storybeat4_2
    robin "No, but..."
    robin "The other night, I heard someone knock on our apartment door."
    hide storybeat4_2
    pro "What the fuck?"
    pro "Did you get a look at them?"
    show storybeat4_2
    robin "No, but I was really freaked out."
    robin "What if it's the same guy?"
    robin "What if he was able to find me and he's just-"
    hide storybeat4_2
    pro "Hey, it's okay."
    pro "Even if it's him, I'll be here to protect you."
    show storybeat4_2:
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 0.2 zoom 1.3 xalign 0.3
        ease 0.1 zoom 1.25
    robin "But what if he brings others with him?"
    show storybeat4_2:
        zoom 1.25 xalign 0.3 yalign 0.5
        ease 0.2 zoom 1.5 xalign 0.3
        ease 0.1 zoom 1.45
    robin "Or tries to force himself into our apartment?"
    hide storybeat4_2
    show storybeat4_1:
        zoom 1.45 xalign 0.3 yalign 0.5
        ease 2.0 zoom 1.0 xalign 0.5
    pro "Hey, slow down Robin..."
    pro "I promise that won't happen."
    pro "They don't know you live here..."
    pro "And I'm here too, I'll protect you."
    show storybeat4_3
    "He looks at me and smiles."
    robin "Okay..."
    play sound power_out
    scene black
    pause 2.0
    "Suddenly, the room goes pitch black."
    show black with hpunch:
        zoom 1.3
    "I feel Robin grab my chest and fall on top of me."
    robin "Oh my god, the power went out!"
    play sound heart_beat fadein 1.0 loop
    "He's shaking. I can feel his heart pounding against my chest."
    pro "It's okay, Robin. I'm right here."
    scene storybeat4_4 at slight_wobble with dissolve:
        subpixel True
        zoom 1.05 xalign 0.5 yalign 0.5
    "After a few moments, the backup generator kicks in and a dim light above the couch turns on."
    pro "R-robin..."
    "He's still gripping onto my shirt, his breathing heavy and panicked."
    robin "Sorry, I just..."
    robin "I don't like being in the dark."
    pro "Hey, it's okay. You're safe, okay?"
    pro "I won't let anything bad happen to you, I promise."
    "I can feel his body relaxing slowly as he gets used to the dim light."
    pro "It's okay, we just need to wait until the power comes back on."
    robin "S-sorry about falling on top of you like that..."
    pro "No worries..."
    show black with dissolve
    stop sound fadeout 1.0
    "He slowly gets off of me and sits up again."
    scene storybeat4_5 with dissolve:
        zoom 1.6 xalign 0.2 yalign 0.5
        ease 5.0 zoom 1.0 xalign 0.5
    "Robin looks so scared."
    "His face is pale and he's shaking a little bit."
    pro "Hey, it's okay."
    pro "I'm sure the power will be back on soon."
    pro "And remember, I'm right here with you."
    robin "It's just..."
    robin "The knock on the door the other night... it felt like I was alone with that stalker all over again."
    show storybeat4_6
    robin "It sounds dumb, but that's how I feel..."
    hide storybeat4_6
    pro "It's not dumb, Robin. You have every right to be scared."
    pro "That experience was really traumatic, and you're still processing it."
    pro "Just know that I'm here for you, okay?"
    robin "Right..."
    robin "What do you usually do when something scares you?"
    pro "Well, I guess I just try to distract myself."
    pro "Watch some TV or play a video game or something."
    robin "Those are things I can't really do right now though..."
    show storybeat4_6
    robin "Want to just talk instead? Maybe that will help me calm down a little."
    hide storybeat4_6
    pro "Sure, what do you want to talk about?"
    robin "Well, we could talk about anything I guess."
    pro "How about... our future plans?"
    robin "Our future plans?"
    pro "Yeah, like where we see ourselves in a year or two."
    pro "I can go first, if you want."
    robin "Okay..."
    pro "Well, as you know, I'm an indie game developer."
    pro "I'm hoping to have the first version of my project released by the end of this year."
    pro "If all goes well, I can hopefully afford to rent out a studio where I can hire a team to help me make my games!"
    show storybeat4_7
    robin "Wow, that's really ambitious!"
    pro "Yeah, but I've been working on this game for a long time so it's exciting to see it come to fruition."
    robin "That's so cool, I'm excited for you."
    pro "Thanks. So yeah, that's what I plan on doing."
    hide storybeat4_7
    show storybeat4_5
    robin "Alright, my turn."
    robin "Well, I'm not exactly sure how to say this but..."
    pro "It's okay, take your time."
    "I think Robin {color=#918fff}trusts{/color} me enough to confide in me."    
    robin "I want to find someone..."
    robin "Someone who will love me for me."
    pro "Robin..."
    robin "Maybe that's a little too far ahead for me to be thinking about, but..."
    robin "It's always been a dream of mine to find someone, find a partner."
    robin "Someone who really loves me and isn't just using me..."
    robin "Since I'm a streamer, I rarely leave the house..."
    robin "It's hard to meet people."
    robin "Being sexualized all the time online also hasn't been good for my self-worth issues..."
    menu:
        "You deserve so much better than that, Robin.":
            robin "It comes with the job, I guess."
            robin "But it's still hard to deal with."
            pro "People online are horny idiots, don't let them get to you."
            robin "I try not to, but it's hard."
            robin "I just want to find someone who sees me for me."

        "What else do they say?":
            robin "I don't know... they just make me feel like I'm not worth anything."
            robin "Like I'm just a piece of meat to them."
            pro "Wow, that's really fucked up."
            robin "Yeah..."

    robin "A career on the internet has always been my dream, but now that it's become a reality..."
    robin "I guess I'm just kind of lost."
    robin "I don't know what I want to do anymore."
    pro "Hey, if you ever want to talk about anything like this..."
    pro "I'm always here for you, okay?"
    robin "Th-thanks. It means a lot to me."
    pro "You don't need to have your entire future figured out you know..."
    pro "Sometimes things just happen unexpectedly."
    pro "Like us, we were complete strangers when you first moved in."
    pro "Now, you're one of the closest friends I have."
    robin "Yeah, that's true."
    show storybeat4_7
    robin "I'm glad we became friends."
    robin "You make me feel so... comfortable."
    robin "I don't know how you do it."
    pro "It's a gift."
    "We laugh together, and for a moment the fear of the dark subsides."
    hide storybeat4_7
    show storybeat4_6
    robin "Can I... ask you for something?"
    pro "Of course, what is it?"
    robin "If you wouldn't mind, can I sleep in your room tonight?"
    robin "If the power doesn't come back on, of course!"
    hide storybeat4_7
    show storybeat4_5
    "His face flushes with embarrassment. It's adorable."
    pro "Sure, you can sleep in my room with me."
    robin "Are you sure it isn't weird?"
    pro "Not at all!"
    pro "I just want you to feel safe."
    show storybeat4_7
    robin "Right... thank you. That means a lot to me."
    robin "You're the best."
    robin "Anyway, let's try and pass the time until the power comes back on!"
    scene black with dissolve
    "We the next few hours the night chatting and joking around."
    "I know he's still afraid, but I'm glad Robin feels comfortable enough to talk and laugh with me."
    pro "Hey, it's starting to get really late..."
    pro "I say we call it and head to bed, don't think the power is going to come back anytime soon."
    robin "Oh, okay..."
    robin "I guess I'm sleeping in your room tonight then, huh..."
    "He seems nervous."
    pro "If you want, I can sleep on the floor or something-"
    robin "If you don't mind... I'd actually like to sleep next to you."
    robin "Your presence is really reassuring..."
    "I'm blushing furiously."
    pro "Y-yeah, I can sleep next to you if you want."
    robin "Thank you..."
    robin "All right then, let's go to bed."
    pro "Yeah, let's go."
    "We enter my room and climb into my bed."
    scene storybeat4_8 at slight_wobble with dissolve:
        zoom 1.05 xalign 0.5 yalign 0.5
        subpixel True
    "We lay in my bed together, my heart racing faster than I've ever felt it."
    "Robin's ass is facing me, his body pressed up against mine."
    "Fuck... I really hope I can suppress my dirty thoughts."
    robin "This is nice..."
    pro "Y-yeah... I think so too."
    "I can slowly feel a boner start to form in my pants."
    "I need to calm the fuck down."
    "The feeling of his ass pressed up against my dick isn't helping either."
    robin "Your breathing is a little heavy, are you okay?"
    pro "O-oh, I'm fine!"
    pro "Just uh... a little nervous."
    robin "Nervous?"
    pro "Yeah, it's fine! Don't worry about it!"
    scene storybeat4_9 with dissolve
    "Robin shifts his body and faces me."
    "Holy shit, he's so close..."
    robin "Sorry for falling on top of you earlier..."
    robin "You probably think I'm a total mess, huh?"
    pro "I don't think you're a mess. You've been through a lot, you're allowed to be scared."
    show storybeat4_10
    "He looks into my eyes and smiles sweetly."
    robin "You mean a lot to me, you know that?"
    robin "You're really kind and understanding and..."
    robin "You make me feel safe."
    pro "Well, I'm happy to hear that."
    "I take a deep breath and try to relax."
    pro "I'll always be here for you, Robin. No matter what."
    robin "I know. It's just, after what happened at my old place..."
    robin "I really didn't want to let myself get attached to anyone."
    robin "But with you..."
    robin "I feel like I can trust you, and that means a lot to me."
    robin "Sorry if that's cringey or whatever."
    robin "I had to get it off my chest."
    pro "No worries. I'm glad you feel that way about me."
    pro "I'm really glad I met you too, Robin."
    "Robin smiles at me and turns back around."
    scene storybeat4_8 with dissolve
    "I watch him shift his ass against my dick again and hold back every urge in my body to move."
    "God, I need to stop thinking about it."
    pro "Goodnight Robin."
    robin "Goodnight."
    show black with dissolve
    stop music fadeout 1.0
    "I drift off to sleep with Robin's ass rubbing against my dick and a smile on my face."
    "Fuck, I think I'm in love."
    $ achievement.grant("storybeat4")
    $ renpy.end_replay()
    $ key_task += 1
    $ robin_progression_level += 1
    play sound positive_event_01
    system "{color=#FF5454}Progression Level{/color} has increased"
    show prologue9 with dissolve
    pause 1.0
    hide prologue9 with dissolve
    jump day

label story_beat5:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    stop music fadeout 1.0
    scene black with dissolve
    pause 1.0
    play sound positive_stinger
    show storybeat5_1 with dissolve
    pause 1.5
    hide storybeat5_1 with dissolve
    scene mc_bedroom_evening with dissolve
    pro "Wow... I got a lot done today huh."
    pro "Maybe I should reward myself with a fancy dinner tonight."
    pro "I wonder if Robin would be down to join me, could give me a nice excuse to hang out with him again."
    pro "Yeah, maybe I'll invite him."
    scene black with dissolve
    "I get up and head to Robin's room."
    pro "Hey Robin, I was wondering if-"
    play sound door_open
    scene white with dissolve
    pause 0.8
    show storybeat5_2 at slight_wobble with dissolve
    "I open the door without knocking and see Robin riding a dildo."
    pro "OH SHIT-"
    robin "!!!"
    show whiteflash zorder 50
    hide storybeat5_2
    show storybeat5_3 at slight_wobble
    "Robin looks at me and instantly cums all over himself, his body shivering from the shock of being caught."
    "Oh fuck, did I just..."
    pro "I-I'm so sorry!"
    pro "I should have knocked..."
    robin "Close the door...!"
    scene storybeat5_4 with hpunch:
        subpixel True
    $ achievement.grant("storybeat5_1")
    play sound door_slam
    "I slam the door back shut."
    play music sad_jingle_loop fadein 1.0
    pro "Fuck..."
    pro "What the hell am I supposed to do now?"
    pro "I'm such a fucking idiot..."
    pro "Shit. Shit. Shit."
    show storybeat5_5 with dissolve
    show robin neutral blush with easeinbottom
    "Robin emerges from his room after a few minutes, his face red with embarrassment."
    robin "..."
    pro "I'm... so fucking sorry."
    pro "I'm a genuine fucking idiot."
    robin "It's fine..."
    robin "Just..."
    robin "Can we forget that happened?"
    pro "Y-yeah, of course."
    pro "I feel awful for walking in on you like that, I really am so sorry."
    robin "..."
    pro "I'm... going to go back to my room now..."
    robin "..."
    scene black with dissolve
    "I slowly back away into my room."
    scene mc_bedroom_evening with dissolve
    pro "What the fuck have I done??"
    pro "Now he's going to think I'm a total pervert!"
    pro "Fuck! Fuck! Fuck!"
    pro "How could I have been so stupid..."
    pro "Roommate rule number one... always knock."
    "I throw myself onto my bed and groan with frustration."
    pro "Should have just ordered takeout and worked on my game!"
    stop music fadeout 1.0
    "As I'm wallowing in self-loathing, I hear a soft knock on my door."
    pro "..."
    pro "Robin?"
    pro "Are you..."
    robin "May I come in?"
    pro "Uh... yeah."
    show robin neutral with easeinright
    "He slowly opens the door and steps inside my room."
    robin "..."
    robin "See how it's done?"
    pro "Yeah... sorry again."
    pro "I really should have knocked."
    pro "And just so you know, I really didn't see much-"
    robin "It's fine..."
    pro "Please don't think I'm some kind of creep or anything."
    robin "I don't think you're a creep."
    robin "It was just bad timing, I should've locked my door anyway..."
    pro "Yeah... still though."
    pro "Is there anyway I can make it up to you?"
    robin "..."
    show robin open
    robin "Sit down."
    pro "Huh?"
    robin "Just sit in your chair, please."
    scene storybeat5_6 with dissolve
    "I take a seat in my chair."
    scene storybeat5_7 with dissolve
    "Robin sits down on my bed and faces me."
    robin "Can we talk..."
    pro "Oh... yeah for sure."
    pro "About what just happened?"
    robin "Well, not exactly."
    robin "More venting, than anything."
    pro "Sure, I don't mind that."
    "Seems like a weird time to vent, but I'm not going to push him away after I just invaded his space."
    play music sad fadein 2.0
    robin "I'm... gay."
    robin "You already know that, but I thought it was important to say out loud."
    robin "And I'm pretty sure you know that I was using a dildo on myself too."
    pro "Yeah..."
    pro "Look, you don't have to worry about me telling anyone or-"
    robin "It's not that..."
    robin "I'm not worried about you telling anyone."
    robin "You're the most trustworthy person I know, you wouldn't do that."
    pro "Oh... good."
    robin "But like, I think you also know how lonely it can be... being someone like me."
    robin "Before I moved here, I was always too scared to even make friends, let alone date."
    robin "I barely went outside, let alone had any real connections with anyone."
    robin "All my relationships were online..."
    robin "It was horrible..."
    pro "Robin..."
    robin "So I think it's important to me that I just... tell you everything."
    robin "Not in a 'here's all my trauma' kind of way, but in a way that says 'I trust you.'"
    robin "That's why I wanted to sleep in your room the other night."
    robin "I like being close to you. It makes me feel safe."
    robin "And I haven't felt safe in so long."
    robin "People take advantage of me..."
    robin "They think that because of my small body and feminine voice... I'm weak."
    robin "Mentally and physically... like I'm someone they can corrupt and take advantage of."
    robin "Someone who can easily be used for their own pleasure..."
    pro "Robin... that sounds really scary."
    robin "It is."
    robin "And I don't want to be afraid anymore. I'm tired of it."
    robin "I just want to be loved, you know? Just loved and cared for."
    robin "I've never even held someones hand... I've never tried getting close to anyone before."
    robin "It's not a fulfilling life... It's just loneliness. Emptiness."
    robin "I'm tired of it."
    pro "Robin..."
    pro "I understand. You deserve someone who will love you for you, not just for your body or your appearance."
    pro "Someone who will respect you and be patient with you as you navigate your sexuality and identity."
    pro "You deserve so much better than just being treated as a toy..."
    pro "You deserve someone who will adore you for the beautiful, kind person that you are."
    robin "Then why was I born this way..."
    robin "I'm unloveable..."
    robin "Atleast, in the way I want to be loved."
    robin "Nobody wants to date a broken person."
    robin "Nobody wants the person who can't even walk to the store by himself."
    robin "Or the person who needs constant reassurance."
    robin "Or whose identity is so fucked up that they don't even know who they are anymore."
    robin "My entire existence is just a fucking mess."
    robin "It's not fair. I didn't ask for this."
    pro "Robin I-"
    robin "I know, it's weird that this is all spilling out after you caught me masturbating..."
    robin "But since you've seen me at my most vulnerable, why not go all out huh..."
    robin "I masturbate every single day, sometimes multiple times a day."
    robin "It makes me feel like, for once, I have control over my own body and mind."
    robin "That's all I've ever wanted, you know? To just feel in control."
    robin "And yet, no matter how much I try to feel better or happier..."
    robin "I'm still... alone."
    "Robin takes a deep breath, seemingly holding back tears."
    robin "I'm sorry... I didn't mean to put all of this on you."
    pro "You don't have to apologize."
    pro "I'm always here for you. And I want you to know that."
    robin "I'm not some horny freak, you know?"
    robin "I'm just..."
    robin "I'm a mess..."
    robin "Even this little rant was a mess..."
    show storybeat5_8 with dissolve
    robin "But honestly, I was thinking of you [protagonist_name]."
    pro "W-what?"
    robin "I was... thinking about you when you walked in on me."
    robin "I have been thinking about you every time I touch myself for awhile now... ever since that beach trip."
    robin "Where you... you protected me."
    robin "You actually saw me as a person instead of a some corruptible toy. It made me feel something."
    robin "Something new."
    robin "Something that I didn't know I was capable of feeling."
    robin "And the more I thought about it, the more I couldn't get you out of my head."
    robin "You're sweet and caring and funny and..."
    robin "You actually make me feel warm inside. Not just physically, but emotionally."
    robin "And I don't know what to do with that feeling."
    pro "Robin... I didn't know you felt that way about me."
    pro "Why didn't you tell me?"
    robin "I didn't want to scare you off!"
    robin "We're roommates and I didn't want to ruin our friendship with my feelings."
    robin "But after you caught me masturbating, this all just spilled out..."
    hide storybeat5_8
    show storybeat5_9
    "Robin smiles at me and holds back tears, his entire face red with embarrassment."
    robin "I like you, okay?"
    robin  "I like you a lot. And it scares me because I've never felt this way about anyone before."
    pro "Robin, I-"
    robin "Don't respond just yet... I still have more to say."
    robin "But I need to be honest with you, otherwise I'll just keep holding it in and end up hating myself even more than I already do."
    robin "I've been trying to suppress it for so long... I just want to be myself again. The real me."
    robin "Not just some doll people can play with. Someone who is vibrant and full of life and wants to be loved too."
    robin "That's why I wanted to tell you everything. Because I feel like I can finally be honest with myself and with you."
    pro "You want to explore your identity and learn more about yourself, right?"
    robin "Yes! That's exactly it!"
    robin "I just want to be myself. Not what other people expect me to be."
    robin "And you... you make me feel like I can do that."
    robin "Like I'm not disgusting or weird or..."
    robin "Just... thank you. Thank you for listening to me."
    robin "Thank you for protecting me at the beach."
    robin "Thank you for being close to me when the power went out."
    robin "Thank you... for not pushing me away."
    robin "For not using me."
    robin "For making me feel like I have someone I can trust."
    hide storybeat5_9
    show storybeat5_8
    "He pauses and takes another deep breath."
    robin "..."
    robin "Sorry."
    robin "My emotions are gross and messy sometimes."
    robin "Anyway, what I'm saying is, if you don't like me back or if you don't want anything more than friendship, I understand."
    robin "But I need to be true to myself and my feelings, even if it's scary."
    pro "Robin..."
    pro "I... I like you too."
    show storybeat5_10
    robin "What..."
    robin "But you're not-"
    pro "Not gay?"
    pro "So, maybe I'm bisexual. I don't really know yet, but I know I like you."
    robin "B-but-"
    pro "But nothing."
    pro "You're so sweet, and funny, and kind... and beautiful too."
    pro "What's there not to like about you?"
    robin "I, uh... well-"
    pro "You're all of those things, and more."
    pro "And listen, maybe our feelings don't go anywhere."
    pro "But since you opened up to me, it's only fair that I open up to you."
    pro "You deserve honesty too, Robin. And I want to give you that."
    robin "But I'm a mess..."
    pro "Relationships are messy, life is messy."
    pro "But if you're willing to face that messiness with me, then we can figure it out together."
    robin "I..."
    robin "You..."
    "He looks dazed and confused, like he's still processing my words."
    scene mc_bedroom_evening with dissolve
    show robin neutral blush with easeinbottom
    "He gets up and slowly approaches me, his eyes searching mine for any signs of hesitation or fear."
    robin "Are you serious..."
    robin "This isn't a joke?"
    robin "You really..."
    robin "You really want me?"
    pro "Of course I do."
    pro "I'd be an idiot not to."
    stop music fadeout 2.0
    robin "Get on the bed..."
    pro "Wh-"
    show robin open blush at jumper
    robin "Just do it, dummy!"
    scene white with dissolve
    "Without protest, I get onto my bed and lay on my back, my body almost frozen in shock at Robin's sudden change in demeanor."
    "Robin crawls towards me on the end of the bed, his eyes still fixated on mine."
    pro "Robin... what are you..."
    "Before I can finish my sentence, Robin takes off my pants and throws my boxers away."
    robin "I've never sucked a dick before..."
    robin "But I've practiced on my toys..."
    pro "Robin..."
    play sound suck_low fadein 1.0 loop
    scene storybeat5_11 with dissolve:
        xalign 0.5 yalign 0.5
        ease 0.25 yalign 1.0 zoom 1.045
        ease 0.2 yalign 0.5 zoom 1.0
        repeat
    "He leans down and wraps his mouth around the tip of my cock, swirling his tongue around the head in a circular motion."
    pro "Holy fuck..."
    "Robin slowly begins to bob his head up and down, his mouth slowly inching closer to the base of my cock."
    "He is sucking me off with surprising skill, his lips and tongue creating a steady rhythm."
    pro "Oh... oh my god..."
    pro "Robin... that feels amazing..."
    "I've never experienced a blowjob like this before. It's so sensual, so... meaningful."
    pro "You're doing so good, Robin. Keep going."
    robin "Mmmmmm..."
    pro "Yeah, that's it..."
    "His technique is messy, but passionate."
    "He is moaning softly as he continues to bob his head up and down, his blue eyes still fixed on mine."
    robin "Mmph... mmmmph..."
    pro "Yes... just like that..."
    pro "You're such a good boy, Robin."
    "I moan loudly, my mind reeling from the sensation of Robin's warm mouth."
    pro "You're so good... such a good boy."
    robin "Mmmm..."
    pro "Take it... take all of me into your mouth..."
    pro "Your lips feel so fucking good on my cock..."
    "Robin nods his head and picks up the pace, his saliva dripping down onto my balls as he gags slightly."
    pro "Ohh... ohhhh shit..."
    pro "I'm not going to last long if you keep this up..."
    robin "Mmmm..."
    play sound slight_exertion_slow fadein 0.5 loop
    scene storybeat5_12 at slight_wobble with dissolve
    "He takes my cock out of his mouth and looks up at me, his eyes watery with tears."
    pro "What's wrong?"
    robin "Just... I can't wait any longer."
    robin "I need to feel you inside me... please."
    pro "Are you sure you're ready for this Robin..."
    pro "It's your first time and-"
    robin "I am sure, I need you."
    robin "I trust you."
    robin "I need someone who will take care of me, and I feel like that person is you."
    pro "Okay... okay Robin."
    robin "Let me ride you."
    robin "Let me prove to you how good I can be."
    stop sound fadeout 0.5
    scene white with dissolve
    "I nod and shift my body until I'm lying flat on my back, my eyes locked on Robin as he slowly begins to undress himself."
    pro "You're so beautiful, Robin..."
    "He smiles and blushes slightly, his cheeks turning a rosy pink."
    robin "Here goes nothing..."
    "He carefully inserts the tip of my cock into his ass, his eyes closed tightly in anticipation."
    play sound storybeat5_13 loop
    scene storybeat5_13 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.7 yalign 1.0 zoom 1.07
        ease 0.6 yalign 0.5 zoom 1.0
        repeat
    "He carefully lowers himself down onto my cock, his ass stretching out as I fill him completely."
    pro "Take it slow, Robin. Don't rush."
    robin "I'm trying. I just need to get used to it."
    pro "How does it feel?"
    robin "It feels..."
    robin "It feels weird... but good."
    pro "You're doing so good, Robin. You're taking me so well."
    robin "Y-yeah?"
    robin "You really think so?"
    pro "I do."
    pro "I think you're perfect, Robin. Absolutely perfect."
    "He starts to move his ass up and down, grinding against me as I'm fully inside of him."
    pro "Fuck... oh fuck..."
    "I can feel his tightness, his warmth, his love. It's overwhelming."
    robin "It feels... good..."
    robin "Your dick... its so..."
    robin "I can feel it all..."
    robin "I can feel my hole stretching... I can feel your cock moving inside me."
    pro "You're doing great Robin..."
    pro "Good boy..."
    robin "Really... you think I'm a good boy?"
    pro "Such a good boy..."
    pro "If you feel comfortable... maybe you can start speeding up."
    robin "Mhm..."
    robin "I'll try..."
    play sound storybeat5_14 loop
    scene storybeat5_14 with vpunch:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.3 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.0
        repeat
    "Robin begins to completely ride me, bouncing on my cock as he moans in pleasure."
    robin "Fuck..."
    robin "Oh my god..."
    robin "Real dick feels nothing like my toys..."
    robin "It's like I can feel every inch of you... all of it."
    "He starts to pick up the pace, thrusting his ass up and down and whimpering softly."
    pro "Don't hold back... you're doing so good Robin..."
    robin "Mm... fuck..."
    robin "I've always wanted to know what this was like... to be filled up with something real."
    robin "The feel of your warm... thick... juicy cock... it's mind-blowing."
    "I look up at him, mesmerized by how he moves on my cock and how wet his own cock is leaking pre-cum."
    pro "Yes, that's right, Robin... such a good boy taking care of my cock so well."
    robin "Y-Yeah?"
    robin "Oh... o-oh shit..."
    robin "Y-You're cock is rubbing up against s-something..."
    pro "That's your prostate Robin."
    robin "O-Oh my god, that's... that's why it feels so... so... ah!"
    pro "Ride it, Robin. Use it."
    pro "Bounce that ass on my dick."
    robin "R-Right! Ohmygod... ohmygod...!"
    robin "It's so good...! Fuck..."
    robin "Fuckfuckfuckfuck..."
    play sound storybeat5_14_2 loop
    scene storybeat5_14 at slight_wobble:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.0
        repeat
    "He starts to ride me at full speed, moaning louder and louder as his hole tightens around my cock."
    robin "Fuck my tight little hole... my warm, wet, sloppy asshole..."
    pro "Yesss Robin... don't stop, keep riding me... don't you dare slow down."
    robin "God, yes..."
    robin "You feel so good...!"
    robin "Your big fucking cock is stretching me so wide...!"
    robin "Keep fucking me, keep fucking me...!"
    robin "Use me, use my ass to your liking!"
    pro "I'm close, Robin... I'm going to blow a load into your tight little ass..."
    robin "Don't! Hold back! Please, don't!"
    robin "Please please... just a little more... I'm so close!"
    "His hips are moving faster and faster as he looks down at me desperately."
    robin "Yesssss!"
    menu:
        "Cum":
            pro "I'm cumming...!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    scene white with dissolve
    pause 1.0
    scene storybeat5_15 at slight_wobble with dissolve
    play sound storybeat5_15_climax
    "I shoot my load into his ass, my cum filling him up as he whimpers loudly."
    "Simultaneously, Robin's cock erupts with a warm, sticky load of cum."
    robin "I'm cumming, I'm cumming...!"
    robin "I'm cumming so fucking hard...!"
    robin "Fuck!!"
    robin "Your cum... it's so warm and thick!"
    robin "I can feel it filling me up...!"
    "I stay still as I let him ride out his orgasm."
    scene white with dissolve
    "After a few moments of silence, he collapses on the bed."
    play sound slight_exertion_slow fadein 0.5 loop
    scene storybeat5_16 at slight_wobble with dissolve:
        subpixel True
        zoom 1.02 xalign 0.5 yalign 0.5
        pause 2.0
        ease 3.0 zoom 1.3 xalign 0.3 yalign 0.5
        pause 2.0
        ease 3.0 xalign 0.5
        pause 1.0
        ease 5.0 zoom 1.02 xalign 0.5 yalign 0.5
        pause 1.0
        repeat
    robin "I... holy fuck..."
    robin "That was..."
    robin "That was... perfect."
    robin "I've never felt like that before."
    pro "Me too... that was intense."
    pro "You were so good, Robin. So good."
    robin "I'll get better."
    robin "I want to get better. For you."
    pro "You already are perfect."
    robin "Really?"
    pro "Yes, Robin. You really are."
    robin "You always know exactly what to say to me..."
    pro "In a good way, I hope?"
    robin "Hehe, just shut up and fuck me again already!"
    pro "W-what!"
    stop sound fadeout 0.5
    scene white with dissolve
    "He gets up and lowers himself onto my cock again, this time facing himself towards me and riding me cowgirl style."
    play sound storybeat5_17 loop
    scene storybeat5_17 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.0
        repeat
    robin "Come on, dummy... we've got all night..."
    robin "I've wanted this for so long. Don't deny me anymore!"
    "His movements are rough, but he slowly begins to ease back into the rhythm from before."
    pro "F-fuck...!"
    pro "Your ass feels so fucking good!"
    pro "Good boy..."
    robin "Hehe, I love it when you say that..."
    robin "Fuck... your cock is so fucking good!"
    robin "I... I don't know how I was living without this!"
    robin "I need this every night from now on... every single night!"
    pro "Fuck... I can feel myself getting addicted to your body, Robin..."
    "His ass bounces up and down, the rhythm starting to match mine perfectly."
    "We are in sync, both of us filled with lust and desire for each other."
    pro "Good boy... good fucking boy...!"
    robin "Ahn... mphm... mmm..."
    "It doesn't take me long to feel myself reaching the edge again."
    "I can feel his pace begin to quicken, his hole clenching on my cock."
    pro "S-So close..."
    robin "I want it! Please let me feel you cum inside me again!"
    robin "Cum in my asshole!"
    robin "Breed my femboy bussy!"
    pro "Oh, you want me to breed you?"
    robin "Yes, YES!"
    robin "BREED MY DELICATE FEMBOY ASSHOLE!"
    stop sound fadeout 0.5
    scene white with dissolve
    "Hearing that flips a switch in me and I push Robin off of me."
    robin "W-what?"
    "I lay him down in a mating press position, his legs pushed up to his shoulders and his hole spread wide open."
    robin "[protagonist_name] wait s-slow down-"
    play sound storybeat5_18 fadein 0.5 loop
    scene storybeat5_18 with dissolve:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.0
        repeat      
    "Without responding, I push my cock back into him, pounding away at his tight ass as he whimpers with delight."
    robin "FUCKKK!"
    "I can feel the tip of my dick reaching his prostate again as I relentlessly fuck him with unbridled lust and desire."
    pro "Is that good Robin... you want me to breed you like this? You want to be my femboy cumslut?"
    robin "Y-Yes! I'm yours, your cumslut! Do it!"
    robin "Breed me breed me!"
    "I can feel every single inch of his body as it quivers underneath me, his moans growing louder and louder."
    "He is struggling, his voice reaching new high pitches as I continue to pound into him at full speed."
    pro "So tight..."
    pro "You're taking me so well Robin, I knew you could do it."
    robin "Every time you slam your cock into me..."
    robin "I can feel the walls of my ass stretching to take you in...!"
    pro "You want me to go faster, Robin?"
    robin "Ye-"
    scene storybeat5_18:
        xalign 0.5 yalign 0.5
        zoom 1.0
        ease 0.17 yalign 1.0 zoom 1.07
        ease 0.12 yalign 0.5 zoom 1.0
        repeat
    "Robin can barely finish his sentence before I start pounding even faster, the sound of slapping skin echoing through the room."
    "His eyes are beginning to roll into the back of his head as he is overcome with the pleasure that I'm providing."
    robin "A-Ahn! Ahn!"
    robin "Y-yes, yes, yes, yes, YES!"
    "We are moving so fast that the entire bed starts to rock back and forth."
    robin "D-Don't stop...! Please...! I'm s-so close...!"
    robin "PLEASE, P-PLEAAAASE!"
    "I can feel myself reaching my limit, but I continue to pound him without slowing down at all."
    "He moans with every thrust, his hole tightening as he is about to cum."
    menu:
        "Cum":
            robin "I'm... I'm going to..."
    robin "Cumming, I'm cu~umming!~~!"
    robin "AAAAAAAAH~!"
    pro "ME TOO, FUCK!"
    pro "F-F-FUCK, FUCK! ROBIN-!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    scene white with dissolve
    pause 1.0
    stop sound fadeout 0.5
    play sound storybeat5_15_climax fadein 0.5
    scene storybeat5_19 at slight_wobble with dissolve
    "With a powerful thrust, I cum into his ass, filling him with my seed."
    "Robin cums all over his own chest, his cock pumping load after load of warm, sticky cum onto his pale body."
    robin "AHH~"
    robin "SO... WARM...!"
    robin "I can feel you filling me up...!"
    pro "That was fucking amazing..."
    scene white with dissolve
    "I slowly pull my cock out of his ass and watch as Robin lays there, cum overflowing from his asshole."
    play sound slight_exertion_slow fadein 0.5 loop
    scene storybeat5_20 at slight_wobble with dissolve:
        subpixel True
        zoom 1.02 xalign 0.5 yalign 0.5
        pause 2.0
        ease 3.0 zoom 1.3 xalign 0.3 yalign 0.5
        pause 2.0
        ease 3.0 xalign 0.5
        pause 1.0
        ease 5.0 zoom 1.02 xalign 0.5 yalign 0.5
        pause 1.0
        repeat
    robin "Fuck... that was so intense..."
    pro "Ah... yes, that was..."
    "After a few moments, I gain some clarity on what just happened."
    pro "Are you okay Robin?"
    pro "I wasn't too rough, right?"
    robin "N-no, you were perfect. Perfect for me."
    pro "Are you sure?"
    robin "Positive."
    robin "That was..."
    robin "Incredible..."
    stop sound fadeout 0.5
    scene white with dissolve
    "We spend the rest of the night exploring each other's bodies."
    "Every single inch of Robin's soft skin, every curve and crevice, I feel myself wanting more and more."
    "After hours of cuddling, fucking, and talking, Robin finally falls asleep in my arms."
    scene black with dissolve    
    pro "Robin..."
    pro "I think I'm in love with you."
    "..."
    scene storybeat5_21 with dissolve
    play music 'audio/music/highschool_dream_piano.mp3'
    "I wake up the next morning to Robin staring at me."
    pro "Oh, hey..."
    robin "Hey..."
    robin "You slept like a baby, hehe."
    pro "Ah, sorry..."
    pro "Did I snore or something?"
    robin "Not at all."
    pro "Ah, good haha."
    robin "Hey, [protagonist_name]?"
    pro "Hm?"
    robin "Sorry if I came onto you a little too strong yesterday..."
    robin "I really appreciate you being so patient and understanding with me."
    robin "You made me feel comfortable, safe, and... loved."
    robin "And... I like what we have."
    robin "I'm excited to explore it further."
    pro "Robin..."
    pro "You have nothing to apologize for. Last night was amazing and I would do it again in a heartbeat."
    pro "You're a beautiful person and I want to be with you."
    robin "But I come with a lot of baggage..."
    robin "I worry that I'll be too clingy or annoying, or not be able to keep up with you."
    pro "You're worth it, Robin."
    pro "Every ounce of you is worth it."
    scene storybeat5_22 with dissolve
    robin "You're gonna make me cry, dammit..."
    robin "Stop being so sweet all the time."
    scene white with dissolve
    "He digs his face into my chest."
    "We lay in my bed for another hour, enjoying each other's presence."
    $ achievement.grant("storybeat5_2")
    scene black with dissolve
    $ renpy.end_replay()
    $ key_task += 1
    $ robin_progression_level += 1
    play sound positive_event_01
    system "{color=#FF5454}Progression Level{/color} has increased"
    system "{color=#FF5454}Max Progression Level{/color} reached."
    system "You can now do {color=#FF5454}everything{/color} with Robin."
    show prologue9 with dissolve
    pause 1.0
    hide prologue9 with dissolve
    jump day

label story_beat6:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    stop music fadeout 1.0
    scene black with dissolve
    "For the next few weeks, Robin and I were inseparable."
    "Everywhere we could fuck, we fucked."
    "We explored our sexuality together, pushing each other's boundaries and trying new things."
    "I've never felt so connected with someone before in my life."
    "Robin was everything I've ever wanted in a partner."
    "But, we hadn't defined our relationship yet."
    "I don't know what we are or what we could be."
    "..."
    pause 1.0
    play sound positive_stinger
    show storybeat5_1 with dissolve
    pause 1.5
    hide storybeat5_1 with dissolve
    play music starry_night_nopercussion fadein 1.0
    scene mc_bedroom_night with dissolve
    "Knock-Knock"
    pro "Come in!"
    show robin smile with easeinright
    robin "Hey [protagonist_name]."
    robin "I missed you, hehe."
    pro "Hey Robin, you finish up your stream early?"
    pro "It's only 7."
    robin "No actually, I didn't stream tonight."
    robin "I didn't feel like it, so I made a post saying that I had plans tonight and wouldn't be able to stream!"
    pro "And I assume I'm those plans you mentioned?"
    robin "Of course!"
    robin "Time hanging out with you is time well spent!"
    "God, he's adorable."
    pro "What were you wanting to do?"
    show robin smile blush
    robin "Um..."
    pro "I guess I'm guessing you want to..."
    pro "Play around a little bit?"
    robin "Yeah..."
    show robin open blush
    robin "Can we talk for a minute first though?"
    pro "Oh yeah, what's up?"
    show robin open
    robin "Well... uh..."
    robin "I don't really know how to word this but, what exactly is our relationship?"
    robin "Are we dating, are we boyfriends... friends with benefits?"
    pro "I... don't really know."
    pro "What would you prefer?"
    pro "If you're not ready, we don't have to define the relationship."
    show robin neutral
    robin "No no, I want to."
    robin "It's just, I have a hard time with this stuff, haha."
    pro "Don't worry. I'll help you figure out what you want."
    show robin smile
    robin "Thanks..."
    show robin open
    robin "I don't really know what I'm looking for..."
    robin "All I know is that I like you a lot. You make me feel good and safe."
    show robin smile blush
    robin "And well, we have a LOT of sex, so..."
    show robin neutral blush
    pro "Haha yeah."
    pro "What do you think a romantic relationship with me would look like?"
    show robin open blush
    robin "Um... I guess it would involve a lot of kissing and holding hands... stuff like that."
    pro "That's cute."
    show robin open
    robin "I'd want us to be exclusive too..."
    pro "That makes sense."
    pro "What about a friendship with me? What would that look like to you?"
    robin "A friendship? Well..."
    robin "We would just hang out, I guess... and play video games, and stuff..."
    pro "That's pretty standard."
    pro "But we do all that already, right?"
    robin "Yeah..."
    pro "What do you think about having sex while we figure things out?"
    pro "Does that scare you or bother you?"
    show robin smile
    robin "Not at all... I really like it, actually."
    robin "The way you make love to me makes me feel wanted..."
    show robin smile blush
    robin "And honestly, it makes me feel like... I deserve it, like I deserve to be loved and cherished like that."
    robin "It's new to me, but I like it y'know?"
    pro "I do know what you mean."
    show robin open blush
    robin "I really want to keep having sex with you, that's for sure..."
    show robin smile blush
    robin "You make me feel things I didn't even know were possible."
    robin "It's hard to put it into words..."
    pro "So then why is it hard for you to put a label on it?"
    pro "Why put a label on it at all?"
    show robin open
    robin "I don't know..."
    robin "I want a label, but if we have something tangible then it means it can also end."
    pro "What do you mean?"
    pro "You're afraid if we have a title it can all end, but it can also end without one too, you know?"
    robin "Yes... I'm just..."
    show robin neutral
    robin "I guess it just doesn't seem real to me that I can have a happy ending."
    pro "That doesn't sound like someone who wants to take it slow to me."
    robin "It's not about taking it slow or anything..."
    robin "It's about..."
    robin "It's about not wanting to lose something that's good."
    robin "Something that makes me happy..."
    pro "I get that."
    robin "I don't want to lose you."
    robin "If we had sex without defining anything... that could be scary, but at least there's a safety net, you know?"
    robin "There's no risk of getting my heart broken, just... getting my feelings hurt."
    show robin open
    robin "But that's still scary, even if it's less than the other."
    robin "I've never had a boyfriend... or even a romantic partner."
    pro "I understand where you're coming from. Really, I do."
    pro "It sounds like you're really torn between the two."
    pro "Like, you're trying to weigh the pros and cons and decide what would be the least risky."
    show robin neutral
    robin "I don't want to mess up."
    robin "Like, maybe we shouldn't even have sex anymore until we figure this out..."
    robin "That might be the best course of action..."
    robin "Then, maybe we can get to know each other better and-"
    pro "Hey, it's okay."
    pro "You're being really sweet and trying to protect both of us from getting hurt."
    pro "That's something I really appreciate and love about you."
    pro "But, I also think you're putting too much pressure on yourself to make a decision."
    robin "How so?"
    pro "I mean... you're already feeling anxious and stressed out about this, aren't you?"
    pro "And that's not good. That's going to lead to an unhappy decision, regardless of which path you choose."
    robin "But what else can I do..."
    pro "Well, I think it's important for you to take the time to think things through."
    pro "Take the time to figure out what's best for you."
    pro "And... I want to help you with that, too."
    show robin open
    robin "You do?"
    pro "Of course..."
    pro "Let me take care of you Robin."
    pro "Let me love you and show you how wonderful it can be."
    robin "B-but how?"
    show robin neutral
    pro "You said you didn't want to have any more sex until we figured things out, right?"
    pro "That means you've already chosen your answer, haven't you?"
    pro "You've just chosen the harder option to avoid taking a leap of faith."
    pro "But you need to understand that there are no right answers, only the answers that are right for us."
    pro "I'm not trying to pressure you into a relationship, but I think it would be good for both of us to give it a try."
    pro "We can go as slow or as fast as you want, I'm not in a rush either."
    pro "But if you want to take a risk, and you want to try for a happy ending, then I think it's worth taking a leap of faith."
    pro "I'll catch you. I'll be there for you."
    robin "..."
    robin "Okay..."
    pro "Okay?"
    pro "What's okay?"
    show robin smile
    robin "Let's do it..."
    robin "I'm willing to try."
    robin "You're right. There's no use in worrying about it."
    robin "I just have to have a little courage."
    robin "If we're meant to be, we're meant to be, and if we're not then we can move on without hurting each other."
    pro "I'm so proud of you, Robin."
    pro "This is a big step for you, and I'm glad that we can do this together."
    robin "Yeah, it's kind of scary, but I'm excited."
    robin "I've never been this close with someone before, it feels nice."
    "I still feel like he's unsure..."
    "Maybe he doesn't know how devoted I am to him... how much I want this to work."
    "Maybe I should just..."
    stop music fadeout 1.0
    pro "Hey, Robin?"
    show robin open
    robin "Yeah?"
    pro "I..."
    pro "I love-"
    play sound door_knock
    scene black with dissolve
    "Before the words can leave my mouth, I hear a loud pounding on the front door."
    robin "EEH!"
    pro "Who is that..."
    scene storybeat6_1 with dissolve
    "I go to the front door and check through the peephole."
    pro "Hm, there's nobody there..."
    robin "W-what..."
    pro "Weird..."
    play music scary fadein 1.0
    scene storybeat6_2 with dissolve
    "I open the door and look around, but there is nobody there."
    robin "Whats that..."
    "I look down and see a note."
    pro "What the fuck..."
    scene storybeat6_3 with dissolve
    "I bend down and pick it up."
    pro "This is..."
    pro "A note addressed to Robin..."
    show storybeat6_4 with easeinbottom:
        yalign 0.3 xalign 0.5
    "I open up the letter and begin to read it to Robin."
    show storybeat6_5 with dissolve:
        yalign 0.3 xalign 0.5
    pro "'Dear my sweet Robin...'"
    show storybeat6_6 with dissolve:
        yalign 0.3 xalign 0.5
    pro "'I'm sorry you felt frightened by me the last time we met...'"
    show storybeat6_7 with dissolve:
        yalign 0.3 xalign 0.5
    pro "'But you did not have to move so far from me.'"
    robin "What the fuck."
    robin "This is from my stalker..."
    "I read the note some more..."
    show storybeat6_8 with dissolve:
        yalign 0.3 xalign 0.5
    pro "'I miss you. I can't wait to see you in person again."
    show storybeat6_9 with dissolve:
        yalign 0.3 xalign 0.5
    pro "'See you soon, my love.'"
    pro "..."
    scene storybeat6_10 at slight_wobble with dissolve:
        zoom 1.05 xalign 0.5 yalign 0.5
    pro "Robin... are you alright?"
    "His eyes have gone wide, and tears are welling up in them."
    pro "Robin, it's alright. We can figure this out. He can't get in here. You're safe."
    robin "Y-Yeah, I..."
    robin "I don't feel so safe..."
    pro "Robin..."
    pro "Listen to me."
    pro "We're going to be okay-"
    robin "No... no we aren't."
    robin "Fuck fuck fuck..."
    robin "I can't believe he found me."
    robin "What if he breaks in..."
    pro "Robin..."
    pro "Robin please calm down."
    pro "Listen to me..."
    pro "I know it's scary, and it feels like your whole world is crashing down around you."
    pro "But I want you to take a deep breath, alright?"
    pro "Take a deep breath..."
    scene storybeat6_11 at slight_wobble with dissolve:
        zoom 1.05 xalign 0.5 yalign 0.5
    "Robin runs off into his room."
    pro "Robin!"
    scene robin_room_outside_night at slight_wobble with dissolve:
        zoom 1.05 xalign 0.5 yalign 0.5
    "Robin slams the door shut."
    "Fuck, fuck..."
    scene black with dissolve
    "I enter the room and see Robin in the corner of his room."
    scene storybeat6_12 with dissolve
    show storybeat6_13 at slight_wobble with dissolve:
        subpixel True
        yoffset 5
        linear 0.5 xoffset -5
        linear 0.5 xoffset 5
        repeat
    pro "Robin..."
    robin "I knew it... I knew he would find me..."
    robin "I knew this wouldn't last forever..."
    robin "Shit... what do I do."
    robin "What do I do, [protagonist_name]?"
    "His eyes are wide and full of terror. He is absolutely terrified."
    pro "We can't panic."
    pro "It won't help us to panic. We have to be smart and rational. We have to figure this out together."
    robin "He's out there right now."
    robin "I'm not safe anymore. He knows I live here."
    robin "I... I'm..."
    robin "What do I do, I don't know what to do..."
    "He's hyperventilating and crying now, tears streaming down his face."
    robin "This is it..."
    robin "This is my nightmare come to life."
    pro "No, no... It's okay Robin... You're okay."
    pro "Everything will be okay."
    pro "You just need to calm down, and we can figure this out together, okay?"
    pro "I'm not going to let anything happen to you, Robin. I'll make sure of it, no matter what. I'll protect you."
    robin "I... I'm not safe. I need to get out of here."
    robin "I need to leave."
    robin "I need to go somewhere else where nobody knows where I am. I can't stay here."
    robin "What if he breaks in?"
    robin "What if he tries to do something to me while I'm asleep?"
    "Fuck, he's spiraling again."
    robin "No, no... I have to leave now, I can't be here any longer..."
    pro "Robin, no... listen to me."
    pro "You're panicking."
    pro "You can't let fear dictate what you do, that's what will get you hurt."
    robin "But..."
    robin "I don't want to be hurt. I'm scared. I'm so scared..."
    pro "Do you trust me, Robin?"
    robin "W-what?"
    pro "Do you trust me? Can you trust me with this?"
    robin "I trust you, but I'm not sure I trust myself..."
    robin "I can't think clearly... I don't want to make the wrong decision, but I don't know what to do..."
    pro "Then follow my lead. Do what I do, and you'll be alright."
    robin "But I don't want you to get hurt... or worse..."
    robin "I'm scared."
    pro "We're not going to get hurt. I promise."
    robin "You can't guarantee that... no one can."
    robin "I need to go somewhere he won't find me, and then maybe we'll be safe."
    "I have to make a decision, I have to say something."
    "Until I make a choice for Robin, he'll continue to spiral."
    $ renpy.end_replay()

    screen final_choice:
        modal True

        add "images/overlay/choice_overlay.png"

        text "{color=#FF002A}Important Decision{/color}" xalign 0.5 yalign 0.1:
            size 95
            font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0, 0.5)
            imagebutton:
                idle "images/overlay/ending1_idle.png"
                hover "images/overlay/ending1_hover.png"
                at decision_hover
                action [Hide("final_choice"), Jump("ending1")]
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Confront the Stalker{/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'

        vbox:
            align (0.5, 0.5)
            imagebutton:
                idle "images/overlay/ending2_idle.png"
                hover "images/overlay/ending2_hover.png"
                at decision_hover                
                action [Hide("final_choice"), Jump("ending2")]
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Run Away{/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'      

        vbox:
            align (1.0, 0.5)
            imagebutton:
                idle "images/overlay/ending3_idle.png"
                hover "images/overlay/ending3_hover.png"
                at decision_hover                
                action [Hide("final_choice"), Jump("ending3")]
                xalign 0.1
                yalign 0.4

            text "{color=#ffffff}Do Nothing{/color}" xalign 0.5 yalign 0.99:
                size 30
                font 'fonts/FredokaOne-Regular.ttf'

    show screen final_choice with dissolve
    "What should I do?"



label ending1:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    pro "Robin, listen to me."
    pro "I'll confront him, if he even steps a foot near you I'll kick his fucking ass."
    pro "I'm done letting this stupid stalker psychologically torture you like this."
    pro "Let's take this fucker down."
    pro "If anything, this could be an opportunity."
    pro "We could set a trap, bait him into making the first move, and get the police involved."
    robin "What..."
    pro "Don't you want him to face justice? Don't you want him to rot away in a cell for being such a scumbag?"
    robin "I... I want to forget he ever existed and hope I never see his face again."
    pro "I know you do, but if you just run away from it..."
    pro "It will always be looming over your head. And it will always have its hooks in you, tugging at you, tormenting you."
    robin "But... I'm so afraid. I can barely even imagine facing him alone."
    pro "You're not alone."
    pro "I'm here, always."
    pro "I'm here to support you."
    pro "I'm here to take care of you."
    robin "..."
    pro "We need to act fast, Robin."
    robin "I don't know... I just don't know. What if I regret it?"
    pro "Do you trust me?"
    robin "Yes, but I'm worried you'll do something stupid or reckless or—"
    pro "Robin."
    pro "We're partners. You and me. Partners. And we're stronger together than apart."
    robin "..."
    stop music fadeout 1.0
    scene robin_room2 with dissolve
    show robin neutral with dissolve
    "Robin gets off the floor."
    robin "Alright, but if I die, I'm gonna haunt your ass as a ghost for the rest of eternity."
    pro "Deal. Let's do this."
    show robin smile
    "Robin has a smile on his face again."
    show robin open
    robin "So, what's the plan?"
    show robin neutral
    pro "This creep clearly knows you're with someone."
    pro "He's just waiting for an opportunity where you're alone before striking, that's when he has power."
    pro "Given that he was able to disappear after leaving the note, that means he is still somewhere near the building."
    pro "He may even be inside our apartment building, even now."
    robin "..."
    pro "Hey, don't worry. He won't do anything until he knows you're alone and defenseless."
    pro "So here's my plan."
    pro "Tonight, when it gets late, turn on your stream and pretend that I'm out of the house."
    pro "If he's watching, this will be his chance to strike."
    pro "At least he'll think so."
    pro "I'll hide somewhere and wait for him to appear."
    pro "I'll also call the cops and have them on stand-by."
    robin "That sounds so dangerous..."
    robin "What if he hurts you?"
    pro "Trust me, I may look a bit scrawny but I can take care of myself."
    robin "I hope so..."
    pro "Once he shows up, I'll confront him and subdue him."
    pro "And the cops can swoop in to finish the job."
    robin "This feels like a weird dream, I can't believe this is happening..."
    pro "It's the only way. Otherwise, he'll never leave you alone."
    robin "But what if he-"
    pro "Robin."
    pro "Do you trust me?"
    robin "..."
    robin "Yes, I do."
    pro "I promise, it will be over after this."
    pro "I... I love you Robin."
    robin "...!"
    robin "L... love?"
    robin "You... you love me?"
    pro "Yes, I love you."
    pro "You're the most amazing person I've ever met. I would do anything to protect you, Robin."
    robin "I... I..."
    scene storybeat6_14 with dissolve
    "I can see the fear in his eyes slowly turning into determination."
    robin "I trust you, but I'm also scared..."
    robin "Above all else, I want this to end."
    robin "I'll do it. I'll help you catch him. I'll do anything for you, because I..."
    robin "Because I love you too."
    pro "I'll protect you, Robin."
    pro "No one is going to hurt you ever again."
    robin "I believe you. I'm ready to face my fears."
    scene black with dissolve
    "..."
    robin "Hey chat!"
    robin "What games should we play today, hm..."
    robin "My roommate isn't home, so I can be as loud as I want."
    robin "Maybe let's play a horror game!"
    play music scary fadein 1.0
    scene storybeat6_15 with dissolve
    "Robin starts his stream, acting as though nothing is wrong and I'm not in the house."
    "I hide in the bathroom. It's right beside Robin's room, so I can quickly make a move if anything were to happen."
    "I keep my phone on, ready to call the police."
    scene black with dissolve
    "..."
    "..."
    "..."
    scene storybeat6_15 with dissolve
    "Two hours go by with nothing."
    "Maybe the stalker didn't bite, or maybe he just isn't watching at the moment."
    "Or..."
    "Or maybe this is a stupid plan."
    "But it's too late now. We're in too deep. We have to follow through."
    stop music fadeout 1.0
    robin "Well guys, I'm getting a bit tired. I think I'm going to call it a night."
    "This is our last chance."
    "If the stalker is going to strike, he'll have to do it now."
    "I hear Robin turn off his computer, looks like the stream is wrapped up."
    "..."
    play sound door_knock
    "I hear a thud, and then a loud knock on the door."
    "This fucker is here."
    "He's here."
    "He waited until Robin was off stream."
    robin "..."
    "I hear Robin get up and walk towards the door. He's following the plan."
    play sound door_open
    "The door slowly creaks open."
    scene black with dissolve
    "I slightly open the bathroom door and peek through."
    play sound heart_beat loop
    scene storybeat6_16 at slight_wobble with dissolve:
        zoom 1.03 xalign 0.5 yalign 0.5
    stalker "Hello, my dear Robin."
    robin "Eeep..."
    "A large, menacing figure stands in the doorway, his face covered in a dark hood."
    stalker "I've missed you."
    robin "W-What do you want?"
    stalker "I want you, of course."
    robin "What..."
    stalker "You belong to me."
    "Robin freezes up, paralyzed with fear."
    "He needs my help."
    "I need to intervene."
    "Now is the time."
    robin "Get away!"
    stalker "Don't tell me what to do."
    robin "Eeek!"
    stop sound fadeout 0.5
    play music intruder fadein 1.0
    scene black with dissolve
    "I call the police and drop my phone before rushing out of the bathroom and jumping in front of Robin."
    scene storybeat6_17 with dissolve
    pro "HEY!"
    stalker "HUH, WHO ARE YOU?"
    pro "Get lost asshole!"
    robin "Ah! B-Be careful!"
    stalker "But Robin was supposed to be home alone..."
    stalker "This isn't how it was supposed to go..."
    pro "What do you want from Robin, why the fuck do you keep stalking him?"
    stalker "Stalking... is that what you think this is?"
    stalker "This is devotion... this is me taking what's mine."
    stalker "Robin... from the moment I saw his face on that live stream."
    stalker "I knew he had to be mine."
    pro "So you tracked down where he lives?"
    pro "You fucking followed him, stalked him, waited for the perfect opportunity to come do god knows what to him?"
    "I gotta keep buying time until the police manage to arrive."
    "If he runs now, I don't know whether we'll be able to catch him."
    pro "What gives you the right to ruin someone's life like this?"
    pro "You are ruining his mental health with your creepy ass fucking stalking."
    pro "You took your parasocial relationship with him way too fucking far."
    pro "He is a streamer, all he did was entertain you."
    pro "Yet here you are, thinking you know him, thinking that he'd even want to be with a person like you."
    scene storybeat6_18 with dissolve
    show robin neutral with dissolve:
        xpos 680
    show stalker smile with dissolve:
        xpos -600
    robin "..."
    stalker "Do you not get it?"
    stalker "He's a rare breed..."
    stalker "A femboy, a genuine femboy."
    pro "So he's just a fucking fetish to you?"
    stalker "No, of course not."
    stalker "He's pure."
    stalker "He's not corrupted by modern society."
    stalker "Femboys are meant to be protected."
    pro "Are you joking with me? He's not some poor innocent little thing for you to shelter."
    pro "He is a human being who deserves basic respect."
    pro "He's not a prize for you to win, he's not property."
    show robin open at jumper
    robin "That's right!"
    "Robin finally speaks up."
    robin "I am NOT an object to own. I'm a human being."
    show robin open:
        zoom 1.0
        xpos 680
        ease 0.1 zoom 1.05 xpos 660
        ease 0.05 zoom 1.04 xpos 660
    robin "Fuck you, fuck you and your stalker ass."
    show robin open:
        zoom 1.04
        xpos 660
        ease 0.1 zoom 1.08 xpos 640
        ease 0.05 zoom 1.07 xpos 640    
    robin "Fuck you for tracking down where I live, twice."
    show robin open:
        zoom 1.07
        xpos 640
        ease 0.1 zoom 1.1 xpos 610
        ease 0.05 zoom 1.09 xpos 610       
    robin "And fuck you for ever thinking that you'd have a chance with me in a million years."
    show robin neutral:
        zoom 1.09
        xpos 610
        ease 1.0 zoom 1.0 xpos 680 ypos 10
    show stalker angry
    stalker "Wh-"
    pro "Fuck yeah, tell him Robin!"
    stalker "I know everything about you, I know who you really are."
    stalker "Why do you act so tough? Is it to impress this loser?"
    stalker "We're meant for each other, my dear. Come with me."
    stalker "Give me a chance to show you... show you how good I can make you feel."
    pro "Shut the fuck up."
    robin "You disgust me."
    stalker "How can you say such hurtful things..."
    stalker "You... you aren't supposed to be like this."
    stalker "You're supposed to be pure..."
    stalker "You..."
    stalker "What kind of femboy curses?"
    stalker "Is this your doing?"
    stalker "You've corrupted him haven't you?"
    pro "Fuck off, dude. Leave."
    robin "Please get out of here."
    stalker "..."
    stalker "No..."
    stalker "No... NO!"
    stalker "FUCK THIS SHIT!"
    stalker "THIS WASN'T SUPPOSED TO HAPPEN."
    scene black with dissolve
    "The man pushes me aside and lunges at Robin."
    pro "ROBIN!"
    stalker "STAY STILL, IT'LL ONLY HURT FOR A SECOND!"
    scene storybeat6_19 at slight_wobble with dissolve:
        zoom 1.03 xalign 0.5 yalign 0.5
    "Without thinking, I tackle the stalker to the ground, grabbing him by the shoulders and slamming him onto the floor."
    "I can hear the faint sound of sirens coming up from the street."
    pro "THE POLICE ARE HERE YOU SICK FUCK!"
    "I hold him down on the ground, locking him in place."
    scene storybeat6_19 at slight_wobble:
        xalign 0.5 yalign 0.5 zoom 1.03
        ease 0.2 zoom 1.5
        ease 0.1 zoom 1.45
    stalker "GET OFF OF ME OR I SWEAR I'LL FUCKING KILL YOU!"
    "He thrashes his body violently, trying desperately to escape."
    pro "I DARE YOU, MOTHERFUCKER. TRY SOMETHING, DO IT!"
    "The man continues to struggle underneath me."
    robin "!!!"
    scene black with dissolve
    "I keep him restrained until I see flashing red lights outside the window."
    stop music fadeout 3.0
    "Within moments, two officers run inside."
    cop "Stay down, hands on your head!"
    "I release him from my grip, and the police immediately cuff him."
    "I step aside, my heart still racing as the adrenaline rush subsides."
    "Everything happened so quickly that I can barely comprehend what just occurred."
    cop "Can you tell us what's going on here?"
    "We spend the next hour or so explaining the situation to the police."
    "We also hand them the note and any other evidence they need."
    "They arrest the stalker and take him away."
    cop "If there's ever an issue like this again, you let us know."
    cop "We're always willing to help in situations like this."
    pro "Will do. Thank you very much, officer."
    "And with that, the police finally left."
    scene livingroom_night with dissolve
    show robin neutral with dissolve
    pro "Robin... are you okay?"
    pro "That was intense but... it's over now."
    pro "He's gone, for good."
    robin "..."
    robin "T-Thank you..."
    robin "For everything."
    pro "Of course. I couldn't let that guy hurt you."
    robin "But still... you risked yourself for me."
    pro "And I'd do it again."
    pro "Robin..."
    pro "I love you."
    pro "I love you with all my heart, and I'm so glad you're okay."
    robin "..."
    play music love fadein 3.0
    show robin neutral blush
    robin "... I love you too."
    scene white with dissolve
    "Without warning, he kisses me."
    scene storybeat6_20 with dissolve:
        subpixel True
        zoom 1.1 xalign 0.2 yalign 0.5
        ease 4.0 xalign 0.3 zoom 1.0
    pro "...!"
    pro "Robin..."
    robin "Mmmm..."
    pro "I love you... so much."
    robin "Me too, dummy."
    pro "I want to do everything I can to take care of you."
    robin "You already have done so much."
    pro "Not yet... not even close."
    pro "You deserve to feel safe."
    pro "I want you to feel loved and comfortable."
    pro "I want to cuddle you and kiss you whenever you desire."
    pro "Anything you want, anything."
    pro "Let me give it to you."
    pro "All you have to do is ask."
    robin "Anything...?"
    pro "Anything, forever and always."
    scene white with dissolve
    "He takes my hand and guides me to my room."
    robin "Then, let's do something."
    "His voice is soft and shy."
    "I close the door behind me."
    robin "Take me. Make me yours. Make me feel safe. Make me feel loved."
    scene storybeat6_21 with dissolve
    "I lay him down onto my bed and take off his pants."
    play sound storybeat6_21 fadein 1.0 loop
    show tongue with dissolve:
        xpos 830 ypos 900
        anchor (0.5, 1.0)
        ease 1.0 rotate 15
        ease 1.0 rotate -15
        repeat
    "I slowly spread his legs and begin eating his ass out."
    robin "Ahn..."
    "His asshole is warm and wet, his insides are inviting and soft."
    robin "Mmmm..."
    pro "You taste amazing."
    robin "F-Fuck... it feels so good."
    "I rub the rim of his asshole, teasing him slightly as he lets out cute moans."
    robin "A-Ah..."
    robin "Ohhhh..."
    "My dick is throbbing in my pants."
    robin "Mmm..."
    robin "F-Fuck me..."
    robin "Fuck me, fuck me, please fuck me..."
    stop sound fadeout 1.0
    hide tongue with dissolve
    "I slowly pull my tongue out of his ass."
    pro "You ready Robin?"
    robin "Yes, please."
    scene white with dissolve
    "I pull my pants off and rub my dick against the outside of his asshole."
    pro "Tell me if anything is uncomfortable."
    robin "Mmmhm."
    pro "Alright, here we go..."
    play sound storybeat5_14 loop
    scene storybeat6_22 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.01
        repeat
    "I slowly insert my cock inside his ass."
    robin "Ahhhn..."
    "I start thrusting in and out."
    robin "F-fuck, it feels so good."
    robin "Your big, warm cock inside me."
    pro "You're so tight, Robin."
    robin "Y-Yes..."
    robin "Yes, yessss."
    "Robin moans softly as I thrust inside him."
    pro "You feel so amazing Robin, your body is perfect."
    robin "D-Do you think so? Mmm."
    robin "Your cock feels so big inside of me... I love it."
    "I can feel Robin's body shake and shudder with each thrust, his soft moans growing louder."
    robin "It... it feels so good right now..."
    robin "Everything is just... ahn..."
    robin "Everything is just perfect..."
    robin "Y-Your cock, mmmh... i-it's making my legs weak."
    robin "Y-Your words, t-they make me melt."
    robin "You're... ahn... s-so perfect."
    play sound storybeat5_14_2 loop
    scene storybeat6_22 with vpunch:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.01
        repeat
    "I start pounding harder, increasing the pace of my thrusts as he lets out more cute little whimpers."
    robin "I-It feels like I'm floating..."
    pro "You gonna cum?"
    robin "N-Not yet... ahn..."
    robin "W-Want to enjoy this..."
    "I continue to fuck Robin's ass, his cute cock flopping up and down with each thrust."
    robin "[protagonist_name]..."
    robin "Do you think that I can maybe... ahn..."
    robin "Maybe ride you..."
    robin "I don't want you to be the only one putting in effort, I... ah..."
    robin "I wanna put in effort for you too."
    stop sound fadeout 1.0
    scene white with dissolve
    "I stop thrusting, pulling my dick out and laying down on the bed."
    robin "Here I go..."
    scene storybeat6_23 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.2 yalign 1.0 zoom 1.07
        ease 0.15 yalign 0.5 zoom 1.01
        repeat
    play sound storybeat6_23 loop
    "Robin begins riding me, his insides tightening around my cock as he bounces up and down."
    pro "H-Holy fuck, that feels incredible..."
    "I can hear him breathing heavily with every movement he makes."
    robin "Fuck..."
    robin "This... feels amazing."
    robin "Ah, ahhh."
    pro "Fuck, Robin."
    pro "You're so perfect..."
    pro "Everything about you is perfect..."
    robin "Ahh..."
    robin "F-fuck... you feel so good inside of me..."
    "Everything about this moment feels perfect."
    "Our body's are completely one with one another."
    "After what happened today, I feel closer to Robin."
    "Both emotionally and physically."
    robin "Ahhhn, ahhn."
    pro "You're doing great Robin..."
    pro "You're being such a good boy..."
    robin "F-Fuck..."
    robin "Y-Yes... yes..."
    pro "Good boy... good boy."
    robin "Y-Your cock is hitting me just right."
    robin "I... I want you to..."
    robin "I want you to fill my bussy."
    robin "I want to take it all, as many times as you need..."
    robin "I want... I want you to be with me forever."
    pro "Fuck... I'm close."
    pro "I'm so close Robin..."
    robin "Ah, ahhh!"
    robin "F-fuck me, fill me up please...!"
    menu:
        "Cum": 
            pro "Robin...!"
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    scene storybeat6_24 at slight_wobble with dissolve:
        subpixel True
        zoom 1.03 xalign 0.5 yalign 0.2
        ease 4.0 zoom 1.3 yalign 0.5
        pause 1.0
        ease 4.0 zoom 1.03 yalign 0.4
        pause 1.0
        ease 4.0 zoom 1.03 yalign 0.2
        repeat    
    play sound storybeat5_15_climax
    "I feel Robin tighten up around my cock as I shoot my load deep into his asshole."
    "He moans loudly as he climaxes."
    robin "Ahn~!"
    robin "So... warm~"
    "He's completely exhausted, his breathing is shallow and labored."
    pro "I love you Robin."
    robin "I... I love you too."
    scene white with dissolve
    "He collapses on top of me."
    robin "You..."
    robin "You saved me tonight..."
    "I wrap my arms around him and cuddle him closely."
    "I don't know how to respond, so instead I stay quiet and hold him close to me."
    pro "Good night Robin..."
    robin "Goodnight..."
    robin "My hero."
    stop music fadeout 1.0
    scene black with dissolve
    pause 1.0
    play sound positive_stinger
    show prologue9 with dissolve
    pause 1.5
    show black with dissolve
    scene mc_bedroom with dissolve
    "The next morning, I wake up and Robin is gone."
    pro "Hm?"
    pro "He must've got up before me..."
    scene livingroom_day with dissolve
    show robin neutral with dissolve
    "I step outside my room and see Robin in the living room."
    pro "Hey Robin, looks like I slept in."
    pro "Sorry, last night was pretty exhausting haha..."
    robin "Yeah it was..."
    robin "Hey, can we talk?"
    pro "Oh, of course."
    show robin neutral blush
    play music love fadein 1.0
    robin "I never truly and sincerely said this but... thank you for saving me."
    pro "Oh, it was nothing-"
    show robin open blush
    robin "No, not just from the stalker. You... you saved my life."
    robin "You've made me realize how much I was holding on to the past, how much I was hurting myself by trying to protect myself."
    robin "And last night made me realize something."
    pro "Hm?"
    robin "That if you're willing to put yourself in danger to save me, that means you actually care about me. Like, really really care."
    robin "Nobody else in my life has shown that level of care to me before."
    show robin neutral blush
    robin "You... make me want to get better, and be better."
    robin "And that's why I..."
    show robin smile blush
    robin "I want you to be my boyfriend!"
    pro "Robin..."
    pro "Of course I'll be your boyfriend."
    pro "I'm just kicking myself for not asking you earlier."
    show robin open blush at jumper
    robin "R-Really?"
    pro "Absolutely. There is no one else in this world who I'd rather be with than you."
    robin "I..."
    pro "What's wrong?"
    show robin smile blush
    robin "It's... It's just a lot, I guess."
    robin "I... I thought I'd live and die alone."
    robin "I love you, [protagonist_name]..."
    robin "I love you so much!"
    scene white with dissolve
    "Robin jumps into my arms."
    pro "Woah there, haha!"
    "I hug him tightly."
    "After a moment, he lets go."
    scene storybeat6_25 with dissolve:
        zoom 1.6 xalign 0.5 yalign 0.5
        ease 4.5 zoom 1.0
    robin "You're the best thing that ever happened to me..."
    robin "I'll be a good boyfriend to you... the best boyfriend ever..."
    pro "Of course, and I'll try to be a good boyfriend to you too."
    pro "But..."
    pro "Don't feel obligated to try so hard, alright?"
    robin "What do you mean?"
    pro "You don't have to be anything other than you."
    pro "I fell in love with the true Robin."
    pro "The real Robin."
    pro "So I want the real Robin to never change."
    pro "Be Robin. Be you."
    "Robin looks at me with his big beautiful eyes."
    robin "I'm so glad that you and I became roommates."
    robin "I love you so much!"
    scene white with dissolve
    pause 0.5
    play sound positive_stinger
    show storybeat6_26 with dissolve
    pause 2.0
    scene white with dissolve
    "The door creaks open as I come in through the door, home after a long day."
    scene storybeat6_27 with dissolve:
        zoom 1.6 xalign 0.5 yalign 0.5
        ease 4.5 zoom 1.0
    robin "You're late... dinner is gonna get cold if you don't eat now!"
    "My husband Robin stands in the kitchen wearing an apron."
    pro "I know, I'm sorry! I had to stay a little late today to fix up some last minute bugs."
    pro "With my game releasing next week, the entire studio has really been working hard."
    robin "It's okay! But seriously, you should eat."
    robin "I didn't slave over the stove for you not to appreciate it!"
    pro "Haha, alright, alright."
    scene white with dissolve
    "I walk up and kiss him."
    robin "Hehehe..."
    "..."
    play sound storybeat5_14 loop
    scene storybeat6_28 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.01
        repeat
    pro "Fuck... you feel so good baby..."
    "Ever since I opened up my own indie game studio last year, Robin hasn't had to work."
    "He still streams occasionally as a hobby, but for the most part he's a house husband." 
    "The last 3 years have been a dream, I can see myself spending the rest of my life with Robin."
    "It's also nice that Robin gets super, super fucking horny seeing me all tired and worn out after a long day of work."
    robin "Hehe, you still have so much stamina honey!"
    "I thrust into him deeper."
    pro "Fuck... I'm reaching my limit baby!"
    robin "Do it, fill me up!"
    pro "Here it comes, here it comes!"
    stop sound fadeout 0.5
    play sound storybeat5_15_climax fadein 0.5
    scene white with dissolve
    "I let my load loose inside of him."
    robin "Ahn~!"
    robin "So... much...!"
    pro "Fuck... that felt good..."
    robin "Hehe... yeah..."
    pro "I love you baby..."
    scene black with dissolve
    "I close my eyes, feeling exhausted from my day at work."
    pro "I think I'm gonna pass out, I'm so tired."
    robin "Oh no, no you're not!"
    "I suddenly feel him climb on top of me, grabbing my soft cock and shoving it up his wet asshole again."
    robin "We can't go to sleep without you getting off one more time!"
    pro "F-Fuck, you're right."
    robin "Now, get ready for the ride of your life~!"
    stop music fadeout 0.5
    $ renpy.end_replay()
    play sound positive_event_01
    $ achievement.grant("ending1")
    system "Ending 1 Complete"
    jump end_of_game

label ending2:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    pro "Robin, listen to me."
    pro "We have to leave this apartment."
    pro "Take whatever belongings you need and let's pack up our stuff."
    pro "This is the only way I can protect you."
    robin "You... you mean leave right now? Tonight?"
    pro "Yes, right now. It's not safe here."
    robin "B-But..."
    pro "We need to leave, Robin."
    robin "But what if-"
    pro "You said you trust me, right?"
    pro "This is the only way."
    pro "Leaving will give us enough time to figure out a long term plan."
    pro "But we can't stay here any longer."
    robin "..."
    robin "Okay, let's go..."
    scene robin_room2 with dissolve
    show robin neutral with dissolve
    "Robin begins packing his bags in a hurry."
    pro "It'll be okay, Robin."
    pro "We're going to go somewhere safe, okay?"
    pro "I'll call my friend to see if we can crash there."
    pro "He's got a lot of extra room and he's very accommodating."
    pro "We'll be fine there, Robin. Everything will be fine. Trust me."
    robin "Alright... I just..."
    robin "I hope you're right."
    pro "Robin."
    pro "It will be fine. We will get through this together."
    pro "You just need to follow my lead. Everything will work out."
    "I can see a tiny spark of hope in his eyes."
    robin "O-Okay."
    pro "We're going to be okay, Robin. I'll make sure of that."
    scene black with dissolve
    "We take the next hour to pack our necessary belongings."
    "Bulky stuff like my computer won't be able to come, but I bring my backup drives so I don't lose any of my work."
    scene livingroom_night with dissolve
    show robin neutral with dissolve
    pro "You have everything we need?"
    robin "Y-Yes."
    robin "Are you sure this is the right decision though?"
    robin "If we just run away like this, he could find us and..."
    pro "No, Robin."
    pro "This is the right move."
    pro "He's already found you here, and it's only a matter of time before he does something more drastic than a note."
    pro "I'm worried about what might happen if we stay."
    pro "If we leave now and get to a safe location, then maybe we can figure out a long term solution to this."
    robin "You... you're probably right..."
    robin "It's just so scary, being on the run like this..."
    pro "I'm scared too, Robin. I'm scared for you and for us. But I know this is the best course of action right now. I can feel it."
    pro "Now come on, let's get going. It'll take a few hours to get there."
    robin "O-Okay."
    stop music fadeout 3.0
    scene black with dissolve
    "The car ride was long and silent."
    "I can feel Robin's anxiety, it's like a heavy weight pressing down on my chest."
    "I'm trying my best not to think about it. To stay calm. To stay focused."
    "But it's difficult... I can't help but wonder what the next few weeks are going to be like..."
    "How long will we be on the run? Where are we going to go?"
    pause 0.5
    play sound positive_stinger
    show storybeat6_29 with dissolve
    pause 2.0
    scene black with dissolve
    "Living at my friends place has been surprisingly easy."
    scene storybeat6_30 with dissolve
    "It's not as nice as our apartment, and the space isn't quite the same, but my friend has been very accommodating of our needs."
    "Robin seems to be adjusting to the situation better than I am."
    "He still seems on edge and skittish, but I can tell he's getting used to the new normal."
    "We've been trying to make the best of our time here, but I can't help but worry that we'll never get back home again."
    "But as long as Robin's safe, I don't care."
    show robin neutral with dissolve
    pro "Hey Robin, how are you feeling?"
    robin "I'm doing okay... just a little worried about everything still."
    robin "It's not as easy for me to forget the situation as I'd hoped, but it's better than I thought."
    pro "Don't worry, everything will work out in the end."
    pro "And if not... well at least we're together."
    robin "Yeah..."
    robin "So we never got the chance to get back to the conversation we were having before..."
    robin "What are we, [protagonist_name]?"
    pro "Oh yeah..."
    pro "Well, we're living together. That means we're pretty close."
    pro "I mean, I ditched my apartment to be with you."
    pro "I think that's enough, isn't it?"
    robin "Yeah..."
    play music love fadein 1.0
    show robin smile
    robin "I like what we have, y'know?"
    robin "It's... comfortable."
    show robin open
    robin "But I was talking more in terms of labels and titles."
    show robin neutral
    pro "Haha yeah. I guess that makes sense. But I don't know if I have anything for you that I can call it."
    robin "Yeah..."
    show robin smile
    robin "Maybe... maybe we don't have to give it a label."
    robin "It can just be what it is, y'know?"
    pro "That's true, haha. It's definitely not a conventional relationship."
    robin "Yeah, but I think that's the point."
    robin "It's special because of its uniqueness, not because it fits into a certain category or box."
    robin "And it makes me feel like we're really close."
    pro "Yeah... that's what makes it special. And that's why I like what we have, Robin."
    pro "I don't care if you call it a relationship or a friendship or whatever."
    show robin smile blush
    robin "Me neither. All I care about is being together with you, and knowing you love me."
    robin "Because I love you."
    pro "Oh, you do?"
    robin "Yeah."
    pro "That's perfect. I love you too."
    pro "And I think we're on the right track here. It's just taking some getting used to."
    pro "But it's better than I expected. I mean, we've only been here for 3 weeks, and I already feel like I'm home."
    robin "Mhm!"
    robin "Y'know... I don't think any of your friends are home right now."
    robin "That means we're home alone..."
    pro "Oh... what are you suggesting?"
    scene white with dissolve
    "He tackles me onto the bed."
    pro "Oh! Hey!"
    robin "You've been so sweet and patient with me, I just..."
    robin "I feel so safe with you."
    robin "Let's... let me feel your love."
    pro "I'd be happy to."
    robin "Now let's get these clothes off, hmm?"
    scene storybeat6_31 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.5
        zoom 1.01
        ease 0.25 yalign 1.0 zoom 1.07
        ease 0.2 yalign 0.5 zoom 1.01
        repeat
    play sound "audio/sound/nsfw_sounds/suck_2.wav" loop
    "He takes off my pants and begins sucking my dick."
    pro "Mmmm, that's it. Good boy... good boy."
    robin "Mmm~"
    "His technique has improved so much since we first started getting sexual with each other."
    "His tongue feels so amazing."
    pro "Just like that..."
    "His sloppy wet blowjob noises fill the room, turning me on even more."
    robin "Mmmmmhmm~"
    robin "The taste... the smell..."
    robin "It's driving me crazy... I need your cum..."
    pro "Keep going Robin, suck it all out of me..."
    robin "Mmmmgphh~"
    pro "This is everything..."
    pro "This is all I need..."
    pro "You're all I need..."
    robin "Mmm~"
    pro "Fuck... I'm reaching my limit..."
    pro "Robin... I'm going to..."
    pro "I'm going to cum, Robin... keep going."
    "I can hear the sounds of his slurping increase."
    menu:
        "Cum": 
            pro "Robin...!"
            pro "Here it comes!"
    window hide
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    show whiteflash zorder 50
    pause 1.0
    stop sound fadeout 1.0
    scene white with dissolve
    pause 1.0
    scene storybeat6_32 at slight_wobble with dissolve:
        zoom 1.04 xalign 0.5 yalign 0.5
    play sound storybeat6_32
    robin "MMMGGGGPPPPHHH~"
    "Robin doesn't move, taking in every inch of my cock as he milks it dry."
    pro "F-Fuck, Robin..."
    robin "Mmmm~"
    "I hear him gulp as much of my cum as he can."
    scene white with dissolve
    "After a few moments, he slowly pulls my dick out of his mouth."
    robin "I want more...~"
    pro "Haha, you're insatiable, Robin."
    pro "Here, climb onto the bed."
    robin "Yes sir~"
    scene storybeat6_33 with dissolve
    "Robin gets on all fours and presents his tight little asshole for me."
    pro "Fuck..."
    robin "C'mon and fuck me..."
    robin "You said you loved me didn't you?"
    robin "Your friends won't be home for a few hours, so we have all day..."
    pro "Robin, I don't know how long we can stay like this."
    scene white with dissolve
    pro "But... I love you."
    stop music fadeout 1.0
    $ renpy.end_replay()
    play sound positive_event_01
    $ achievement.grant("ending2")
    system "Ending 2 Complete"
    jump end_of_game

label ending3:

    if _in_replay:

        show screen Replayexit

        $ protagonist_name = persistent.name

    pro "Robin, listen to me."
    pro "You'll be fine, okay?"
    pro "The note is clearly just a sign that he doesn't have the balls to actually do something."
    pro "Plus I'm here, I'll protect you in case anything happens."
    pro "So we shouldn't do anything."
    robin "B-but..."
    pro "I'm serious. This is not something you need to worry about."
    pro "I promise I'll keep an eye on things, and I'll make sure that nothing happens."
    robin "Okay, I..."
    robin "I'm still worried."
    robin "But if you say everything will be okay, then I guess I should trust you."
    scene robin_room2 with dissolve
    show robin neutral with dissolve
    "I can still see the doubt in his eyes, but at least he isn't panicking anymore."
    pro "It's going to be alright..."
    pro "If you're still worried, you can sleep with me tonight, and I'll keep an eye on things."
    pro "That way, if something happens, we'll be together."
    robin "Actually I think I'm going to stay up a bit longer..."
    robin "I'm still spooked so I'll need some time to calm down."
    pro "Oh... sure."
    pro "I can stay up with you if you want."
    pro "We can watch something on the TV."
    robin "No it's okay, you can go to sleep."
    robin "I'll be okay... I think."
    pro "Alright, well..."
    pro "Don't hesitate to come to me if you need me, okay?"
    robin "Of course."
    pro "Goodnight, Robin."
    stop music fadeout 3.0
    scene black with dissolve
    "I exit Robin's room and enter mine."
    scene storybeat2_10 with dissolve
    "I lay in bed for a few moments, thinking about the situation."
    "I feel useless. I can't do anything to help him right now, except just be there for him."
    pro "Maybe I should have been more proactive... he seems pretty freaked out."
    "But I don't know what to do... I've never been in this kind of situation before..."
    "I should be doing something... but what?"
    pro "I need to be strong, I need to be his rock."
    pro "He needs someone to lean on, and I have to be that person for him. If not me, then who else?"
    pro "I have to protect him, no matter what. He's too precious to lose."
    pro "I'm the only person who can help him through this, and I have to be strong enough for the both of us."
    pro "I can't let him down. Not again."
    scene black with dissolve
    "I drift off to sleep, my mind still swimming with thoughts of what I can do..."
    "..."
    "..."
    "..."
    robin "AH!"
    play music intruder fadein 1.0
    scene mc_bedroom_night with vpunch:
        subpixel True
        zoom 1.1
    "I jolt awake."
    pro "Robin."
    scene storybeat6_18 with dissolve
    show robin open with dissolve:
        xpos 680
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        repeat

    show stalker smile with dissolve:
        xpos 400
        linear 0.2 xoffset 20
        linear 0.1 xoffset -20
        repeat
    "I run out of my room and see Robin pinned to the ground by his stalker."
    "Robin is kicking and screaming, but he can't seem to fight him off."
    pro "HEY, WHAT THE FUCK!"
    scene black with dissolve
    "Before I can reach him, he dashes into Robin's room and locks the door behind him."
    pro "SHIT, NO!"
    scene robin_room_outside_night with dissolve
    "I try to open the door, but it's locked."
    "I can hear Robin crying out in pain on the other side of the door."
    pro "ROBIN!"
    pro "LET HIM GO!"
    scene robin_room_outside_night:
        zoom 1.0 xalign 0.5 yalign 0.5
        ease 0.2 zoom 1.3 xalign 0.45
        ease 0.1 zoom 1.25
        ease 0.5 zoom 1.0 xalign 0.5
        repeat
    "I bang and kick on the door as much as I can, but it won't budge."
    pro "ROBIN!"
    pro "ROBIN, ARE YOU OKAY?"
    pro "ROBIN!"
    pro "GOD FUCKING DAMMIT! OPEN UP!"
    pro "OPEN THE DOOR! OPEN IT!"
    "I take a step back and charge at the door, throwing all my weight against it."
    "I can feel it start to give way..."
    pro "COME ON!"
    pro "OPEN THIS FUCKING DOOR!"
    "I continue ramming the door with my shoulder."
    pro "ROBIN!"
    pro "HANG IN THERE!"
    "I can hear him sobbing uncontrollably, and it sounds like he's begging to be let go."
    pro "I'M COMING, HANG ON ROBIN!"
    "I throw myself against the door as hard as I can, and finally..."
    scene black with dissolve
    pro "FUCK!"
    "I break through the door, sending wood splintering across the room."
    scene robin_room2 with dissolve
    show robin open with dissolve:
        xpos 680
        linear 0.1 xoffset -5
        linear 0.1 xoffset 5
        repeat
    show stalker smile with dissolve:
        xpos 400
        linear 0.2 xoffset 20
        linear 0.1 xoffset -20
        repeat
    "I see Robin's attacker standing over Robin's bed."
    robin "P-Please, I-"
    pro "GET THE FUCK OFF OF HIM!"
    scene black with dissolve
    "I sprint towards him, tackling him to the floor."
    scene storybeat6_19 at slight_wobble with dissolve:
        zoom 1.03 xalign 0.5 yalign 0.5    
    pro "CALL THE POLICE ROBIN!"
    "He tries to fight back, but I keep him pinned down."
    show storybeat6_34 at slight_wobble with dissolve:
        zoom 1.03 xalign 0.5 yalign 0.5    
    pro "DON'T YOU FUCKING TOUCH HIM!"
    pro "DON'T YOU EVER FUCKING TOUCH HIM AGAIN!"
    pro "YOU FUCKING HEAR ME?"
    pro "DON'T FUCKING TOUCH HIM, EVER AGAIN!"
    "I can hear Robin's voice behind me on the phone with the police."
    show storybeat6_35 at slight_wobble with dissolve:
        zoom 1.03 xalign 0.5 yalign 0.5
    pro "YOU PIECE OF SHIT! HOW COULD YOU DO THAT TO HIM?"
    "I'm seeing red."
    "I don't know whats happening any more."
    scene storybeat6_36 with dissolve
    "All of a sudden, my vision is completely red."
    scene black with dissolve
    "Then black."
    stop music fadeout 2.0
    "And then..."
    cop "Sir..."
    cop "..."
    cop "Sir, are you listening?"
    scene livingroom_night with dissolve
    "I snap out of the trance I was in."
    "What the fuck..."
    "We're in the living room now..."
    "And the cops are here."
    cop "Sir, please sit down."
    cop "We need to get your statement."
    pro "My statement..."
    "The police ask me questions regarding what happened."
    "Apparently, by the time they had arrived to the apartment, I had already beaten and knocked out the stalker."
    "I can barely remember anything, I feel like I blacked out."
    pro "And where is Robin?"
    cop "We had a paramedic look him over, but he's okay."
    cop "Just shaken up, and bruised."
    pro "Oh thank god..."
    pro "I was so worried..."
    cop "We've arrested the man and he's on his way to jail, so he won't be able to harm Mr. Robin anymore."
    pro "Can I see him?"
    cop "Sure, I'll ask the paramedics to release him. We should be leaving right now any way."
    pro "Thank you, officer."
    "The police officer leaves."
    show robin neutral with easeinleft
    "A few minutes later, Robin comes back into the apartment."
    pro "Robin, thank god you're-"
    show robin open
    robin "Don't..."
    robin "Don't talk to me..."
    pro "What...?"
    pro "But-"
    play music sad fadein 1.0
    robin "No..."
    robin "Just shut the fuck up..."
    pro "Robin..."
    "I can see tears welling up in his eyes."
    robin "I trusted you..."
    robin "You told me everything would be okay if we just did nothing..."
    robin "You fell asleep peacefully while I was fucking terrified!"
    pro "But you said I could... I couldn't have known that-"
    robin "Then maybe I shouldn't have trusted you in the first place..."
    robin "You could have gotten me killed..."
    robin "You could have gotten yourself killed..."
    robin "And not to mention how violent you got with him..."
    robin "You... your hands were all bloody."
    pro "I didn't mean to... I didn't even realize I was..."
    pro "I blacked out and when I came to, the cops were-"
    robin "I'm leaving."
    show robin neutral
    robin "I'm moving out and going somewhere else."
    robin "I... I can't stay with you any more."
    robin "You broke my trust... I can't anymore."
    robin "I'm sorry."
    "I'm stunned. I don't know what to say."
    robin "I'm going to stay at a motel tonight. Don't bother trying to contact me."
    robin "I'll be back for my stuff tomorrow..."
    robin "I can pay for the damages to the door you broke too."
    pro "Robin... no..."
    pro "I was... I was just..."
    hide robin with easeoutleft
    "Without another word, he turns around and leaves."
    "I'm alone... again..."
    "And this time it's my fault..."
    "I failed him..."
    "I told him to trust me..."
    "If maybe I had stayed up with him... or even just ran away with him."
    "This wouldn't have happened."
    scene black with dissolve
    "I... I don't even know what to think."
    "What do I do now...?"
    "Was this the end of things?"
    "I guess so..."
    "I'm... I'm horrible."
    stop music fadeout 1.0
    $ renpy.end_replay()
    play sound positive_event_01
    $ achievement.grant("ending3")
    system "Ending 3 Complete"
    jump end_of_game

image game_end2 = Movie(play="gui/Femboy.webm")

label end_of_game:
    play sound positive_event_02
    scene game_end2 with dissolve
    call screen game_end with dissolve    

label annviersary_event:
    robin "Goodmorning handsome..."
    "Robin gently smiles at me, his beautiful blue eyes glowing in the morning sun."
    pro "Morning sleepy head..."
    robin "Sleepy head? I woke up before you!"
    pro "You also passed out first last night, dummy."
    robin "Hey, it's not my fault your voice makes me drowsy..."
    robin "You're super soothing to listen to!"
    "This is Robin, my roommate and boyfriend."
    "Tomorrow, it'll officially be the one year anniversary since we started dating."
    "My relationship with Robin has been the best thing to ever happen to me."
    "He started out as my shy roommate who could barely even hold eye-contact with me."
    "Over time, we slowly became closer as friends."
    "I started to see him as more than just my roommate, but I didn't want to risk our friendship and confess."
    "At least, not until he confessed to me himself after I walked in on him masturbating..."
    "After what felt like an eternity of building sexual tension, we were able to release ourselves and live how we wanted."
    "It took awhile, but Robin was finally comfortable embracing his true self."
    "And damn, does he look gorgeous..."
    robin "Anyways, I'm gonna hop in the shower real quick, okay?"
    robin "Feel free to make yourself breakfast while I'm in there!"
    pro "Okay, sounds good."
    "Robin heads off to the bathroom and I get out of bed."
    "I walk to the kitchen to make myself some breakfast."
    "Honestly, it's kind of amazing how far we've come."
    "While we've encountered scary situations, like the time his stalker found out where we lived, things have generally been great for us."
    "He's been attending therapy sessions regularly for months now, and it's improved his mental health greatly."
    "I know we've still got a long way to go together, but we are better off now than we've ever been."
    "I finish my breakfast just in time for Robin to get out of the shower."
    "He steps into the living room in his towel."
    robin "Morning again..."
    "Seeing him always makes my heart skip a beat."
    pro "Morning again, Robin."
    pro "How was your shower?"
    robin "It was refreshing!"
    robin "I can feel all that sleepyness and grogginess washing away, hehe."
    pro "You excited for tomorrow?"
    pro "Y'know, our first year anniversary as a couple."
    "Robin's face lights up."
    robin "I've never been this excited for something in my entire life!"
    robin "I know you're keeping it a surprise but... can you give me any hints about what you have planned for us?"
    pro "Tsk, tsk."
    pro "Not a chance, you gotta be patient for this!"
    robin "C'moooon!"
    robin "At least a teeny-tiny hint..."
    pro "Hmm..."
    pro "I could tell you, but that'd ruin all the fun."
    pro "I have a full day of excitement lined up, so you should save that energy of yours."
    robin "Fine, I guess I can wait just one more day..."
    "I've been planning our anniversary trip for quite awhile now."
    "I had to get everything perfect. Robin deserves it."
    "The past year with Robin has been nothing short of fantastic, even with all the stress and difficult situations we've experienced."
    "He means the absolute world to me, and I want our relationship to grow even further."
    pro "I'm gonna go get ready for the day, okay baby?"
    pro "I'll talk to you later."
    robin "Okay, see you soon!"
    "I head back to my room to get dressed."
    pro "Man, I can't wait for tomorrow..."

