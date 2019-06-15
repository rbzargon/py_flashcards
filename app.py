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

       
        file_valid = False
        while not file_valid:
            self.file_name = filedialog.askopenfilename(
                filetypes=(('Csv files', '*.csv'), ('All types', '*')),
                title="Choose a flashcard Q/A csv with semicolon delimiters...")
            with open('planets.csv', 'r', newline='') as in_csv:
                input_reader = csv.reader(in_csv, delimiter=';')


                file_valid = True

        print(self.answer_to_question)
        print(self.question_to_answer)




if __name__ == '__main__':
    app = App()
    app.title = 'PyFlashcards'
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
