def count_steps(distances) :
    ''' 
    let distances be an input list [x,y,z,...,n]
    A runner is doing exercises, sprinting back and forth between multiple lines.
    Starting at their starting position, they run x steps to get to the starting pylon,
    then run x steps back to their starting position. Then the runner runs to the
    second pylon, which is x + y steps away, then back to the starting position,
    running another x + y steps. The runner continues this pattern until they have
    reached the final pylon - note that they do not return to the starting position
    upon reaching the final pylon.
    Create a program that receives a list input containing the distances between each
    pylon (x is the distance from the starting position to the first pylon) and outputs
    the total number of steps taken by the runner throughout the whole exercise. Solve this
    program recursively.
    '''
    if not distances:
        return 0
    if len(distances) == 1:
        return distances[0]
    else:
        return count_steps(distances[:-1]) + 2*sum(distances[:-1]) + distances[-1]
    
    
    
def test(answer, expected):
    if (answer == expected):
        result = "\033[92mPASS\033[0m"
        print("PASS")
    else:
        result = "\033[91mFAIL\033[0m"
        print("ANS:", answer, "Expected:", expected)
        print(result, "\n")


input_1 = [1,2,3,4,5,6]
input_2 = [20, 21, 5, 4, 3, 21, 22]
input_3 = [20, 21, 5, 4, 3, 23, 22]
input_4 = [7, 9, 11, 13, 8, 6, 3]
input_5 = [50, 1, 1, 1, 0, 2, 1, 50]
input_6 = [50, 1, 1, 1, 55, 2, 1, 50]

test(count_steps(input_1),91)
test(count_steps(input_2),664)
test(count_steps(input_3),670)
test(count_steps(input_4),441)
test(count_steps(input_5),846)
test(count_steps(input_6),1231)


