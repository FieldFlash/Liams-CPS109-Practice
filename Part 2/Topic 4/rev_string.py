def rev(s):
    if s == "":
        return s
    else:
        return s[-1] + rev(s[:-1])
    
    
def main():
    s = "hello"
    print(rev(s))
    
    
main()