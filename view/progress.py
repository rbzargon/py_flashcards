"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application - view for a progress bar
"""
import tkinter as tk
from tkinter import ttk
from utils import pad_children


class ProgressView(ttk.Frame):
    '''Class for displaying a progress bar'''

    def __init__(self, parent, maximum, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._value: tk.IntVar = tk.IntVar(0)
        self.progressbar = ttk.Progressbar(
            self, value=0, maximum=maximum)
        self.progressbar.grid(column=0, row=0, sticky='nsew')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        pad_children(self)

    @property
    def value(self) -> int:
        return self.progressbar['value']

    @value.setter
    def value(self, value: int) -> None:
        self.progressbar['value'] = value
