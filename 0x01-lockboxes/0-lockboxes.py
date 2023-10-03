#!/usr/bin/python3
""" Lockboxes Challenges """


def canUnlockAll(boxes):
    """
    Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
    Task: Write a method that determines if all the boxes can be opened.
    """

    if boxes == 0:
        return False

    if not isinstance(boxes, list):

    if len(boxes) == 0:
        return False

    check = [0]
    list_ing = [i for i in range(len(boxes))]
    for in_check in check:
        for in_boxes in boxes[in_check]:
            if in_boxes not in check and in_boxes in list_ing:
                if in_boxes >= len(boxes):
                    return False
                check.append(in_boxes)

                if len(check) == len(boxes):
        return True
    else:
        return False
