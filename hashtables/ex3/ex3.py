def intersection(arrays):
    """
    Return list of intersecting integers from list of lists
    """
    # For each list in the list of lists, iterate through and make key for each number that also appears in next list
    # Each key's value is number of lists on which it appears
    # So as you iterate through each list, +=1 the values for its numbers
    # This is essentially the same as word count exercise, just with ints
    # Return keys whose values match the length of the list of lists

    count = {}
    num_lists = len(arrays)
    # Get initial list of contenders
    for i in arrays[0]:
        if i in arrays[1]:
            count[i] = 2
    
    for arr in arrays[2:]:
        for i in count:
            if i in arr:
                count[i] += 1

    result = []
    for i in count:
        if count[i] == num_lists:
            result.append(i)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000, 2000)) + [1, 2, 3])
    arrays.append(list(range(2000, 3000)) + [1, 2, 3])
    arrays.append(list(range(3000, 4000)) + [1, 2, 3])

    print(intersection(arrays))
