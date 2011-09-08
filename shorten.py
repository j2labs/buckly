#!/usr/bin/env python


class BaseConverter(object):
    decimal_digits = "0123456789"
    base62 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    base52 = 'BCDFGHJKLMNPQRSTVWXYZ0123456789bcdfghjklmnpqrstvwxyz'
    
    def __init__(self, base_chars=base62):
        self.base_chars = base_chars
    
    def from_decimal(self, i):
        return self.convert(i, self.decimal_digits, self.base_chars)
    
    def to_decimal(self, s):
        return int(self.convert(s, self.base_chars, self.decimal_digits))
    
    def convert(number, fromdigits, todigits):
        # Based on http://code.activestate.com/recipes/111286/
        if str(number)[0] == '-':
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
            x = x * len(fromdigits) + fromdigits.index(digit)
    
        # create the result in base 'len(todigits)'
        if x == 0:
            res = todigits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(todigits)
                res = todigits[digit] + res
                x = int(x / len(todigits))
            if neg:
                res = '-' + res
        return res
    convert = staticmethod(convert)
