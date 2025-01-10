class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        """Add a node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_n_after_m(self, m, n):
        """Delete N nodes after skipping M nodes."""
        current = self.head
        while current:
            # Skip M nodes
            for _ in range(m - 1):
                if not current:
                    return
                current = current.next

            if not current or not current.next:
                return

            # Start deleting N nodes
            temp = current.next
            for _ in range(n):
                if not temp:
                    break
                temp = temp.next

            # Connect the remaining nodes
            current.next = temp
            current = temp

# Example Usage
ll = LinkedList()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in data:
    ll.append(item)

print("Original Linked List:")
ll.display()

# Delete 2 nodes after skipping 3 nodes
m, n = 3, 2
ll.delete_n_after_m(m, n)

print(f"Linked List after deleting {n} nodes after every {m} nodes:")
ll.display()