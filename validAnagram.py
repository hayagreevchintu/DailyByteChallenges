'''

Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.
Ex: Given the following strings:
s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false

'''
def validAnagram(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    str1 = ""
    for i in string1:
        str1 += i
    str2 = ""
    for i in string2:
        str2 += i
    return (str1 == str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print(validAnagram(string1,string2))
