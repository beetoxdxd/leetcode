# Last updated: 1/8/2026, 5:29:25 p.m.
class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hdrd = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thsn = ["", "M", "MM", "MMM"]

        return thsn[num//1000] + hdrd[num//100 % 10] + tens[num//10 % 10] + ones[num%10]