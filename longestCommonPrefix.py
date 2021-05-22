'''
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.
Ex: Given the following arrays:
["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"
'''
def longestCommonPrefix(strings):
    if len(strings) == 0:
        return ""
    current = strings[0]
    for i in range(1,len(strings)):
        temp = ""
        if len(current) == 0:
           break
        for j in range(len(strings[i])):
            if j<len(current) and current[j] == strings[i][j]:
               temp+=current[j]
            else:
               break
        current = temp
    return current
strings = input("Enter the strings to be checked: ").split()
print("Longest common Prefix is: ",longestCommonPrefix(strings))