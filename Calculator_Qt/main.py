import sys

from PySide6.QtWidgets import QApplication

from controller import CalculatorController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorController('dark')
    window.view.show()
    sys.exit(app.exec())
