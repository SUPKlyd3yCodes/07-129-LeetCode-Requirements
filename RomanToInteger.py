class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0

        roman_alphabet = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for letter in range(len(s)):
            current_value = roman_alphabet[s[letter]]
            
            if letter == len(s)-1:
                print("w")
                value += current_value
                continue
            
            next_value = roman_alphabet[s[letter+1]]
            if current_value < next_value:
                value -= current_value
            else:
                value += current_value
        return value
