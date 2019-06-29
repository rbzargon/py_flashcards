"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - view to hold answers
"""

from functools import partial
import tkinter as tk
from tkinter import ttk
from typing import Callable, Iterable
from utils import pad_children


class AnswerView(ttk.LabelFrame):
    '''Responsible for visual representation of quiz answers'''
    CORRECT_STYLE = {'bg': 'green', 'wraplength': 160, 'width': 22}
    INCORRECT_STYLE = {'bg': 'red', 'wraplength': 160, 'width': 22}
    BUTTON_STYLE = {'bg': 'white', 'wraplength': 160, 'width': 22}

    def __init__(
            self, parent, next_handler: Callable[[], None], *args, **kwargs):
        super().__init__(parent, *args, text="Answers", **kwargs)
        self.next_handler = next_handler
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
                button_handler = partial(
                    self.correct_handler, button=answer_button)
                answer_button.config(command=button_handler)

    def correct_handler(self, button: tk.Button) -> None:
        '''Change the button style and call for next after one second'''
        button.config(**AnswerView.CORRECT_STYLE)
        button.after(1000, func=self.next_handler)

    def incorrect_handler(self, button: tk.Button) -> None:
        button.config(**AnswerView.INCORRECT_STYLE)

    @property
    def answers(self) -> Iterable[str]:
        return [a['text'] for a in self._answers]

    @answers.setter
    def answers(self, answers: Iterable[str]) -> None:
        for answer_button, answer in zip(self._answers, answers):
            button_handler = partial(
                self.incorrect_handler, button=answer_button)
            answer_button.config(command=button_handler,
                                 text=answer,
                                 **AnswerView.BUTTON_STYLE)
