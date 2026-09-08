class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts = {}

        left =0
        max_frequency = 0

        for right, character in enumerate(s):

            counts[character] = counts.get(character, 0) + 1

            max_frequency = max(max_frequency, counts[character])

            while (right - left + 1) - max_frequency > k:
                counts[s[left]] -=1
                left +=1

            longest_length = right-left+1
            if right ==0:
                best_length = longest_length
            else:
                best_length = max(best_length, longest_length)

        return best_length if s else 0


