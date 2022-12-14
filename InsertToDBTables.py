import pyodbc
import pandas
from auxiliaryQueries import *

# this file contain function for each table in DB. 
# each function get the rellavent fields as a parameters.

#----------------------------insert_to_songs----------------------------#
def insert_to_songs(songID, song, artist, txtlink):
    song = song.lower()
    artist = artist.lower()
    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        sql_insert_to_songs = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM songs 
                                                    WHERE song = ?
                                                    AND artist = ?)
                                    BEGIN
                                        INSERT INTO songs (songID, song, artist, txtlink)
                                        VALUES (?, ?, ?, ?)
                                    END
                                END"""

        # insert to table - SONGS
        cursor.execute(sql_insert_to_songs, song, artist, songID, song, artist, txtlink)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#----------------------------insert_to_songs----------------------------#

#----------------------------insert_to_words----------------------------#
def insert_to_words(wordID, word, length):
    word = word.lower()
    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')

        cursor=connection.cursor()

        sql_insert_to_words = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM words 
                                                    WHERE word = ?)
                                    BEGIN
                                        INSERT INTO words (word, wordID, length)
                                        VALUES (?, ?, ?)
                                    END
                                END"""

        # insert to table WORDS
        cursor.execute(sql_insert_to_words, word, word, wordID, length)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#----------------------------insert_to_words----------------------------#

#--------------------------insert_to_wordIndex--------------------------#
def insert_to_wordIndex(wordID,songID,paragraph,line,index):

    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')

        cursor=connection.cursor()

        sql_insert_to_wordIndex = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM wordIndex 
                                                    WHERE wordID = ?
                                                    and songID = ?
                                                    and paragraph = ?
                                                    and line = ?
                                                    and indexNum = ?)
                                    BEGIN
                                        INSERT INTO wordIndex (wordID,songID,paragraph,line,indexNum)
                                        VALUES (?, ?, ?, ?, ?)
                                    END
                                END"""

        # insert to table wordsIndex
        cursor.execute(sql_insert_to_wordIndex, wordID,songID,paragraph,line,index,wordID,songID,paragraph,line,index)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#--------------------------insert_to_wordIndex--------------------------#

#----------------------------insert_to_phrase---------------------------#
def insert_to_phrase(phraseID, phraseName):

    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        # Add one line to phrase table
        phraseID = get_last_id_from_phrase_table() + 1

        sql_insert_to_phrase = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM phrase 
                                                    WHERE phraseID = ?
                                                    and phraseName = ?)
                                    BEGIN
                                        INSERT INTO phrase (phraseID, phraseName)
                                        VALUES (?, ?)
                                    END
                                END"""

        cursor.execute(sql_insert_to_phrase, phraseID, phraseName, phraseID, phraseName)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#----------------------------insert_to_phrase---------------------------#

#------------------------insert_to_phraseDetails------------------------#
def insert_to_phraseDetails(phraseID, wordID, wordIndex):

    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        # Add one line to phrase table
        sql_insert_to_phraseDetails = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM phraseDetails 
                                                    WHERE phraseID = ?
                                                    and wordID = ?
                                                    and wordIndex = ?)
                                    BEGIN
                                        INSERT INTO phraseDetails (phraseID, wordID, wordIndex)
                                        VALUES (?, ?, ?)
                                    END
                                END"""

        cursor.execute(sql_insert_to_phraseDetails, phraseID, wordID, wordIndex,phraseID, wordID, wordIndex)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#------------------------insert_to_phraseDetails------------------------#

#----------------------------insert_to_group----------------------------#
def insert_to_group(groupID, groupName):

    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        # Add one line to phrase table
        groupID = get_last_id_from_group_table() + 1

        sql_insert_to_group = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM [FinalProject].[dbo].[group] 
                                                    WHERE groupID = ?
                                                    and groupName = ?)
                                    BEGIN
                                        INSERT INTO [FinalProject].[dbo].[group] (groupID, groupName)
                                        VALUES (?, ?)
                                    END
                                END"""

        cursor.execute(sql_insert_to_group, groupID, groupName, groupID, groupName)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#----------------------------insert_to_group---------------------------#

#------------------------insert_to_groupDetails------------------------#
def insert_to_groupDetails(groupID, wordID):

    # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        # Add one line to groupDetails table
        sql_insert_groupDetails = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM [FinalProject].[dbo].[groupDetails] 
                                                    WHERE groupID = ?
                                                    and wordID = ?)
                                    BEGIN
                                        INSERT INTO [FinalProject].[dbo].[groupDetails] (groupID, wordID)
                                        VALUES (?, ?)
                                    END
                                END"""

        cursor.execute(sql_insert_groupDetails, groupID, wordID, groupID, wordID)
        connection.commit()

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
#------------------------insert_to_groupDetails------------------------#