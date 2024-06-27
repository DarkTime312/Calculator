import customtkinter as ctk
from settings import *
from buttons import NumButton, Button, MathButton


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color=BLACK if is_dark else WHITE)
        ctk.set_appearance_mode('dark' if is_dark else 'light')
        self.is_dark = is_dark
        # window setup
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.title('')
        self.iconbitmap('empty.ico')

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

        self.top_output_label = OutputLabel(self, text='6 +', font=font, textvariable=self.result_var)
        self.top_output_label.grid(row=0, column=0, columnspan=4, sticky='se', padx=10)

        self.input_label = OutputLabel(self, font=font_large, textvariable=self.input_num)
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
        current_num = self.input_num.get()
        if current_num == '0' and pressed_num != '.':
            current_num = ''
        # if current_num == '0' and pressed_num == '.':
        #     current_num = ''
        elif pressed_num == '.' and '.' in current_num:
            return
        new_num = current_num + pressed_num
        self.input_num.set(new_num)

    def clear(self):
        self.input_num.set('0')
        self.result_var.set('')

    def change_sign(self):
        current_num: str = self.input_num.get()
        is_negative: bool = '-' in current_num

        if is_negative:
            new_num = current_num.removeprefix('-')
        else:
            new_num = '-' + current_num

        self.input_num.set(new_num)

    def convert_to_percent(self):
        current_num: str = self.input_num.get()
        if current_num != '0':
            new_num: float = float(current_num) / 100
            self.input_num.set(str(new_num))

    def math_operation(self, operator):
        input_num: str = self.input_num.get()
        self.input_num.set(value='')
        result_num: str = self.result_var.get()
        if not result_num:  # first time
            final_result = str(input_num) + ' ' + str(operator)
            print(final_result)
        else:  # other times
            final_result = str(result_num) + ' ' + str(input_num) + ' ' + str(operator)
            print(final_result)

        self.result_var.set(value=final_result)

    def equal(self):
        input_num: str = self.input_num.get()
        if input_num:
            result_num: str = self.result_var.get()
            result = eval(result_num + input_num)
            self.input_num.set(value=round(result, 3))
            self.result_var.set(value='')
        else:
            print(input_num)


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, text_color=WHITE if parent.is_dark else BLACK, **kwargs)


app = Calculator(is_dark=True)
app.mainloop()
