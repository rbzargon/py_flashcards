"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - main view
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Iterable

from .progress import ProgressView
from .question import QuestionView
from .answer import AnswerView


class MainView(tk.Tk):
    '''Main view with progress, question, and answer views'''
    def __init__(
            self, next_handler: Callable[[], None], maximum: int,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = ttk.Frame(self, padding='8 8 8 8')

        self.frame.grid(row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=4)
        self.frame.rowconfigure(2, weight=4)
        self.frame.rowconfigure(3, weight=1)

        self.progress_view = ProgressView(self.frame, maximum)
        self.question_view = QuestionView(self.frame)
        self.answer_view = AnswerView(self.frame, next_handler=next_handler)

        self.progress_view.grid(row=0, sticky='nsew', )
        self.question_view.grid(row=1, sticky='nsew', pady='10')
        self.answer_view.grid(row=2, sticky='nsew')

    @property
    def progress_value(self) -> int:
        return self.progress_view.value

    @progress_value.setter
    def progress_value(self, value: int) -> None:
        self.progress_view.value = value

    @property
    def question(self) -> str:
        return self.question_view.question

    @question.setter
    def question(self, question: str) -> None:
        self.question_view.question = question

    @property
    def correct_answer(self) -> str:
        return self.answer_view.correct_answer

    @correct_answer.setter
    def correct_answer(self, answer: str) -> None:
        self.answer_view.correct_answer = answer

    @property
    def answers(self) -> Iterable[str]:
        return self.answer_view.answers

    @answers.setter
    def answers(self, answers: Iterable[str]) -> None:
        self.answer_view.answers = answers
