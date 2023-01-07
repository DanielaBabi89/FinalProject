import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a canvas widget and pack it into the main window
canvas = tk.Canvas(root)
canvas.pack()

# Use the create_line method to draw a line on the canvas
line = canvas.create_line(0, 0, 50, 50)

# Run the Tkinter event loop
root.mainloop()
