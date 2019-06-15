
from typing import Iterable, Tuple
from model.quiz import QuizModel


class Quiz:

    def __init__(self, rows: Iterable[Tuple[str, str]]):
        super().__init__()
        quiz_model = QuizModel(rows=rows)
        
        for quiz in quiz_model:
            question, answer, all_answers = quiz

    