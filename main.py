import customtkinter as ctk
from settings import *
from buttons import NumButton, Button, MathButton
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
        self.start_from_beginning = False

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
        self.equal = MathButton(self, '=', command=self.equal)

    def press_num(self, pressed_num):
        current_num = humanize_int_numbers(self.input_num.get(), reverse=True)
        if current_num == '0' and pressed_num != '.':
            current_num = ''
        elif pressed_num == '.' and ('.' in current_num or current_num == ''):
            return

        new_num = current_num + pressed_num
        self.input_num.set(humanize_int_numbers(new_num))

    def clear(self):
        self.input_num.set('0')
        self.result_var.set('')

    def change_sign(self):
        current_num: str = self.input_num.get()
        is_negative: bool = '-' in current_num

        if is_negative:
            new_num = current_num.removeprefix('-')
            self.input_num.set(new_num)
        elif current_num != '0':
            new_num = '-' + current_num
            self.input_num.set(new_num)

    def convert_to_percent(self):
        current_num: str = humanize_int_numbers(self.input_num.get(), reverse=True)
        if current_num != '0':
            new_num: float = float(current_num) / 100
            self.input_num.set(str(new_num))

    def math_operation(self, operator):
        input_num: str = humanize_int_numbers(self.input_num.get(), reverse=True)
        result_num: str = self.result_var.get()
        if not result_num or self.start_from_beginning:  # first time
            final_result = str(input_num) + ' ' + str(operator)
            self.start_from_beginning = False
        elif result_num[-1] in set('+-*/') and input_num == '':
            final_result = result_num[:-1] + operator
        else:  # other times
            final_result = str(result_num) + ' ' + str(input_num) + ' ' + str(operator)
        self.input_num.set(value='')
        self.result_var.set(value=final_result)

    def equal(self):
        input_num: str = humanize_int_numbers(self.input_num.get(), reverse=True)
        result_num: str = self.result_var.get()

        if input_num and not self.start_from_beginning:
            the_formula = result_num + ' ' + input_num
            result = eval(the_formula)

            self.input_num.set(value=humanize_int_numbers(normalize_numeric_type(round(result, 3))))
            self.result_var.set(value=the_formula)
            self.start_from_beginning = True
        elif self.start_from_beginning:
            self.result_var.set(value=input_num)


# is_dark = darkdetect.isDark()
app = Calculator(is_dark=True)
app.mainloop()
