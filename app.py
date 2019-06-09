"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI
"""
from tkinter import Tk
import tkinter as tk
from tkinter import ttk

from progressFrame import ProgressFrame
from questionFrame import QuestionFrame
from answerFrame import AnswerFrame

class App(Tk):

    def __init__(self):
        super().__init__()

        self.frame = ttk.Frame(self, padding='8 8 8 8')
        self.frame.grid(row=0, sticky='nsew')
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=4)
        self.frame.rowconfigure(2, weight=4)
        
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