def sum_nested(nested):
    if not nested:
        return 0
    if isinstance(nested, int):
        return nested
    return sum_nested(nested[0]) + sum_nested(nested[1:])
    
    
    
def main():
    nested = [1,[2,[3,4],5],6]
    print(sum_nested(nested))
    
main()