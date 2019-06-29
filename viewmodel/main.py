
"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - main viewmodel
"""
from typing import Iterable, Tuple
from model.quiz import QuizModel
from view.main import MainView


class MainViewModel:

    def __init__(self, rows: Iterable[Tuple[str, str]]):
        super().__init__()

        quiz_model = QuizModel(rows=rows)
        self.quizzes = tuple(quiz_model)
        self.index = 0
        self.view = MainView(next_handler=self.next_handler,
                             maximum=len(self.quizzes))
        self.next_handler()

    def next_handler(self):
        '''Controls moving to the next quiz question, program exits when done'''
        if (self.index < len(self.quizzes)):
            current_quiz = self.quizzes[self.index]
            self.view.question = current_quiz.question
            self.view.answers = current_quiz.all_answers
            self.view.correct_answer = current_quiz.answer
            self.index += 1
            self.view.progress_value = self.index
        else:
            exit(0)
