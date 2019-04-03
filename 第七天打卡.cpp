public class Solution {
    public ListNode reverse(ListNode head) {
        if(null == head || null == head.next) 
          return head;
        ListNode p = head, q = head;
        while(p.next != null) 
        {
            head = p.next;
            p.next = head.next;
            head.next = q;
            q = head;
        }
        return head;
    }
}
