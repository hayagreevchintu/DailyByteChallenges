'''

Question:
Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position.
The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.
Ex: Given the following strings:
"LR", return true
"URURD", return false
"RUULLDRD", return true

'''

#Solution begins here:
def vaccumCleanerRoute(route):
    routeDict = {'U' : 0, 'D' : 0, 'L' : 0, 'R' : 0}
    for i in route:
        routeDict[i] += 1
    if routeDict['U'] == routeDict['D'] and routeDict['L'] == routeDict['R']:
        return 'true'
    return 'false'

route = input("Enter the Vaccum Cleaner's route: ")
print(vaccumCleanerRoute(route))
