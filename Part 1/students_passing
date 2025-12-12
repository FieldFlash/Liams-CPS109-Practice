def students_passing(data):
    passingList = []
    for x,y in data.items():
        passing = 0
        for i in range(len(y)):
            if y[i] <= 60:
                pass
            else:
                passing += 1
        if passing == 3:
            passingList.append(x)
    return passingList
        
def main():
    data = { 
    "Alice": [70, 85, 90], 
    "Bob": [50, 40, 62], 
    "Cara": [88, 72, 91] 
    }   
    print(students_passing(data))
    
main()