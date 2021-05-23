'''

Question:
Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
Ex: Given the following strings:
"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true

'''

#Solution begins here:
def validPalindrome(string):
    initialString = ''
    reversedString = ''
    for i in string:
        if i.isalpha():
            initialString = initialString + i
            reversedString = i + reversedString
    if initialString.lower() == reversedString.lower():
        return 'true'
    return 'false'

string = input("Enter string to be checked: ")
print(validPalindrome(string))
    
