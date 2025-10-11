import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtCore import Qt


class CounterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Concise Counter")
        self.setGeometry(100, 100, 350, 150)
        self.count = 0

        self.label = QLabel(f"Current Count: {self.count}")
        self.label.setStyleSheet("font-size: 24px;")

        self.inc_button = QPushButton("Increase")
        self.dec_button = QPushButton("Decrease")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.dec_button)
        button_layout.addWidget(self.inc_button)

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.inc_button.clicked.connect(lambda: self.change_count(1))
        self.dec_button.clicked.connect(lambda: self.change_count(-1))

    def change_count(self, delta):
        self.count += delta
        self.label.setText(f"Current Count: {self.count}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CounterApp()
    main_window.show()
    sys.exit(app.exec())

