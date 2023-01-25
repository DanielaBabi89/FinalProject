import pyodbc
import pandas

#------------------------ID's from tables------------------------#
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


def get_wordID(word):
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


def get_groupID(group):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_max_wordID= """select groupID
                        from [FinalProject].[dbo].[group]
                        where groupName = ?"""

    cursor.execute(sql_max_wordID, group)
    groupID = cursor.fetchone()

    cursor.close()
    connection.close()

    if (groupID == None): # first row
        return -1
    else:
        return groupID.groupID


def get_phraseID(phrase):
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_max_phraseID = """select phraseID
                        from [FinalProject].[dbo].[phrase]
                        where phraseName = ?"""

    cursor.execute(sql_max_phraseID, phrase)
    phraseID = cursor.fetchone()

    cursor.close()
    connection.close()

    if (phraseID == None): # first row
        return -1
    else:
        return phraseID.phraseID
#------------------------ID's from tables------------------------#



#----------------------last ID's from tables---------------------#
def get_last_id_from_phrase_table():
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


def get_last_id_from_word_table():
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
#----------------------last ID's from tables---------------------#



#------------------------details from tables---------------------#
def get_song_name(songID):
    # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT song
                                FROM [FinalProject].[dbo].[songs]
                                WHERE songID = ?"""
    cursor.execute(sql_frequency_table, songID)
        # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        song = row.song
    else:
        song = -1

    cursor.close()
    connection.close()
    return song


def get_song_link(songID):
    # return DataFrame of all words from DB with the speciefic index
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    # get word indexes from DB by given paragraph and line
    sql_frequency_table =  """SELECT txtlink
                                FROM [FinalProject].[dbo].[songs]
                                WHERE songID = ?"""
    cursor.execute(sql_frequency_table, songID)

    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        txtlink = row.txtlink
    else:
        txtlink = -1

    cursor.close()
    connection.close()
    return txtlink
    

def get_line_from_song(songID, line):
    path = get_song_link(songID)
    with open(path, encoding="utf-8") as file:
        song_in_lines = file.readlines()
    song_in_lines = [line for line in song_in_lines if line != '\n']
    song_in_lines = [""] + song_in_lines

    if(line < len(song_in_lines)):
        return song_in_lines[line]
    else:
        return ""
#------------------------details from tables---------------------#

    

#---------------------------text functions-----------------------#
def df_to_text(df):
    context_str = ""
    if len(df)>0:
        current_song = df.loc[0]["songID"]
        current_par = df.loc[0]["paragraph"]
        context_str += "------> "+ get_song_name(int(df.loc[0]["songID"])) + "\n"
    
    for index, row in df.iterrows():
        context_str += get_line_from_song(int(row["songID"]), int(row["line"]))
        if row["songID"] == current_song and row["paragraph"] != current_par:
            current_par = row["paragraph"]
            context_str += "\n"
        if row["songID"] != current_song:
            current_song = row["songID"]
            current_par = row["paragraph"]
            context_str += "\n\n------> "+ get_song_name(int(row["songID"])) + "\n"
    return context_str


def get_context_of_word_df(word):
    word = word.lower()
    # return DataFrame of all words from DB the located in the prev, cur, and next line of a given word
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_query = """select s.[songID]
                        ,[paragraph]
                        ,[line]
                    from [FinalProject].[dbo].[wordIndex]
                    left join [FinalProject].[dbo].[words] on [words].wordID = [wordIndex].wordID
                    left join [FinalProject].[dbo].[songs] as s on s.songID = [wordIndex].songID
                    where  wordIndex.line in (select line - 1 
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
                    group by s.songID, paragraph, line
                    order by [songID], paragraph, line"""

    cursor.execute(sql_query,word, word, word)

    # define DF according to the SQL query
    df_context_of_word = pandas.DataFrame(columns=["songID", "paragraph", "line"])
    
    # add all results from query to the DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            df_context_of_word.loc[len(df_context_of_word)] = [
                                                     row.songID,
                                                     row.paragraph,
                                                     row.line]
            row = cursor.fetchone()

    cursor.close()
    connection.close()

    return df_context_of_word


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
#---------------------------text functions-----------------------#


