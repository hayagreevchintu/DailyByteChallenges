'''

Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
Ex: Given the following strings:
"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false

'''
def palindrome(string):
    return string == string[::-1]

def removechar(string,character):
    newString=""
    for i in range(len(string)):
        if i != character:
            newString += string[i]
    return newString

string = input("Enter a string: ")
count = 0
for i in range(0,len(string)):
    if palindrome(string):
        count += 1
    elif palindrome(removechar(string,i)):
        count += 1
if count == 0:
    print('false')
else:
    print('true')