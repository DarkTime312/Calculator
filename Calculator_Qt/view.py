import sys

from PySide6.QtWidgets import QWidget, QApplication

from Calculator_dark_ui import Ui_CalculatorDarkView
from Calculator_light_ui import Ui_CalculatorLightView


class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()
        self.view = Ui_CalculatorLightView()
        self.view.setupUi(self)
