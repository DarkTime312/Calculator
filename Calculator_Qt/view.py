import sys
from typing import Literal
from functools import partial

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QApplication, QPushButton
from hPyT import *

from Calculator_dark_ui import Ui_CalculatorDarkView
from Calculator_light_ui import Ui_CalculatorLightView

# Constants
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 50
NORMAL_FONT_SIZE = 25

INPUT_LENGTH_THRESHOLD = 6
RESULT_LENGTH_THRESHOLD = 20
INPUT_FONT_REDUCTION = 30
RESULT_FONT_REDUCTION = 10

MATH_OPERATIONS = '+-*/'
SPACE = ' '


def humanize_int_numbers(str_num: str, reverse=False) -> str:
    """
    Format or unformat integer strings by adding or removing thousands separators.

    This function handles both humanization (adding commas as thousands separators)
    and dehumanization (removing commas) of integer strings. It leaves float strings unchanged.

    Parameters:
    str_num (str): The string representation of the number to be processed.
    reverse (bool, optional): If False (default), humanizes the number by adding commas.
                              If True, dehumanizes by removing commas.

    Returns:
    str: The processed string representation of the number.

    Examples:
    >>> humanize_int_numbers("1000000")
    '1,000,000'
    >>> humanize_int_numbers("1,000,000", reverse=True)
    '1000000'
    >>> humanize_int_numbers("1000.5")
    '1000.5'
    >>> humanize_int_numbers("1,000.5", reverse=True)
    '1,000.5'
    """
    # If it's a float, return it unchanged
    if '.' in str_num:
        return str_num
    else:  # If it's an integer
        if reverse:  # Dehumanize: remove commas
            return str_num.replace(',', '')
        else:  # Humanize: add commas
            return f'{int(str_num):,}'


def normalize_numeric_type(num: int | float) -> str:
    """
    Normalize a numeric value to a string representation.

    This function takes a numeric input (integer or float) and returns a string
    representation. For integer values or floats that are whole numbers, it
    returns the number as an integer string. For non-whole floats, it simply
    returns it as string.

    Args:
        num (int | float): The numeric value to normalize.

    Returns:
        str: A string representation of the normalized number.

    Examples:
        >>> normalize_numeric_type(5)
        '5'
        >>> normalize_numeric_type(3.0)
        '3'
    """
    # Check if the number is an integer or a whole float
    if num.is_integer():
        # Convert to integer and then to string
        return str(int(num))
    return str(num)


class CalculatorView(QWidget):
    def __init__(self, theme: Literal['dark', 'light']):
        super().__init__()
        self.ui = None
        self.apply_theme(theme)
        self.setWindowTitle(' ')
        self.buttons_disabled = False  # state of buttons
        self.last_action_was_equal = False

        self.connect_events()

    def apply_theme(self, theme):
        if theme == 'light':
            self.ui = Ui_CalculatorLightView()
            title_bar_color.set(self, '#f3f3f3')  # sets the titlebar color to white
        elif theme == 'dark':
            self.ui = Ui_CalculatorDarkView()
            title_bar_color.set(self, '#000000')  # sets the titlebar color to black

        self.ui.setupUi(self)

    def connect_events(self):
        # Connect signals to slots
        for btn in self.findChildren(QPushButton):
            btn_text = btn.text()
            if btn_text in set('0123456789'):
                btn.clicked.connect(partial(self.press_num, btn_text))

        self.ui.btn_dot.clicked.connect(partial(self.press_num, '.'))

        self.ui.btn_ac.clicked.connect(self.reset_view)
        self.ui.btn_change_sign.clicked.connect(self.switch_sign)
        self.ui.btn_percent.clicked.connect(self.convert_to_percent)
        self.ui.btn_plus.clicked.connect(partial(self.math_operation, '+'))
        self.ui.btn_minus.clicked.connect(partial(self.math_operation, '-'))
        self.ui.btn_multiply.clicked.connect(partial(self.math_operation, '*'))
        self.ui.btn_divide.clicked.connect(partial(self.math_operation, '/'))
        self.ui.btn_equal.clicked.connect(self.evaluate_expression)

    def adjust_display_font(self, *,
                            input_text: str | None = None,
                            result_text: str | None = None) -> None:
        """
        Adjust the font size of the input and result displays based on the length of the text.

        This method dynamically resizes the font to ensure that long numbers or expressions
        fit within the display area. It handles both the input display and the result display separately.

        Parameters:
        input_text (str | None): The text to be displayed in the input field. If None, input display is not adjusted.
        result_text (str | None): The text to be displayed in the result field. If None, result display is not adjusted.

        Returns:
        None

        Behavior:
        - For the input display:
          - Starts reducing font size when text length exceeds INPUT_LENGTH_THRESHOLD
          - Reduces font size by 15 points for every 3 characters over the threshold
          - Minimum font size is OUTPUT_FONT_SIZE - INPUT_FONT_REDUCTION
        - For the result display:
          - Starts reducing font size when text length exceeds RESULT_LENGTH_THRESHOLD
          - Reduces font size by 10 points for every 3 characters over the threshold
          - Minimum font size is NORMAL_FONT_SIZE - RESULT_FONT_REDUCTION
        """
        # Adjust input display font size
        if input_text:
            # Calculate new font size based on input text length
            new_size = OUTPUT_FONT_SIZE - (max(0, len(input_text) - INPUT_LENGTH_THRESHOLD) // 3) * 15
            # Ensure font size doesn't go below the minimum
            new_size = max(new_size, OUTPUT_FONT_SIZE - INPUT_FONT_REDUCTION)
            # Apply new font size to input label
            self.ui.lbl_big.setFont(QFont(FONT, int(new_size)))

        # Adjust result display font size
        if result_text:
            # Calculate new font size based on result text length
            new_size = NORMAL_FONT_SIZE - (max(0, len(result_text) - RESULT_LENGTH_THRESHOLD) // 3) * 10
            # Ensure font size doesn't go below the minimum
            new_size = max(new_size, NORMAL_FONT_SIZE - RESULT_FONT_REDUCTION)
            # Apply new font size to result label
            self.ui.lbl_small.setFont(QFont(FONT, int(new_size)))

    def press_num(self, pressed_num: str) -> None:
        """
        Process a number or decimal point pressed on the calculator.

        This method handles the logic for adding a digit or decimal point
        to the current number displayed in the calculator's input field.

        Parameters:
        pressed_num (str): The digit or decimal point that was pressed.

        Returns:
        None

        Behavior:
        - If a decimal point is pressed when one already exists or the input is empty, it's ignored.
        - If '0' is the current input and a non-decimal digit is pressed, the '0' is replaced.
        - In all other cases, the pressed number is appended to the current input.
        - The input is always displayed with proper thousands separators.
        """
        # Remove formatting from the current number for processing
        current_num: str = humanize_int_numbers(self.ui.lbl_big.text(), reverse=True)

        # Check for existing decimal point and empty input
        already_has_decimal: bool = '.' in current_num
        input_is_empty: bool = current_num == ''

        # Handle special cases for decimal point
        if pressed_num == '.' and (already_has_decimal or input_is_empty):
            return  # Ignore additional decimal points or decimal at start
        elif current_num == '0' and pressed_num != '.':
            current_num: str = ''  # Replace leading zero with new digit

        # Append the pressed number to the current number
        new_num: str = current_num + pressed_num
        # Adjust the font size so the text fit
        self.adjust_display_font(input_text=new_num)
        # Update the input field with the new number, properly formatted
        self.ui.lbl_big.setText(humanize_int_numbers(new_num))

    def math_operation(self, operator: Literal['+', '-', '*', '/']) -> None:
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
        # Get the last input number without formatting
        last_input_num: str = humanize_int_numbers(self.ui.lbl_big.text(), reverse=True)
        # Get the current formula from the result display
        current_formula: str = self.ui.lbl_small.text()

        # Don't do anything if at the start
        # user presses math button without any input
        if last_input_num == '0' and not current_formula:
            return

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

        # Clear the input field
        self.ui.lbl_big.setText('')
        # Adjust the font size so the text fit
        self.adjust_display_font(result_text=final_result)
        # Update the result display with the new formula
        self.ui.lbl_small.setText(final_result)

    def reset_view(self) -> None:
        if self.buttons_disabled:
            self.change_buttons_state(disabled=False)
        # Reset the input field to '0'
        self.ui.lbl_big.setText('0')
        # Clear the result display
        self.ui.lbl_small.setText('')
        # Change the font size of the labels back to default size
        self.ui.lbl_big.setFont(QFont(FONT, OUTPUT_FONT_SIZE))
        self.ui.lbl_small.setFont(QFont(FONT, NORMAL_FONT_SIZE))

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
        last_input_number: str = humanize_int_numbers(self.ui.lbl_big.text(), reverse=True)
        # Get the previous formula from the result display
        prev_formula: str = self.ui.lbl_small.text()

        if self.last_action_was_equal:
            # If the last action was '=', set the result to the last input number
            self.ui.lbl_small.setText(last_input_number)
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
                self.ui.lbl_small.setText("Cannot divide by zero")
                self.change_buttons_state(disabled=True)
                return

            # Format the result
            rounded_and_normalized: str = normalize_numeric_type(round(result, 3))
            # Adjust font size for input text
            self.adjust_display_font(input_text=rounded_and_normalized)
            self.ui.lbl_big.setText(humanize_int_numbers(rounded_and_normalized))

            # Adjust the font size for formula text
            self.adjust_display_font(result_text=final_formula)
            # Update the result display with the full formula
            self.ui.lbl_small.setText(final_formula)
            # Mark that the last action was '='
            self.last_action_was_equal: bool = True

    def change_buttons_state(self, disabled: bool = True) -> None:
        """
        Change the state of all calculator buttons except the 'AC' button.

        Args:
        disabled (bool): If True, disable buttons; if False, enable buttons.

        Returns:
        None
        """

        for btn in self.findChildren(QPushButton):
            if btn.text() != 'AC':
                btn.setDisabled(disabled)

        self.buttons_disabled: bool = disabled

    def switch_sign(self) -> None:
        """
        Toggle the sign of the current number in the input field.

        This method changes the sign of the number currently displayed
        in the calculator's input field. It performs the following actions:
        1. If the number is positive, it adds a minus sign.
        2. If the number is negative, it removes the minus sign.
        3. If the number is zero, it does nothing.
        """
        # Get the current number from the input field
        current_num: str = self.ui.lbl_big.text()

        # Check if the number is already negative
        already_is_negative: bool = current_num.startswith('-')

        if already_is_negative:
            # If negative, remove the minus sign
            new_num: str = current_num.removeprefix('-')
        elif current_num != '0':
            # If positive and not zero, add a minus sign
            new_num: str = '-' + current_num
        else:
            # If the number is 0, do nothing and exit the function
            return

        # Update the input field with the new number
        self.ui.lbl_big.setText(new_num)

    def convert_to_percent(self) -> None:
        """
        Convert the current input number to its percentage representation.

        This method performs the following actions:
        1. Retrieves the current input number, removing any formatting.
        2. If the input is not '0' or empty, it divides the number by 100.
        3. Updates the input field with the new percentage value.

        The function does nothing if the current input is '0' or an empty string.
        """
        # Remove formatting from the current input number
        current_input_num: str = humanize_int_numbers(self.ui.lbl_big.text(), reverse=True)

        # Only process if the input is not '0' and not empty
        if current_input_num and current_input_num != '0':
            # Convert to float and divide by 100 to get percentage
            new_num: float = float(current_input_num) / 100
            # Update the input field with the new percentage value, properly formatted
            self.ui.lbl_big.setText(normalize_numeric_type(new_num))

    # def change_buttons_state(self, disabled: bool = True) -> None:
    #     """
    #     Change the state of all calculator buttons except the 'AC' button.
    #
    #     Args:
    #     disabled (bool): If True, disable buttons; if False, enable buttons.
    #
    #     Returns:
    #     None
    #     """
    #     new_state: str = 'disabled' if disabled else 'normal'
    #
    #     for widget in self.winfo_children():
    #         if widget.cget('text') != 'AC':
    #             widget.configure(state=new_state)
    #
    #     self.buttons_disabled: bool = disabled
