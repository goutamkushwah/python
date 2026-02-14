def bubbleSort(list):
    for item in range(len(list)-1,0,-1):
        # for item in range(0,len(list),1):
        for idx in range(item):
            if(list[idx] > list[idx+1]):
                temp = list[idx]
                list[idx]=list[idx+1]
                list[idx+1]=temp
    return list            
          
lst=[19,21,31,4,6,11,12,27]
a=bubbleSort(lst)
print(a)                
