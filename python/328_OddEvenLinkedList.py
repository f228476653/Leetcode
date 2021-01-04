# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        odd.next = even.next
        head2 = even
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = head2
        return head
if __name__ == "__main__":
    l=ListNode(73,74)
    s = Solution()
    s.oddEvenList(l)
            

        