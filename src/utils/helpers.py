# src/utils/helpers.py

class HelperFunctions:
    @staticmethod
    def display_message(message, color=(255, 255, 255)):
        # Example helper function for displaying messages on screen
        print(f"Message: {message} - Color: {color}")

    @staticmethod
    def calculate_damage(attack_power, defense):
        # Example helper function to calculate damage
        return max(0, attack_power - defense)
