from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

# Параметры шутки
MAX_WINDOWS = 200
INITIAL_SPAWN = 2
SPAWN_ON_CLOSE = 15
SPAWN_DELAY_MS = 200
_total_created = 0
_alive_windows = []


class JokeWindow(QMainWindow):
    def __init__(self, idx):
        super().__init__()
        global _total_created
        _total_created += 1
        self.idx = idx
        self.setWindowTitle(f"Шутка #{idx}")
        self.setFixedSize(240, 110)

        lbl = QtWidgets.QLabel(f"game {idx} 😄\ndo u want to play?",
                               parent=self, alignment=QtCore.Qt.AlignCenter)
        self.setCentralWidget(lbl)

        screen = QApplication.primaryScreen().size()
        w, h = 240, 110
        x = random.randint(0, max(0, screen.width() - w))
        y = random.randint(0, max(0, screen.height() - h - 40))
        self.move(x, y)

    def closeEvent(self, event):
        spawn_after_close(SPAWN_ON_CLOSE)
        try:
            _alive_windows.remove(self)
        except ValueError:
            pass
        event.accept()


def spawn_windows(count):
    global _total_created, _alive_windows
    created = []
    for _ in range(count):
        if _total_created >= MAX_WINDOWS:
            break
        idx = _total_created + 1
        w = JokeWindow(idx)
        _alive_windows.append(w)
        w.show()
        created.append(w)
    return created


def spawn_after_close(count):
    remaining = MAX_WINDOWS - _total_created
    to_spawn = min(count, remaining)
    if to_spawn <= 0:
        return
    QtCore.QTimer.singleShot(SPAWN_DELAY_MS, lambda: spawn_windows(to_spawn))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Games")

        label = QtWidgets.QLabel("Game№1", parent=self)
        label.move(50, 50)

    def closeEvent(self, event):
        self.hide()
        spawn_windows(INITIAL_SPAWN)
        event.ignore()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
