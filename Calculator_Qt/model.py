from typing import Literal

from enums import *


class CalculatorModel:
    def __init__(self):
        super().__init__()

        self.last_action_was_equal = False

    def perform_operation(self,
                          operator: Literal['+', '-', '*', '/'],
                          last_input_num,
                          current_formula
                          ) -> str | bool:
        """
        Process a mathematical operation and update the calculator's state.

        This method handles the logic when a mathematical operator (+, -, *, /) is pressed.
        It updates the current formula and prepares the calculator for the next input.

        Parameters:
        operator (Literal['+', '-', '*', '/']): The mathematical operator that was pressed.

        Returns:
        None

        Behavior:
        - If there's no current formula or the last action was '=', start a new operation.
        - If the formula ends with an operator and there's no new input, replace the last operator.
        - Otherwise, append the new number and operator to the existing formula.
        """

        # Don't do anything if at the start
        # user presses math button without any input
        if last_input_num == '0' and not current_formula:
            return False

        # Check if the formula ends with an operator
        formula_ends_with_operator: bool = bool(current_formula) and current_formula[-1] in MATH_OPERATIONS

        # Check if we're overwriting the last operator (no new number input)
        overwrote_operator: bool = formula_ends_with_operator and last_input_num == ''

        # Handle different scenarios
        if not current_formula or self.last_action_was_equal:
            # Start a new operation
            final_result: str = last_input_num + SPACE + operator
            self.last_action_was_equal = False
        elif overwrote_operator:
            # Replace the last operator
            final_result: str = current_formula[:-1] + operator
        else:
            # Append new number and operator to existing formula
            final_result: str = current_formula + SPACE + last_input_num + SPACE + operator

        return final_result
