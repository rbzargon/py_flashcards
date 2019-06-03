from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PyFlashcards")
root_frame = ttk.Frame(root, padding="8 8 8 8")




q = ttk.Label(root_frame, text="Question")

a1 = ttk.Label(root_frame, text="Answer 1")
a2 = ttk.Label(root_frame, text="Answer 2")
a3 = ttk.Label(root_frame, text="Answer 3")
a4 = ttk.Label(root_frame, text="Answer 4")

root_frame.grid( row=0, sticky='nsew')
q.grid(column=0, row=1, columnspan=4, sticky='nsew')
a1.grid(column=0, row=2, sticky='ew')
a2.grid(column=1, row=2, sticky='ew')
a3.grid(column=2, row=2, sticky='ew')
a4.grid(column=3, row=2, sticky='ew')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
for i in range(4):
    root_frame.columnconfigure(i, weight=1)
root_frame.rowconfigure(0, weight=1)
root_frame.rowconfigure(1, weight=1)



for child in root_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()