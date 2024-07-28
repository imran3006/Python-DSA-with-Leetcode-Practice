"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""

def balancedStringSplit(s):
    
    r_count = 0
    l_count = 0
    rl_pair = 0

    
    for ch in s:
        if ch == 'R':
            r_count+=1
        elif ch=='L':
            l_count+=1   

        if r_count == l_count:
            rl_pair+=1 
    
    return rl_pair
        
print(balancedStringSplit("RLRRLLRLRL"))
