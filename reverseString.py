'''

Question:
Given a string, reverse all of its characters and return the resulting string.
Ex: Given the following strings:
“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”

'''

#Solution begins here:
def reverseString(string):
    n = len(string)
    i = 0
    j = n-1
    while(i < j):
        string[i], string[j] = string[j] , string[i]
        i += 1
        j -= 1
    return string
string = input("Enter string to be reversed: ")
string = [i for i in string]
reversedString = reverseString(string)
print("Reversed String is: ", end='')
for i in reversedString:
    print(i, end='')
