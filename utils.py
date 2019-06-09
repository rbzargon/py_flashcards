from tkinter import ttk

def pad_children(frame: ttk.Frame, padx: int = 5, pady: int = 5) -> None:
    for child in frame.winfo_children():
        child.grid_configure(padx=padx, pady=pady)