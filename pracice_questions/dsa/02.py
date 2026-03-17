# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

# class Solution(object):
#     def secondHighest(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         li = sorted(set(x for x in list(s) if x.isdigit()))
#         # print(li)
#         if len(li) > 1: return int(li[-2])
#         return -1
 

# another solution much more efficient, no need to sort the whole list.
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        max1 = -1
        max2 = -1
        for c in s:
            if c.isdigit():
                d = int(c)
                if d > max1:
                    max2 = max1
                    max1 = d
                elif max1 > d > max2:
                    max2 = d
        return max2