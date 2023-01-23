import pyodbc
import pandas

def statistic_word_frequency_list():
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT word, count(*) as frequency
                            FROM [FinalProject].[dbo].[wordIndex],
                                    [FinalProject].[dbo].[words]
                            WHERE [words].wordID = [wordIndex].wordID
                            GROUP BY word
                            ORDER BY frequency DESC"""
    cursor.execute(sql_frequency_table)
    
    # define DF according to the SQL query
    word_frequency_df = pandas.DataFrame(columns=["Word", "Frequency"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            word_frequency_df.loc[len(word_frequency_df)] = [row.word,
                                            row.frequency]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return word_frequency_df


def statistic_words_in_song(song):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT max(indexNum) as 'Words'
                            FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[songs]

                            WHERE song = ?"""
    cursor.execute(sql_frequency_table, song)

    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        words = row.Words
    else:
        words = -1

    cursor.close()
    connection.close()
    return words


def statistic_words_in_paragraphs(song):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT [paragraph], count(*) as 'countWords'
                            FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[songs]

                            WHERE song = ?
                            GROUP BY paragraph
                            ORDER BY countWords DESC"""
    cursor.execute(sql_frequency_table, song)
    
    # define DF according to the SQL query
    words_in_par_df = pandas.DataFrame(columns=["Paragraph Number", "Number of Words"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            words_in_par_df.loc[len(words_in_par_df)] = [row.paragraph,
                                            row.countWords]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return words_in_par_df


def statistic_words_in_lines(song):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT [line], count(*) as 'countWords'
                            FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[songs]

                            WHERE song = ?
                            GROUP BY line
                            ORDER BY 'countWords' DESC"""
    cursor.execute(sql_frequency_table, song)
    
    # define DF according to the SQL query
    words_in_line_df = pandas.DataFrame(columns=["Line Number", "Number of Words"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            words_in_line_df.loc[len(words_in_line_df)] = [row.line,
                                            row.countWords]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return words_in_line_df


def statistic_chars_in_song(song):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT sum(length) as song_length
                                FROM [FinalProject].[dbo].[wordIndex],
                                    [FinalProject].[dbo].[songs],
                                    [FinalProject].[dbo].[words]

                                WHERE wordIndex.wordID = words.wordID and wordIndex.songID = songs.songID
                                    and song = ?

                                group by wordIndex.songID"""
    cursor.execute(sql_frequency_table, song)

    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        song_length = row.song_length
    else:
        song_length = -1

    cursor.close()
    connection.close()
    return song_length


def statistic_chars_in_paragraphs(song):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT paragraph, sum(length) as length
                            FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[songs],
                                [FinalProject].[dbo].[words]

                            WHERE wordIndex.wordID = words.wordID and wordIndex.songID = songs.songID
                                and song = ?

                            group by wordIndex.paragraph
                            order by length DESC"""
    cursor.execute(sql_frequency_table, song)
    
    # define DF according to the SQL query
    chars_in_par_df = pandas.DataFrame(columns=["Paragraph Number", "Number of Characters"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            chars_in_par_df.loc[len(chars_in_par_df)] = [row.paragraph,
                                            row.length]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return chars_in_par_df


def statistic_chars_in_lines(song):
     # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT line, sum(length) as length
                            FROM [FinalProject].[dbo].[wordIndex],
                                [FinalProject].[dbo].[songs],
                                [FinalProject].[dbo].[words]

                            WHERE wordIndex.wordID = words.wordID and wordIndex.songID = songs.songID
                                and song = ?

                            group by wordIndex.line
                            order by length DESC"""
    cursor.execute(sql_frequency_table, song)
    
    # define DF according to the SQL query
    chars_in_line_df = pandas.DataFrame(columns=["Line Number", "Number of Characters"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            chars_in_line_df.loc[len(chars_in_line_df)] = [row.line,
                                            row.length]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return chars_in_line_df

