#!/usr/bin/python3
"""Module defines the canUnlockAll functions to determine if all boxes can be
   opened.
"""


def canUnlockAll(boxes):
    """Functions to determine all the boxes can be opened

       Args:
           boxes (list of lists): A list where each index represents a box and
           a list of keys to other boxes.

       Returns:
           bools: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = set([0])
    keys = boxes[0][:]

    while keys:
        key = keys.pop()
        if key not in opened and key < n:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
