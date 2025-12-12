def invert_dict(d):
    newDict = {}
    for key, value in d.items():
        newDict[value] = key
    return newDict

def main():
    d = {'a': 1, 'b': 2}
    print(invert_dict(d))
    
main()