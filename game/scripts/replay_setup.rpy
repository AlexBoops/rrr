## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.
init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (3 + 1)

    replay_page = 0

    class ReplayItem:
        def __init__(self, thumbs, replay, name):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name

        def num_replay(self):
            return len(self.thumbs)

    #add replay items here format below
    #Replay_items.append(ReplayItem(["the thumbnail"], "the_label_from_code", "brief description"))
    Replay_items = []

    Replay_items.append(ReplayItem(["storybeat1"], "story_beat1", "{color=#ffffff}Story Event 1{/color}"))
    Replay_items.append(ReplayItem(["storybeat2"], "story_beat2", "{color=#ffffff}Story Event 2{/color}"))
    Replay_items.append(ReplayItem(["storybeat3"], "story_beat3", "{color=#ffffff}Story Event 3{/color}"))
    Replay_items.append(ReplayItem(["storybeat4"], "story_beat4", "{color=#ffffff}Story Event 4{/color}"))
    Replay_items.append(ReplayItem(["storybeat5"], "story_beat5", "{color=#ffffff}Story Event 5{/color}"))
    Replay_items.append(ReplayItem(["storybeat6"], "story_beat6", "{color=#ffffff}Story Event 6 (Ending){/color}"))
    Replay_items.append(ReplayItem(["ending1"], "ending1", "{color=#ffffff}Ending 1{/color}"))
    Replay_items.append(ReplayItem(["ending2"], "ending2", "{color=#ffffff}Ending 2{/color}"))
    Replay_items.append(ReplayItem(["ending3"], "ending3", "{color=#ffffff}Ending 3{/color}"))


#the locked image for the replay gallery if you're using the gallery you can use the same (if you want to)
image replay_locked = "images/replay/replay_lock.jpg"

#384x216 (16x9) set 1280x720p for the lock and thumbnails
#600x338 (16x9) set 1920x1080 for the lock and thumbnails
#replay thumbnails images setup defined here
image Rthumb1 = ("images/replay/replay_unlock.jpg")
