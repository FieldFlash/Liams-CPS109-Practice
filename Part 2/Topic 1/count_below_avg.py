def count_below_avg(nums):
    sum = 0
    belowAvg = 0
    for i in range(len(nums)):
        sum += nums[i]
    average = sum / len(nums)

    for i in range(len(nums)):
        if nums[i] < average:
            belowAvg += 1
    
    return belowAvg
    
def main():
    nums = [1,2,3,4,5,6,7,8,9,10,11]
    print(count_below_avg(nums))
    
main()
