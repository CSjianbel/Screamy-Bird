class GameStatus:
    def __init__(self):
        self.is_game_over = False
        self.is_game_started = False
        self.is_game_idle = True

    def set_game_over(self):
        self.is_game_over = True
        self.is_game_started = False
        self.is_game_idle = False

    def set_game_started(self):
        self.is_game_over = False
        self.is_game_started = True
        self.is_game_idle = False

    def set_game_idle(self):
        self.is_game_over = False
        self.is_game_started = False
        self.is_game_idle = True