import unittest

#1-->2-->3-->4-->5-->null
#5-->4-->3-->2-->1-->null
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#class Solution1:
    # @param {ListNode} head
    # @return {ListNode}
    # def reverseList1(self, head):
    #     pre = None
    #     cur = head
    #     lat = head.next

    #     while lat != None:
    #         cur.next = pre
    #         pre = cur
    #         cur = lat
    #         lat = lat.next

    #     cur.next = pre
    #     return cur
    """
    https://www.cnblogs.com/jiqing9006/p/7615467.html
    https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-zhi-chang-gui-si-lu-he-die-dai/

    Step 1
        pre   cur  lat
        null   1 -> 2 -> 3 -> 4 -> 5 -> null
        
        cur.next = pre
        pre   cur  lat
        null <-1    2 -> 3 -> 4 -> 5 -> null
        
        pre = cur，cur = lat，lat = lat.next
              pre  cur  lat
        null <-1    2 -> 3 -> 4 -> 5 -> null
    
    Step 2
              pre  cur  lat
        null <-1    2 -> 3 -> 4 -> 5 -> null

        cur.next = pre
              pre  cur  lat
        null <-1 <--2 -> 3 -> 4 -> 5 -> null

        pre = cur，cur = lat，lat = lat.next
                    pre  cur  lat
        null <-1 <--2 -> 3 -> 4 -> 5 -> null

    Step 3
                    pre  cur  lat
        null <-1 <--2 -> 3 -> 4 -> 5 -> null

        cur.next = pre
                    pre  cur  lat
        null <-1 <--2 <--3 -> 4 -> 5 -> null

        pre = cur，cur = lat，lat = lat.next
                        pre  cur  lat
        null <-1 <--2 <--3 -> 4 -> 5 -> null
    
    Step 3
                        pre  cur  lat
        null <-1 <--2 <--3 -> 4 -> 5 -> null

        cur.next = pre
                        pre  cur  lat
        null <-1 <--2 <--3 <-- 4 -> 5 -> null

        pre = cur，cur = lat，lat = lat.next
                            pre   cur   lat
        null <-1 <--2 <--3 <--4 -> 5 -> null
    step 4
        cur.next = pre
                            pre   cur   lat
        null <-1 <--2 <--3 <--4<-- 5   null
    """

class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = None
        c = head
        while c!=None:
            n = c.next
            c.next = p
            p = c
            c = n
        print(p.val)
        return p

if __name__ == "__main__":
    s = Solution2()
    node=ListNode([1,2,3,4,5])
    a= s.reverseList(node)