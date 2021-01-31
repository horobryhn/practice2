from math import sqrt


def check_if_int(x):
    return int(x) == float(x)


class CalcIteration:
    def __init__(self, value):
        self.next = 0
        self.value = value

    def iter(self):
        return self

    def next(self):
        if self.next == 0:
            self.next += 1
            return self.value
        raise StopIteration


class Calculator:
    def __init__(self, init_value=0.0, valid_number_of_atr=10):
        self.value = init_value
        self.valid_number_of_atr = valid_number_of_atr

    def __setattr__(self, key, value):
        if not hasattr(self, 'valid_number_of_atr') or len(self.__dict__) < self.valid_number_of_atr:
            self.__dict__[key] = value

    def __add__(self, component):
        if isinstance(component, Calculator):
            value = component.value
        else:
            value = component
        return Calculator(self.value + value)

    def __mul__(self, component):
        if isinstance(component, Calculator):
            value = component.value
        else:
            value = component
        return Calculator(self.value * value)

    def __pow__(self, component):
        if isinstance(component, Calculator):
            value = component.value
        else:
            value = component
        if self.value < 0 and not check_if_int(value):
            return Calculator(0, True)
        else:
            return Calculator(self.value ** value)

    def __truediv__(self, component):
        if isinstance(component, Calculator):
            value = component.value
        else:
            value = component
        return Calculator(self.value / value)

    def __sub__(self, component):
        if isinstance(component, Calculator):
            value = component.value
        else:
            value = component
        return Calculator(self.value - value)

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)

    def root(self):
        self.value = sqrt(self.value)
        return self


if __name__ == '__main__':
    calculator1 = Calculator(10, 10)
    calculator2 = Calculator(3)
    print(calculator1 + 34)
    print(calculator2 - 8)
    print(calculator1 * 78)
    print(calculator1 / 2)
    print(calculator1 ** calculator2)
    calculator2.opy = 5


