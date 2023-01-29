class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.peeked = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked is None:
            self.peeked = self.next()
        return self.peeked

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            ret = self.peeked
            self.peeked = None
            return ret
        else:
            return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked:
            return True
        else:
            return self.iter.hasNext()
        