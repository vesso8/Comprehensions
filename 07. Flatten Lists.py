lists_of_nums = input().split("|")
lists_of_nums.reverse()

flatten_nums = [value for i in range(len(lists_of_nums)) for value in lists_of_nums[i].split()]
print(*flatten_nums)