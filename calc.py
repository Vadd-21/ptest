import numbers


class Calc:
    def is_num(self, x):
        return isinstance(x, numbers.Number)

    def add(self, x, y):
        if self.is_num(x) and self.is_num(y):
            return x + y
        else:
            raise TypeError

    def sub(self, x, y):
        if self.is_num(x) and self.is_num(y):
            return x - y
        else:
            raise TypeError

    def mul(self, x, y):
        if self.is_num(x) and self.is_num(y):
            return x * y
        else:
            raise TypeError

    def div(self, x, y):
        if y == 0:
            raise TypeError
        elif self.is_num(x) and self.is_num(y):
            return x / y
        else:
            raise TypeError
