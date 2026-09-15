def add(first_name: str,
        last_name: str,
        role: str,
        underlying: list[list[str]]) -> None:
    """
    Adds a new record [first_name, last_name, role] to the underlying list.
    """
    new_record = [first_name, last_name, role]
    underlying.append(new_record)


def add_unique_first_name(first_name: str,
                          last_name: str,
                          role: str,
                          underlying: list[list[str]]) -> None:
    """
    Adds a new record only if no existing record has the same first_name.
    No 'in' operator allowed, so we manually scan the list.
    """

    i = 0
    found = False

    while i < len(underlying):
        if underlying[i][0] == first_name:
            found = True
            i = len(underlying)  # exit loop without break
        i += 1

    if not found:
        underlying.append([first_name, last_name, role])


def add_unique_last_name(first_name: str,
                         last_name: str,
                         role: str,
                         underlying: list[list[str]]) -> None:
    """
    Adds a new record only if no existing record has the same last_name.
    """

    i = 0
    found = False

    while i < len(underlying):
        if underlying[i][1] == last_name:
            found = True
            i = len(underlying)
        i += 1

    if not found:
        underlying.append([first_name, last_name, role])


def remove_first_name(first_name: str,
                      underlying: list[list[str]]) -> list[str] | None:
    """
    Removes and returns the FIRST record whose first_name matches.
    If none found, return None.
    """

    i = 0
    while i < len(underlying):
        if underlying[i][0] == first_name:
            removed = underlying.pop(i)
            return removed   # justified early return
        i += 1

    return None


def remove_all_first_name(first_name: str,
                          underlying: list[list[str]]) -> list[list[str]] | None:
    """
    Removes and returns ALL records whose first_name matches.
    If none found, return None.
    """

    removed_records: list[list[str]] = []

    i = 0
    while i < len(underlying):
        if underlying[i][0] == first_name:
            removed_records.append(underlying.pop(i))
            # do NOT increment i because list shrinks
        else:
            i += 1

    if len(removed_records) == 0:
        return None

    return removed_records
