from PyQt6.QtWidgets import QApplication
from H_syed_jump_stop_gui_loader import GameWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())