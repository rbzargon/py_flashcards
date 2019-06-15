"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application - interface for question, answer, and a group of answers
"""

from typing import Iterable, NamedTuple


class QuestionGroup(NamedTuple):
    '''Interface for question, answer, and a group of answers'''
    question: str
    answer: str
    all_answers: Iterable[str]
