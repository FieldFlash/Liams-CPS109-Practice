def first_decline(nums):
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return i
    return -1
    
    
def main():
    nums = [1,1,1,1,1,1,3,1]
    print(first_decline(nums))
    
main()