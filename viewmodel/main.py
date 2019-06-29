
"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - main viewmodel
"""
from tkinter import Tk
from typing import Iterable, Tuple
from model.quiz import QuizModel
from view.main import MainView


class MainViewModel:
    '''Controls overall model/view interactions'''

    def __init__(self, parent: Tk, rows: Iterable[Tuple[str, str]]):
        super().__init__()

        quiz_model = QuizModel(rows=rows)
        self._quizzes = tuple(quiz_model)
        self._index = 0
        self.view = MainView(parent=parent,
                             next_handler=self.next_handler,
                             maximum=len(self._quizzes))
        self.next_handler()

    def next_handler(self):
        '''Controls moving to the next quiz question, program exits when done'''
        if self.index < len(self._quizzes):
            current_quiz = self._quizzes[self._index]
            self.view.question = current_quiz.question
            self.view.answers = current_quiz.all_answers
            self.view.correct_answer = current_quiz.answer
            self.view.progress_value = self._index
            self._index += 1
        else:
            exit(0)
