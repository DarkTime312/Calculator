import customtkinter as ctk
from settings import *
from PIL import Image


class NumButton(ctk.CTkButton):
    def __init__(self, parent, num, **kwargs):
        super().__init__(master=parent,
                         text=num,
                         font=(FONT, NORMAL_FONT_SIZE),
                         text_color=COLORS['light-gray']['text'],
                         corner_radius=STYLING['corner-radius'],
                         fg_color=COLORS['light-gray']['fg'],
                         hover_color=COLORS['light-gray']['hover'],
                         **kwargs)

        self.grid(row=NUM_POSITIONS[num]['row'],
                  column=NUM_POSITIONS[num]['col'],
                  columnspan=NUM_POSITIONS[num]['span'],
                  padx=STYLING['gap'],
                  pady=STYLING['gap'],
                  sticky='news')


class Button(ctk.CTkButton):
    def __init__(self, parent, text, **kwargs):
        super().__init__(master=parent,
                         text=OPERATORS[text]['text'],
                         font=(FONT, NORMAL_FONT_SIZE),
                         text_color=COLORS['dark-gray']['text'],
                         corner_radius=STYLING['corner-radius'],
                         hover_color=COLORS['dark-gray']['hover'],
                         **kwargs)
        images = OPERATORS[text]['image path']
        if images:
            ctk_img = ctk.CTkImage(light_image=Image.open(images['dark']),
                                   dark_image=Image.open(images['light']))
            self.configure(image=ctk_img)
        self.configure(fg_color=COLORS['dark-gray']['fg'])

        self.grid(row=OPERATORS[text]['row'],
                  column=OPERATORS[text]['col'],
                  padx=STYLING['gap'],
                  pady=STYLING['gap'],
                  sticky='news')

class MathButton(ctk.CTkButton):
    def __init__(self, parent, sign, **kwargs):
        super().__init__(master=parent,
                         text=MATH_POSITIONS[sign]['character'],
                         font=(FONT, NORMAL_FONT_SIZE),
                         text_color=COLORS['orange']['text'],
                         corner_radius=STYLING['corner-radius'],
                         hover_color=COLORS['orange']['hover'],
                         **kwargs)
        images = MATH_POSITIONS[sign]['image path']
        if images:
            ctk_img = ctk.CTkImage(light_image=Image.open(images['dark']),
                                   dark_image=Image.open(images['light']))
            self.configure(image=ctk_img)
        self.configure(fg_color=COLORS['orange']['fg'])

        self.grid(row=MATH_POSITIONS[sign]['row'],
                  column=MATH_POSITIONS[sign]['col'],
                  padx=STYLING['gap'],
                  pady=STYLING['gap'],
                  sticky='news')
