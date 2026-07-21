class MovementController:

    def __init__(
        self,
        speed,
        gravity,
        ground
    ):

        self.speed = speed
        self.gravity = gravity
        self.ground = ground

        self.velocity_y = 0
        self.jumping = False


    def move_left(self, player):

        player.x -= self.speed

        if player.x < 0:
            player.x = 0


    def move_right(self, player):

        player.x += self.speed

        if player.x > player.game.ancho - player.width:
            player.x = player.game.ancho - player.width


    def jump(self):

        if not self.jumping:

            self.velocity_y = -18
            self.jumping = True



    def update(self, player):

        if self.jumping:

            self.velocity_y += self.gravity

            player.y += self.velocity_y


            if player.y >= self.ground:

                player.y = self.ground
                self.velocity_y = 0
                self.jumping = False