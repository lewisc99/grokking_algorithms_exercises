def find_longest_common_substring(word1: str, word2: str) -> tuple[str, int]:
    """
    Finds the longest common substring between word1 and word2 using dynamic programming.
    Returns the substring and its length.
    """
    len1 = len(word1)
    len2 = len(word2)
    # Create a DP table where dp[i][j] is the length of the longest common substring
    # ending at word1[i-1] and word2[j-1]
    # Initialize the DP table with zeros -
    dp = [] 
    for _ in range(len1 + 1):
        dp.append([0] * (len2 + 1))
    max_length = 0
    end_index_word1 = 0  # End index of the longest common substring in word1

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index_word1 = i
            else:
                dp[i][j] = 0  # No common substring at these indices

    # Extract the longest common substring from word1
    longest_substring = word1[end_index_word1 - max_length:end_index_word1]
    return longest_substring, max_length


# Example usage:
first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")
substring, length = find_longest_common_substring(first_word, second_word)
print()
print(f'Longest Common Substring: "{substring}"')
print(f"Length: {length}")
