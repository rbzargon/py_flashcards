"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application - main application
"""

import csv
import tkinter as tk
from tkinter import filedialog
from typing import Iterable, Tuple

from sys import stderr

from viewmodel.main import MainViewModel


class App(tk.Tk):
    '''Main flashcard app class'''

    def __init__(self, title: str = 'PyFlashcards', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.winfo_toplevel().title(title)
        self.rows = self.get_rows_from_file()
        self.viewmodel = MainViewModel(parent=self, rows=self.rows)

    @staticmethod
    def get_rows_from_file() -> Iterable[Tuple[str, str]]:
        '''Gets user input for a file that is semicolon delimited csv with two
        entries per line (a question and an answer), returns the rows'''
        file_valid = False
        while not file_valid:
            file_name = filedialog.askopenfilename(
                filetypes=(('Csv files', '*.csv'),
                           ('All types', '*')),
                title="Choose a flashcard Q/A csv with semicolon delimiters...")
            try:
                with open(file_name, 'r', newline='') as in_csv:
                    input_reader = csv.reader(App.noncomment_filter(in_csv),
                                              delimiter=';')
                    rows = [*input_reader]
                    if all([length == 2 for length in map(len, rows)]):
                        file_valid = True
                    else:
                        bad_index = 0
                        bad_row_len = 0
                        for idx, row in enumerate(rows):
                            if len(row) != 2:
                                bad_index = idx
                                bad_row_len = len(row)
                                break
                        print(
                            'Expected length 2 (question/answer) but found length'
                            f' {bad_row_len} on row {bad_index}.\n'
                            'File must be delimited by a semicolon'
                            ' and have a question/answer entry per line',
                            file=stderr)
                        exit(-1)
            except IOError as e:
                print(f'Error opening file: {e}', file=stderr)

        return rows

    @staticmethod
    def noncomment_filter(rows: Iterable[str]) -> Iterable[str]:
        return filter(lambda row: row.lstrip()[0] != '#', rows)


if __name__ == '__main__':
    app = App()
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
