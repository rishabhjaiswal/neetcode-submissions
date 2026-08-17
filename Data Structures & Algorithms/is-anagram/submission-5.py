class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if (len(s) != len(t)):
            return False
        for item in s:
            if item in hashmap.keys():
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        for item in t:
            if item in hashmap.keys():
                hashmap[item] -= 1
            else:
                return False
        if(all(value == 0 for value in hashmap.values())):
            return True
        else: 
            return False