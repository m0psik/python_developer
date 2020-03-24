from array import *


class ArrayList:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, *args):
        if args:
            if type(args[0]) == int:
                self.data = array('i', args)
            elif type(args[0]) == str:
                self.data = array('u', args)
            elif type(args[0]) == float:
                self.data = array('f', args)
            self.arrType = type(args[0])
        else:
            self.arrType = None
            self.data = None

    def __delitem__(self, index):
        if index >= len(self.data) or index < 0:
            raise Exception("Out of range")
        del self.data[index]

    def __str__(self):
        if self.data is None:
            return ''
        return str(self.data)

    def __getitem__(self, index):
        if index >= len(self.data) or index < 0:
            raise Exception("Out of range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index >= len(self.data) or index < 0:
            raise Exception("Out of range")
        if type(value) != self.arrType:
            raise Exception("Wrong Type")
        self.data[index] = value

    def __iter__(self):
        if self.data is None:
            return
        for i in range(self.data.buffer_info()[1]):
            yield self.data[i]

    def __len__(self):
        if self.data is not None:
            return len(self.data)
        return 0

    def __contains__(self, value):
        if self.data is not None:
            if type(value) != self.arrType:
                raise Exception("Wrong Type")
            return value in self.data
        else:
            return False

    def __reversed__(self):
        if self.data is not None:
            return self.data[::-1]

    def __iadd__(self, other):
        if other.data is None:
            return self
        if self.data is None:
            self.data = other.data
            self.arrType = other.arrType
            return self
        if self.arrType == other.arrType:
            self.data += other.data
            return self
        else:
            raise Exception("Wrong Type")

    def append(self, value):
        if self.data is not None:
            if type(value) != self.arrType:
                raise Exception("Wrong Type")
            self.data.fromlist([value])
        else:
            self.arrType = type(value)
            if type(value) == int:
                self.data = array('i', [value])
            elif type(value) == str:
                self.data = array('u', [value])
            elif type(value) == float:
                self.data = array('f', [value])

    def count(self, value):
        if self.data is None:
            return 0
        if type(value) != self.arrType:
            raise Exception("Wrong Type")
        s = 0
        for x in self.data:
            if x == value:
                s += 1
        return s

    def index(self, value):
        if self.data is None:
            raise Exception("List is empty")
        if type(value) != self.arrType:
            raise Exception("Wrong type")
        for i in range(len(self.data)):
            if self.data[i] == value:
                return i
        else:
            raise Exception("No value")

    def pop(self, index=None):
        if self.data is None:
            raise Exception("List is empty")
        if index is None:
            index = len(self.data) - 1
        while index >= len(self.data):
            index -= len(self.data)
        while index < 0:
            index += len(self.data)
        x = self.data[index]
        del self.data[index]
        return x

    def remove(self, value):
        if self.data is None:
            raise Exception("No value")
        if self.arrType != type(value):
            raise Exception("Wrong type")
        for i, x in enumerate(self.data):
            if x == value:
                self.pop(i)
                break
        else:
            raise Exception("No value")

    def extend(self, other):
        return self.__iadd__(other)

    def clear(self):
        self.data = None
        self.arrType = None
        return self
