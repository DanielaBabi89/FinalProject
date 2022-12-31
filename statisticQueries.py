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

print(statistic_words_in_song("Withbmhbmness"))