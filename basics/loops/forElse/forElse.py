nums = [12,16,18,2,26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else: print("not found") #since this loop is never breaked


nums = [12,16,15,2,26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else: print("not found") #prints 15 since loop is for the loop

#USED ONLY WITH BREAK STATEMENTS