class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator   # числитель
        self.denominator = denominator  # знаменатель
        
    def __add__(self, other):
        # Сумма двух рациональных чисел (a/b + c/d = (ad + bc) / bd)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)
    
    def __sub__(self, other):
        # Разность двух рациональных чисел (a/b - c/d = (ad - bc) / bd)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)
    
    def __mul__(self, other):
        # Произведение двух рациональных чисел (a/b * c/d = ac/bd)
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)
    
    def __truediv__(self, other):
        # Деление двух рациональных чисел (a/b / c/d = ad/bc)
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Rational(num, den)
    
    def __float__(self):
        # Перевод рационального числа в обычное float число
        return float(self.numerator) / float(self.denominator)

