# main.py
import tkinter as tk
from autotyper.gui import AutotyperGUI

if __name__ == "__main__":
    root = tk.Tk()
    gui = AutotyperGUI(root)
    root.attributes('-topmost', True)  # Keep window on top
    root.mainloop()