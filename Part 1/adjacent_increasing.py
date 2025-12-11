def adjacent_increasing(nums):
    """
    Write a function adjacent_increasing(nums) that:
    ● takes a list of integers
    ● returns a new list containing only the integers that are strictly larger than the
    number immediately before them in the list.

    Example:
    adjacent_increasing([5, 7, 3, 9, 9, 12]) → [7, 9, 12]
    """
    newList = []
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            newList.append(nums[i])
    return newList


def main():
    nums = [5, 7, 3, 9, 9, 12]
    print(adjacent_increasing(nums))

main()