class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        max_len = 0
        char_dict = {}

        for i, char in enumerate(s):

            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
            
            if sum(char_dict.values()) > max(char_dict.values()) + k:
                char_dict[s[l]] -= 1
                l += 1
            
        print(len(s) - l, max(char_dict.values())+k)
        return len(s) - l





class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize variables
        max_freq = left_pointer = 0
        char_count = {}  # Dictionary to store character counts
        # Loop through the string
        for right_pointer, char in enumerate(s):
            # Update the count of the current character
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
            # Update the maximum frequency encountered so far
            max_freq = max(max_freq, char_count[char])
            
            # Check if the window needs to be shrunk
            if right_pointer - left_pointer + 1 > max_freq + k:
                # Update the count for the character at the left pointer
                char_count[s[left_pointer]] -= 1
                # Move the left pointer to shrink the window
                left_pointer += 1
        
        # Return the length of the longest valid substring
        return len(s) - left_pointer
