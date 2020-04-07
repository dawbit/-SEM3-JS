class Complex(object):
    def __init__(self, real, imag=0.0):
        self.imag = imag
        self.real = real

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __abs__(self):
        return Complex(self.real ** 2, self.imag ** 2)

    def __eq__(self, other):
        return Complex(self.real == other.real, self.imag == other.imag)

    def __str__(self):
        return return '(%g, %g)' % (self.real, self.imag)
