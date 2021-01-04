# ### [1290\. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

# Difficulty: **Easy**  

# Related Topics: [Linked List](https://leetcode.com/tag/linked-list/), [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/)


# Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1\. The linked list holds the binary representation of a number.

# Return the _decimal value_ of the number in the linked list.

# **Example 1:**

# ![](https://assets.leetcode.com/uploads/2019/12/05/graph-1.png)

# ```
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# ```

# **Example 2:**

# ```
# Input: head = [0]
# Output: 0
# ```

# **Example 3:**

# ```
# Input: head = [1]
# Output: 1
# ```

# **Example 4:**

# ```
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
# ```

# **Example 5:**

# ```
# Input: head = [0,0]
# Output: 0
# ```

# **Constraints:**

# *   The Linked List is not empty.
# *   Number of nodes will not exceed `30`.
# *   Each node's value is either `0` or `1`.


# #### Solution

# Language: **Python3**

# ```python3
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         
# ```

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        total = 0
        curr = head
        while head is not None:
            length+=1
            head = head.next
        for i in range(length-1,-1,-1):
            total += (curr.val)* 2**i
            curr =curr.next
        return total

