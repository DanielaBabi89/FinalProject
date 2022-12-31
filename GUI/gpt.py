import tkinter as tk
from tkinter import ttk
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'Dave'],
                   'age': [25, 30, 35, 40],
                   'selected': [True, False, False, True]})

# Create the Tkinter window and frame
window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

# Create the Treeview widget
tree = ttk.Treeview(frame, columns=('name', 'age', 'selected'), show='headings')

# Set the column headings
tree.heading('name', text='Name')
tree.heading('age', text='Age')
tree.heading('selected', text='Selected')

# Add the checkbox column
tree['displaycolumns'] = ('selected',)

# Add the data to the Treeview widget
for i, row in df.iterrows():
    # Create a checkbox widget for the selected column
    cb = ttk.Checkbutton(tree, variable=row['selected'])
    tree.insert('', 'end', values=(row['name'], row['age'], cb))

# Pack the Treeview widget
tree.pack(side='left')

# Define a function to get the selected rows
def get_selected_rows():
    # Get the list of selected rows
    selected_rows = tree.selection()

    # Print the indexes of the selected rows in the DataFrame
    print(selected_rows)

# Create a button to get the selected rows
button = tk.Button(frame, text='Get Selected Rows', command=get_selected_rows)
button.pack(side='right')

# Run the Tkinter event loop
window.mainloop()
