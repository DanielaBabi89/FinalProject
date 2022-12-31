import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

# create a tkinter window
window = tk.Tk()

# create a dataframe
df = pd.DataFrame({'First Name': ['John', 'Jane', 'Bob'],
                   'Last Name': ['Doe', 'Doe', 'Smith'],
                   'Email': ['john.doe@example.com', 'jane.doe@example.com', 'bob.smith@example.com']})

# create a treeview widget to display the dataframe
treeview = ttk.Treeview(window, columns=df.columns, show='headings')

# set the column headings

for i, col in enumerate(df.columns):
    treeview.heading(i, text=col)
    
# add the data to the treeview
for i in df.index:
    treeview.insert("", "end", values=list(df.iloc[i]))

# pack the treeview widget
treeview.pack(expand=True, fill='both')

# start the tkinter event loop
window.mainloop()
