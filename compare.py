class Solution:
    def compareFrac(self, str):

        frac1, frac2 = str.split(", ")

        # Extract the numerators and denominators
        num1, den1 = map(int, frac1.split("/"))
        num2, den2 = map(int, frac2.split("/"))

        # Compare the fractions by cross-multiplication
        if num1 * den2 > num2 * den1:
            return frac1
        elif num1 * den2 < num2 * den1:
            return frac2
        else:
            return "equal"
