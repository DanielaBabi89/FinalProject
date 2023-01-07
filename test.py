import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a frame to hold the Text and Scrollbar widgets
frame = tk.Frame(root)
frame.pack()

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Text widget
text = tk.Text(frame, yscrollcommand=scrollbar.set)

# Insert some long text into the Text widget
text.insert(tk.END, "This is a very long text that will require scrolling to see the whole thing. " * 1000)

# Configure the Scrollbar widget to work with the Text widget
scrollbar.config(command=text.yview)

# Pack the Text widget
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Run the main loop
root.mainloop()
