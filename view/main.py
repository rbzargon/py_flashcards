import tkinter as tk
from tkinter import filedialog, ttk

from progressFrame import ProgressFrame
from questionFrame import QuestionFrame
from answerFrame import AnswerFrame

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.frame = ttk.Frame(self, padding='8 8 8 8')

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
