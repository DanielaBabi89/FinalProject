import tkinter as tk

def selection_callback(event):
    selection = event.widget.get("sel.first", "sel.last")
    print(f"Selection: {selection}")

root = tk.Tk()

text = tk.Text(root, bg="white")
text.pack()

text.insert("1.0", "Hello, World!")

text.bind("<Button-1>", selection_callback)

root.mainloop()
