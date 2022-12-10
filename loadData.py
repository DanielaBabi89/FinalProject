import pyodbc
import pandas


def insert_to_songs(songID, song, artist, txtlink):
    # Exception Handling
    try:
        # Trusted Connection to Named Instance 
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CCRSS4\SQLEXPRESS;DATABASE=FinalProject;Trusted_Connection=yes;')

        cursor=connection.cursor()

        sql_insert_to_songs = """BEGIN
                                    IF NOT EXISTS (SELECT * FROM songs 
                                                    WHERE song = ?
                                                    AND artist = ?)
                                    BEGIN
                                        INSERT INTO songs (songID, song, artist, txtlink)
                                        VALUES (?, ?, ?, ?)
                                    END
                                END"""

        # insert to table SONGS
        cursor.execute(sql_insert_to_songs, song, artist, songID, song, artist, txtlink)
        connection.commit()
        print("Done.")

        cursor.close()
        connection.close()

    except pyodbc.Error as ex:
        print("Exception: ",ex)
        cursor.close()
        connection.close()
        print("Closing program...")
        print()
        exit()

    print()