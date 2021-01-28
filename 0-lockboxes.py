#!/usr/bin/python3

def canUnlockAll(boxes):
    """Boxes connections unlocked"""
    N = len(boxes)

    b_dict = {}

    for i, box in enumerate(boxes):
        b_dict[i] = sorted(box)

    L = []
    keys = list(b_dict.keys())
    k = 0
    while True:
        for index in keys:
            if k != index:
                try:
                    if b_dict[k][0] == index:
                        L.append(k)
                        L.append(index)
                        L = list(set(L))
                        if len(b_dict[k]) > 1:
                            b_dict[k].pop(0)
                        k = index
                        break
                    elif index >= N:
                        print("False")
                        return False
                    elif b_dict[k][0] == k and len(b_dict[k]) == 1:
                        return False
                except IndexError:
                    return False
            continue
        if len(L) >= N:
            break
    return(True)
