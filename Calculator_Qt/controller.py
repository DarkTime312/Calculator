from typing import Literal

from view import CalculatorView


class CalculatorController:
    def __init__(self, theme: Literal['dark', 'light']):
        super().__init__()

        self.view = CalculatorView(theme)
