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

    def __str__(self) -> str:
        return f'''Question: {self.question}
Correct answer: {self.answer}
Random answers: {self.all_answers}'''

    def __repr__(self) -> str:
        return f'QuestionGroup\n{self.__str__()}'

if __name__ == '__main__':
    qg = QuestionGroup('q1', 'a1', ('a1','a2','a3','a4'))
    print('__str__', qg, sep='\n')
    print()
    print('__repr__', qg.__repr__(), sep='\n')
