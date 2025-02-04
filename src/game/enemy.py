# src/game/enemy.py

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        # Example enemy attack
        player.health -= self.attack_power
        return player.health
