
from typing import Iterable, Tuple
from model.quiz import QuizModel
from view.main import MainView


class MainController:

    def __init__(self, rows: Iterable[Tuple[str, str]]):
        super().__init__()

        quiz_model = QuizModel(rows=rows)
        self.quizzes = tuple(quiz_model)
        self.index = 0
        self.view = MainView(next_handler=self.next_handler,
                             maximum=len(self.quizzes))

    def next_handler(self):
        '''Controls moving to the next quiz question'''
        if (self.index < len(self.quizzes)):
            self.view.question, self.view.answers, self.view.correct_answer = self.quizzes[
                self.index]
            self.index += 1
            self.view.progress_value = self.index
        else:
            exit(0)
