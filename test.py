import tkinter as tk

# Create the main window
window = tk.Tk()

# Create the first container for the buttons
container1 = tk.Frame(window)
container1.pack(side='left')

# Create the buttons and add them to the first container
button1 = tk.Button(container1, text='Button 1')
button1.pack()
button2 = tk.Button(container1, text='Button 2')
button2.pack()
button3 = tk.Button(container1, text='Button 3')
button3.pack()

# Create the second container for the entries and button
container2 = tk.Frame(window)
container2.pack(side='left')

# Create the entries and button, and add them to the second container
entry1 = tk.Entry(container2)
entry1.pack()
entry2 = tk.Entry(container2)
entry2.pack()
entry3 = tk.Entry(container2)
entry3.pack()
button4 = tk.Button(container2, text='Button 4')
button4.pack()

# Create the third container for the dataframe
container3 = tk.Frame(window)
container3.pack(side='left')

# Add a placeholder label to the third container
label = tk.Label(container3, text='Dataframe goes here')
label.pack()

# Start the main loop
window.mainloop()
