

#--------------------------search_phrase_in_songs------------------------#
# def search_phrase_in_songs(phrase):
#     phrase_to_list = phrase.split()
#     context = concatenate__into_str2(get_words_in_next_prev_lines(phrase_to_list[0]), phrase)
#     context = context.split("_")

#     return seperate_string_to_lines(context, phrase)
#--------------------------search_phrase_in_songs------------------------#


# def seperate_string_to_lines(context, phrase):
#     str = ""
#     for element in context:
#         deatails = element.split("*")[0]
#         appearance = element.split("*")[1]
#         print(appearance + "\n")
#         new_appearance = ""
#         if phrase in appearance:
#             str += "--" + deatails + "\n"
#             appearance_list = appearance.split()
#             count_words = 1
#             for word in appearance_list:
#                 new_appearance += word + " "
#                 if (count_words %10 == 0) and len(appearance_list) - count_words >6:
#                     new_appearance += "\n"
#                 count_words += 1
#             str += new_appearance
#             str += "\n\n"
#             new_appearance = ""
            
#     return str




# def concatenate__into_str(df):
#     str1 = ''
#     print(df)

#     prev = 0
#     current = 0
#     start = True
#     for index, row in df.iterrows():
#         if(start):
#             str1 += "--" + row.song + ", paragraph: " + str(row.paragraph) + "\n"
#             prev = row.line
#             start = False
#             str1 += row.word + " "
#             pass
#         else: 
#             current = row.line
#             if (current - 1 == prev):
#                 str1 += "\n"
#             if (current - 1 > prev):
#                 str1 += "\n\n"
#                 str1 += "--" + row.song + ", paragraph: " + str(row.paragraph) + "\n"
#             str1 += row.word + " "
#         prev = row.line
#     return str1


# def concatenate__into_str2(df, phrase):
#     # for each appreacnce - _deatails * appearace
#     str1 = ''
#     prev = 0
#     current = 0
#     start = True
#     for index, row in df.iterrows():
#         if(start):
#             str1 += "-" + row.song + ", paragraph: " + str(row.paragraph) + "*\n"
#             prev = row.line
#             start = False
#             str1 += row.word + " "
#             pass
#         else: 
#             current = row.line
#             if (current - 1 > prev):
#                 str1 += "_"
#                 str1 += "-" + row.song + ", paragraph: " + str(row.paragraph) + "*\n"

#             str1 += row.word + " "
#         prev = row.line
 
#     return str1

