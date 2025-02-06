def bubble_sort(arr):
    n = len(arr)
   
    for i in range(n - 1):
        swapped = False  
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

nums = [64, 34, 25, 12, 22, 11, 90]
print("排序前:", nums)
sorted_nums = bubble_sort(nums)
print("排序后:", sorted_nums)
