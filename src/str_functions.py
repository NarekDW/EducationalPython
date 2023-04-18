from collections import Counter
class StrFunctions:
    def get_number_of_longest_repeated_characters(self, string: str) -> int:
        a = Counter(string)
        return string.count(a.most_common(1)[0][0])



