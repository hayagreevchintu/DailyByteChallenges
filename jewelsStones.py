'''

Given a string representing your stones and another string representing a list of jewels,
return the number of stones that you have that are also jewels.
Ex: Given the following jewels and stones...
jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0

'''
def jewelsStones(jewels, stones):
    count = 0
    stonesDict = {}
    for i in stones:
        if i in stonesDict:
            stonesDict[i] += 1
        else:
            stonesDict[i] = 1
    for i in jewels:
        try:
            count += stonesDict[i]
        except:
            count += 0
    return count

jewels = input("Enter the jewels: ")
stones = input("Enter the stones: ")
print("Number of stones that are jewels:",jewelsStones(jewels,stones))