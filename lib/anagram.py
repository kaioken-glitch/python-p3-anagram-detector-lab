# Anagram detector class
class Anagram:
    def __init__(self, word):
        self.original_word = word

    def match(self, possible_anagrams):
        matches = []
        original_sorted = sorted(self.original_word.lower())
        for candidate in possible_anagrams:
            if candidate.lower() == self.original_word.lower():
                continue
            if sorted(candidate.lower()) == original_sorted:
                matches.append(candidate)
        return matches

