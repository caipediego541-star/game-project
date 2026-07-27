from patterns.decorator.item_decorator import ItemDecorator

class ExamDecorator(ItemDecorator):
    def use(self, player):
        super().use(player)
        enemy = (
            player.game.player2
            if player == player.game.player1
            else player.game.player1)

        player.game.fight_state.question_box.start_question(
            self.item.materia,
            player,
            enemy)