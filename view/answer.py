"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - view to hold answers
"""

import tkinter as tk
from tkinter import ttk
from typing import Iterable
from utils import pad_children


class AnswerView(ttk.LabelFrame):
    CORRECT_STYLE = {'bg': 'green'}
    INCORRECT_STYLE = {'bg': 'red'}

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, text="Answers", **kwargs)
        self.a1 = tk.Button(self, text="Answer 1")
        self.a2 = tk.Button(self, text="Answer 2")
        self.a3 = tk.Button(self, text="Answer 3")
        self.a4 = tk.Button(self, text="Answer 4")
        self._answers: Iterable[tk.Button] = [
            self.a1, self.a2, self.a3, self.a4]
        for a in self._answers:
            a.config(bg='white')

        self.a1.grid(column=0, row=0, sticky='nsew')
        self.a2.grid(column=1, row=0, sticky='nsew')
        self.a3.grid(column=2, row=0, sticky='nsew')
        self.a4.grid(column=3, row=0, sticky='nsew')

        for i in range(4):
            self.columnconfigure(i, weight=1)
        self.rowconfigure(0, weight=1)
        pad_children(self)

    @property
    def correct_answer(self) -> str:
        for a in self._answers:
            if a['bg'] == 'green':
                return a['text']
        return ''

    @correct_answer.setter
    def correct_answer(self, answer: str) -> None:
        for answer_button in self._answers:
            if answer_button['text'] == answer:
                answer_button.config(**AnswerView.CORRECT_STYLE)

    @property
    def answers(self) -> Iterable[str]:
        return [a['text'] for a in self._answers]

    @answers.setter
    def answers(self, answers: Iterable[str]) -> None:
        for answer_button, answer in zip(self._answers, answers):
            answer_button.config(text=answer, wraplength=160,
                                 **AnswerView.INCORRECT_STYLE)
