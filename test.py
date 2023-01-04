import tkinter as tk

def selection_callback(event):
    selection = event.widget.cget("textvariable")
    print(f"Selection: {selection.get()}")

root = tk.Tk()

label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text, bg="white")
label.pack()

label_text.set("Hello, World!")

label.bind("<Button-1>", selection_callback)

root.mainloop()
