"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application - view for a question
"""

import tkinter as tk
from tkinter.ttk import Label, LabelFrame
from typing import List
from utils import pad_children


class QuestionView(LabelFrame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, text='Question', **kwargs)
        self._question = Label(self, text='Question',
                               anchor='center',
                               wraplength=480,
                               )

        self._question.grid(column=0, row=0, sticky='nsew')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        pad_children(self)

    @property
    def question(self):
        return self._question['text']

    @question.setter
    def question(self, question: str):
        self._question['text'] = question
