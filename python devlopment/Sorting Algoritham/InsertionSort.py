def insertion(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
           list[j + 1] = list[j]
           j -= 1
        list[j + 1] = key    
    return list                   

lst=[19,21,31,4,6,11,12,27]
insertion(lst)
print(lst)     
