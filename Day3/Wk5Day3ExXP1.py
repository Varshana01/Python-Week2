# #exercise1
#
# '''Your best friend.'''
#
# def abs():
#     """Return the absolute value of the argument. """
#     pass
# def int():
#     """Return the value of the argument. """
#     pass
# def input():
#     """Return the input of the argument. """
#     pass
#
#
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)

#exercise2

class Currency():
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
    def __str__(self):
        return f'{self.amount}{self.symbol}'
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f'{self.amount}{self.symbol}'

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other:
                return self.amount + other.amount
            else:
                raise Exception("Cannot add between Currency type <dollar> and <shekel>")
        else:
            raise Exception("Cannot add except objects and ints")

c1 = Currency(' dollars ', 5)
c2 = Currency(' dollars ', 10)
c3 = Currency(' shekel ', 1)
c4 = Currency(' shekels ', 10)


print(str(c1))
print(int(c1))
print(repr(c1))
print(c1.__int__() + 5)
print(c1.__int__() + c2.__int__())
print(c1)
