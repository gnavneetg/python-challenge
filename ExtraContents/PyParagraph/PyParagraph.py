import os
import string
inputfile = os.path.join("..", "resources","paragraph.txt")



with open(inputfile, 'r') as txtfile:
    readfile = txtfile.read()


#sentence count using dot, question mark & exclaimation marks [ ., ? , !]
sen_count = readfile.count('.') + readfile.count('?') + readfile.count('!')


#List of words 
paragraph_list = readfile.split(" ")

#counts all of the letters in list paragraph
for word in paragraph_list:
    letter_total += len(word)

#word count 
word_count = len(paragraph_list)

#Average word length 
avg_word_length = letter_total/word_count

# Calculating words per sentence 
words_per_sentence = word_count/sen_count

#outputfile 
output_file = os.path.join("..", "resources","paragraph_analysis.txt")

# Writing in output file 
with open(output_file, 'w') as txtfile:

    txtfile.write('Paragraph Analysis\n-----------------\nApproximate Word Count: ' 
                        + str(word_count)+ '\nApproximate Sentence Count: '+ str(sen_count) + 
                        '\nAverage Letter Count: ' + str(round(avg_word_length,2)) + 
                        '\nAverage Sentence Length: ' + str(words_per_sentence))

# Printing to terminal
print('Paragraph Analysis\n-----------------\nApproximate Word Count: ' 
                        + str(word_count)+ '\nApproximate Sentence Count: '+ str(sen_count) + 
                        '\nAverage Letter Count: ' + str(round(avg_word_length,2)) + 
                        '\nAverage Sentence Length: ' + str(words_per_sentence))
    