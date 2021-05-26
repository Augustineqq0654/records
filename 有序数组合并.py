arr1 = [1, 3, 4, 6, 10]
arr2 = [2, 5, 8, 11, 15]

arr3 = arr1.copy()         # 复制数组1
i = 0
for j in range(len(arr2)):
    while i < len(arr1):        # 用数组1而不要用新的数组3作为判断条件
        if arr2[j] < arr1[i]:
            arr3.insert(i+j, arr2[j])   # 插入数据
            break                       # 插入数据后选择下一个数据
        else:
            i += 1
    else:
        arr3 = arr3 + arr2[j:]          #若数大于数组1中的最后一个，直接拼接
        break
print(arr3)
