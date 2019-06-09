"""
Cooper King
CS521
Due June 30, 2019
Term project
Flashcard application GUI
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PyFlashcards")
root_frame = ttk.Frame(root, padding="8 8 8 8")

question_frame = ttk.Labelframe(root_frame, text="Question")
q = ttk.Label(question_frame, text="Question text")

answer_frame = ttk.LabelFrame(root_frame, text="Answer")
a1 = ttk.Label(answer_frame, text="Answer 1")
a2 = ttk.Label(answer_frame, text="Answer 2")
a3 = ttk.Label(answer_frame, text="Answer 3")
a4 = ttk.Label(answer_frame, text="Answer 4")

root_frame.grid(row=0, sticky='nsew')
question_frame.grid(row=0, sticky='nsew')
q.grid(column=0, row=0, sticky='nsew')
answer_frame.grid(row=1, sticky='nsew')
a1.grid(column=0, row=0, sticky='nsew')
a2.grid(column=1, row=0, sticky='nsew')
a3.grid(column=2, row=0, sticky='nsew')
a4.grid(column=3, row=0, sticky='nsew')

#column, row configs
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root_frame.columnconfigure(0, weight=1)
root_frame.rowconfigure(0, weight=1)
root_frame.rowconfigure(1, weight=1)

question_frame.rowconfigure(0, weight=1)
question_frame.columnconfigure(0, weight=1)

for i in range(4):
    answer_frame.columnconfigure(i, weight=1)
answer_frame.rowconfigure(0, weight=1)

def pad_children(frame: ttk.Frame, padx: int = 5, pady: int = 5) -> None:
    for child in frame.winfo_children():
        child.grid_configure(padx=padx, pady=pady)

pad_children(question_frame)
pad_children(answer_frame)

root.mainloop()