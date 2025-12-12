def count_occ(lst, x):
    if not lst:
        return 0
    else:
        if lst[0] == x:
            return 1 + count_occ(lst[1:], x)
        else:
            return count_occ(lst[1:],x)
    
    
def main():
    lst = [1,1,1,1,3,3,3,3,4,4,4,4]
    x = 3
    print(count_occ(lst, x))
    
main()