def remove_code_dups(myList):
    newList = []
    for i in range(len(myList)):
        try:
            if myList[i] != myList[i+1]:
                newList.append(myList[i])
        except IndexError:
            newList.append(myList[i])
    return newList
    
def main():
    myList = [1,1,2,2,2,3,1,1]
    print(remove_code_dups(myList))
    
main()

