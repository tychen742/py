import tkinter as tk
from tkinter import messagebox
def on_button_click():
    messagebox.showinfo("Information", "Button was clicked!")
window = tk.Tk()
window.title("Simple GUI")
window.geometry("300x200")  
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=20)
window.mainloop()