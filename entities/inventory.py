from data.exam_items import EXAM_ITEMS


class Inventory:

    MAX_SLOTS = 3
    
    def __init__(self):

        self.slots = [
            None,
            None,
            None
        ]

        self.observers = []


    def add_observer(self, observer):

        if observer not in self.observers:
            self.observers.append(observer)


    def notify(self):

        for observer in self.observers:
            observer.update_inventory(
                self
            )


    def add_item(self, item):

        for index in range(self.MAX_SLOTS):

            if self.slots[index] is None:

                self.slots[index] = item

                self.notify()

                return True

        return False


    def remove_item(self, index):

        if index < 0 or index >= self.MAX_SLOTS:
            return None


        item = self.slots[index]


        if item:

            self.slots[index] = None

            self.notify()


        return item



    def use_item(self, index, player):

        item = self.remove_item(
            index
        )


        if item:


            # SI ES ITEM EXAMEN
            if item.name in EXAM_ITEMS:


                enemy = None


                if player == player.game.player1:

                    enemy = player.game.player2

                else:

                    enemy = player.game.player1



                categoria = EXAM_ITEMS[item.name]
                player.game.fight_state.question_box.start_question(
                    categoria,
                    player,
                    enemy
                )


            else:

                # ITEM NORMAL
                item.use(
                    player
                )



            player.game.resource_manager.get_sound(
                "usar_item"
            ).play()



    def get_items(self):

        return self.slots