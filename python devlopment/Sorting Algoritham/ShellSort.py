def ShellSort(list):
    gap = len(list)//2
    while gap>0:
        for i in range (gap,len(list)):
            temp =  list[i]
            i=i

            while i>= gap and list[i-gap]>temp:
                list[i]  = list[i-gap]
                i-=gap
            list[i] = temp
        gap//=2
    return list     
list=[19,21,31,4,6,11,12,27]
ShellSort(list)
print(list)                
