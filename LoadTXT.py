import re
import pandas
import numpy
import pyodbc

# TODO: Parse txt to WordIndex table

def txt_to_table (src, dst, fileName):
    #-----create song DF--------
    songName = fileName.split(" - ")[0]
    artist = fileName.split(" - ")[1]
    songs_table = pandas.DataFrame({'songID':[1],'song': [songName], 'artist': [artist], 'txtlink': [src]})

    #-----create wordsIndex DF--------
    wordIndex_columnNames = ["word","song","paragraph","line","index"]
    wordIndex_table = pandas.DataFrame(columns=wordIndex_columnNames)

    with open(src, 'r', encoding='utf-8') as f:
        fullSong = f.read()

    charctersToAvoid = "!#$%^&*(),.?" 
    for charcter in charctersToAvoid:
        fullSong = fullSong.replace(charcter, " ")

    #split text into paaragraphs
    paragraphs = fullSong.split('\n\n')

    #split each paragraph into lines
    paragraphCounter = 1 
    lineCounter = 1
    wordCounter = 1
    for par in paragraphs:
        lines = par.split("\n")
        for line in lines:
            #split each line into words
            words = line.split()
            for word in words:
                newLineToLoad = [word,songName,paragraphCounter,lineCounter,wordCounter]
                wordCounter+=1
                wordIndex_table.loc[len(wordIndex_table.index)] = newLineToLoad
            lineCounter+=1
        paragraphCounter+=1
    wordIndex_table.to_csv(dst)

    #-----create words DF--------
    words_columnNames = ["wordID","word", "length"]
    words_table = pandas.DataFrame(columns=words_columnNames)
    
    words_list = pandas.Series(wordIndex_table.word).to_list()
    words_list = list(dict.fromkeys(words_list))
    wordID = 1
    
    #fil words DF
    for word in words_list:
        newLineToLoad = [wordID, word, len(word)]
        words_table.loc[len(words_table)] = newLineToLoad
        wordID += 1
    
    #------update wordsIndex df - add wordID + songID column------
    wordIndex_table = wordIndex_table.merge(words_table, how="left", on="word")
    wordIndex_table = wordIndex_table.merge(songs_table, how="left", on= "song")
    wordIndex_table = wordIndex_table.drop(columns=['song','artist', 'word', 'txtlink'])


    return songs_table, words_table, wordIndex_table

src = "C:\\Users\\babid\\Desktop\\FinalProject\\songsTXT\\Witness - Ketty Perry.txt"
dst = "C:\\Users\\babid\\Desktop\\FinalProject\\songsCSV\\Witness - Ketty Perry(toLoad).csv"
fileName = "Witness - Ketty Perry"
#txt_to_table (src, dst, fileName)

# TODO: FUNCTION : get song as txt file > parse file to df > add to words + songs + wordIndex tables
   
def load_song_to_DB():
    # TODO: find the last wordID, songID number.
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find last wordID to continue from it
    sql_max_wordID= """select wordID as max
                        from words
                        where wordID = (select MAX(wordID) from words)"""
    cursor.execute(sql_max_wordID)
    last_wordID = cursor.fetchone().max

    #find last songID to continue from it
    sql_max_wordID= """select songID as max
                        from songs
                        where songID = (select MAX(songID) from songs)"""
    cursor.execute(sql_max_wordID)
    last_songID = cursor.fetchone().max

    cursor.close()
    connection.close()
    
    #parse song to wordIndex

    #parse song to words    
    #parse song to songs

    #insert song to wordIndex
    #insert song to words
    #insert song to songs
    print()
