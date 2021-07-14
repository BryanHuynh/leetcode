def firstUniqChar(s: str) -> int:
    occurances = {}
    index = {}
    for i in range(len(s)):
        if(s[i] in occurances):
            occurances.update({s[i]: occurances[s[i]] + 1})
        else:
            occurances.update({s[i]: 1})
            index.update({s[i]: i})
    for i in index:
        if occurances[i] == 1:
            return index[i]
    return -1




if __name__ == '__main__':
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aabb"))