import pyodbc
import pandas
from auxiliaryQueries import *
from InsertToDBTables import *

def define_group(groupName, group):
 # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        # Define DF for phraseDetails
        groupDetails_df = pandas.DataFrame(columns=["groupID","wordID"])
        
        # Add one line to phrase table
        if get_groupID(groupName) == -1:
            groupID = get_last_id_from_group_table() + 1
            insert_to_group(groupID, groupName)

            for word in group:
                if word !="":     
                    if (get_wordID(word) == -1):
                        wordID = get_last_id_from_word_table() + 1
                        # word does not exists - add word to word table
                        insert_to_words(wordID, word, len(word))
                    else:
                        wordID = get_wordID(word)


                newLineToLoad = [groupID, wordID]
                groupDetails_df.loc[len(groupDetails_df)] = newLineToLoad

            for index, row in groupDetails_df.iterrows():
                insert_to_groupDetails(int(row['groupID']), int(row['wordID']))
        print(groupDetails_df)
        return groupDetails_df

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()
