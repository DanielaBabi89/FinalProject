import tkinter as tk

# Const colors:
PURPLE = "#ADA2FF"
BLUE = "#C0DEFF"
PINK = "#FFE5F1"
YELLOW = "#FFF8E1"

# Create the main window
window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

title = tk.Label(text="SONGS CONCORDANCE", font=("Verdana", 30, "bold italic"), justify=tk.CENTER)
title.pack()
title = tk.Label(text="Made By Daniela Babi", font=("Verdana", 15, "bold italic"), fg=BLUE, justify=tk.CENTER)
title.pack()

#-----------------------------------------section frame-----------------------------------------#
search_frame = tk.Frame(window, height=screen_height, width=screen_width*(1/10), background=BLUE)
search_frame.pack(side = "left")

full_songs_list_button = tk.Button(search_frame,
                                    text="Songs",
                                    bg=PURPLE,
                                    fg="white", 
                                    font=("Helvetica", 14),  
                                    activeforeground=PURPLE)

full_songs_list_button.pack(side="top")

full_words_list_button = tk.Button(search_frame,
                                    text="Words",
                                    bg=PURPLE,
                                    fg="white", 
                                    font=("Helvetica", 14), 
                                    activeforeground=PURPLE)
full_words_list_button.pack(side="top")

full_groups_list_button = tk.Button(search_frame,
                                    text="Groups",
                                    bg=PURPLE,
                                    fg="white", 
                                    font=("Helvetica", 14), 
                                    activeforeground=PURPLE)
full_groups_list_button.pack(side="top")

full_phrases_list_button = tk.Button(search_frame,
                                    text="Phrases",
                                    bg=PURPLE,
                                    fg="white", 
                                    font=("Helvetica", 14), 
                                    activeforeground=PURPLE)
full_phrases_list_button.pack()

#-----------------------------------------section frame-----------------------------------------#


#------------------------------------------search frame-----------------------------------------#
search_frame = tk.Frame(window, height=screen_height, width=screen_width*(2/10), background=BLUE)
search_frame.pack(side = "left")

#------------------------------------------search frame-----------------------------------------#


#-----------------------------------------results frame-----------------------------------------#
results_frame = tk.Frame(window, height=screen_height, width=screen_width*(7/10), background=PINK)
results_frame.pack(side = "left")

#-----------------------------------------results frame-----------------------------------------#



# Run the main loop
window.mainloop()