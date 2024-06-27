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

        self.top_output_label = OutputLabel(self, text='6 +', font=font)
        self.top_output_label.grid(row=0, column=0, columnspan=4, sticky='se', padx=10)

        self.output_label = OutputLabel(self, text='9', font=font_large)
        self.output_label.grid(row=1, column=0, columnspan=4, sticky='e', padx=10)

        # Create number buttons
        self.num_1 = NumButton(self, num=1, )
        self.num_2 = NumButton(self, num=2, )
        self.num_3 = NumButton(self, num=3, )
        self.num_4 = NumButton(self, num=4, )
        self.num_5 = NumButton(self, num=5, )
        self.num_6 = NumButton(self, num=6, )
        self.num_7 = NumButton(self, num=7, )
        self.num_8 = NumButton(self, num=8, )
        self.num_9 = NumButton(self, num=9, )
        self.num_0 = NumButton(self, num=0, )
        self.num_dot = NumButton(self, num='.', )

        # other buttons
        self.clear_btn = Button(self, text='clear')
        self.invert_btn = Button(self, text='invert')
        self.percent_btn = Button(self, text='percent')

        # math buttons
        self.divide = MathButton(self, '/')
        self.multiply = MathButton(self, '*')
        self.minus = MathButton(self, '-')
        self.plus = MathButton(self, '+')
        self.equal = MathButton(self, '=')


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, **kwargs):
        super().__init__(master=parent, **kwargs)


app = Calculator(is_dark=False)
app.mainloop()
