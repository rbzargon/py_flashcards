import tkinter as tk
from tkinter import ttk
from typing import List
from utils import pad_children
from typing import Tuple

class AnswerFrame(ttk.LabelFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, text="Answers", **kwargs)
        a1 = tk.Button(self, text="Answer 1")
        a2 = tk.Button(self, text="Answer 2")
        a3 = tk.Button(self, text="Answer 3")
        a4 = tk.Button(self, text="Answer 4")
        for a in (a1, a2, a3, a4):
            a.config(bg='white')

        a1.grid(column=0, row=0, sticky='nsew')
        a2.grid(column=1, row=0, sticky='nsew')
        a3.grid(column=2, row=0, sticky='nsew')
        a4.grid(column=3, row=0, sticky='nsew')
        self.answers = [a1, a2, a3, a4]
        for i in range(4):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)
        pad_children(self)

    def set_answers(self, answers: Tuple[str, str, str, str], correct_index: int):
        for answer_button, answer in zip(self.answers, answers):
            answer_button.config(text=answer)