def rec_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], rec_max(lst[1:]))
    
def main():
    lst = [1,2,3,4,5,6,7,8,10]
    print(rec_max(lst))
    
main()