'''

Question:
Given two strings representing sentences, return the words that are not common to both strings 
(i.e. the words that only appear in one of the sentences). 
You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.
Ex: given the following strings:
sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]

'''
def uncommonWords(string1, string2):
    string = string1 + ' ' + string2
    string = string.split()
    wordsDict = {}
    uncommonWordsList = []
    for i in string:
        if i in wordsDict.keys():
            wordsDict[i] += 1
        else:
            wordsDict[i] = 1
    for i in wordsDict.keys():
        if wordsDict[i] == 1:
            uncommonWordsList.append(i)
    return uncommonWordsList

string1 = input("Enter the first sentence: ")
string2 = input("Enter the second sentence: ")
print("The words that are not common to both the strings are ",uncommonWords(string1,string2))