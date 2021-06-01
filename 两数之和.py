#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 两数之和，输出元素数组下标
def twoSum(nums, target: int):
    dict = {}
    for i in range(len(nums)):
        m = nums[i]
        if target-m in dict:
            return dict[target-m],i
        dict[m] = i
    else:
        return None

nums = [2,7,11,15]
target = 13
index = twoSum(nums, target)
print(index)


# In[ ]:




