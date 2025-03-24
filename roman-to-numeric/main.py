class Numbers:
    def romanToInt(self, s: str) -> int:
        romanDef = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        numeric = 0
        for i in range(len(s)):
            if i == len(s)-1 or romanDef[s[i]] >= romanDef[s[i+1]]:
                numeric += romanDef[s[i]]
            else:
                numeric -= romanDef[s[i]]
            i += 1
        return numeric

if __name__ == "__main__":
    numbers = Numbers()
    print(numbers.romanToInt("MMCCCLVI"))