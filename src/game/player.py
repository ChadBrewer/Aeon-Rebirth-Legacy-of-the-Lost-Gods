# src/game/player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, enemy):
        # Example attack function
        enemy.health -= self.attack_power
        return enemy.health

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
