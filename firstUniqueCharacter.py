'''

Given a string, return the index of its first unique character. If a unique character does not exist, return -1.
Ex: Given the following strings:
"abcabd", return 2
"thedailybyte", return 1
"developer", return 0

'''
def firstUniqueCharacter(string):
    characterCount = {}
    for i in string:
        if i in characterCount:
            characterCount[i] += 1
        else:
            characterCount[i] = 1
    for i in range(len(string)):
        if characterCount[string[i]] == 1:
            return i
    return -1

string = input("Enter the string:")
print("The first unique character's index is: ", firstUniqueCharacter(string))    