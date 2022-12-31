import pyodbc
import pandas

# TODO: Add try & except


def get_first_lineNum_in_paragraph(paragraph):
    # get paragraph number
    # return the first line number in this paragraph **in each song**
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_find_song = """SELECT [songID], [paragraph], [line], [indexNum]
                        FROM [FinalProject].[dbo].[wordIndex]
                        WHERE paragraph = ? and indexNum = (SELECT MIN(indexNum)
                                                            FROM [FinalProject].[dbo].[wordIndex]
                                                            WHERE paragraph = ?)"""
    cursor.execute(sql_find_song, paragraph, paragraph)
    
    # Define DataFrame according to the SQL query
    first_lines_df = pandas.DataFrame(columns=['songID', 'paragraph', 'firstLine', 'indexNum'])

    # add results of the query to DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            first_lines_df.loc[len(first_lines_df)] = [row.songID, row.paragraph, row.line, row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return first_lines_df


def get_first_wordNum_in_line(line):
    # get line number
    # return the first word index in this line number **in each song**
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # sql query
    sql_find_song = """SELECT [wordID]
                            ,[songID]
                            ,[paragraph]
                            ,[line]
                            ,[indexNum]
                        FROM [FinalProject].[dbo].[wordIndex]
                        WHERE line = ? and indexNum = (SELECT MIN(indexNum)
                                                            FROM [FinalProject].[dbo].[wordIndex]
                                                            WHERE line = ?)"""
    cursor.execute(sql_find_song, line, line)
    
    # Define DataFrame according to the SQL query
    first_lines_df = pandas.DataFrame(columns=['wordID', 'songID', 'paragraph', 'line', 'indexNum'])

    # add results of the query to DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            first_lines_df.loc[len(first_lines_df)] = [row.wordID, row.songID, row.paragraph, row.line, row.indexNum]
            row = cursor.fetchone()

    cursor.close()
    connection.close()
    return first_lines_df


def get_last_id_from_phrase_table ():
    # return the last phraseID in phrase table
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find last wordID to continue from it
    sql_max_wordID= """select phraseID as max
                        from phrase
                        where phraseID = (select MAX(phraseID) from phrase)"""
    cursor.execute(sql_max_wordID)
    
    last_phraseID = cursor.fetchone()
    
    cursor.close()
    connection.close()

    if (last_phraseID == None): # first row
        return 0
    else:
        return last_phraseID.max


def get_last_id_from_word_table ():
    #return the last ID that in the DB tables: words and songs
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find last wordID to continue from it
    sql_max_wordID= """select wordID as max
                        from words
                        where wordID = (select MAX(wordID) from words)"""
    cursor.execute(sql_max_wordID)
    last_wordID = cursor.fetchone()

    cursor.close()
    connection.close()

    if (last_wordID == None): # first row
        return 0
    else:
        return last_wordID.max


def get_wordID (word):
    #return the last ID that in the DB tables: words and songs
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find last wordID to continue from it
    sql_max_wordID= """select wordID
                        from words
                        where word = ?"""

    cursor.execute(sql_max_wordID, word)
    wordID = cursor.fetchone()

    cursor.close()
    connection.close()

    if (wordID == None): # first row
        return -1
    else:
        return wordID.wordID


def get_last_id_from_group_table():
    # return the last groupID in group table
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    #find last groupID to continue from it
    sql_max_groupID= """select groupID as max
                        from [FinalProject].[dbo].[group]
                        where groupID = (select MAX(groupID) from [FinalProject].[dbo].[group])"""
    cursor.execute(sql_max_groupID)
    
    last_groupID = cursor.fetchone()
    
    cursor.close()
    connection.close()

    if (last_groupID == None): # first row
        return 0
    else:
        return last_groupID.max


def concatenate__into_str(df):
    str = ''

    prev = 0
    current = 0
    start = True
    for index, row in df.iterrows():
        if(start):
            prev = row.line
            start = False
            str += row.word + " "
            pass
        else: 
            current = row.line
            if (current - 1 == prev):
                str += "\n"
            if (current - 1 > prev):
                str += "\n\n"
            str += row.word + " "
        prev = row.line
    return str
# USE ME: int(get_first_lineNum_in_paragraph(2)["firstLine"][0])
