def char_freqs(s):
    """
    Problem 2 — Character Frequency Dictionary
    Write a function char_freq(s) that:
    ● takes a string
    ● returns a dictionary mapping each character → the number of times it appears
    Example:
    char_freq("banana") → {'b': 1, 'a': 3, 'n': 2}
    """
    myDict = {}
    for i in range(len(s)):
        if s[i] in myDict:
            myDict[s[i]] += 1
        else:
            myDict[s[i]] = 1
    return myDict

def main(): 
    s = "banana"
    print(char_freqs(s))


main()

