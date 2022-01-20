class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        fast_pointer = head
        slow_pointer = head
        
        while True:
            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            
            if fast_pointer:
                fast_pointer = fast_pointer.next
            
            if not fast_pointer:
                return None
            
            if slow_pointer == fast_pointer:
                break
                
        start = head
        while start != slow_pointer:
            start = start.next
            slow_pointer = slow_pointer.next
            
        return start
        
