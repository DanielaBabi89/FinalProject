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

        # Add one line to phrase table
        groupID = get_last_id_from_group_table() + 1
        insert_to_group(groupID, groupName)

        # Define DF for phraseDetails
        groupDetails_df = pandas.DataFrame(columns=["groupID","wordID"])

        for word in group:    
            if (get_wordID(word) == -1):
                wordID = get_last_id_from_word_table() +1
            else:
                wordID = get_wordID(word)

            newLineToLoad = [groupID, wordID]
            groupDetails_df.loc[len(groupDetails_df)] = newLineToLoad

        for index, row in groupDetails_df.iterrows():
            insert_to_groupDetails(int(row['groupID']), int(row['wordID']))

        return groupDetails_df

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()


#print(define_group("first group", ["If", "I" ,"lost"]))