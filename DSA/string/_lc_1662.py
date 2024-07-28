"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"

"""
def arrayStringsAreEqual( word1, word2 ):
    join_word1 = "".join(word1)
    join_word2 = "".join(word2)

    if join_word1 == join_word2:
        return True
    else:
        return False
    
print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))

