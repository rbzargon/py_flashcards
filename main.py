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

root = Tk()
root.title("PyFlashcards")
root_frame = ttk.Frame(root, padding="8 8 8 8")

progress_frame = ttk.LabelFrame(root_frame, text="Progress")
p = ttk.Progressbar(root_frame, maximum=10, value=5)

question_frame = ttk.LabelFrame(root_frame, text="Question")
q = tk.Button(question_frame, text="Question text")

answer_frame = ttk.LabelFrame(root_frame, text="Answer")
a1 = tk.Button(answer_frame, text="Answer 1")
a2 = tk.Button(answer_frame, text="Answer 2")
a3 = tk.Button(answer_frame, text="Answer 3")
a4 = tk.Button(answer_frame, text="Answer 4")
for a in (a1, a2, a3, a4):
     a.config(bg='white')

root_frame.grid(row=0, sticky='nsew')

progress_frame.grid(row=0, sticky='nsew')
p.grid(column=0, row=0, sticky='nsew')

question_frame.grid(row=1, sticky='nsew')
q.grid(column=0, row=0, sticky='nsew')

answer_frame.grid(row=2, sticky='nsew')
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
root_frame.rowconfigure(2, weight=1)

progress_frame.rowconfigure(0, weight=1)
progress_frame.columnconfigure(0, weight=1)

question_frame.rowconfigure(0, weight=1)
question_frame.columnconfigure(0, weight=1)

for i in range(4):
    answer_frame.columnconfigure(i, weight=1)
answer_frame.rowconfigure(0, weight=1)

def pad_children(frame: ttk.Frame, padx: int = 5, pady: int = 5) -> None:
    for child in frame.winfo_children():
        child.grid_configure(padx=padx, pady=pady)

pad_children(progress_frame)
pad_children(question_frame)
pad_children(answer_frame)

root.mainloop()