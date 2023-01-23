import tkinter as tk
import pandas as pd
from queries import *
import tkinter.messagebox as messagebox
from statisticQueries import *
import tkinter.ttk as ttk
from defineGroup import *
from definePhrase import *
from tkinter import filedialog
from LoadTXT import *
from tkinter import PhotoImage
from auxiliaryQueries import *

#region Const
PURPLE = "#7B2869"
BLUE = "#9D3C72"
PINK = "#FFBABA"
YELLOW = "#FFFAE7"
YELLOW2 = "#E1D7C6"
RED = "#850000"
FONT_BODY = ("Verdana", 12, "bold")
FONT1 = ("Verdana", 30, "bold italic")
FONT2 = ("Verdana", 10, "bold")
FONT3 = ("Verdana", 20, "bold")
FONTB = ("Gill Sans MT", 10, "bold")
FONTB2 = ("JasmineUPC", 9, "bold")
FONT4 = ("Verdana", 10, "bold underline")
#endregion

#region Create the main window
window = tk.Tk()
window.config(bg=YELLOW)
window.title("Daniela Babi")
window.state("zoomed")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

image = PhotoImage(file="logo1.png")
image = image.subsample(2)
title = tk.Label(window, image=image, borderwidth=0)
title.pack()
#endregion

#region Create the containers - MENU, SEARCH and RESULTS
menu_frame = tk.Frame(window, height=screen_height, width=screen_width*(1/10), background=BLUE, border=5)
menu_frame.pack(side='left',fill=tk.BOTH)

search_frame = tk.Frame(window, height=screen_height, width=screen_width*(2/10), background=PINK, borderwidth=5)
search_frame.pack(side='left', fill=tk.BOTH)

result_frame = tk.Frame(window, height=screen_height, width=screen_width*(7/10), background=YELLOW, border=5)
result_frame.pack(side='left',fill=tk.BOTH, expand=True)
#endregion

def load_new_song():
    src = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    src_splited = src.split("/")
    file_name = src_splited[len(src_splited)-1].split(".")[0]
    dst = "C:/Users/babid/Desktop/FinalProject/songsCSV/" + file_name + ".csv"
    load_song_to_DB(src, dst, file_name)

    messagebox.showinfo('new song', "Song added successfully")
    

def show_result_table(df):
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    global treeview 
    treeview = ttk.Treeview(result_frame, columns=df.columns, show='headings')

    # set the column headings

    for i, col in enumerate(df.columns):
        treeview.heading(i, text=col)
        
    # add the data to the treeview
    for i in df.index:
        treeview.insert("", "end", values=list(df.iloc[i]))

    # pack the treeview widget
    treeview.pack(expand=True, fill='both')


def no_result_found():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    label = tk.Label(result_frame, 
                    text='No Results Found',
                    font=FONT2,
                    fg=RED,
                    background=YELLOW)
    label.pack()


#region Songs Tab
def search_by_song_button_result(name1):
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    # create a treeview widget to display the dataframe
    df = get_song_by_name(name1)

    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_by_song_artist_result(artist):
    df = get_songs_by_artist(artist)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_by_song_word_result(word):
    df = get_songs_by_word(word)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def read_song_on_click():
    selected_rows = treeview.selection()
    # Get the data of the selected rows
    item = treeview.item(selected_rows[0])
     # Clear the content frame
    path_column = len(item['values']) - 1
    path = item['values'][path_column]
    with open(path, mode="r") as file:
        song = file.read()

    if song and song != "":
        songs_button_default()
        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a Text widget
        text = tk.Text(result_frame, yscrollcommand=scrollbar.set)
        text.insert(tk.END, song)
        scrollbar.config(command=text.yview)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    else:
        no_result_found()
#endregion


#region Words Tab
def search_word_result(word):
    df = get_speciefic_word(word)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_word_by_length_result(length):
    df = get_word_by_length(length)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_word_by_stem(word):
    df = get_word_by_stem(word)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)
#endregion


#region WordIndex Tab
def search_word_by_index_result(paragraph, line):
    if paragraph == "":
        try:
            line = int(line)
        except:
            tk.messagebox.showerror("error", "You must enter a number")
        df = get_word_by_line(line)
    elif line == "":
        try:
            paragraph = int(paragraph)
        except:
            tk.messagebox.showerror("error", "You must enter a number")
        df = get_word_by_paragraph(paragraph)
    else:
        try:
            paragraph = int(paragraph)
            line = int(line)
        except:
            tk.messagebox.showerror("error", "You must enter a number")
        df = get_word_by_Index(paragraph, line)
    
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_index_of_word_result(word):
    df = get_index_of_word(word)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_index_of_group_result(group):
    df = get_index_of_group(group)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_range_word_result(word): 
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    range_string = concatenate_context_of_word(word)
    if range_string != "":
        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a Text widget
        text = tk.Text(result_frame, yscrollcommand=scrollbar.set)
        text.insert(tk.END, range_string)
        scrollbar.config(command=text.yview)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    else:
        no_result_found()
#endregion


#region Group Tab
def search_group_result(group):
    df = get_speciefic_group(group)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_group_by_word_result(word):
    df = get_group_by_word(word)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def words_for_group_button():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    df = get_full_words_table()
    show_result_table(df)

def refresh_groups():
    df = get_full_groupDetails_table()
    show_result_table(df)

def create_group_from_db(groupName):
    selected_rows = treeview.selection()
    if groupName == "":
        tk.messagebox.showerror("error", "You must add group name")
    elif len(selected_rows) == 0:
        tk.messagebox.showerror("error", "You must choose words from the list")
    else:
        # Get the data of the selected rows
        data = []
        for row in selected_rows:
            item = treeview.item(row)
            data.append(item['values'][1])
        define_group(groupName, data)
        
        massage = groupName + ": " + str(data)
        messagebox.showinfo('new group', "new group added: \n"+massage)
    
def create_group_from_text(groupName, data):
    print(data)
    if groupName == "":
        tk.messagebox.showerror("error", "You must add group name")
    elif data == ['','']:
        tk.messagebox.showerror("error", "You must choose words from the list")
    else:
        define_group(groupName, data)
        
        massage = groupName + ": " + ", ".join(data)
        messagebox.showinfo('new group', "new group added: \n"+massage)
#endregion


#region Phrase Tab
def search_phrase_result(phrase):
    df = get_speciefic_phrase(phrase)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_phrase_by_word_result(word):
    df = get_phrase_by_word(word)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)

def search_phrase_in_song_result (phrase):
    for widget in result_frame.winfo_children():
        widget.destroy()

    range_string = concatenate_context_of_phrase(phrase)
    if range_string != "":
        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        range_string = range_string.replace(phrase, " **" + phrase + "** ")
        # Create a Text widget
        text = tk.Text(result_frame, yscrollcommand=scrollbar.set)
        text.insert(tk.END, range_string)
        scrollbar.config(command=text.yview)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    else:
        no_result_found()
    
def create_phrase_from_text(name, phrase):
    if name == "":
        tk.messagebox.showerror("error", "You must add phrase name")
    elif phrase == "":
        tk.messagebox.showerror("error", "You must add phrase")
    else:
        define_phrase(name, phrase)        
        massage = name + ": " + phrase
        messagebox.showinfo('new phrase', "new phrase added: \n"+massage)
#endregion


#region Statistic Tab
def by_paragraph_statistics(song):
    df = statistic_words_in_paragraphs(song)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)


def by_line_statistics(song):
    df = statistic_words_in_lines(song)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)


def by_word_statistics(song):
    count = statistic_words_in_song(song)
    if (count == None):
        no_result_found()
    else:
        for widget in result_frame.winfo_children():
            widget.destroy()

        massage = str(count) + " words in the song: " + song
        label = tk.Label(result_frame, 
                        text=massage,
                        font=FONT3,
                        fg=PURPLE,
                        background=YELLOW)
        label.pack()


def chars_by_word_statistics(song):
    count = statistic_chars_in_song(song)
    if (count == None):
        no_result_found()
    else:
        for widget in result_frame.winfo_children():
            widget.destroy()

        massage = str(count) + " characters in the song: " + song
        label = tk.Label(result_frame, 
                        text=massage,
                        font=FONT3,
                        fg=PURPLE,
                        background=YELLOW)
        label.pack()


def chars_by_line_statistics(song):
    df = statistic_chars_in_lines(song)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)


def chars_by_paragraph_statistics(song):
    df = statistic_chars_in_paragraphs(song)
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)


def frequency_list_statistics():
    df = statistic_word_frequency_list()
    if(len(df)==0):
        no_result_found()
    else:
        show_result_table(df)
#endregion


#region Search Frame
def show_songs_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # -----> show full song text
    label = tk.Label(search_frame, text='Choose song', background=PINK)
    label.pack()
    read_song_button = tk.Button(search_frame, text='READ', 
                            command=read_song_on_click)
    read_song_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    read_song_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search by song name
    label = tk.Label(search_frame, text='Song name', background=PINK)
    label.pack()
    song_name_entry = tk.Entry(search_frame)
    song_name_entry.pack()
    search_by_song_button = tk.Button(search_frame, text='search', 
                            command=lambda: search_by_song_button_result(song_name_entry.get()))
    search_by_song_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_by_song_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search by artist name
    label = tk.Label(search_frame, text='Artist', background=PINK)
    label.pack()
    artist_entry = tk.Entry(search_frame)
    artist_entry.pack()
    search_by_artist_button = tk.Button(search_frame, text='search',
                            command=lambda: search_by_song_artist_result(artist_entry.get()))
    search_by_artist_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_by_artist_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search by word
    label = tk.Label(search_frame, text='Word', background=PINK)
    label.pack()
    word_entry = tk.Entry(search_frame)
    word_entry.pack()
    search_by_word_button = tk.Button(search_frame, text='search',
                                command=lambda: search_by_song_word_result(word_entry.get()))
    search_by_word_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_by_word_button.pack()
    
def show_words_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # -----> search by word
    label = tk.Label(search_frame, text='Word', font=FONT2, background=PINK)
    label.pack()
    word_entry1 = tk.Entry(search_frame)
    word_entry1.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_word_result(word_entry1.get()))
    search_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search by length
    label = tk.Label(search_frame, text='Length of Words', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Length', background=PINK)
    label.pack()
    length_entry = tk.Entry(search_frame)
    length_entry.pack()
    search_by_length_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_word_by_length_result(length_entry.get()))
    search_by_length_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_by_length_button.pack()  
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search word in its range
    label = tk.Label(search_frame, text='Range of Word', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Word', background=PINK)
    label.pack()
    word_entry6 = tk.Entry(search_frame)
    word_entry6.pack()
    search_range_word_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_range_word_result(word_entry6.get()))
    search_range_word_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_range_word_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search word in its range
    label = tk.Label(search_frame, text='Search words\n by stem !!!', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Word \ stem', background=PINK)
    label.pack()
    stem_entry = tk.Entry(search_frame)
    stem_entry.pack()
    search_by_stem_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_word_by_stem(stem_entry.get()))
    search_by_stem_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_by_stem_button.pack()  

def show_indexes_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # -----> search index of word
    label = tk.Label(search_frame, text='Index of word', font=FONT2, background=PINK)
    label.pack()
    word_entry2 = tk.Entry(search_frame)
    word_entry2.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_index_of_word_result(word_entry2.get()))
    search_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search index of group 
    label = tk.Label(search_frame, text='Index of group', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Group', background=PINK)
    label.pack()
    group_entry2 = tk.Entry(search_frame)
    group_entry2.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_index_of_group_result(group_entry2.get()))
    search_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search by index
    label = tk.Label(search_frame, text='Word in index', font=FONT2, background=PINK)
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
    search_by_index_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_by_index_button.pack() 

def show_groups_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # -----> search by group name
    label = tk.Label(search_frame, text='Group Name', font=FONT2, background=PINK)
    label.pack()  
    group_name_entry = tk.Entry(search_frame)
    group_name_entry.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_group_result(group_name_entry.get()))
    search_index_by_group_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search group by word
    label = tk.Label(search_frame, text='Group by word', font=FONT2, background=PINK)
    label.pack()  
    label = tk.Label(search_frame, text='word', background=PINK)
    label.pack()  
    word_entry4 = tk.Entry(search_frame)
    word_entry4.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_group_by_word_result(word_entry4.get()))
    search_index_by_group_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_index_by_group_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack(pady=15)


    # > INSERT NEW GROUPS
    label = tk.Label(search_frame, text='Create new group',
                    font=FONT4, background=PINK)
    label.pack(pady=5)

    # enter group name
    label = tk.Label(search_frame, text='Group name', background=PINK)
    label.pack()
    new_group_entry = tk.Entry(search_frame)
    new_group_entry.pack(pady=5)

    # -----> create group from selection
    label = tk.Label(search_frame, text='1. Choose words \nfrom word list', background=PINK, font=FONT2)
    label.pack()
    link = tk.Label(search_frame, text="open word list", fg="blue", cursor="hand2", background=PINK)
    link.pack()
    link.bind("<Enter>", lambda e: link.config(fg="purple"))
    link.bind("<Leave>", lambda e: link.config(fg="blue"))
    link.bind("<Button-1>", lambda e: words_for_group_button())

    add_group_button = tk.Button(search_frame, text='create',
                                    command=lambda: create_group_from_db(new_group_entry.get()))
    add_group_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    add_group_button.pack() 
    
    # -----> create group from text
    label = tk.Label(search_frame, text='2. Enter words', background=PINK, font=FONT2)
    label.pack(pady=5)
    text = tk.Text(search_frame, width=15, height=9)
    text.pack()

    add_group_button1 = tk.Button(search_frame, text='create',
                command=lambda: create_group_from_text(new_group_entry.get(), (text.get('1.0', 'end').split('\n'))))
    add_group_button1.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    add_group_button1.pack(pady=5)

def show_phrases_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # -----> search phrase by name
    label = tk.Label(search_frame, text='Phrase by name', font=FONT2, background=PINK)
    label.pack() 
    label = tk.Label(search_frame, text='phrase', background=PINK)
    label.pack()  
    phrase_name_entry = tk.Entry(search_frame)
    phrase_name_entry.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_phrase_result(phrase_name_entry.get()))
    search_index_by_group_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_index_by_group_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search phrase by word
    label = tk.Label(search_frame, text='Phrase by word', font=FONT2, background=PINK)
    label.pack()  
    label = tk.Label(search_frame, text='word', background=PINK)
    label.pack()  
    word_entry5 = tk.Entry(search_frame)
    word_entry5.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_phrase_by_word_result(word_entry5.get()))
    search_index_by_group_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_index_by_group_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()

    # -----> search phrase in songs and show context
    label = tk.Label(search_frame, text='Write a phrase \nto see its context\n in the songs', font=FONT2, background=PINK)
    label.pack()  
    label = tk.Label(search_frame, text='phrase', background=PINK)
    label.pack()  
    word_entry8 = tk.Entry(search_frame)
    word_entry8.pack()
    search_phrase_in_song_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_phrase_in_song_result(word_entry8.get()))
    search_phrase_in_song_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    search_phrase_in_song_button.pack()
    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack(pady=15)

    # > INSERT NEW PHRASES
    label = tk.Label(search_frame, text='Create new phrase',
                    font=FONT4, background=PINK)
    label.pack()

    # -----> crate phrase
    label = tk.Label(search_frame, text='Phrase Name', background=PINK)
    label.pack()
    new_phrase_entry = tk.Entry(search_frame)
    new_phrase_entry.pack()
    label = tk.Label(search_frame, text='The phrase', background=PINK)
    label.pack()
    phrase_entry = tk.Entry(search_frame)
    phrase_entry.pack()
    add_group_button = tk.Button(search_frame, text='create phrase',
                                    command=lambda: create_phrase_from_text(
                                        new_phrase_entry.get(),
                                        phrase_entry.get()))
    add_group_button.configure(fg=PURPLE, bg=YELLOW2, font=FONTB2)
    add_group_button.pack() 

def show_statistics_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    frequency_button = tk.Button(search_frame, text='Full Frequency List', background=YELLOW,
                                    command=frequency_list_statistics)
    frequency_button.pack(pady=10)

    line = tk.Label(search_frame, text='__________________________', background=PINK)
    line.pack()
    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Choose song to \n get its statistics', font=FONT2, background=PINK)
    label.pack()  
    song_entry = tk.Entry(search_frame)
    song_entry.pack(pady=10)

    # --------------- Words statistics
    label = tk.Label(search_frame, text='Words Statistics', font=FONT4, background=PINK)
    label.pack() 
    paragraph_stats_button = tk.Button(search_frame, text='By Paragraphs',
                                    command=lambda: by_paragraph_statistics(song_entry.get()))
    paragraph_stats_button.configure(width=11, background=YELLOW2)
    paragraph_stats_button.pack(pady=2)

    line_stats_button = tk.Button(search_frame, text='By Lines',
                                    command=lambda: by_line_statistics(song_entry.get()))
    line_stats_button.configure(width=11, background=YELLOW2)
    line_stats_button.pack(pady=2)

    song_stats_button = tk.Button(search_frame, text='By Words',
                                    command=lambda: by_word_statistics(song_entry.get()))
    song_stats_button.configure(width=11, background=YELLOW2)
    song_stats_button.pack(pady=2)

    # --------------- Characters statistics
    label = tk.Label(search_frame, text='Charactes Statistics', font=FONT4, background=PINK)
    label.pack() 
    paragraph_stats_button = tk.Button(search_frame, text='By Paragraphs',
                                    command=lambda: chars_by_paragraph_statistics(song_entry.get()))
    paragraph_stats_button.configure(width=11, background=YELLOW2)
    paragraph_stats_button.pack(pady=2)

    line_stats_button = tk.Button(search_frame, text='By Lines',
                                    command=lambda: chars_by_line_statistics(song_entry.get()))
    line_stats_button.configure(width=11, background=YELLOW2)
    line_stats_button.pack(pady=2)

    song_stats_button = tk.Button(search_frame, text='By Words',
                                    command=lambda: chars_by_word_statistics(song_entry.get()))
    song_stats_button.configure(width=11, background=YELLOW2)
    song_stats_button.pack(pady=2)

#endregion


#region Menu Frame
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

def phrases_button_default():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    show_phrases_search()
    df = get_full_phrase_table()
    show_result_table(df)

def statistics_button_default():
    # Clear the content frame
    for widget in result_frame.winfo_children():
        widget.destroy()

    show_statistics_search()
#endregion


#region Create the buttons and add them to the first container
songs_button = tk.Button(menu_frame, text='Songs', command=songs_button_default)
words_button = tk.Button(menu_frame, text='Words', command=words_button_default)
indexes_button = tk.Button(menu_frame, text='Indexes', command=indexes_button_default)
groups_button = tk.Button(menu_frame, text='Groups', command=groups_button_default)
phrases_button = tk.Button(menu_frame, text='Phrases', command=phrases_button_default)
statistics_button = tk.Button(menu_frame, text='Statistics', command=statistics_button_default)
add_button = tk.Button(menu_frame, text='Add New Song', command=load_new_song)

songs_button.configure(width=12, font=FONTB, background=YELLOW)
songs_button.pack()
words_button.configure(width=12, font=FONTB, background=YELLOW)
words_button.pack()
indexes_button.configure(width=12, font=FONTB, background=YELLOW)
indexes_button.pack()
groups_button.configure(width=12, font=FONTB, background=YELLOW)
groups_button.pack()
phrases_button.configure(width=12, font=FONTB, background=YELLOW)
phrases_button.pack()
statistics_button.configure(width=12, font=FONTB, background=YELLOW)
statistics_button.pack()
add_button.configure(width=12, font=FONTB, background=YELLOW)
add_button.pack()
#endregion

window.mainloop()
