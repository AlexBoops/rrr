init python:

    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb_source=None, thumb_size=(384, 216), locked="lockedthumb"):
            self.name = name
            self.images = images
            if thumb_source is None:
                thumb_source = images[0]
            self.thumb_source = thumb_source
            self.thumb_size = thumb_size
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme

        @property
        def thumb(self):
            thumb_displayable = renpy.displayable(self.thumb_source)
            if thumb_displayable is None:
                renpy.log(f"Warning: Image tag '{self.thumb_source}' not found.")
                return None
            else:
                return im.Scale(thumb_displayable, *self.thumb_size)


    gallery_items = []
    gallery_items.append(GalleryItem("{color=#000}Image 1{/color}", ["prologue4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 2{/color}", ["prologue7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 3{/color}", ["prologue12"]))
    gallery_items.append(GalleryItem("{color=#000}Image 4{/color}", ["storybeat1_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 5{/color}", ["storybeat1_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 6{/color}", ["storybeat2_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 7{/color}", ["storybeat2_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 8{/color}", ["storybeat2_7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 9{/color}", ["storybeat2_11"]))
    gallery_items.append(GalleryItem("{color=#000}Image 10{/color}", ["storybeat2_13"]))
    gallery_items.append(GalleryItem("{color=#000}Image 11{/color}", ["storybeat3_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 12{/color}", ["storybeat3_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 13{/color}", ["storybeat3_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 14{/color}", ["storybeat3_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 15{/color}", ["storybeat3_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 16{/color}", ["storybeat3_10"]))
    gallery_items.append(GalleryItem("{color=#000}Image 17{/color}", ["storybeat3_12"]))
    gallery_items.append(GalleryItem("{color=#000}Image 18{/color}", ["storybeat3_14"]))
    gallery_items.append(GalleryItem("{color=#000}Image 19{/color}", ["storybeat4_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 20{/color}", ["storybeat4_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 21{/color}", ["storybeat4_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 22{/color}", ["storybeat4_8"]))
    gallery_items.append(GalleryItem("{color=#000}Image 23{/color}", ["storybeat4_9"]))
    gallery_items.append(GalleryItem("{color=#000}Image 24{/color}", ["storybeat5_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 25{/color}", ["storybeat5_7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 26{/color}", ["storybeat5_11"]))
    gallery_items.append(GalleryItem("{color=#000}Image 27{/color}", ["storybeat5_12"]))
    gallery_items.append(GalleryItem("{color=#000}Image 28{/color}", ["storybeat5_13"]))
    gallery_items.append(GalleryItem("{color=#000}Image 29{/color}", ["storybeat5_14"]))
    gallery_items.append(GalleryItem("{color=#000}Image 30{/color}", ["storybeat5_15"]))
    gallery_items.append(GalleryItem("{color=#000}Image 31{/color}", ["storybeat5_16"]))
    gallery_items.append(GalleryItem("{color=#000}Image 32{/color}", ["storybeat5_17"]))
    gallery_items.append(GalleryItem("{color=#000}Image 33{/color}", ["storybeat5_18"]))
    gallery_items.append(GalleryItem("{color=#000}Image 34{/color}", ["storybeat5_19"]))
    gallery_items.append(GalleryItem("{color=#000}Image 35{/color}", ["storybeat5_20"]))
    gallery_items.append(GalleryItem("{color=#000}Image 36{/color}", ["storybeat5_21"]))
    gallery_items.append(GalleryItem("{color=#000}Image 37{/color}", ["storybeat6_10"]))
    gallery_items.append(GalleryItem("{color=#000}Image 38{/color}", ["storybeat6_14"]))
    gallery_items.append(GalleryItem("{color=#000}Image 39{/color}", ["storybeat6_16"]))
    gallery_items.append(GalleryItem("{color=#000}Image 40{/color}", ["storybeat6_17"]))
    gallery_items.append(GalleryItem("{color=#000}Image 41{/color}", ["storybeat6_19"]))
    gallery_items.append(GalleryItem("{color=#000}Image 42{/color}", ["storybeat6_20"]))
    gallery_items.append(GalleryItem("{color=#000}Image 43{/color}", ["storybeat6_21"]))
    gallery_items.append(GalleryItem("{color=#000}Image 44{/color}", ["storybeat6_22"]))
    gallery_items.append(GalleryItem("{color=#000}Image 45{/color}", ["storybeat6_23"]))
    gallery_items.append(GalleryItem("{color=#000}Image 46{/color}", ["storybeat6_24"]))
    gallery_items.append(GalleryItem("{color=#000}Image 47{/color}", ["storybeat6_25"]))
    gallery_items.append(GalleryItem("{color=#000}Image 48{/color}", ["storybeat6_27"]))
    gallery_items.append(GalleryItem("{color=#000}Image 49{/color}", ["storybeat6_28"]))
    gallery_items.append(GalleryItem("{color=#000}Image 50{/color}", ["storybeat6_31"]))
    gallery_items.append(GalleryItem("{color=#000}Image 51{/color}", ["storybeat6_32"]))
    gallery_items.append(GalleryItem("{color=#000}Image 52{/color}", ["storybeat6_33"]))
    gallery_items.append(GalleryItem("{color=#000}Image 5666666{/color}", ["robin_door_open_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["trust_movie_1_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 54{/color}", ["desire_movie_1_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 55{/color}", ["desire_movie_1_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 56{/color}", ["affection_movie_1_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["trust_movie_2_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["trust_movie_2_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["trust_movie_3_7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["trust_movie_3_8"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["trust_movie_3_11"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["affection_movie_3_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["affection_movie_3_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["affection_movie_3_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["affection_movie_3_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["affection_movie_3_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["affection_movie_3_6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["desire_movie_2_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["desire_movie_2_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["desire_movie_3_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["desire_movie_3_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["desire_movie_3_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 53{/color}", ["desire_movie_3_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 57{/color}", ["desireevent1_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 58{/color}", ["robin_bathroom"]))
    gallery_items.append(GalleryItem("{color=#000}Image 59{/color}", ["robin_bathroom_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 60{/color}", ["robin_bathroom_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 61{/color}", ["robin_bathroom_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 62{/color}", ["robin_bathroom_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 63{/color}", ["robin_bathroom_6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 64{/color}", ["robin_bathroom_7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 65{/color}", ["walkin1_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 66{/color}", ["walkin1_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 67{/color}", ["walkin1_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 68{/color}", ["walkin1_6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 69{/color}", ["kitchen_night1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 70{/color}", ["kitchen_night2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 71{/color}", ["kitchen_night3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 72{/color}", ["kitchen_night4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 73{/color}", ["kitchen_night5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 74{/color}", ["kitchen_night6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 75{/color}", ["kitchen_night7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 76{/color}", ["kitchen_night8"]))
    gallery_items.append(GalleryItem("{color=#000}Image 77{/color}", ["kitchenaffection_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 78{/color}", ["kitchenaffection_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 79{/color}", ["kitchenaffection_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 83{/color}", ["kitchentalk_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 84{/color}", ["pizza_kitchen"]))
    gallery_items.append(GalleryItem("{color=#000}Image 85{/color}", ["popcorn_kitchen"]))
    gallery_items.append(GalleryItem("{color=#000}Image 86{/color}", ["sandwich_kitchen"]))
    gallery_items.append(GalleryItem("{color=#000}Image 87{/color}", ["lr_affection1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 88{/color}", ["lr_affection2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 89{/color}", ["lr_affection3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 90{/color}", ["lr_talk1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 91{/color}", ["lr_talk2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 92{/color}", ["bear_gift"]))
    gallery_items.append(GalleryItem("{color=#000}Image 93{/color}", ["booters_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 94{/color}", ["booters_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 95{/color}", ["booters_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 96{/color}", ["booters_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 97{/color}", ["booters_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 98{/color}", ["booters_6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 99{/color}", ["booters_7"]))
    gallery_items.append(GalleryItem("{color=#000}Image 100{/color}", ["booters_45"]))
    gallery_items.append(GalleryItem("{color=#000}Image 101{/color}", ["catlingerie_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 102{/color}", ["catlingerie_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 103{/color}", ["catlingerie_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 104{/color}", ["catlingerie_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 105{/color}", ["catlingerie_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 106{/color}", ["console_gift"]))
    gallery_items.append(GalleryItem("{color=#000}Image 107{/color}", ["furry_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 108{/color}", ["furry_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 109{/color}", ["furry_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 110{/color}", ["panties_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 111{/color}", ["panties_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 112{/color}", ["panties_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 113{/color}", ["panties_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 114{/color}", ["panties_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 115{/color}", ["panties_6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 116{/color}", ["plug_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 118{/color}", ["plug_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 119{/color}", ["wine_1"]))
    gallery_items.append(GalleryItem("{color=#000}Image 120{/color}", ["wine_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 121{/color}", ["wine_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 122{/color}", ["wine_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 123{/color}", ["dildo_2"]))
    gallery_items.append(GalleryItem("{color=#000}Image 124{/color}", ["dildo_3"]))
    gallery_items.append(GalleryItem("{color=#000}Image 125{/color}", ["dildo_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 126{/color}", ["dildo_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 127{/color}", ["dildo_6"]))
    gallery_items.append(GalleryItem("{color=#000}Image 128{/color}", ["ghost_4"]))
    gallery_items.append(GalleryItem("{color=#000}Image 128{/color}", ["ghost_5"]))
    gallery_items.append(GalleryItem("{color=#000}Image 129{/color}", ["ghost_6"]))




image lockedthumb = im.Scale("images/gallery/thumbs/tgallery0.jpg", 384, 216)

