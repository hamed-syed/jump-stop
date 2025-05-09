from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer, Qt
from H_syed_jump_stop_logic import GameLogic
from PyQt6.QtGui import QPainter

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("H_syed_jump_stop_gui.ui", self)
        self.setWindowTitle("Jump Stop")
        self.setGeometry(300, 300, 800, 400)

        self.game_logic = GameLogic(self.width(), self.height())
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)

        self.start_btn.clicked.connect(self.start_game)

    def start_game(self):
        self.start_btn.hide()
        self.instructions_label.hide()
        self.timer.start(30)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.game_logic.jump()

    def update_game(self):
        self.game_logic.update()
        self.score_label.setText(f"Score: {self.game_logic.score} | High Score: {self.game_logic.high_score}")
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.game_logic.draw(painter)