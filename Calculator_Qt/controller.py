from functools import partial
from typing import Literal

from view import CalculatorView
from model import CalculatorModel

from enums import *


class CalculatorController:
    def __init__(self, theme: Literal['dark', 'light']):
        super().__init__()

        self.view = CalculatorView(theme)
        self.model = CalculatorModel()

        self.view.ui.btn_plus.clicked.connect(partial(self.math_operation, '+'))
        self.view.ui.btn_minus.clicked.connect(partial(self.math_operation, '-'))
        self.view.ui.btn_multiply.clicked.connect(partial(self.math_operation, '*'))
        self.view.ui.btn_divide.clicked.connect(partial(self.math_operation, '/'))
        self.view.ui.btn_equal.clicked.connect(self.evaluate_expression)

    def math_operation(self, operation):
        # Get the last input number without formatting
        last_input_num: str = self.view.get_input_text()
        # Get the current formula from the result display
        current_formula: str = self.view.get_formula_text()

        final_result = self.model.perform_operation(operation, last_input_num, current_formula)
        if final_result:
            # Update the result display with the new formula
            self.view.set_formula_text(final_result)

            # Clear the input field
            self.view.set_input_text('')

    def evaluate_expression(self) -> None:
        """
        Evaluate the current mathematical expression and update the calculator's state.

        This method handles the following scenarios:
        1. If the last action was '=', it sets the result to the last input number.
        2. If there's no new input, it does nothing.
        3. Otherwise, it evaluates the full expression and updates the display.

        The method also handles errors such as division by zero, disabling buttons
        (except AC) when an error occurs.

        Returns:
        None
        """
        # Get the last input number without formatting
        last_input_number: str = self.view.get_input_text()
        # Get the previous formula from the result display
        prev_formula: str = self.view.get_formula_text()

        if self.model.last_action_was_equal:
            # If the last action was '=', set the result to the last input number
            self.view.set_formula_text(last_input_number)
        elif not last_input_number:
            # If there's no new input, do nothing
            return

        else:
            # Combine previous formula with the last input number
            final_formula: str = prev_formula + SPACE + last_input_number
            try:
                # Attempt to evaluate the formula
                result: int | float = eval(final_formula)
            except (SyntaxError, ZeroDivisionError):
                # Handle division by zero or syntax errors
                self.view.set_formula_text("Cannot divide by zero")
                self.view.change_buttons_state(disabled=True)
                return

            self.view.set_input_text(round(result, 3))

            # Update the result display with the full formula
            self.view.set_formula_text(final_formula)
            # Mark that the last action was '='
            self.model.last_action_was_equal = True
