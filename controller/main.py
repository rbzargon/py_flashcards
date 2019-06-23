
from typing import Iterable, Tuple
from model.quiz import QuizModel
from view.main import MainView


class MainController:

    def __init__(self, rows: Iterable[Tuple[str, str]]):
        super().__init__()
        quiz_model = QuizModel(rows=rows)
        view = MainView()
        for quiz in quiz_model:
            view.question, view.answers, view.correct_answer = (
                quiz.question, quiz.all_answers, quiz.answer)
