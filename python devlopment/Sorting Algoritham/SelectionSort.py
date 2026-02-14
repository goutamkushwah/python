def SelectionSort(list):
    for item in range(len(list)):
        min_idx = item
        for j in range(item+1,len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
            
        list[item] , list[min_idx] = list[min_idx] , list[item]    
    return list                   

lst=[19,21,31,4,6,11,12,27]
a=SelectionSort(lst)
print(a)                
