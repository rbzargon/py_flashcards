from typing import Iterable, List, Optional, Set, Tuple
import random


class Quiz:
    '''Converts tuples of (question, answer) into an iterable instance of
    (question, correct_answer, wrong_answers)'''
    def __init__(self, rows: Iterable[Tuple[str, str]]):
        self.answers: Set[str] = set()
        self.question_to_answer: Set[Tuple[str, str]] = set()
        for row in rows:
            a, q = row
            self.answers.add(a)
            self.question_to_answer.add((q, a))


    # returns question, correct_answer, wrong_answers
    def __iter__(self) -> Iterable[Tuple[str, str, Iterable[str]]]:
        '''Returns (question, correct_answer, wrong_answers)'''
        for question, correct_answer in self.question_to_answer:
            wrong_answers = Quiz.get_random_wrong_answers(
                correct_answer, possible_answers=self.answers, length=4)
            yield (question, correct_answer, wrong_answers)

    @staticmethod
    def get_random_wrong_answers(
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
        for _ in range(length-1):
            choice = random.choice(wrong_answer_choices)
            wrong_answer_choices.remove(choice)
            random_wrong_answers.append(choice)

        return random_wrong_answers
