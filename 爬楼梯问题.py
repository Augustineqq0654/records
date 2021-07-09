
def upstairs(n):
    if n < 1:       # 判断当前台阶数是否小于1
        print(0)
    if n == 1:      # 判断当前台阶数是否为1
        print(1)
    if n == 2:
        print(2)    # 判断当前台阶数是否为2

    a = 1  # 初始化边界值
    b = 2
    temp = 0
    for i in range(3, n+1):   # 迭代求解各级台阶的走法数量
        temp = a + b
        a = b
        b = temp
    print(temp)     # 输出计算结果

upstairs(10)