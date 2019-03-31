# Question 6
"""
TO DO:
2. Add Comments.
"""
# Created input prompt to save integer as variable sentence
sentence = input("Please enter a sentence: ")
# Make a list of the words in the sentence.
sentenceList = sentence.split()
# Create an empty list for converted sentence
finalList = []
# Create an empty string to place words of converted sentence
finalSentence = ''
# for a number (i) select every second element with a range from 
# zero to length of sentence list.
for i in range(0, len(sentenceList), 2):
    # Add every second work to empyt list finalList
    finalList.append(sentenceList[i])
    # Add the first element of finalList to finalSentence
    finalSentence = finalList[0]
# for a number (a) select every element in finalList except the first 
for a in range(1, len(finalList)):
    # Concatinate on a space (' ') and the next word in the list
    finalSentence = finalSentence+' '+finalList[a]

# Print the final sentence.
print(finalSentence)