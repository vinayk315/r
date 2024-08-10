import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="naak telusu ra unga")
    label.pack(padx=20, pady=20)

def move_button(event):
    x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("instagram: @pythonlearnerr")
root.geometry("400x400")

question_label = tk.Label(root, text="are you gay?")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=show_popup)
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No")
no_button.pack(pady=10)

no_button.bind("<Enter>", move_button)

root.mainloop()
