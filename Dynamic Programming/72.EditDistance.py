class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        def minEditDistance(word1, word2, word1Index, word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index

            if memo[word1Index][word2Index] is not None:
                return memo[word1Index][word2Index]
            minDistance = 0
            if word1[word1Index - 1] == word2[word2Index - 1]:
                minDistance = minEditDistance(
                    word1, word2, word1Index - 1, word2Index - 1
                )
            else:
                InsertDistance = minEditDistance(
                    word1, word2, word1Index, word2Index - 1
                )
                DeleteDistance = minEditDistance(
                    word1, word2, word1Index - 1, word2Index
                )
                ReplaceDistance = minEditDistance(
                    word1, word2, word1Index - 1, word2Index - 1
                )

                minDistance = min(InsertDistance, DeleteDistance, ReplaceDistance) + 1
            memo[word1Index][word2Index] = minDistance
            return minDistance

        return minEditDistance(word1, word2, len(word1), len(word2))
