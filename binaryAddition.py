'''

Question:
Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0
Ex: Given the following binary strings:
"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"

'''

#Solution begins here:
def binaryAddition(binary1, binary2):
    binary1 = int(binary1,2)
    binary2 = int(binary2,2)
    return bin(binary1 + binary2)

binary = input("Enter the binary strings: ").split()
print(str(binaryAddition(binary[0], binary[1]))[2:])
