from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map.setdefault(sorted_word, []).append(word)
        return list(anagram_map.values())
    
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],  # Should group eat/tea/ate, tan/nat, and bat
        [""],                                    # Should return [[""]]
        ["a"],                                   # Should return [["a"]]
    ]
    
    for strs in test_cases:
        result = solution.groupAnagrams(strs)
        print(f"Input: {strs}")
        print(f"Output: {result}\n")