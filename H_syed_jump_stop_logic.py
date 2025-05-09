from PyQt6.QtGui import QPainter, QColor
import os

class GameLogic:
    def __init__(self, screen_width: int, screen_height: int):
        self.width = screen_width
        self.height = screen_height
        self.player_x = 100
        self.player_y = self.height - 50
        self.jump_height = 100
        self.gravity = 5
        self.velocity_y = 0
        self.is_jumping = False
        self.obstacles = []
        self.score = 0
        self.high_score = self.load_high_score()

    def jump(self) -> None:
        if not self.is_jumping:
            self.velocity_y = -22
            self.is_jumping = True

    def update(self) -> None:
        self.velocity_y += self.gravity
        self.player_y += self.velocity_y
        if self.player_y >= self.height - 50:
            self.player_y = self.height - 50
            self.velocity_y = 0
            self.is_jumping = False
        for obs in self.obstacles:
            obs['x'] -= 10
        if len(self.obstacles) == 0 or self.obstacles[-1]['x'] < self.width - 300:
            self.obstacles.append({'x': self.width, 'y': self.height - 50})
        self.obstacles = [o for o in self.obstacles if o['x'] > 0]
        for obs in self.obstacles:
            if abs(self.player_x - obs['x']) < 30 and abs(self.player_y - obs['y']) < 30:
                self.save_high_score()
                self.score = 0
                self.obstacles.clear()
                break
        self.score += 1
        self.high_score = max(self.high_score, self.score)

    def draw(self, painter: QPainter) -> None:
        painter.setBrush(QColor("blue"))
        painter.drawRect(self.player_x, self.player_y, 30, 30)
        painter.setBrush(QColor("red"))
        for obs in self.obstacles:
            painter.drawRect(obs['x'], obs['y'], 30, 30)

    def load_high_score(self) -> int:
        try:
            if os.path.exists("H_syed_jump_stop_score.txt"):
                with open("H_syed_jump_stop_score.txt", "r") as f:
                    return int(f.read().strip())
        except:
            pass
        return 0

    def save_high_score(self) -> None:
        try:
            with open("H_syed_jump_stop_score.txt", "w") as f:
                f.write(str(self.high_score))
        except:
            pass