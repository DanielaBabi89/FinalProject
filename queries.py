import pyodbc
import pandas
from auxiliaryQueries import *
import nltk
from nltk.stem.snowball import SnowballStemmer


#----------------------------get_song_by_name----------------------------#
def get_song_by_name(song_name):
    song_name = song_name.lower()
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
#----------------------------get_song_by_name----------------------------#

#---------------------------get_songs_by_artist--------------------------#
def get_songs_by_artist(artist):
    artist = artist.lower()

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
#---------------------------get_songs_by_artist--------------------------#

#---------------------------get_songs_by_word----------------------------#
def get_songs_by_word(word):
    word = word.lower()

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
#---------------------------get_songs_by_word----------------------------#

#-------------------------get_full_words_table---------------------------#
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
#-------------------------get_full_words_table---------------------------#

#-------------------------get_full_songs_table---------------------------#
def get_full_songs_table():
    # return DF of all words from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get full words table
    sql_songs_table =  """SELECT [songID]
                            ,[song]
                            ,[artist]
                            ,[txtlink]
                        FROM [FinalProject].[dbo].[songs]"""

    cursor.execute(sql_songs_table)
    
    # define DF according to the SQL query
    words_df = pandas.DataFrame(columns=["songID", 
                                        "song", 
                                        "artist",
                                        "txtlink"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            words_df.loc[len(words_df)] = [row.songID, row.song, row.artist, row.txtlink]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return words_df
#-------------------------get_full_songs_table---------------------------#

#-------------------------get_full_groups_table---------------------------#
def get_full_groupDetails_table():
    # return DF of all words from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get full words table
    sql_groups_table =  """SELECT [groupName]
                                ,[word]
                            FROM [FinalProject].[dbo].[groupDetails], 
                                [FinalProject].[dbo].[group],
                                [FinalProject].[dbo].[words]
                            WHERE [groupDetails].wordID = [words].wordID 
                                    and [groupDetails].groupID = [group].groupID"""

    cursor.execute(sql_groups_table)
    
    # define DF according to the SQL query
    groups_df = pandas.DataFrame(columns=["group", 
                                        "word"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            groups_df.loc[len(groups_df)] = [row.groupName, row.word]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return groups_df
#-------------------------get_full_songs_table---------------------------#

#-------------------------get_full_phrase_table---------------------------#
def get_full_phrase_table():
    # return DF of all words from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get full words table
    sql_phrases_table =  """SELECT [phraseName]
                                ,[word]
                                ,[wordIndex]
                            FROM [FinalProject].[dbo].[phraseDetails], 
                                [FinalProject].[dbo].[phrase],
                                [FinalProject].[dbo].[words]
                            WHERE [phraseDetails].wordID = [words].wordID 
                                    and [phraseDetails].phraseID = [phrase].phraseID"""

    cursor.execute(sql_phrases_table)
    
    # define DF according to the SQL query
    phrases_df = pandas.DataFrame(columns=["Phrase", 
                                        "Word",
                                        "Word Index"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            phrases_df.loc[len(phrases_df)] = [row.phraseName, row.word, row.wordIndex]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return phrases_df
#-------------------------get_full_phrase_table---------------------------#

#-----------------------get_full_wordIndex_table-------------------------#
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
#-----------------------get_full_wordIndex_table-------------------------#

#---------------------------get_phrase_by_name----------------------------#
def get_speciefic_phrase(phrase):
    # return DF of all words from DB
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get full words table
    sql_phrases_table =  """SELECT [phraseName]
                                ,[word]
                                ,[wordIndex]
                            FROM [FinalProject].[dbo].[phraseDetails], 
                                [FinalProject].[dbo].[phrase],
                                [FinalProject].[dbo].[words]
                            WHERE [phraseDetails].wordID = [words].wordID 
                                    and [phraseDetails].phraseID = [phrase].phraseID
                                    and [phraseDetails].phraseName = ?"""

    cursor.execute(sql_phrases_table, phrase)
    
    # define DF according to the SQL query
    phrases_df = pandas.DataFrame(columns=["Phrase", 
                                        "Word",
                                        "Word Index"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            phrases_df.loc[len(phrases_df)] = [row.phraseName, row.word, row.wordIndex]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return phrases_df
#---------------------------get_phrase_by_name----------------------------#

#---------------------------get_word_by_Index----------------------------#
def get_speciefic_word(word):
    word = word.lower()
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_word_table =  """SELECT [word]
                        FROM [FinalProject].[dbo].[words]
                        WHERE [word] = ?"""
    cursor.execute(sql_word_table, word)
    
    # define DF according to the SQL query
    word_df = pandas.DataFrame(columns=["word"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            word_df.loc[len(word_df)] = [row.word]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return word_df
#---------------------------get_word_by_Index----------------------------#

#---------------------------get_word_by_Index----------------------------#
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
#---------------------------get_word_by_Index----------------------------#

#---------------------------get_word_by_length----------------------------#
def get_word_by_length(length):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_words_table =  """SELECT words.[word]
                            ,words.length
                        FROM [FinalProject].[dbo].[words]
                        WHERE words.length = ?"""
    cursor.execute(sql_words_table, length)
    
    # define DF according to the SQL query
    words_df = pandas.DataFrame(columns=["word", "length"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            words_df.loc[len(words_df)] = [row.word,
                                            row.length]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return words_df
#---------------------------get_word_by_length----------------------------#

#----------------------get_words_in_next_prev_lines----------------------#
def get_words_in_next_prev_lines(word):
    word = word.lower()
    # return DataFrame of all words from DB the located in the prev, cur, and next line of a given word
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_query = """select word
                        ,wordIndex.[wordID]
                        ,[song]
                        ,wordIndex.[songID]
                        ,[paragraph]
                        ,[line]
                        ,[indexNum]
                    from [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words], [FinalProject].[dbo].[songs] as s
                    where [words].wordID = [wordIndex].wordID and 
                            s.songID = [wordIndex].songID and
                            wordIndex.line in (select line - 1 
                                                FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words]
                                                WHERE [words].wordID = [wordIndex].wordID and
													s.songID = [wordIndex].songID and
                                                        [words].word = ?

                                                union

                                                select line 
                                                FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words]
                                                WHERE [words].wordID = [wordIndex].wordID and
												s.songID = [wordIndex].songID and
                                                        [words].word = ?

                                                union 

                                                select line + 1
                                                FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words]
                                                WHERE [words].wordID = [wordIndex].wordID and
												s.songID = [wordIndex].songID and
                                                        [words].word = ?)
                    order by [songID], [indexNum]"""

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
#----------------------get_words_in_next_prev_lines----------------------#

#-----------------------------get_words_by_index-------------------------#
def get_words_by_index(paragraph, line):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # the lines in the DB is the line number in the whole song.
    # therefor we need to calculate the actual number the the user asked for.
    # for example: line number 2 in paragraph 2 --> is line number 7 in the DB.
    real_line = int(get_first_lineNum_in_paragraph(paragraph)["firstLine"][0]) + line - 1

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

    cursor.execute(sql_query,paragraph, real_line)

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
#-----------------------------get_words_by_index-------------------------#

#------------------------------get_index_of_word-------------------------#
def get_index_of_word(word):
    word = word.lower()
    # return DataFrame of all indexes of given word
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_query = """SELECT words.[word]
                        ,songs.song
                        ,[paragraph]
                        ,[line]
                        ,[indexNum]
                    FROM [FinalProject].[dbo].[wordIndex], [FinalProject].[dbo].[words],
                            [FinalProject].[dbo].songs
                    WHERE [wordIndex].[wordID] = [words].[wordID]
                            and [songs].songID = [wordIndex].songID
                            and word = ?"""

    cursor.execute(sql_query,word)

    # define DF according to the SQL query
    indexes_of_word_df = pandas.DataFrame(columns=["word",
                                                 "song", 
                                                 "paragraph", 
                                                 "line", 
                                                 "indexNum"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            indexes_of_word_df.loc[len(indexes_of_word_df)] = [
                                                 row.word, 
                                                 row.song, 
                                                 row.paragraph, 
                                                 row.line, 
                                                 row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return indexes_of_word_df
#------------------------------get_index_of_word-------------------------#

#---------------------------get_group_by_name----------------------------#
def get_speciefic_group(groupName):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_group_table =  """SELECT [groupName]
                                ,[word]
                            FROM [FinalProject].[dbo].[groupDetails], 
                                [FinalProject].[dbo].[group],
                                [FinalProject].[dbo].[words]
                            WHERE [groupDetails].wordID = [words].wordID 
                                    and [groupDetails].groupID = [group].groupID
                                    and [groupName] = ?"""
    cursor.execute(sql_group_table, groupName)
    
    # define DF according to the SQL query
    group_df = pandas.DataFrame(columns=["Group", "word"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            group_df.loc[len(group_df)] = [row.groupName, row.word]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return group_df
#---------------------------get_group_by_name----------------------------#

#---------------------------get_group_by_word----------------------------#
def get_group_by_word(word):
    word = word.lower()

     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_group_table =  """SELECT [groupName]
                                ,[word]
                            FROM [FinalProject].[dbo].[groupDetails], 
                                [FinalProject].[dbo].[group],
                                [FinalProject].[dbo].[words]
                            WHERE [groupDetails].wordID = [words].wordID 
                                    and [groupDetails].groupID = [group].groupID
                                    and [word] = ?"""
    cursor.execute(sql_group_table, word)
    
    # define DF according to the SQL query
    group_df = pandas.DataFrame(columns=["Group", "word"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            group_df.loc[len(group_df)] = [row.groupName, row.word]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return group_df
#---------------------------get_group_by_word----------------------------#

#---------------------------get_phrase_by_word----------------------------#
def get_phrase_by_word(word):
    word = word.lower()
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_phrase_table =  """SELECT [phraseName]
                                ,[word]
                            FROM [FinalProject].[dbo].[phraseDetails], 
                                [FinalProject].[dbo].[phrase],
                                [FinalProject].[dbo].[words]
                            WHERE [phraseDetails].wordID = [words].wordID 
                                    and [phraseDetails].phraseID = [phrase].phraseID
                                    and [word] = ?"""
    cursor.execute(sql_phrase_table, word)
    
    # define DF according to the SQL query
    group_df = pandas.DataFrame(columns=["Phrase", "word"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            group_df.loc[len(group_df)] = [row.phraseName, row.word]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return group_df
#---------------------------get_phrase_by_word----------------------------#

#------------------------------get_index_of_group-------------------------#
def get_index_of_group(groupName):
 # return DataFrame of all indexes of given group name
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_query = """ SELECT  [groupDetails].[groupID]
                        ,[groupName]
                        ,[groupDetails].[wordID]
                        ,[songID]
                        ,[paragraph]
                        ,[line]
                        ,[indexNum]
                    FROM [FinalProject].[dbo].[wordIndex]
                        , [FinalProject].[dbo].[group], [FinalProject].[dbo].[groupDetails]
                    WHERE [group].[groupID] = [groupDetails].[groupID]
                        and [wordIndex].[wordID] = [groupDetails].[wordID]
                        and [groupName] = ?"""

    cursor.execute(sql_query, groupName)

    # define DF according to the SQL query
    indexes_of_group_df = pandas.DataFrame(columns=["groupID"
                                                ,"groupName"
                                                ,"wordID"
                                                ,"songID" 
                                                ,"paragraph" 
                                                ,"line"
                                                ,"indexNum"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            indexes_of_group_df.loc[len(indexes_of_group_df)] = [
                                                 row.groupID,
                                                 row.groupName,
                                                 row.wordID, 
                                                 row.songID, 
                                                 row.paragraph, 
                                                 row.line, 
                                                 row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return indexes_of_group_df
#------------------------------get_index_of_group-------------------------#

#----------------------------------df_to_csv-----------------------------#
def df_to_csv(df, file_name, dst_path):
    df.to_csv(dst_path + "\"" + file_name + ".csv",)
#----------------------------------df_to_csv-----------------------------#

#--------------------------search_phrase_in_songs------------------------#
def search_phrase_in_songs(phrase):
    phrase_to_list = phrase.split()
    context = concatenate__into_str2(get_words_in_next_prev_lines(phrase_to_list[0]), phrase)
    context = context.split("_")

    return seperate_string_to_lines(context, phrase)

#--------------------------search_phrase_in_songs------------------------#
def get_word_by_stem(given_word):
    word = word.lower()

    stemmer = SnowballStemmer("english")
    
    df = get_full_words_table()
    stems_column = [stemmer.stem(word) for word in df["word"]]
    df["stem"] = stems_column
    result = df[df["stem"] == stemmer.stem(given_word)].reset_index()
    result.drop(columns=["index"],inplace=True)
    return result
#-----------------------------get_words_by_stem--------------------------#


