class MyLinked():
    def __init__(self):
        self.head = None

    def add_value(self, value):
        '''Add node in the head'''
        if self.head is None:
            self.head = SingeLinkedNode(value)
        else:
            node = SingeLinkedNode(value)
            self.add_node(node)

    def add_node(self, node):
        node.next = self.head
        self.head = node

    def __repr__(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return '->'.join(map(lambda x:str(x),result))

    def reverse(self):
        '''reverse the link'''
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            self.head = current_node
            current_node = next_node
        return self #链式调用



class MyLink2():
    def __init__(self):
        self.head = SingeLinkedNode(None)

    def add_value(self, value):
        node = SingeLinkedNode(value)
        return self.add_node(node)


    def add_node(self, node):
        node.next = self.head.next
        self.head.next = node
        return node

    def __repr__(self):
        result = []
        if self.head:
            current_node = self.head.next
            while current_node is not None:
                result.append(current_node.value)
                current_node = current_node.next
            return '->'.join(map(lambda x: str(x), result))
        else:
            return ''

    def reverse(self):
        if self.head.next:
            current_node = self.head.next
            next_node = current_node.next
            current_node.next = None #split the list into two parts
            while next_node:
                current_node = next_node
                next_node = next_node.next
                current_node.next = self.head.next
                self.head.next = current_node
        return self

    def get_middle_node(self):
        '''类似减速齿轮,不光可以计算一半，还可以计算其他节点'''
        if self.head.next:
            i = 0
            current_node = self.head.next
            mid_node = self.head
            while current_node:
                if i%2==0:
                    mid_node = mid_node.next
                current_node = current_node.next
                i += 1
            return mid_node
        else:
            return None

    def delete_node(self, index, reverse=False):
        '''use a ruler'''
        if index <=0:
            raise Exception('index should bigger than 0')
        if reverse==True:
            current_node = self.head.next
            ruler = 1
            previous_node = self.head
            while current_node:
                if ruler < index+1:
                    ruler += 1
                elif ruler == index+1:
                    previous_node = previous_node.next
                current_node = current_node.next
            if ruler==index+1:
                previous_node.next = previous_node.next.next

    def detect_circle(self):
        current_slow = self.head
        current_quick = self.head
        while current_quick and current_quick.next:
            current_slow = current_slow.next
            current_quick = current_quick.next.next
            if current_slow == current_quick:
                return True
        return False





def merge_sorted_link2(link1, link2):
    current1 = link1.head.next
    current2 = link2.head.next
    link = MyLink2()
    while True:
        if current1 is None and current2 is None:
           break
        elif current1 is None and current2 is not None:
            while current2:
                link.add_value(current2.value)
                current2 = current2.next
            break
        elif current1 is not None and current2 is None:
            while current1:
                link.add_value(current1.value)
                current1 = current1.next
            break
        elif current1 is not None and current2 is not None:
            if current1.value <= current2.value:
                link.add_value(current1.value)
                current1 = current1.next
            else:
                link.add_value(current2.value)
                current2 = current2.next
    return link


class SingeLinkedNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def test_reverse():
    #r = map(lambda x:MyLinked(x), list('abcdefgh'))
    #for i in range(len(r)-1):
    #   r[i].next = r[i+1]
    linked = MyLinked()
    linked.add_value('f')
    linked.add_value('e')
    linked.add_value('d')
    linked.add_value('c')
    linked.add_value('b')
    linked.add_value('a')
    print(linked)
    linked.reverse()
    print(linked)

def test_MyLink2_reverse():
    #r = map(lambda x:MyLinked(x), list('abcdefgh'))
    #for i in range(len(r)-1):
    #   r[i].next = r[i+1]
    linked = MyLink2()
    linked.add_value('f')
    linked.add_value('e')
    linked.add_value('d')
    linked.add_value('c')
    linked.add_value('b')
    linked.add_value('a')
    print(linked)
    linked.reverse()
    print(linked)


def test_MyLink2_mid_node():
    #r = map(lambda x:MyLinked(x), list('abcdefgh'))
    #for i in range(len(r)-1):
    #   r[i].next = r[i+1]
    linked = MyLink2()
    linked.add_value('e')
    linked.add_value('d')
    linked.add_value('c')
    linked.add_value('b')
    linked.add_value('a')
    print(linked)
    print(linked.get_middle_node())
    linked.add_value('z')
    print(linked)
    print(linked.get_middle_node())


def test_MyLink2_delete_node():
    #r = map(lambda x:MyLinked(x), list('abcdefgh'))
    #for i in range(len(r)-1):
    #   r[i].next = r[i+1]
    linked = MyLink2()
    linked.add_value('e')
    linked.add_value('d')
    linked.add_value('c')
    linked.add_value('b')
    linked.add_value('a')
    print(linked)
    linked.delete_node(index=2, reverse=True)
    print(linked)
    linked.delete_node(index=3, reverse=True)
    print(linked)
    linked.delete_node(index=3, reverse=True)
    print(linked)
    linked.delete_node(index=3, reverse=True)
    print(linked)


def test_MyLink2_detect_circle():
    linked = MyLink2()
    node_e = linked.add_value('e')
    linked.add_value('d')
    linked.add_value('c')
    node_b = linked.add_value('b')
    #node_e.next = node_b
    linked.add_value('a')
    print(linked.detect_circle())

def test_merge_sorted_link2():
    link1 = MyLink2()
    link1.add_value(9)
    link1.add_value(6)
    link1.add_value(4)
    link1.add_value(1)
    print(link1)
    link2 = MyLink2()
    link2.add_value(7)
    link2.add_value(5)
    link2.add_value(4)
    link2.add_value(3)
    link2.add_value(1)
    print(link2)
    print(merge_sorted_link2(link1, link2).reverse())


if __name__ == '__main__':
    #test_reverse()
    #test_MyLink2_reverse()
    #test_MyLink2_mid_node()
    #test_MyLink2_delete_node()
    #test_merge_sorted_link2()
    test_MyLink2_detect_circle()
