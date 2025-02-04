# src/game/item.py

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def use(self, player):
        # Example item usage
        if self.effect == "heal":
            player.health += 20
            if player.health > 100:
                player.health = 100
