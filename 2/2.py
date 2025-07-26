# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # idea: sommo numero per numero e mi porto dietro il riporto(carry) se superano 10
        # finche una delle due liste non è vuota vado avanti e faccio la somma numero per numero
        # se una delle due finisce e non ho piu riporto posso finire altrimenti vado avanti 
        # e continuo la somma tra riporto e numeri che restano
        head = ListNode(0)
        res = head
        # carry è il riporto, inizialmente 0
        carry=0
        while l1 is not None or l2 is not None:
            calc = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if calc >= 10:
                calc = calc - 10
                carry = 1
            else:
                carry = 0
            res.val = calc
            # scorro in avanti tutto
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # se ho ancora carry e non ho finito le liste creo un nuovo nodo
            if l1 is not None or l2 is not None or carry > 0:
                res.next = ListNode(0)  # creo il prossimo nodo
                res = res.next
        # se ho ancora carry alla fine lo metto nel nodo finale
        # altrimenti non lo metto e il nodo finale sarà 0
        if carry > 0:
            res.val = carry
        else:
            res = None
        return head
        