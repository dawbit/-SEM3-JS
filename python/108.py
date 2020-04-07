from queue import PriorityQueue


class Node():
    '''
    A Node with a symbol, frequency, left child, and right child.
    '''

    def __init__(self, symbol=None, frequency=None, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __str__(self):
        '''
        Return the string reprsentation of the Node.
        '''
        return "Node(" + (self.symbol).__repr__() + ", " + str(self.frequency) + ", " + str(self.left) + ", " + str(
            self.right) + ")"

    def __repr__(self):
        '''
        Return a reprsentation of the Node (the string representation is returned).
        '''
        return self.__str__()

    def __gt__(self, other):
        '''
        Return True iff this Node is greater than other.
        Criteria compared: frequency.
        '''
        if (self.frequency is None):
            return False
        if (other.frequency is None):
            return True
        return self.frequency > other.frequency


def tree_to_list(tree):
    '''
    Given the tree representation of the prefix code,
    return a list containing tuples of symbols and their corresponding code word.

    >>> tree_to_list(Node(None, None, Node(None, None, Node('A', 1, None, None), Node('B', 2, None, None)), Node('C', 3, None, None)))
    [('A', '00'), ('B', '01'), ('C', '1')]
    '''

    def _tree_to_list(tree, word):
        if tree is None:
            return []
        if tree.symbol is None:
            return _tree_to_list(tree.left, word + "0") + _tree_to_list(tree.right, word + "1")
        return [(tree.symbol, word)]

    return _tree_to_list(tree, "")


def shannon_fano(nodes):
    '''
    Given a list of nodes,
    return Shannon-Fano encoding tree representation.
    '''

    def _shannon_fano(nodes):
        length = len(nodes)
        if length == 1:
            return nodes[0]
        if length == 2:
            return Node(None, None, nodes[0], nodes[1])

        # Figure out where to split the list.    
        total = 0
        for i in range(length):
            total += nodes[i].frequency
        second_half_total = 0
        index = length

        while (index >= 0) and (second_half_total <= (total - second_half_total)):
            index -= 1
            second_half_total += nodes[index].frequency

        diff1 = second_half_total - (total - second_half_total)
        diff2 = abs(diff1 - (2 * nodes[index].frequency))
        if (diff2 < diff1):
            index += 1

        left = _shannon_fano(nodes[0:index])
        right = _shannon_fano(nodes[index:])

        return Node(None, None, left, right)

    nodes.sort()
    nodes.reverse()
    if len(nodes) == 1:
        return Node(None, None, nodes[0], None)
    return _shannon_fano(nodes)


def huffman(nodes):
    '''
    Given a list of nodes,
    return the Huffman encoding tree representation. 
    '''
    trees = PriorityQueue()  # elements: (total_frequency, tree)
    for node in nodes:
        trees.put((node.frequency, node))

    while (trees.qsize() > 1):
        min1 = trees.get()
        min2 = trees.get()
        trees.put((min1[0] + min2[0], Node(None, None, min1[1], min2[1])))

    return trees.get()[1]