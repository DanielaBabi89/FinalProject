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
# Const colors:
PURPLE = "#ADA2FF"
BLUE = "#C0DEFF"
PINK = "#FFE5F1"
YELLOW = "#FFF8E1"
RED = "#850000"
FONT_BODY = ("Verdana", 12, "bold")
FONT1 = ("Verdana", 30, "bold italic")
FONT2 = ("Verdana", 10, "bold")
FONT3 = ("Verdana", 20, "bold")

# Create the main window
window = tk.Tk()
window.config(bg=YELLOW)
window.state("zoomed")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

title = tk.Label(text="SONGS CONCORDANCE", 
                font=FONT1, 
                fg=PURPLE, justify=tk.CENTER, 
                background=YELLOW)
title.pack()
title = tk.Label(text="Made By Daniela Babi", 
                font=FONT1, 
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


def load_new_song():
    src = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    src_splited = src.split("/")
    file_name = src_splited[len(src_splited)-1].split(".")[0]
    dst = "C:/Users/babid/Desktop/FinalProject/songsCSV/" + file_name + ".csv"
    load_song_to_DB(src, dst, file_name)

def create_group_from_text(groupName, data):
    define_group(groupName, data)
    
    massage = groupName + ": " + ", ".join(data)
    messagebox.showinfo('new group', "new group added: \n"+massage)

def create_group_from_db(groupName):
    selected_rows = treeview.selection()
    # Get the data of the selected rows
    data = []
    for row in selected_rows:
        item = treeview.item(row)
        data.append(item['values'][1])
    define_group(groupName, data)
    
    massage = groupName + ": " + str(data)
    messagebox.showinfo('new group', "new group added: \n"+massage)
    
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

#-------------------songs - SEARCH BUTTONS-------------------#
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

#-------------------words - SEARCH BUTTONS-------------------#
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

#-------------------word indexes - SEARCH BUTTONS-------------------#
def search_word_by_index_result(paragraph, line):
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
    
    range_string = get_words_in_next_prev_lines(word)
    if range_string != "":
        range_string = range_string.replace(word, " **" + word + "** ")
        label = tk.Label(result_frame,text=range_string, 
                        font=FONT3,
                        background=YELLOW)
        label.pack(pady=50)
    else:
        no_result_found()


#-------------------group - SEARCH BUTTONS-------------------#
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

#-------------------phrase - SEARCH BUTTONS-------------------#
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

    range_string = search_phrase_in_songs(phrase)
    if range_string != "":
        range_string = range_string.replace(phrase, " **" + phrase + "** ")
        label = tk.Label(result_frame,text=range_string, 
                        font=FONT3,
                        background=YELLOW)
        label.pack(pady=50)
    else:
        no_result_found()
    
def create_phrase_from_text(name, phrase):
    define_phrase(name, phrase)
    
    massage = name + ": " + phrase
    messagebox.showinfo('new phrase', "new phrase added: \n"+massage)

#-------------------Statistics - SEARCH BUTTONS-------------------#
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
        popup = tk.Toplevel()
        popup.title(song)

        massage = str(count) + " words in the song: " + song
        # Add a label to the pop-up window with the string "Hello, world!"
        label = tk.Label(popup, text=massage, font=("Arial", 30))
        label.pack()

def frequency_list_statistics():
    df = statistic_word_frequency_list()
    if(len(df)==0):
        no_result_found()
    else:
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
    label = tk.Label(search_frame, text='Word', font=FONT2, background=PINK)
    label.pack()
    word_entry1 = tk.Entry(search_frame)
    word_entry1.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_word_result(word_entry1.get()))
    search_button.pack()

    label = tk.Label(search_frame, text='Length of Words', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Length', background=PINK)
    label.pack()
    length_entry = tk.Entry(search_frame)
    length_entry.pack()
    search_by_length_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_word_by_length_result(length_entry.get()))
    search_by_length_button.pack()  

    label = tk.Label(search_frame, text='Range of Word', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Word', background=PINK)
    label.pack()
    word_entry6 = tk.Entry(search_frame)
    word_entry6.pack()
    search_range_word_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_range_word_result(word_entry6.get()))
    search_range_word_button.pack() 

def show_indexes_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Query - index by word
    label = tk.Label(search_frame, text='Index of word', font=FONT2, background=PINK)
    label.pack()
    word_entry2 = tk.Entry(search_frame)
    word_entry2.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_index_of_word_result(word_entry2.get()))
    search_button.pack()

    # Query - index of group
    label = tk.Label(search_frame, text='Index of group', font=FONT2, background=PINK)
    label.pack()
    label = tk.Label(search_frame, text='Group', background=PINK)
    label.pack()
    group_entry2 = tk.Entry(search_frame)
    group_entry2.pack()
    search_button = tk.Button(search_frame, text='search',
                                command=lambda: search_index_of_group_result(group_entry2.get()))
    search_button.pack()

    # Query - word by index
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
    search_by_index_button.pack() 

def show_groups_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Group Name', font=FONT2)
    label.pack()  
    group_name_entry = tk.Entry(search_frame)
    group_name_entry.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_group_result(group_name_entry.get()))
    search_index_by_group_button.pack()

    label = tk.Label(search_frame, text='Group by word', font=FONT2)
    label.pack()  
    label = tk.Label(search_frame, text='word')
    label.pack()  
    word_entry4 = tk.Entry(search_frame)
    word_entry4.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_group_by_word_result(word_entry4.get()))
    search_index_by_group_button.pack()

    
    label = tk.Label(search_frame, text='*****', background=PINK)
    label.pack(pady=15)
    label = tk.Label(search_frame, text='Select or Type \n words to create\n new group',
                    font=FONT2, background=PINK)
    label.pack()
    add_group_button = tk.Button(search_frame, text='words list', background=PINK,
                                    command=words_for_group_button)
    add_group_button.pack() 
    label = tk.Label(search_frame, text='Group Name', background=PINK)
    label.pack()
    new_group_entry = tk.Entry(search_frame)
    new_group_entry.pack()

    add_group_button = tk.Button(search_frame, text='create for selection',
                                    command=lambda: create_group_from_db(new_group_entry.get()))
    add_group_button.pack() 
    label = tk.Label(search_frame, text='Words', background=PINK)
    label.pack(pady=5)
    text = tk.Text(search_frame, width=15, height=9)
    text.pack()

    add_group_button1 = tk.Button(search_frame, text='create from text',
                command=lambda: create_group_from_text(new_group_entry.get(), (text.get('1.0', 'end').split('\n'))))
    add_group_button1.pack(pady=5)

def show_phrases_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Phrase Name')
    label.pack()  
    phrase_name_entry = tk.Entry(search_frame)
    phrase_name_entry.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_phrase_result(phrase_name_entry.get()))
    search_index_by_group_button.pack()

    label = tk.Label(search_frame, text='Phrase by word', font=FONT2)
    label.pack()  
    label = tk.Label(search_frame, text='word')
    label.pack()  
    word_entry5 = tk.Entry(search_frame)
    word_entry5.pack()
    search_index_by_group_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_phrase_by_word_result(word_entry5.get()))
    search_index_by_group_button.pack()

    label = tk.Label(search_frame, text='Phrase in songs', font=FONT2)
    label.pack()  
    label = tk.Label(search_frame, text='phrase')
    label.pack()  
    word_entry8 = tk.Entry(search_frame)
    word_entry8.pack()
    search_phrase_in_song_button = tk.Button(search_frame, text='search',
                                    command=lambda: search_phrase_in_song_result(word_entry8.get()))
    search_phrase_in_song_button.pack()

    label = tk.Label(search_frame, text='*****', background=PINK)
    label.pack(pady=15)
    label = tk.Label(search_frame, text='Select or Type \n words to create\n new phrase',
                    font=FONT2, background=PINK)
    label.pack()
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
    add_group_button.pack() 

def show_statistics_search():
    # Clear the content frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Create the entries and button, and add them to the second container
    label = tk.Label(search_frame, text='Song Statistics', font=FONT2)
    label.pack()  
    song_entry = tk.Entry(search_frame)
    song_entry.pack()

    paragraph_stats_button = tk.Button(search_frame, text='By Paragraphs',
                                    command=lambda: by_paragraph_statistics(song_entry.get()))
    paragraph_stats_button.pack()

    line_stats_button = tk.Button(search_frame, text='By Lines',
                                    command=lambda: by_line_statistics(song_entry.get()))
    line_stats_button.pack()

    song_stats_button = tk.Button(search_frame, text='By Words',
                                    command=lambda: by_word_statistics(song_entry.get()))
    song_stats_button.pack()

    frequency_button = tk.Button(search_frame, text='Full Frequency List', background=PURPLE,
                                    command=frequency_list_statistics)
    frequency_button.pack(pady=50)


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
phrases_button = tk.Button(menu_frame, text='Phrases', command=phrases_button_default)
phrases_button.pack()

phrases_button = tk.Button(menu_frame, text='Statistics',background=BLUE,
                             command=statistics_button_default)
phrases_button.pack()

phrases_button = tk.Button(menu_frame, text='Add New Song', command=load_new_song)
phrases_button.pack()


# Start the main loop
window.mainloop()
