import customtkinter as ctk
from settings import *
from buttons import NumButton, Button, MathButton
from typing import Literal
import darkdetect


def normalize_numeric_type(num: int | float) -> str:
    """
    Converts a numeric value to its string representation, removing unnecessary decimal points.

    This function takes an integer or float as input and returns a string representation.
    If the input is a float that represents a whole number (e.g., 5.0), it removes the decimal point and trailing zero.

    Parameters:
    num (int | float): The number to be normalized.

    Returns:
    str: A string representation of the number. For whole numbers, it returns the integer representation without decimal point.

    Examples:
    >>> normalize_numeric_type(5.0)
    '5'
    >>> normalize_numeric_type(5.5)
    '5.5'
    >>> normalize_numeric_type(10)
    '10'
    """
    number_as_string = str(num)
    if number_as_string.endswith('.0'):
        return number_as_string.removesuffix('.0')

    return number_as_string


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


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color=BLACK if is_dark else WHITE)
        ctk.set_appearance_mode('dark' if is_dark else 'light')
        self.is_dark = is_dark
        # window setup
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.title('')
        self.iconbitmap('empty.ico')
        self.last_action_was_equal = False
        self.buttons_disabled = False

        self.window_layout()
        # vars
        self.input_num = ctk.StringVar(value='0')
        self.result_var = ctk.StringVar(value='')

        self.create_widgets()

    def window_layout(self):
        """
        Sets the window layout using grid manager.
        """
        for index in range(MAIN_ROWS):
            self.rowconfigure(index, weight=1, uniform='a')

        for index in range(MAIN_COLUMNS):
            self.columnconfigure(index, weight=1, uniform='a')

    def create_widgets(self):
        font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        font_large = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        self.top_output_label = ctk.CTkLabel(self,
                                            font=font,
                                            textvariable=self.result_var,
                                            text_color=WHITE if self.is_dark else BLACK)
        self.top_output_label.grid(row=0, column=0, columnspan=4, sticky='se', padx=10)

        self.input_label = ctk.CTkLabel(self,
                                        font=font_large,
                                        textvariable=self.input_num,
                                        text_color=WHITE if self.is_dark else BLACK)
        self.input_label.grid(row=1, column=0, columnspan=4, sticky='e', padx=10)

        # Create number buttons
        self.num_0 = NumButton(self, num=0, command=lambda: self.press_num('0'))
        self.num_1 = NumButton(self, num=1, command=lambda: self.press_num('1'))
        self.num_2 = NumButton(self, num=2, command=lambda: self.press_num('2'))
        self.num_3 = NumButton(self, num=3, command=lambda: self.press_num('3'))
        self.num_4 = NumButton(self, num=4, command=lambda: self.press_num('4'))
        self.num_5 = NumButton(self, num=5, command=lambda: self.press_num('5'))
        self.num_6 = NumButton(self, num=6, command=lambda: self.press_num('6'))
        self.num_7 = NumButton(self, num=7, command=lambda: self.press_num('7'))
        self.num_8 = NumButton(self, num=8, command=lambda: self.press_num('8'))
        self.num_9 = NumButton(self, num=9, command=lambda: self.press_num('9'))
        self.num_dot = NumButton(self, num='.', command=lambda: self.press_num('.'))

        # other buttons
        self.clear_btn = Button(self, text='clear', command=self.clear)
        self.invert_btn = Button(self, text='invert', command=self.change_sign)
        self.percent_btn = Button(self, text='percent', command=self.convert_to_percent)

        # math buttons
        self.divide = MathButton(self, '/', command=lambda: self.math_operation('/'))
        self.multiply = MathButton(self, '*', command=lambda: self.math_operation('*'))
        self.minus = MathButton(self, '-', command=lambda: self.math_operation('-'))
        self.plus = MathButton(self, '+', command=lambda: self.math_operation('+'))
        self.equal = MathButton(self, '=', command=self.evaluate_expression)

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
        current_num = humanize_int_numbers(self.input_num.get(), reverse=True)

        # Check for existing decimal point and empty input
        already_has_decimal: bool = '.' in current_num
        input_is_empty: bool = current_num == ''

        # Handle special cases for decimal point
        if pressed_num == '.' and (already_has_decimal or input_is_empty):
            return  # Ignore additional decimal points or decimal at start
        elif current_num == '0' and pressed_num != '.':
            current_num = ''  # Replace leading zero with new digit

        # Append the pressed number to the current number
        new_num = current_num + pressed_num

        # Update the input field with the new number, properly formatted
        self.input_num.set(humanize_int_numbers(new_num))

    def clear(self) -> None:
        """
        Clear the calculator's current input and result display.

        This method performs the following actions:
        1. Re-enables all buttons if they were previously disabled.
        2. Resets the input field to '0'.
        3. Clears the result display.

        This effectively resets the calculator's visible state and functionality,
        preparing it for a new calculation. It also ensures that all buttons
        are operational after clearing, which is particularly useful if they
        were disabled due to an error condition.

        Returns:
        None
        """
        if self.buttons_disabled:
            self.change_buttons_state(disabled=False)
        # Reset the input field to '0'
        self.input_num.set('0')
        # Clear the result display
        self.result_var.set('')

    def change_sign(self) -> None:
        """
        Toggle the sign of the current number in the input field.

        This method changes the sign of the number currently displayed
        in the calculator's input field. It performs the following actions:
        1. If the number is positive, it adds a minus sign.
        2. If the number is negative, it removes the minus sign.
        3. If the number is zero, it does nothing.
        """
        # Get the current number from the input field
        current_num: str = self.input_num.get()

        # Check if the number is already negative
        already_is_negative: bool = '-' in current_num

        if already_is_negative:
            # If negative, remove the minus sign
            new_num = current_num.removeprefix('-')
        elif current_num != '0':
            # If positive and not zero, add a minus sign
            new_num = '-' + current_num
        else:
            # If the number is 0, do nothing and exit the function
            return

        # Update the input field with the new number
        self.input_num.set(new_num)

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
        current_input_num: str = humanize_int_numbers(self.input_num.get(), reverse=True)

        # Only process if the input is not '0' and not empty
        if current_input_num != '0' and current_input_num != '':
            # Convert to float and divide by 100 to get percentage
            new_num: float = float(current_input_num) / 100
            # Update the input field with the new percentage value, properly formatted
            self.input_num.set(normalize_numeric_type(new_num))

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
        last_input_num: str = humanize_int_numbers(self.input_num.get(), reverse=True)
        # Get the current formula from the result display
        current_formula: str = self.result_var.get()

        # Check if the formula ends with an operator
        formula_ends_with_operator: bool = bool(current_formula) and current_formula[-1] in MATH_OPERATIONS

        # Check if we're overwriting the last operator (no new number input)
        overwrote_operator: bool = formula_ends_with_operator and last_input_num == ''

        # Handle different scenarios
        if not current_formula or self.last_action_was_equal:
            # Start a new operation
            final_result = last_input_num + SPACE + operator
            self.last_action_was_equal = False
        elif overwrote_operator:
            # Replace the last operator
            final_result = current_formula[:-1] + operator
        else:
            # Append new number and operator to existing formula
            final_result = current_formula + SPACE + last_input_num + SPACE + operator

        # Clear the input field
        self.input_num.set(value='')
        # Update the result display with the new formula
        self.result_var.set(value=final_result)

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
        last_input_number: str = humanize_int_numbers(self.input_num.get(), reverse=True)
        # Get the previous formula from the result display
        prev_formula: str = self.result_var.get()

        if self.last_action_was_equal:
            # If the last action was '=', set the result to the last input number
            self.result_var.set(value=last_input_number)
        elif not last_input_number:
            # If there's no new input, do nothing
            return

        else:
            # Combine previous formula with the last input number
            final_formula = prev_formula + SPACE + last_input_number
            try:
                # Attempt to evaluate the formula
                result = eval(final_formula)
            except (SyntaxError, ZeroDivisionError):
                # Handle division by zero or syntax errors
                self.result_var.set("Cannot divide by zero")
                self.change_buttons_state(disabled=True)
                return

            # Format and display the result
            self.input_num.set(value=humanize_int_numbers(normalize_numeric_type(round(result, 3))))
            # Update the result display with the full formula
            self.result_var.set(value=final_formula)
            # Mark that the last action was '='
            self.last_action_was_equal = True

    def change_buttons_state(self, disabled: bool = True) -> None:
        """
        Change the state of all calculator buttons except the 'AC' button.

        Args:
        disabled (bool): If True, disable buttons; if False, enable buttons.

        Returns:
        None
        """
        for widget in self.winfo_children():
            if widget.cget('text') != 'AC':
                widget.configure(state='disabled' if disabled else 'normal')
                self.buttons_disabled = True


# is_dark = darkdetect.isDark()
app = Calculator(is_dark=True)
app.mainloop()
