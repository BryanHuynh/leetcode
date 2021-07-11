from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = {}
    
    for word in strs:
        s = ''.join(sorted(word))
        if s not in result.keys():
            result[s] = [word]
        else: 
            result[s].append(word)

    return(result.values())        
            


if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat",'aab','baa','aba']))