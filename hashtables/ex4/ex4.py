def has_negatives(a):
    """
    Return integers with corresponding negative values in list
    """
    # Iterate through list
    # If number is positive and not already in list, make it a key with value 0
    # If positive and already in list, make value 1
    # If number is negative, multiply it by -1 and check to see if that value is in dict
    # If already keyed in, make value 1

    has_neg = {}
    for i in a:
        if abs(i) not in has_neg:
            has_neg[abs(i)] = 0
        elif abs(i) in has_neg:
            has_neg[abs(i)] = 1
    
    result = []
    for i in list(has_neg):
        if has_neg[i] == 1:
            result.append(i)



    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
