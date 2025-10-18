from decorator import time_it


class Queue_List:
    """
    Самая простая очередь на основе обычного динамического списка
    Добавление элемента в конец очереди O(n)
    Удаление элемента O(n) так как при удалении первого элемента надо сдвинуть остальные элементы списка на позицию в памяти
    Очень прост в реализации, но неэффективен там, где удаление происходит довольно часто
    """

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return not self.queue

    def __str__(self):
        return f"Queue_List: {', '.join(map(str, self.queue))}"

    @time_it
    def insert(self, item):
        self.queue.append(item)

    @time_it
    def remove(self):
        if not self.queue:
            return None

        return self.queue.pop(0)


#########################################################

class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node


class Queue_Linked:
    """
    Очередь на основе связанного списка, где каждая нода хранит ссылку на некст элемент
    Добавление делается в хвост очереди. Так как хранится указатель на хвост, операция требует лишь создание нового узла
    и переключение ссылок.
    Удаление начального элемента требюует лишь переключение указателя на следующий узел. Сложность константная O(1)
    такая же как и при добавлении

    Быстродействие методов в этой реализации накладывает дополнительные расходы на память, так как каждый элемент требует
    допонмтельной памяти для хранения указателя на следующий узел
    """
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.item))
            current = current.next

        return f"Queue_Linked: {', '.join(elements)}"

    @time_it
    def insert(self, item):
        node = Node(item)
        node.next = None
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    @time_it
    def remove(self):
        if self.length == 0:
            return None

        item = self.head.item
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.last = None

        return item
