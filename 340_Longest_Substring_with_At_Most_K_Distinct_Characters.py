"""



"""
'''
Created on Feb 18, 2017

@author: fanxueyi
'''

start = max_len = count = 0
        char_hash = {}
        
        for i in range(len(s)):
            if s[i] not in char_hash:
                count += 1
            char_hash[s[i]] = i
            if count <= k:
                max_len = max(max_len, i-start+1)
            if count > k:
                max_len = max(max_len, i-start)
                count = k
                start = min(char_hash.values())+1
                char_hash.pop(s[start-1])
        return(max_len)
                
        