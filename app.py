"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from progressFrame import ProgressFrame
from questionFrame import QuestionFrame
from answerFrame import AnswerFrame

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        

        self.frame = ttk.Frame(self, padding='8 8 8 8')
        file_not_valid = True
        while file_not_valid:
            self.file_name = filedialog.askopenfilename(
                filetypes=(('Csv files', '*.csv'), ('All types', '*')),
                title="Choose a flashcard Q/A csv...")
            with open(self.file_name, 'r') as in_file:
                print(in_file)
                file_not_valid = False
                
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