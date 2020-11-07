def get_indices_of_item_weights(weights, length, limit):
    """
    Find two weights that sum to limit
    """
    # Store weights as keys, indices as values
    # Iterate over dict, checking to see if limit - key is a key
    # If it is, extract current key, value and pointed to key, value
    # Form return tuple with higher weight index listed 0, lower 1
    # I don't know how to do this with test 2. Duplicates are wiped out when made into keys for a dict.

    weight_dict = {weight: idx for idx, weight in enumerate(weights)}
    if len(weights) < 2:
        return None
    for w in weight_dict:
        target = limit - w
        if target in weight_dict:
            ret_tuples = [(weight_dict[w], w), (weight_dict[target], target)]
        
    ret_val = (max(ret_tuples)[0], min(ret_tuples)[0])
    print(ret_tuples, ret_val)

    return ret_val

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))