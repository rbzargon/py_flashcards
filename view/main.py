"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - main view
"""

import tkinter as tk
from tkinter import ttk

from .progress import ProgressView
from .question import QuestionView
from .answer import AnswerView


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.frame = ttk.Frame(self, padding='8 8 8 8')

        self.frame.grid(row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=4)
        self.frame.rowconfigure(2, weight=4)
        self.frame.rowconfigure(3, weight=1)

        self.progress_view = ProgressView(self.frame)
        self.question_view = QuestionView(self.frame)
        self.answer_view = AnswerView(self.frame)

        self.progress_view.grid(row=0, sticky='nsew', )
        self.question_view.grid(row=1, sticky='nsew', pady='10')
        self.answer_view.grid(row=2, sticky='nsew')

    @property
    def question(self):
        pass  # TODO get question from frame

    @property.setter
    def question(self):
        pass

    @property
    def correct_answer(self):
        pass

    @property.setter
    def correct_answer(self):
        pass

    @property
    def answers(self):
        pass

    @property.setter
    def answers(self):
        pass
