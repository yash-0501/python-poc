nums = [7,8,10,25]

# print(nums[3])

# for i in nums:
#     print(i)

it = iter(nums) #convert list into iterator
print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__()) #Stop Iteration

print(next(it))

for i in nums:
    print(i) #uses iterator


