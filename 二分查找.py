numbers = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]

head ,tail = -1, len(numbers)
number = int(input('请输入要查找的数字：'))

while (tail-head) > 1:
    mid = (tail+head) // 2
    if numbers[mid] == number:
        print(f'下标是{mid}')
        break
    elif numbers[mid] > number:
        tail = mid
    else:
        head = mid
else:
    print(f'{number}不在列表中')