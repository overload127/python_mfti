class Move:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.is_shot = False
        self.shot_x = 0
        self.shot_y = 0

    def up(self):
        self.x = 0
        self.y = -1

    def down(self):
        self.x = 0
        self.y = 1

    def left(self):
        self.x = -1
        self.y = 0

    def right(self):
        self.x = 1
        self.y = 0

    def dir(self, x, y):
        self.x = x
        self.y = y

    def shot(self, x, y):
        self.is_shot = True
        self.shot_x = x
        self.shot_y = y
