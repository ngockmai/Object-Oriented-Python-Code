import math

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator', numerator, 'must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('Denominator', denominator, 'must be an integer')
        self.numerator = numerator
        self.denominator = denominator
        
        # Use the math package to find the greatest common divisor
        greatestCommonDivisor = math.gcd(self.numerator, self.denominator)
        if greatestCommonDivisor > 1:
            self.numerator = self.numerator // greatestCommonDivisor
            self.denominator = self.denominator // greatestCommonDivisor
        self.value = self.numerator / self.denominator

        # Normalize the sign of the numerator and denominator
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        '''Create a string representation of the fraction'''
        output = 'Fraction: ' + str(self.numerator) + '/' + \
                 str(self.denominator) + '\n' +\
                'Value: ' + str(self.value) + '\n'
        return output     

    def __add__(self, oOtherFraction):
        ''' Add two Fraction objects'''
        if not isinstance(oOtherFraction, Fraction):
            raise TypeError('Second value in attempt to add is not a Fraction')
        # Use the math package to find the least common multiple
        newDenominator = math.lcm(self.denominator, oOtherFraction.denominator)
        
        selfMultiplicationFactor = newDenominator // self.denominator
        selfEquivalentNumerator = self.numerator * selfMultiplicationFactor
     
        otherMultiplicationFactor = newDenominator // oOtherFraction.denominator
        oOtherFractionEquivalentNumerator = oOtherFraction.numerator * otherMultiplicationFactor

        newNumerator = selfEquivalentNumerator + oOtherFractionEquivalentNumerator

        oAddedFraction = Fraction(newNumerator, newDenominator)
        return oAddedFraction

    def __eq__(self, oOtherFraction):
        '''Test for equality '''
        if not isinstance(oOtherFraction, Fraction):
            return False  # not comparing to a fraction
        if (self.numerator == oOtherFraction.numerator) and \
           (self.denominator == oOtherFraction.denominator):
            return True
        else:
            return False
        
 # Test code:       
oFraction1 = Fraction(1, 3)  # create a Fraction object
oFraction2 = Fraction(2, 5)
print(oFraction1)  # print the object ... calls  __str__
print(oFraction2)

oSumFraction = oFraction1 + oFraction2  # calls __add__
print(oSumFraction)

print('Are fractions 1 and 2 equal?', (oFraction1 == oFraction2))  # should be False

oFraction3 = Fraction(5, 2)
oFraction4 = Fraction(500, 200)
print(oFraction3 + oFraction4)

oFraction5 = Fraction(-20, 80)
oFraction6 = Fraction(4, -16)
print('Are fractions 5 and 6 equal?', (oFraction5 == oFraction6))  # should be True
