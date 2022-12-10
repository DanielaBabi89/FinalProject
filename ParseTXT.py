# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:14:00 2022

@author: babid
"""
import re
import pandas
import numpy

##--------------------------------------song_file_to_table----------------------------------------##
def song_file_to_table (path, fileName):
    path = "C:\\Users\\babid\\Documents\\SQL Server Management Studio\\Witness - Ketty Perry.txt"
    fileName = "Witness - Ketty Perry"
    
    #Splitting the song to list of words
    with open(path, 'r', encoding='utf-8') as f:
        words = f.readlines()
        words = ' '.join(words)
        words = words.replace("? ", ' ')
    splitedWords = re.split("[\s,?)('.]+", words)
    

    #create 3 columns
    df = pandas.DataFrame(splitedWords)  
    df.columns = ['word']
    df.insert(1,"times",[""]*(len(splitedWords)))
    df = df.groupby("word").count()

    songName = [(re.split(" - ",fileName))[0]]*(len(df))
    Artist = [(re.split("- ",fileName))[1]]*(len(df))
    Album = []

    #add columns to dataframe
    df.insert(1,"songName",songName)
    df.insert(2,"Artist",Artist)

    
    #create new file with table formatting
    df.to_csv(r'C:\\Users\\babid\\Documents\\SQL Server Management Studio\\toload Witness - Ketty Perry.txt', sep = "\t")
##--------------------------------------song_file_to_table----------------------------------------##


