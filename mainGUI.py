import tkinter as tk
import pandas as pd
from queries import *

import tkinter.ttk as ttk
# Const colors:
PURPLE = "#ADA2FF"
BLUE = "#C0DEFF"
PINK = "#FFE5F1"
YELLOW = "#FFF8E1"
FONT_BODY = ("Verdana", 12, "bold")

# Create the main window
window = tk.Tk()
window.config(bg=YELLOW)
window.state("zoomed")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

title = tk.Label(text="SONGS CONCORDANCE", 
                font=("Verdana", 30, "bold italic"), 
                fg=PURPLE, justify=tk.CENTER, 
                background=YELLOW)
title.pack()
title = tk.Label(text="Made By Daniela Babi", 
                font=("Verdana", 15, "bold italic"), 
                fg=BLUE, justify=tk.CENTER, 
                background=YELLOW)
title.pack()

# Create the first container - MENU
menu_frame = tk.Frame(window, height=screen_height, width=screen_width*(1/10), background=BLUE)
menu_frame.pack(side='left',fill=tk.BOTH)

# Create the second container - SEARCH
search_frame = tk.Frame(window, height=screen_height, width=screen_width*(2/10), background=PINK)
search_frame.pack(side='left', fill=tk.BOTH)

# Create the third container - RESULTS
result_frame = tk.Frame(window, height=screen_height, width=screen_width*(7/10), background=YELLOW)
result_frame.pack(side='left',fill=tk.BOTH, expand=True)

def show_result_table(df):
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    treeview = ttk.Treeview(result_frame, columns=df.columns, show='headings')

    # set the column headings

    for i, col in enumerate(df.columns):
        treeview.heading(i, text=col)
        
    # add the data to the treeview
    for i in df.index:
        treeview.insert("", "end", values=list(df.iloc[i]))

    # pack the treeview widget
    treeview.pack(expand=True, fill='both')

#-------------------songs - SEARCH BUTTONS-------------------#
def search_by_song_button_result(name1):
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    # create a treeview widget to display the dataframe
    df = get_song_by_name(name1)

    treeview = ttk.Treeview(result_frame, columns=df.columns, show='headings')

    # set the column headings

    for i, col in enumerate(df.columns):
        treeview.heading(i, text=col)
        
    # add the data to the treeview
    for i in df.index:
        treeview.insert("", "end", values=list(df.iloc[i]))

    # pack the treeview widget
    treeview.pack(expand=True, fill='both')

def search_by_song_artist_result(artist):
    df = get_songs_by_artist(artist)
    show_result_table(df)

def search_by_song_word_result(word):
    df = get_songs_by_word(word)
    show_result_table(df)

#-------------------words - SEARCH BUTTONS-------------------#
def search_word_result(word):
    df = get_speciefic_word(word)
    show_result_table(df)

def search_word_by_length_result(length):
    df = get_word_by_length(length)
    show_result_table(df)

#-------------------word indexes - SEARCH BUTTONS-------------------#
def search_word_by_index_result(paragraph, line):
    df = get_word_by_Index(paragraph, line)
    show_result_table(df)

#-------------------SEARCH FRAME-------------------#
def show_songs_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Song name', background=PINK)
    label.pack()
    song_name_entry = tk.Entry(search_frame)
    song_name_entry.pack()
    search_by_song_button = tk.Button(search_frame, text='search', 
                            command=lambda: search_by_song_button_result(song_name_entry.get()))
    search_by_song_button.pack()

    label = tk.Label(search_frame, text='Artist', background=PINK)
    label.pack()
    artist_entry = tk.Entry(search_frame)
    artist_entry.pack()
    search_by_artist_button = tk.Button(search_frame, text='search',
                            command=lambda: search_by_song_artist_result(artist_entry.get()))
    search_by_artist_button.pack()

    label = tk.Label(search_frame, text='Word', background=PINK)
    label.pack()
    word_entry = tk.Entry(search_frame)
    word_entry.pack()
    search_by_word_button = tk.Button(search_frame, text='search',
                                command=lambda: search_by_song_word_result(word_entry.get()))
    search_by_word_button.pack()
    
def show_words_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Word', background=PINK)
    label.pack()
    word_entry1 = tk.Entry(search_frame)
    word_entry1.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_word_result(word_entry1.get()))
    search_button.pack()


    label = tk.Label(search_frame, text='Length of Words', background=PINK)
    label.pack()
    length_entry = tk.Entry(search_frame)
    length_entry.pack()
    search_by_length_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_word_by_length_result(length_entry.get()))
    search_by_length_button.pack()  

def show_indexes_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Query - index by word
    label = tk.Label(search_frame, text='Index of word', background=PINK)
    label.pack()
    word_entry1 = tk.Entry(search_frame)
    word_entry1.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_word_result(word_entry1.get()))
    search_button.pack()

    # Query - word by index
    label = tk.Label(search_frame, text='Word in index', background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Paragraph', background=PINK)
    label.pack()
    paragraph_entry = tk.Entry(search_frame)
    paragraph_entry.pack()
    label = tk.Label(search_frame, text='Line', background=PINK)
    label.pack()
    line_entry = tk.Entry(search_frame)
    line_entry.pack()
    search_by_index_button = tk.Button(search_frame, text='search',
                command=lambda: search_word_by_index_result(paragraph_entry.get(), line_entry.get()))
    search_by_index_button.pack() 

def show_groups_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Group Name')
    label.pack()  
    group_name_entry = tk.Entry(search_frame)
    group_name_entry.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search')
    search_index_by_group_button.pack()

#-------------------DEFAULT BUTTONS SHOW-------------------#
def songs_button_default():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    show_songs_search()
    df = get_full_songs_table()
    show_result_table (df)

def words_button_default():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    show_words_search()
    df = get_full_words_table()
    show_result_table(df)

def indexes_button_default():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    show_indexes_search()
    df = get_full_wordIndex_table()
    show_result_table(df)

def groups_button_default():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    show_groups_search()
    df = get_full_groupDetails_table()
    show_result_table(df)


# Create the buttons and add them to the first container
#lambda: show_songs("Witness")
songs_button = tk.Button(menu_frame, text='Songs', command=songs_button_default)
songs_button.pack()
words_button = tk.Button(menu_frame, text='Words', command=words_button_default)
words_button.pack()
indexes_button = tk.Button(menu_frame, text='Indexes', command=indexes_button_default)
indexes_button.pack()
groups_button = tk.Button(menu_frame, text='Groups', command=groups_button_default)
groups_button.pack()

# Start the main loop
window.mainloop()
