#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Function that finds out if all boxes can be unlocked"""
    unblocked_box = 0
    unblocked_boxes = [unblocked_box]  # list of unblocked boxes

    for index in unblocked_boxes:
        # goes over every new index added to the unblocked_boxes list
        box_sublist = boxes[index]
        for box_key in box_sublist:
            # goes over every key of each box, one box at a time
            if box_key not in unblocked_boxes and box_key < len(boxes):
                # checks which key can be added to unblocked_boxes
                unblocked_boxes += [box_key]
    if len(unblocked_boxes) == len(boxes):
        return True
    else:
        return False
