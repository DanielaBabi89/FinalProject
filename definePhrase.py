import pyodbc
import pandas
from auxiliaryQueries import *
from InsertToDBTables import *

def define_phrase(phraseName, phrase):
 # Exception Handling
    try:
        # connect to DB
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')
        cursor=connection.cursor()

        # Add one line to phrase table
        phraseID = get_last_id_from_phrase_table() + 1
        insert_to_phrase(phraseID, phraseName)

        # Define DF for phraseDetails
        phraseDetails_df = pandas.DataFrame(columns=["phraseID","wordID","wordIndex"])

        phrase_toList = phrase.split()
        wordIndex = 1
 
        for word in phrase_toList:    
            if (get_wordID(word) == -1):
                wordID = get_last_id_from_word_table() +1
                # word does not exists - add word to word table
                insert_to_words(wordID, word, len(word))
            else:
                wordID = get_wordID(word)

            newLineToLoad = [phraseID, wordID, wordIndex]
            phraseDetails_df.loc[len(phraseDetails_df)] = newLineToLoad
            
            wordIndex += 1
        print (phraseDetails_df)
        for index, row in phraseDetails_df.iterrows():
            insert_to_phraseDetails(int(row['phraseID']), int(row['wordID']), int(row['wordIndex']))

        return phraseDetails_df

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()


# print(define_phrase("first line", "If i lost"))