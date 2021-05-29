#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 输出单链表
ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
print(ListValue[head])
next = ListRight[head]
while next != -1:
    print(ListValue[next])
    next = ListRight[next]
print('-----------------------')

# 双向输出双链表
ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]
head = ListLeft.index(-1)
print(ListValue[head])
next = ListRight[head]
while next != -1:
    print(ListValue[next])
    next = ListRight[next]

print('----------------------')
head = ListRight.index(-1)
print(ListValue[head])
next = ListLeft[head]
while next != -1:
    print(ListValue[next])
    next = ListLeft[next]


# In[13]:


# 单链表添加一个元素
# 定义一个输出链表的函数
def Output(ListValue, ListRight, head):
    print(ListValue[head])
    next = ListRight[head]
    while next != -1:
        print(ListValue[next])
        next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
prepos = 5   # 插入的位置的上一个元素的位置

Output(ListValue, ListRight, head)
print('------------------')

# 单链表添加元素，需要已知要插入的位置的上一个元素的位置
ListValue.append(4)    # 插入数
ListRight.append(ListRight[prepos])    # 插入指针
ListRight[prepos] = len(ListValue) - 1    # 改变指针指向
Output(ListValue, ListRight, head)


# In[6]:


# 向双链表中添加元素
def Output(ListValue, ListRight, head):
    print(ListValue[head])
    next = ListRight[head]
    while next != -1:
        print(ListValue[next])
        next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]

head = 0     # 确定第一个元素的位置
prepos = 5   # 插入的位置的上一个元素的位置

Output(ListValue, ListRight, head)
print('------------------')

# 单链表添加元素，需要已知要插入的位置的上一个元素的位置
ListValue.append(4)    # 插入数
ListRight.append(ListRight[prepos])    # 插入指针
ListLeft.append(ListLeft[ListRight[prepos]])
# 或 ListLeft.append(prepos)
ListRight[prepos] = len(ListValue) - 1    # 改变指针指向
ListLeft[ListRight[prepos]] = len(ListValue) - 1
Output(ListValue, ListRight, head)


# In[8]:


# 删除单链表中的一个元素
def Output(ListValue, ListRight, head):
    print(ListValue[head])
    next = ListRight[head]
    while next != -1:
        print(ListValue[next])
        next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
prepos = 5   # 插入的位置的上一个元素的位置

Output(ListValue, ListRight, head)
print('------------------')

ListRight[prepos] = ListRight[ListRight[prepos]]
Output(ListValue, ListRight, head)


# In[10]:


# 双链表中删除一个元素
def Output(ListValue, ListRight, head):
    print(ListValue[head])
    next = ListRight[head]
    while next != -1:
        print(ListValue[next])
        next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]

head = 0     # 确定第一个元素的位置
prepos = 5   # 插入的位置的上一个元素的位置

Output(ListValue, ListRight, head)
print('------------------')

ListRight[prepos] = ListRight[ListRight[prepos]]
ListLeft[ListRight[ListRight[prepos]]] = prepos

Output(ListValue, ListRight, head)


# In[ ]:




