import tkinter as tk
from tkinter.ttk import LabelFrame
from typing import List
from utils import pad_children

class QuestionFrame(LabelFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, text='Question', **kwargs)
        self.question = tk.Button(self, text="Question text")

        self.question.grid(column=0, row=0, sticky='nsew')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        pad_children(self)