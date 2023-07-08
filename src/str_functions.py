from collections import Counter
class StrFunctions:
    def get_number_of_longest_repeated_characters(self, string: str) -> int:
        result_list = []
        for x in string:
            result_list.append(string.count(x))
        return max(result_list)




