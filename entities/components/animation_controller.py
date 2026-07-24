class AnimationController:

    def __init__(self, animations):

        self.animations = animations

        self.current_animation = "idle"
        self.current_frame = 0

        self.animation_speeds = {
            "idle": 0.13,
            "caminar": 0.2,
            "saltar": 0.35,
            "golpe": 0.25,
            "patada": 0.3,
            "cubrirse": 0.3,
            "recibir_golpe": 0.18,
            "derrota": 0.15,
            "victoria": 0.15
        }


    def update(self, blocking=False):

        frames = self.animations[
            self.current_animation
        ]

        speed = self.animation_speeds.get(
            self.current_animation,
            0.15
        )

        self.current_frame += speed

        if self.current_animation in [
            "victoria",
            "derrota"
        ]:

            if self.current_frame >= len(frames):
                self.current_frame = len(frames) - 1

            return False

        if self.current_animation == "cubrirse":

            if self.current_frame >= len(frames):

                if blocking:
                    self.current_frame = len(frames) - 1

                    return False

                else:
                    return True


        if self.current_frame >= len(frames):
            self.current_frame = 0
            return True


        return False



    def change_animation(self, animation):

        if self.current_animation in [
            "victoria",
            "derrota"
        ]:
            return


        if self.current_animation != animation or animation == "saltar":
            self.current_animation = animation
            self.current_frame = 0


    def get_image(self):

        frames = self.animations[
            self.current_animation
        ]

        return frames[
            int(self.current_frame)
        ]


    def get_current_animation(self):

        return self.current_animation