from classes.AnimSprite import AnimSprite


class Player(AnimSprite):
    def __init__(self, file_name, frame_width=None, frame_height=None, anim_speed=0, speed=2):
        super().__init__(file_name, frame_width, frame_height, anim_speed, speed)
        self.spawn_pos = (625, 22)
        self.reset()

    def reset(self):
        self.rect.topleft = self.spawn_pos