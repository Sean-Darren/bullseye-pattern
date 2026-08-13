from core.vision_engine import visionEngine
from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("financial chart pattern computer vision")
        self.resize(1100, 800)

        self.vision_engine = visionEngine()