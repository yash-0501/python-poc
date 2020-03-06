nums = [25,12,33]
print(nums)
print(nums[0])
print(nums[1:])
print(nums[-1])
print(nums[-3])

names = ['raj','ram','raviraj']
print(names)

values = [25,'raj',2.5] 
print(values)

mil= [names,nums]
print(mil)

nums.append(45)
print(nums)

nums.insert(2,90)
print(nums)

nums.remove(12)
print(nums)


print(nums.pop())

del nums[2:]
print(nums)

nums.extend([29,13,20,48,16])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
