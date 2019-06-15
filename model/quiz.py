"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI - adapter model class to create question/answer
groups for quiz questions
"""

import random
from typing import Iterable, Iterator, List, Set, Tuple

from .questionGroup import QuestionGroup


class QuizModel:
    """Converts tuples of (question, answer) into an iterable instance of
    (question, correct_answer, all_answers)
    >>> quizzes: Iterable[QuestionGroup] = QuizModel(rows=(('q1', 'a1'), ('q2', 'a2'), ('q3', 'a3'), ('q4', 'a4')))
    >>> questions, answers, all_answers = zip(*quizzes)
    >>> sorted(questions)
    ['q1', 'q2', 'q3', 'q4']
    >>> sorted(answers)
    ['a1', 'a2', 'a3', 'a4']
    >>> all([('a1','a2','a3','a4') == tuple(sorted(all_group)) for all_group in all_answers])
    True"""

    def __init__(self, rows: Iterable[Tuple[str, str]]):
        self.answers: Set[str] = set()
        self.question_to_answer: Set[Tuple[str, str]] = set()
        for row in rows:
            q, a = row
            self.answers.add(a)
            self.question_to_answer.add((q, a))

    # returns question, correct_answer, all_answers
    def __iter__(self) -> Iterator[QuestionGroup]:
        '''Returns (question, correct_answer, all_answers)'''
        for question, correct_answer in self.question_to_answer:
            all_answers = QuizModel.get_random_answers(
                correct_answer, possible_answers=self.answers, length=4)
            yield QuestionGroup(question, correct_answer, all_answers)

    @staticmethod
    def get_random_answers(
            correct_answer: str, possible_answers: Iterable[str],
            length: int = 4) -> List[str]:
        '''Given a correct answer and possible answers, returns a list of random
        wrong answers of the specified length. If there are insufficient unique and
        incorrect possible answers, the list is filled with empty strings to the
        specified length.'''
        wrong_answer_choices: List[str] = [
            a for a in set(possible_answers)
            if a.strip().lower() != correct_answer.strip().lower()]

        if len(wrong_answer_choices) < length - 1:  # add blank wrong answers
            for _ in range(length - len(wrong_answer_choices)):
                wrong_answer_choices.append('')

        random_wrong_answers = []
        for _ in range(length - 1):
            choice = random.choice(wrong_answer_choices)
            wrong_answer_choices.remove(choice)
            random_wrong_answers.append(choice)

        random_answers = [correct_answer, *random_wrong_answers]
        random.shuffle(random_answers)
        return random_answers


if __name__ == '__main__':
    from doctest import testmod
    testmod()
