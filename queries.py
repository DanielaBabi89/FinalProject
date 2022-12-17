import pyodbc

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
    
    # return txt link if the song was found. else return None 
    row = cursor.fetchone()
    if(row == None):
        song = None
    else:
        song = {'song': row.song, 'artist': row.artist, 'txtlink':row.txtlink}

    cursor.close()
    connection.close()
    return song


def get_songs_by_artist(artist):
    # get song name
    # return the rellavent row from DB if exist (as dictionary), else return {}
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find song by given song name
    sql_find_song = """SELECT [songID]
                            ,[song]
                            ,[artist]
                            ,[txtlink]
                        FROM [FinalProject].[dbo].[songs]
                        WHERE [artist] = ?"""
    cursor.execute(sql_find_song, artist)
    
    # return txt link if the song was found. else return {} 
    row = cursor.fetchone()
    if(row == None):
        songs = None
    else:
        songs = []
        while row is not None:
            songs.append ({'song': row.song, 'artist': row.artist, 'txtlink':row.txtlink})
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return songs


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
    
    # return txt link if the song was found. else return None 
    row = cursor.fetchone()
    if(row == None):
        songs = None
    else:
        songs = []
        while row is not None:
            songs.append ({'song': row.song, 'artist': row.artist, 'txtlink':row.txtlink})
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return songs


def get_full_words_table():
    # return list of all words from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find songs by given word
    sql_words_table =     """SELECT [word]
                            FROM [FinalProject].[dbo].[words]"""
    cursor.execute(sql_words_table)
    
    # return txt link if the song was found. else return None 
    row = cursor.fetchone()
    if(row == None):
        words = None
    else:
        words = []
        while row is not None:
            words.append (row.word)
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return words

print(get_full_words_table())