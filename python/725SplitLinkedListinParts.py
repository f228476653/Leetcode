class Solution2:
    def splitListToParts(self, root: 'ListNode', k: 'int') -> 'List[ListNode]':
        n, p, res = 0, root, []
        while p:
            n, p = n + 1, p.next
        a, m, start = n // k, n % k, root
        for _ in range(k):
            if not start: res.append(None)
            else:
                end = start
                for _ in range(a + (1 if m else 0) - 1):
                    end = end.next
                if m > 0: m -= 1
                res.append(start)
                start = end.next
                end.next = None
        return res

if if __name__ == "__main__":
    ListNode([3,5,6])
    Solution2()

