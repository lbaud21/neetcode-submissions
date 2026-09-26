class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = self.build_hash(s)
        d2 = self.build_hash(t)

        for key in d1:
            if not key in d2:
                return False
            if d2[key] != d1[key]:
                return False
        return True

    def build_hash(self, string):
        letters_count = {}
        for letter in string:
            if letter in letters_count:
                letters_count[letter] += 1
                continue
            letters_count[letter] = 0
        return letters_count