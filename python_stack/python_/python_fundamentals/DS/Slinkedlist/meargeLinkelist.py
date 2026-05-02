class ListNode:
    def __init__(self, val):
        self.val = val        # ← غيرناها من value إلى val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


# ── Helper: بتحول list عادية إلى linked list ──
def make_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

# ── Helper: print 
def print_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result) if result else "None")


# ── Tests ──
sol = Solution()

print("Test 1: [1,2,4] + [1,3,4]")
print_list(sol.mergeTwoLists(make_list([1,2,4]), make_list([1,3,4])))

print("Test 2: [] + []")
print_list(sol.mergeTwoLists(make_list([]), make_list([])))

print("Test 3: [] + [0]")
print_list(sol.mergeTwoLists(make_list([]), make_list([0])))

print("Test 4: [1,3] + [2,4,5]")
print_list(sol.mergeTwoLists(make_list([1,3]), make_list([2,4,5])))