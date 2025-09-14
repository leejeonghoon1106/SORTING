def bubble_sort (list):
    for i in range(len(list)):
        for j in range (len(list)-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

def merge_sort (list):
    count = 0
    left_list = list[0:len(list)//2]
    right_list = list[len(list)//2:]

    if len(list) > 1:
        merge_sort(left_list)
        merge_sort(right_list)
    
    i = 0
    j = 0
    k = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            list[k] = left_list[i]
            i += 1
        else:
            list[k] = right_list[j]
            j += 1
        k += 1
    while i < len(left_list) or j < len(left_list):
        if i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        if j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

    return list


list = [7,3,6,32,15,17,34,26]

print(f'{bubble_sort(list)} 버블 정렬 알고리즘')
print(f'{merge_sort(list)} 병합 정렬 알고리즘')