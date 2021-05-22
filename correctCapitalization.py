'''
Given a string, return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.
Ex: Given the following strings:
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true

'''

def correctCapitalization(string):
    if string[0].isupper() and (string[i].islower() for i in range(1,len(string))):
        return 'true'
    elif string.isupper() or string.islower():
        return 'true'
    return 'false'

string = input("Enter the string to be checked: ")
print(correctCapitalization(string))