import pyodbc
import pandas

def get_song_by_name(song_name):
    # get song name
    # return the rellavent row from DB if exist (as dictionary), else return None
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find song by given song name
    sql_find_song = """SELECT [songID]
                            ,[song]
                            ,[artist]
                            ,[txtlink]
                        FROM [FinalProject].[dbo].[songs]
                        WHERE [song] = ?"""
    cursor.execute(sql_find_song, song_name)
    
    # Define DataFrame according to the SQL query
    songs_df = pandas.DataFrame(columns=['songID', 'song', 'artist', 'txtlink'])

    # add results of the query to DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            songs_df.loc[len(songs_df)] = [row.songID,
                                            row.song,
                                            row.artist,
                                            row.txtlink]
            row = cursor.fetchone()


    cursor.close()
    connection.close()
    return songs_df


def get_songs_by_artist(artist):
    # get artist name
    # return DF with the rellavent rows from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find song by given artist name
    sql_find_song = """SELECT [songID]
                            ,[song]
                            ,[artist]
                            ,[txtlink]
                        FROM [FinalProject].[dbo].[songs]
                        WHERE [artist] = ?"""
    cursor.execute(sql_find_song, artist)
    
    # Define DataFrame according to the SQL query
    songs_df = pandas.DataFrame(columns=['songID', 'song', 'artist', 'txtlink'])

    # add results of the query to DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            songs_df.loc[len(songs_df)] = [row.songID,
                                            row.song,
                                            row.artist,
                                            row.txtlink]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return songs_df


def get_songs_by_word(word):
    # get some words
    # return list of songs contain this word from DB if exist, else return None
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find songs by given word
    sql_find_song =     """SELECT DISTINCT songs.[songID]
                                                ,[song]
                                                ,[artist]
                                                ,[txtlink]
                            FROM [FinalProject].[dbo].[songs], [FinalProject].[dbo].[wordIndex],
                                    [FinalProject].[dbo].[words]
                            where wordIndex.wordID = words.wordID and wordIndex.songID = songs.songID
                                    and words.word = ? """
    cursor.execute(sql_find_song, word)
    
    # Define DataFrame according to the SQL query
    songs_df = pandas.DataFrame(columns=["songID", "sond", "artist", "txtlink"])

    # inset query results to DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            songs_df.loc[len(songs_df)] = [row.songID,
                                            row.song, 
                                            row.artist,
                                            row.txtlink]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return songs_df


def get_full_words_table():
    # return DF of all words from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get full words table
    sql_words_table =  """SELECT [wordID], [word], [length]
                               FROM [FinalProject].[dbo].[words]"""

    cursor.execute(sql_words_table)
    
    # define DF according to the SQL query
    words_df = pandas.DataFrame(columns=["wordID", "word", "length"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            words_df.loc[len(words_df)] = [row.wordID, row.word, row.length]
            row = cursor.fetchone()


    cursor.close()
    connection.close()
    return words_df


def get_full_wordIndex_table():
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get all word indexes from DB
    sql_wordIndex_table =  """SELECT words.[word]
                            ,songs.song
                            ,[paragraph]
                            ,[line]
                            ,[indexNum]
                        FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[words],
                                [FinalProject].[dbo].[songs] 
                        WHERE words.wordID = wordIndex.wordID and
                                songs.songID = wordIndex.songID"""
    cursor.execute(sql_wordIndex_table)
    
    # define DF according to the SQL query
    wordsIndex_df = pandas.DataFrame(columns=["word", "song", "paragraph", "line", "indexNum"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            wordsIndex_df.loc[len(wordsIndex_df)] = [row.word,
                                                    row.song,
                                                    row.paragraph,
                                                    row.line,
                                                    row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return wordsIndex_df


def get_word_by_Index(paragraph, line):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_wordIndex_table =  """SELECT words.[word]
                            ,songs.song
                            ,[paragraph]
                            ,[line]
                            ,[indexNum]
                        FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[words],
                                [FinalProject].[dbo].[songs] 
                        WHERE words.wordID = wordIndex.wordID and
                                songs.songID = wordIndex.songID and
                                wordIndex.paragraph = ? and
                                wordIndex.line = ?"""
    cursor.execute(sql_wordIndex_table,paragraph, line)
    
    # define DF according to the SQL query
    wordsIndex_df = pandas.DataFrame(columns=["word", "song", "paragraph", "line", "indexNum"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            wordsIndex_df.loc[len(wordsIndex_df)] = [row.word,
                                                    row.song,
                                                    row.paragraph,
                                                    row.line,
                                                    row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return wordsIndex_df
    

def get_words_in_next_prev_lines(word):
    # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_query = """select word
                        ,wordIndex.[wordID]
                        ,[song]
                        ,wordIndex.[songID]
                        ,[paragraph]
                        ,[line]
                        ,[indexNum]
                    from [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words], [FinalProject].[dbo].[songs]
                    where [words].wordID = [wordIndex].wordID and 
                            [songs].songID = [wordIndex].songID and
                            wordIndex.line in (select line - 1 
                                                FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words]
                                                WHERE [words].wordID = [wordIndex].wordID and
                                                        [words].word = ?

                                                union

                                                select line 
                                                FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words]
                                                WHERE [words].wordID = [wordIndex].wordID and
                                                        [words].word = ?

                                                union 

                                                select line + 1
                                                FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words]
                                                WHERE [words].wordID = [wordIndex].wordID and
                                                        [words].word = ?)
                    order by [indexNum] """

    cursor.execute(sql_query,word, word, word)

    # define DF according to the SQL query
    wordsIndex_inRange_df = pandas.DataFrame(columns=["word", "wordID", "song", "songID", "paragraph", "line", "indexNum"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            wordsIndex_inRange_df.loc[len(wordsIndex_inRange_df)] = [row.word,
                                                     row.wordID,
                                                     row.song,
                                                     row.songID,
                                                     row.paragraph,
                                                     row.line,
                                                     row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return wordsIndex_inRange_df


def get_words_by_index(paragraph, line):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_query = """SELECT word
                        ,song
                        ,artist
                        ,words.[wordID]
                        ,songs.[songID]
                        ,[paragraph]
                        ,[line]
                        ,[indexNum]
                    FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words], [FinalProject].[dbo].[songs]
                    WHERE [songs].songID = [wordIndex].songID and [words].wordID = [wordIndex].wordID and [paragraph] = ? and [line] = ?"""

    cursor.execute(sql_query,paragraph, line)

    # define DF according to the SQL query
    words_in_index_df = pandas.DataFrame(columns=["word",
                                                 "song",
                                                 "artist", 
                                                 "wordID", 
                                                 "songID", 
                                                 "paragraph", 
                                                 "line", 
                                                 "indexNum"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            words_in_index_df.loc[len(words_in_index_df)] = [row.word,
                                                 row.song,
                                                 row.artist, 
                                                 row.wordID, 
                                                 row.songID, 
                                                 row.paragraph, 
                                                 row.line, 
                                                 row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return words_in_index_df
    



print(get_words_by_index(1,3))