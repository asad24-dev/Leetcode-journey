def hasCycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

"""
When there is no cycle in the list, the loop ends when the fast pointer becomes null. 
If a cycle exists, the fast pointer moves faster and continuously loops through the cycle. 
With each step, it reduces the gap between itself and the slow pointer by one node. 
For example, if the gap is 10, the slow pointer moves by 1, increasing the gap to 11, 
while the fast pointer moves by 2, reducing the gap to 9. This process continues until 
the fast pointer catches up to the slow pointer, confirming a cycle.
"""