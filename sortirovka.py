import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

class MainApp(QApplication):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.timer = QTimer(self) #self
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        self.count = 0

    def update(self):
        self.count += 1
        print ("update",self.count)
        if self.count >5:
            self.timer.stop()
            self.exit()

if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec())