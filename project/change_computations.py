"""CSC110 Fall 2021 Final Assignment: Game Data Graphs

===============================
This file contains just functions that displays compute the slope between two months to show the
change in spending. It will be imported into main.py.

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jeanine Colleen Ohene-Agyei, Luke Ham, Chelsea Wang, and Bolin Shen.
"""


def change_in_essentials_monthly(essential: list) -> list[int]:
    """Returns the slope of each the essentials list between each month.

    The slope will calculated using floor division.

    >>> change_in_essentials_monthly([12, 24, -14, 55])
    [12, -26, 43]
    """
    change_so_far = []
    for i in range(1, len(essential)):
        change = (essential[i] - essential[0])
        list.append(change_so_far, change)

    return change_so_far


def change_in_nonessentials_monthly(nonessential: list) -> list[int]:
    """Returns the slope of each the essentials list between each month.

    The slope will calculated using floor division.

    >>> change_in_nonessentials_monthly([105, 202, -321])
    [97, -426]
    """
    change_so_far = []
    for i in range(1, len(nonessential)):
        change = (nonessential[i] - nonessential[0])
        list.append(change_so_far, change)

    return change_so_far


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['doctest', 'python_ta.contracts', 'python_ta'],
        'allowed-io': ['change_in_essentials_monthly', 'change_in_nonessentials_monthly'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
