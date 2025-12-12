def is_pal(lst):
    if not lst:
        return True
    else:
        if lst[0] == lst[-1]:
            return is_pal(lst[1:-1])
        else:
            return False
    
def main():
    lst = ["r","a","c","e","c","a","r"]
    print(is_pal(lst))
    
main()