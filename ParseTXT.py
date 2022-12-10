import re
import pandas
import numpy

# TODO: Pasrse txt to WordIndex table

def txt_to_table (src, dst, fileName):
    songName = fileName.split(" - ")[0]
    artist = fileName.split(" - ")[1]

    columnNames = ["word","song", "artist","paragraph","line","index"]
    finalTable = pandas.DataFrame(columns=columnNames)

    with open(src, 'r', encoding='utf-8') as f:
        fullSong = f.read()

    charctersToAvoid = "!#$%^&*(),.?" 
    for charcter in charctersToAvoid:
        fullSong = fullSong.replace(charcter, " ")

    #split text into paaragraphs
    paragraphs = fullSong.split('\n\n')

    #split each paragraph into lines
    paragraphCounter = 1 
    lineCounter = 1
    wordCounter = 1
    for par in paragraphs:
        lines = par.split("\n")
        for line in lines:
            words = line.split()
            for word in words:
                newLineToLoad = [word,songName,artist,paragraphCounter,lineCounter,wordCounter]
                wordCounter+=1
                finalTable.loc[len(finalTable.index)] = newLineToLoad
            lineCounter+=1
        paragraphCounter+=1
    finalTable.to_csv(dst)


src = "C:\\Users\\babid\\Desktop\\FinalProject\\songsTXT\\Witness - Ketty Perry.txt"
dst = "C:\\Users\\babid\\Desktop\\FinalProject\\songsCSV\\Witness - Ketty Perry(toLoad).csv"
fileName = "Witness - Ketty Perry"
txt_to_table (src, dst, fileName)

    

