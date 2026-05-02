# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeLists(self, res, curr):
        if not res:
            res = curr
            return res
        
        if not curr:
            return res

        resPointer = res
        currPointer = curr

        ret = None
        if resPointer.val < currPointer.val:
            ret = resPointer
            resPointer = resPointer.next
        else:
            ret = currPointer
            currPointer = currPointer.next

        ret.next = None
        retPointer = ret

        while resPointer and currPointer:
            if resPointer.val < currPointer.val:
                retPointer.next = resPointer
                resPointer = resPointer.next
            else:
                retPointer.next = currPointer
                currPointer = currPointer.next
            
            retPointer = retPointer.next
            retPointer.next = None

        while resPointer:
            retPointer.next = resPointer
            resPointer = resPointer.next
            retPointer = retPointer.next
            retPointer.next = None

        while currPointer:
                retPointer.next = currPointer
                currPointer = currPointer.next
                retPointer = retPointer.next
                retPointer.next = None


        return ret

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        resultList = lists[0]

        for currentList in lists[1:]:
            resultList = self.mergeLists(resultList, currentList)

        return resultList