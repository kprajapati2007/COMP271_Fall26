def indices_of(list_to_search: list, item_to_find: str, find_all: bool) -> int | list[int]:
    """
    Revised version using break and multiple return statements.
    If find_all is True, return all matching indices.
    Otherwise, return the first matching index or -1 if not found.
    """

    # Reflection:
    # Allowing break and multiple return statements makes the function shorter
    # and clearer. It also makes it a lot easier to understand. When find_all is False, returning
    # immediately after finding the first match avoids unnecessary looping.
    #
    # However, this violates the Programmer's Pact. The Pact forces students to
    # practice writing structured loops and think carefully about control flow.
    #
    # In Python without the pact, break and multiple returns are perfectly acceptable
    # and are often preferred for readability. So yes, these changes improve the
    # function—but they are not allowed under the Pact.

    # If we want all matches, collect them normally.
    if find_all:
        indices: list[int] = []
        for i in range(len(list_to_search)):
            if list_to_search[i] == item_to_find:
                indices.append(i)
        return indices  # direct return

    # Otherwise, return the first match immediately.
    for i in range(len(list_to_search)):
        if list_to_search[i] == item_to_find:
            return i  # early return

    # If we reach here, no match was found.
    return -1
