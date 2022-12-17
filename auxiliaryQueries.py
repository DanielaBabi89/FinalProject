import pyodbc
import pandas

def get_first_lineNum_in_paragraph(paragraph):
    # get paragraph number
    # return the first line number in this paragraph **in each song**
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
    cursor = connection.cursor()

    sql_find_song = """SELECT [songID], [paragraph], [line]
                        FROM [FinalProject].[dbo].[wordIndex]
                        WHERE paragraph = ? and indexNum = (SELECT MIN(indexNum)
                                                            FROM [FinalProject].[dbo].[wordIndex]
                                                            WHERE paragraph = ?)"""
    cursor.execute(sql_find_song, paragraph, paragraph)
    
    # Define DataFrame according to the SQL query
    first_lines_df = pandas.DataFrame(columns=['songID', 'paragraph', 'firstLine'])

    # add results of the query to DF
    row = cursor.fetchone()
    if(row != None):
        while row is not None:
            first_lines_df.loc[len(first_lines_df)] = [row.songID, row.paragraph, row.line]
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


print(get_first_wordNum_in_line(2))