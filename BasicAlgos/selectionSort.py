list=[5,3,8,6,7,2]


def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if(list[minpos]>list[j]):
                minpos=j
        temp = list[i]
        list[i]= list[minpos]
        list[minpos]=temp

sort(list)
print(list)