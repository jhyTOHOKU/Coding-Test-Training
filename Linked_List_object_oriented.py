# If the class ListNode and its constructor are defined as
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# one way of realizing the linked list (3→4→2) is defining a variable C as

def main():
    C = ListNode(3, ListNode(4, ListNode(2)))
    
# Each element of the linked list C can be printed by excuting the lines
    print(C.val) #3
    print(C.next.val) #4
    print(C.next.next.val) #2
    print(C.next.next.next) #None
    
if __name__ == "__main__":
    main()

