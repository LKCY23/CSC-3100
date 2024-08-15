from Pointer import Linked_List_Node
from Linked_List_Seq import Linked_List_Seq


class Cycle_Linked_List(Linked_List_Seq):
    def __init__(self):
        super().__init__()
        self.cycle_size = 0
        self.cycle_start_node = None
        self.start_index = 0

    def create_cycle(self, start_index):
        """ 创建循环，将链表的最后一个节点的 next 指向索引为 start_index 的节点 """
        if start_index >= self.size or self.head is None:
            return  # start_index 超出范围或链表为空，不执行操作

        tail = self.head
        while tail.next:
            tail = tail.next

        # 找到循环开始的节点
        cycle_start_node = self.head
        for _ in range(start_index):
            cycle_start_node = cycle_start_node.next
        
        # 创建循环
        tail.next = cycle_start_node

        self.start_index = start_index
        self.cycle_size = self.size - start_index
        self.cycle_start_node = cycle_start_node

        return 


    def find_cycle_length(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next  # 慢指针移动一步
            fast = fast.next.next  # 快指针移动两步

            if slow == fast:  # 检测到循环
                # 找到循环长度
                cycle_length = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next
                    cycle_length += 1
                return cycle_length
        return 0  # 无循环


if __name__ == '__main__':

    ll = Cycle_Linked_List()
    ll.build([1, 2, 3, 4, 5])  # 创建一个链表 1 -> 2 -> 3 -> 4 -> 5
    ll.create_cycle(2)  # 创建一个循环，开始于索引2（即节点3），形成 1 -> 2 -> 3 -> 4 -> 5 -> 3 ...

    print("Cycle length:", ll.find_cycle_length())  # 应该输出循环的长度，这里是 4
    
