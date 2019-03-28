# Question 6
"""
TO DO:
1. Deal with numbers and boolean.
"""
sentence = input("Please enter a sentence: ")
sentenceList = sentence.split()
finalList = []
finalSentence = ''
for i in range(0, len(sentenceList), 2):
    finalList.append(sentenceList[i])
    finalSentence = finalList[0]
for a in range(1, len(finalList)):
    finalSentence = finalSentence+' '+finalList[a]


print(finalSentence)