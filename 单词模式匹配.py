#!/usr/bin/env python
# coding: utf-8

# 单词模式匹配
def patternMatching(wordPattern, value):
    word = value.split(' ')
    if len(word) != len(wordPattern):
        return False
    hash = {}
    used = {}
    for i in range(len(wordPattern)):
        if wordPattern[i] in hash:
            if hash[wordPattern[i]] != word[i]:
                return False
        else:
            if word[i] in used:
                return False
            hash[wordPattern[i]] = word[i]
            used[word[i]] = True
    
    return True
    
wordPattern = "abbac"
value = "dog cat cat dog fish"
print(patternMatching(wordPattern, value))







