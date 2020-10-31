# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a string, return the first recurring character in it, or null if there is no recurring character.

# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

def repeatChar(string):
    hashMap = {}
    for char in string:
        if char not in hashMap:
            hashMap[char] = 0
        else:
            return char
    return -1

print(repeatChar('abcdefg'))
