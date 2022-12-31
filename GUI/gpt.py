import tkinter as tk

# Create the main window
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Create a frame to hold the buttons and another frame to hold the content
menu_frame = tk.Frame(window)
result_frame = tk.Frame(window)

menu_frame.pack()
result_frame.pack()

# Create a function to be called when the "Page 1" button is pressed
def show_page_1():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    # Create a label and place it in the content frame
    label = tk.Label(result_frame, text="This is page 1")
    label.pack()

# Create a function to be called when the "Page 2" button is pressed
def show_page_2():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
        
    # Create a label and place it in the content frame
        label = tk.Label(result_frame, text='Song name')
        label.pack()
        
        song_name_entry = tk.Entry(result_frame)
        song_name_entry.pack()

        search_button = tk.Button(result_frame, text='search')
        search_button.pack()

# Create the "Page 1" button and place it in the button frame
page_1_button = tk.Button(menu_frame, text="Page 1", command=show_page_1)
page_1_button.pack(side="left")

# Create the "Page 2" button and place it in the button frame
page_2_button = tk.Button(menu_frame, text="Page 2", command=show_page_2)
page_2_button.pack(side="left")

# Run the main loop
window.mainloop()
