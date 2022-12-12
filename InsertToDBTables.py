import pyodbc
import pandas

#----------------------------insert_to_songs----------------------------#
def insert_to_songs(songID, song, artist, txtlink):
    # Exception Handling
    try:
        # Trusted Connection to Named Instance 
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

        # insert to table SONGS
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

# TODO: convet to multiple add - from dataframe
#----------------------------insert_to_words----------------------------#
def insert_to_words(wordID, word, length):

    # Exception Handling
    try:
        # Trusted Connection to Named Instance 
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

        # insert to table SONGS
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

# TODO: convet to multiple add - from dataframe
#--------------------------insert_to_wordIndex--------------------------#
def insert_to_wordIndex(wordID,songID,paragraph,line,index):

    # Exception Handling
    try:
        # Trusted Connection to Named Instance 
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
