def are_isomorphic(s: str, t: str) -> bool:
    """
    Determines whether two strings s and t are isomorphic.
    Two strings are isomorphic if characters in s can be replaced to get t
    with a consistent one-to-one mapping.

    Invalid input:
    - If either s or t is not a string, return False.
    - If lengths differ, return False.

    Returns:
        True if s and t are isomorphic, False otherwise.
    """

    # Invalid input checks
    if type(s) is not str or type(t) is not str:
        return False
    if len(s) != len(t):
        return False

    # We simulate a mapping using lists (no dicts allowed)
    map_s_to_t = []   # list of [char_from_s, char_from_t]
    map_t_to_s = []   # list of [char_from_t, char_from_s]

    # Loop through characters
    i = 0
    while i < len(s):
        cs = s[i]
        ct = t[i]

        # Check if cs already has a mapping
        j = 0
        found_s = False
        while j < len(map_s_to_t):
            if map_s_to_t[j][0] == cs:
                found_s = True
                if map_s_to_t[j][1] != ct:
                    return False
            j += 1

        # Check if ct already has a mapping
        k = 0
        found_t = False
        while k < len(map_t_to_s):
            if map_t_to_s[k][0] == ct:
                found_t = True
                if map_t_to_s[k][1] != cs:
                    return False
            k += 1

        # If neither side had mapping, create one
        if not found_s and not found_t:
            map_s_to_t.append([cs, ct])
            map_t_to_s.append([ct, cs])

        i += 1

    return True



def is_interleaved(s1: str, s2: str, s3: str) -> bool:
    """
    Determines whether s3 is an interleaving of s1 and s2.
    Interleaving means s3 is formed by weaving characters of s1 and s2
    while preserving the order of characters in each string.

    Invalid input:
    - All inputs must be strings.
    - Length of s3 must equal len(s1) + len(s2).

    Returns:
        True if s3 is an interleaving, False otherwise.
    """

    if type(s1) is not str or type(s2) is not str or type(s3) is not str:
        return False
    if len(s3) != len(s1) + len(s2):
        return False

    i = 0  # pointer for s1
    j = 0  # pointer for s2
    k = 0  # pointer for s3

    while k < len(s3):
        c = s3[k]

        # Try to match s1[i]
        if i < len(s1) and c == s1[i]:
            i += 1
        else:
            # Try to match s2[j]
            if j < len(s2) and c == s2[j]:
                j += 1
            else:
                return False

        k += 1

    # If we used all characters correctly
    if i == len(s1) and j == len(s2):
        return True
    return False



def contiguous_length(nums: list[int]) -> int:
    """
    Returns the length of the longest contiguous subarray with equal 0s and 1s.

    Invalid input:
    - nums must be a list of integers containing only 0 and 1.

    Returns:
        The maximum length of a balanced subarray.
        Returns 0 if none exists.
    """

    if type(nums) is not list:
        return 0

    # Validate all elements
    i = 0
    while i < len(nums):
        if nums[i] != 0 and nums[i] != 1:
            return 0
        i += 1

    # Build prefix sum array (0 → -1, 1 → +1)
    prefix = [0]
    i = 0
    while i < len(nums):
        val = -1
        if nums[i] == 1:
            val = 1
        prefix.append(prefix[-1] + val)
        i += 1

    # Check all subarrays
    longest = 0
    start = 0
    while start < len(prefix):
        end = start + 1
        while end < len(prefix):
            if prefix[end] - prefix[start] == 0:
                length = end - start
                if length > longest:
                    longest = length
            end += 1
        start += 1

    return longest

