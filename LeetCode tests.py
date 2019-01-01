
# LeetCode 1: Two Sum

if(1):
    stopword = ""
    nums = []
    for line in iter(input, stopword):
        line = int(line)
        nums.append(line)
    target = int(input("target="))


    def twoSum(nums, target):
        d = {}
        for i in range(len(nums)):
            the_other_num = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[the_other_num] = i
        #    nums_remove = nums
        #    nums_remove.remove(nums[i])
        #    hash_minus_a_num = dict(zip(nums_remove, range(len(nums_remove))))
        #    if hash_minus_a_num.get(the_other_num):
        #    return [i, hash_minus_a_num[the_other_num]+1]


    print(twoSum(nums, target))


