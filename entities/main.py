import sys
from PyQt6.QtWidgets import QApplication
from entities.graphics import VideoGraphics

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoGraphics()
    window.show()
    app.exec()