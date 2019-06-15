"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI
"""

import csv
import tkinter as tk
from tkinter import filedialog, ttk

from typing import Set, Tuple

from view.answerFrame import AnswerFrame
from view.progressFrame import ProgressFrame
from view.questionFrame import QuestionFrame


class App(tk.Tk):
    '''Main flashcard app class'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frame = ttk.Frame(self, padding='8 8 8 8')
        file_valid = False
        while not file_valid:
            self.file_name = filedialog.askopenfilename(
                filetypes=(('Csv files', '*.csv'), ('All types', '*')),
                title="Choose a flashcard Q/A csv with semicolon delimiters...")
            with open('planets.csv', 'r', newline='') as in_csv:
                input_reader = csv.reader(in_csv, delimiter=';')
                self.question_to_answer: Set[Tuple[str, str]] = set()
                self.answer_to_question: Set[Tuple[str, str]] = set()
                for row in input_reader:
                    a, q = row
                    self.answer_to_question.add((a, q))
                    self.question_to_answer.add((q, a))

                file_valid = True

        print(self.answer_to_question)
        print(self.question_to_answer)

        self.frame.grid(row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=4)
        self.frame.rowconfigure(2, weight=4)
        self.frame.rowconfigure(3, weight=1)

        self.progress_frame = ProgressFrame(self.frame)
        self.question_frame = QuestionFrame(self.frame)
        self.answer_frame = AnswerFrame(self.frame)

        self.progress_frame.grid(row=0, sticky='nsew', )
        self.question_frame.grid(row=1, sticky='nsew', pady='10')
        self.answer_frame.grid(row=2, sticky='nsew')


if __name__ == '__main__':
    app = App()
    app.title = 'PyFlashcards'
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
