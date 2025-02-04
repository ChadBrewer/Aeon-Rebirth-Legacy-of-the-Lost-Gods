# src/settings.py

class Settings:
    def __init__(self):
        # Example settings (you can adjust these as per your game)
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)  # Black background
        self.fps = 60

    def update_settings(self, screen_width=None, screen_height=None, bg_color=None):
        if screen_width: self.screen_width = screen_width
        if screen_height: self.screen_height = screen_height
        if bg_color: self.bg_color = bg_color
