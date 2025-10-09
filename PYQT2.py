import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)

# Создаем окно сообщения
msg = QMessageBox()
msg.setWindowTitle("System message")
msg.setText("Critical error")
msg.setIcon(QMessageBox.Critical)
msg.setStandardButtons(QMessageBox.Ok)

# Настроим немного внешний вид, чтобы было похоже на старый стиль
msg.setStyleSheet("""
    QMessageBox {
        background-color: #C0C0C0;  /* серый фон как в Win95 */
        font-family: 'MS Sans Serif';
        font-size: 10pt;
    }
    QPushButton {
        background-color: #E0E0E0;
        border: 1px solid #808080;
        min-width: 60px;
        min-height: 22px;
    }
    QPushButton:pressed {
        background-color: #A0A0A0;
    }
""")

msg.exec_()
