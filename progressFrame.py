from tkinter import ttk
from typing import List
from utils import pad_children

class ProgressFrame(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.progressbar = ttk.Progressbar(self, maximum=10)
        self.progressbar.grid(column=0, row=0, sticky='nsew')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        pad_children(self)
