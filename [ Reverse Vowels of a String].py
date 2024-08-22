def reverseVowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)  # Convert string to list to modify in-place
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer forward until a vowel is found
        while left < right and s[left] not in vowels:
            left += 1
        # Move right pointer backward until a vowel is found
        while left < right and s[right] not in vowels:
            right -= 1
        # Swap the vowels
        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)  # Convert list back to string
