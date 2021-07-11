def twoSum(nums, target):  
    dict = {nums[i]: [] for i in range(0, len(nums))}
    for i in range(len(nums)):
        dict[nums[i]].append(i)
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in dict.keys():
            for j in dict[difference]:
                if i != j:
                    return [i,j]


if __name__ == '__main__':
    print(twoSum([2,7,11,15,15],9))
    print(twoSum([3,3],6))
    print(twoSum([3,2,4],6))